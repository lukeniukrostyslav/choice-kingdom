from __future__ import annotations

from pathlib import Path

import pytest

from runtime.delays import CANONICAL_DELAY_SPECS, due_delays, schedule_authored_delay
from runtime.engine import DecisionEngine
from runtime.state import GameState, PendingDelay, SaveStore


ROOT = Path(__file__).resolve().parents[1]


def test_due_delayed_target_is_activated_by_decision_engine_then_executed():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("target-execution")
    state.resources.update({name: 100 for name in state.resources})
    state.relationships.update({name: 3 for name in state.relationships})
    state.flags.add("merchant_charter")
    state.current_event_id = "E18"

    engine.execute(state, "E18", "E18-B")
    key = "delay.E18B.E243.old_bridge"
    delay = state.pending_delays[key]
    state.turn = delay.scheduled_turn

    result = engine.execute_delayed_target(state, key, "E243-A")
    assert result.event_id == "E243"
    assert state.pending_delays[key].status == "resolved"
    assert state.current_event_id == "E243"
    assert "E243" in state.history
    assert state.activated_delayed_targets == set()


def test_delayed_target_activation_is_exactly_once_and_persists():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("target-exactly-once")
    delay = schedule_authored_delay(state, "E20", "E20-A")
    assert delay is not None
    state.turn = delay.scheduled_turn

    first = engine.activate_delayed_target(state, delay.exactly_once_key)
    assert first.target_event_id == "E245"

    with pytest.raises(ValueError, match="delay is not due|delay is not pending"):
        engine.activate_delayed_target(state, delay.exactly_once_key)

    restored_path = ROOT / "tests" / ".tmp_delayed_target_state.json"
    try:
        SaveStore.save(state, restored_path)
        restored = SaveStore.load(restored_path)
    finally:
        restored_path.unlink(missing_ok=True)
    assert restored.snapshot() == state.snapshot()


def test_competing_due_delays_use_deterministic_turn_priority_and_key_order():
    state = GameState.fresh("competing-delays")
    state.pending_delays = {
        "delay.z": PendingDelay("delay.z", "E18", "E18-B", "E243", 6, priority=2),
        "delay.a": PendingDelay("delay.a", "E20", "E20-A", "E245", 6, priority=1),
        "delay.m": PendingDelay("delay.m", "E25", "E25-B", "E184", 6, priority=1),
        "delay.late": PendingDelay("delay.late", "E45", "E45-B", "E181", 7, priority=0),
    }
    state.turn = 6

    first = tuple(delay.exactly_once_key for delay in due_delays(state))
    second = tuple(delay.exactly_once_key for delay in due_delays(state))

    assert first == ("delay.a", "delay.m", "delay.z", "delay.late")
    assert second == first


def test_all_nine_turn_bound_canonical_delays_have_target_activation_contract():
    engine = DecisionEngine(ROOT)
    turn_bound = [spec for spec in CANONICAL_DELAY_SPECS if not spec.condition_bound]
    assert len(turn_bound) == 9
    for index, spec in enumerate(turn_bound):
        state = GameState.fresh(f"target-{index}")
        delay = schedule_authored_delay(state, spec.source_event_id, spec.source_choice_id)
        assert delay is not None
        state.turn = delay.scheduled_turn
        activation = engine.activate_delayed_target(state, delay.exactly_once_key)
        assert activation.target_event_id == spec.resolution_target
        assert state.pending_delays[delay.exactly_once_key].status == "resolved"
        assert state.current_event_id == spec.resolution_target


def test_condition_bound_e185_requires_explicit_condition_result():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("target-e185")
    delay = schedule_authored_delay(state, "E17", "E17-A")
    assert delay is not None
    with pytest.raises(ValueError, match="condition not satisfied"):
        engine.activate_delayed_target(state, delay.exactly_once_key, condition_satisfied=False)
    assert state.pending_delays[delay.exactly_once_key].status == "pending"


def test_condition_bound_e185_can_activate_target_only_when_condition_is_explicitly_true():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("target-e185-true")
    delay = schedule_authored_delay(state, "E17", "E17-A")
    assert delay is not None

    activation = engine.activate_delayed_target(
        state,
        delay.exactly_once_key,
        condition_satisfied=True,
    )

    assert activation.target_event_id == "E185"
    assert state.pending_delays[delay.exactly_once_key].status == "resolved"
    assert state.current_event_id == "E185"

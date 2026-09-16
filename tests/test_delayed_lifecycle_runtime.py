from __future__ import annotations

import re
from pathlib import Path

import pytest

from runtime.delays import (
    CANONICAL_DELAY_SPECS,
    due_delays,
    resolve_condition_bound_delay,
    resolve_due_delay,
    schedule_authored_delay,
)
from runtime.engine import DecisionEngine
from runtime.state import GameState, PendingDelay, SaveStore


def test_all_ten_frozen_delay_specs_have_canonical_identity():
    assert len(CANONICAL_DELAY_SPECS) == 10
    assert {spec.resolution_target for spec in CANONICAL_DELAY_SPECS} == {
        "E181", "E182", "E183", "E184", "E185", "E242", "E243", "E244", "E245", "E246"
    }
    assert len({spec.exactly_once_key for spec in CANONICAL_DELAY_SPECS}) == 10


def test_frozen_source_choice_identity_matches_machine_delay_contract():
    expected = {
        "E181": ("E45", "B"),
        "E182": ("E117", "B"),
        "E183": ("E118", "B"),
        "E184": ("E25", "B"),
        "E185": ("E17", "A"),
        "E242": ("E118", "B"),
        "E243": ("E18", "B"),
        "E244": ("E09", "B"),
        "E245": ("E20", "A"),
        "E246": ("E160", "A"),
    }
    actual = {
        spec.resolution_target: (spec.source_event_id, spec.source_choice_id)
        for spec in CANONICAL_DELAY_SPECS
    }
    assert actual == expected


def test_authored_choice_schedules_relative_delay_after_source_turn():
    state = GameState.fresh("delay-schedule")
    state.turn = 7
    delay = schedule_authored_delay(state, "E45", "B")

    assert delay is not None
    assert delay.exactly_once_key == "delay.E45B.E181.second_toll_increase"
    assert delay.scheduled_turn == 12
    assert delay.status == "pending"


def test_due_delay_resolves_only_at_earliest_turn_and_only_once():
    state = GameState.fresh("delay-due")
    state.turn = 7
    delay = schedule_authored_delay(state, "E20", "A")
    assert delay is not None
    assert due_delays(state) == ()

    state.turn = delay.scheduled_turn - 1
    assert due_delays(state) == ()
    state.turn = delay.scheduled_turn
    assert due_delays(state)[0].exactly_once_key == delay.exactly_once_key

    resolved = resolve_due_delay(state, delay.exactly_once_key)
    assert resolved.status == "resolved"
    assert due_delays(state) == ()


def test_condition_bound_delay_requires_explicit_resolution_condition():
    state = GameState.fresh("delay-condition")
    delay = schedule_authored_delay(state, "E17", "A")
    assert delay is not None
    assert delay.condition_bound is True
    assert delay.scheduled_turn is None
    assert due_delays(state) == ()

    with pytest.raises(ValueError, match="condition not satisfied"):
        resolve_condition_bound_delay(state, delay.exactly_once_key, False)

    resolved = resolve_condition_bound_delay(state, delay.exactly_once_key, True)
    assert resolved.status == "resolved"


def test_cancellation_is_observable_and_blocks_resolution():
    state = GameState.fresh("delay-cancel")
    delay = PendingDelay(
        exactly_once_key="delay.test.cancel",
        source_event_id="E45",
        source_choice_id="B",
        resolution_target="E181",
        scheduled_turn=4,
    )
    state.schedule(delay)
    cancelled = state.cancel_delay(delay.exactly_once_key)
    assert cancelled.status == "cancelled"

    state.turn = 10
    assert due_delays(state) == ()
    with pytest.raises(ValueError, match="not pending"):
        state.resolve_delay(delay.exactly_once_key)


def test_supersession_marks_prior_delay_without_silent_deletion():
    state = GameState.fresh("delay-supersede")
    old = PendingDelay(
        exactly_once_key="delay.test.old",
        source_event_id="E45",
        source_choice_id="B",
        resolution_target="E181",
        scheduled_turn=4,
    )
    new = PendingDelay(
        exactly_once_key="delay.test.new",
        source_event_id="E118",
        source_choice_id="B",
        resolution_target="E242",
        scheduled_turn=5,
        supersedes=old.exactly_once_key,
    )
    state.schedule(old)
    state.schedule(new)
    assert state.pending_delays[old.exactly_once_key].status == "superseded"
    assert state.pending_delays[new.exactly_once_key].status == "pending"


def test_pending_delay_survives_save_load_and_replay_runs_are_isolated(tmp_path):
    first = GameState.fresh("delay-save-a")
    schedule_authored_delay(first, "E09", "B")
    path = tmp_path / "delay.json"
    SaveStore.save(first, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == first.snapshot()

    second = GameState.fresh("delay-save-b")
    assert second.pending_delays == {}
    assert restored.run_id != second.run_id


def _prime_state_for_authored_source(engine: DecisionEngine, event_id: str) -> GameState:
    """Satisfy only machine-readable trigger requirements; never invent route edges."""
    state = GameState.fresh(f"delay-source-{event_id}")
    event = engine.event(event_id)
    state.resources.update({name: 100 for name in state.resources})
    state.relationships.update({name: 3 for name in state.relationships})
    state.flags.update(re.findall(r"`([^`]+)`", event.trigger))
    prerequisites = engine.catalog.authored_prerequisites(event_id)
    state.history.update(prerequisites)
    if prerequisites:
        state.current_event_id = prerequisites[-1]
    if event_id == "E17":
        state.resources["security"] = 60
    return state


# E160 is deliberately excluded from direct engine execution here: its canonical
# trigger is prose-only ("severe winter") and no machine predicate currently
# represents that condition. Treating it as executable would invent semantics.
EXECUTABLE_DELAY_SPECS = tuple(
    spec for spec in CANONICAL_DELAY_SPECS if spec.source_event_id != "E160"
)


@pytest.mark.parametrize(
    "event_id,choice_id,resolution_target",
    [(spec.source_event_id, spec.source_choice_id, spec.resolution_target) for spec in EXECUTABLE_DELAY_SPECS],
)
def test_each_machine_executable_delayed_choice_executes_through_decision_engine(
    event_id: str, choice_id: str, resolution_target: str
):
    engine = DecisionEngine(Path(__file__).resolve().parents[1])
    state = _prime_state_for_authored_source(engine, event_id)

    result = engine.execute(state, event_id, choice_id)
    delay = next(d for d in state.pending_delays.values() if d.resolution_target == resolution_target)

    assert result.event_id == event_id
    assert delay.source_event_id == event_id
    assert delay.source_choice_id == choice_id
    assert delay.status == "pending"
    assert delay.exactly_once_key
    assert delay.resolution_target == resolution_target

    if delay.condition_bound:
        assert delay.scheduled_turn is None
    else:
        assert delay.scheduled_turn is not None
        state.turn = delay.scheduled_turn
        assert due_delays(state) == (delay,)
        assert resolve_due_delay(state, delay.exactly_once_key).status == "resolved"
        with pytest.raises(ValueError, match="not pending"):
            resolve_due_delay(state, delay.exactly_once_key)


def test_e160_delayed_source_is_explicitly_blocked_until_winter_predicate_exists():
    engine = DecisionEngine(Path(__file__).resolve().parents[1])
    state = _prime_state_for_authored_source(engine, "E160")
    with pytest.raises(ValueError, match="event trigger not satisfied: E160"):
        engine.execute(state, "E160", "A")


def test_all_machine_executable_delays_remain_run_scoped_after_engine_execution(tmp_path):
    engine = DecisionEngine(Path(__file__).resolve().parents[1])
    snapshots = []
    for index, spec in enumerate(EXECUTABLE_DELAY_SPECS):
        state = _prime_state_for_authored_source(engine, spec.source_event_id)
        engine.execute(state, spec.source_event_id, spec.source_choice_id)
        path = tmp_path / f"delay-{index}.json"
        SaveStore.save(state, path)
        restored = SaveStore.load(path)
        snapshots.append(restored.snapshot())

    fresh = GameState.fresh("fresh-after-delayed-sources")
    assert fresh.pending_delays == {}
    assert all(snapshot["pending_delays"] for snapshot in snapshots)

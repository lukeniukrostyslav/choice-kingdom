from __future__ import annotations

from pathlib import Path

import pytest

from runtime.delays import schedule_authored_delay
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_delayed_target_uses_canonical_activation_and_execution() -> None:
    session = GameSession.new(ROOT, "delay-session")
    schedule_authored_delay(session.state, "E181", "E181-A")

    key, delay = next(iter(session.state.pending_delays.items()))
    assert delay.status == "pending"
    assert delay.resolution_target in session.engine.catalog.events

    activated = session.engine.activate_delayed_target(session.state, key)
    assert activated.target_event_id == delay.resolution_target
    assert session.state.current_event_id == delay.resolution_target
    assert delay.resolution_target in session.state.activated_delayed_targets
    assert session.state.pending_delays[key].status == "resolved"

    with pytest.raises(ValueError, match="no due delayed consequence"):
        session.activate_next_due_delay()


def test_game_session_condition_bound_delay_requires_explicit_condition() -> None:
    session = GameSession.new(ROOT, "condition-delay")
    schedule_authored_delay(session.state, "E181", "E181-B")
    key, delay = next(iter(session.state.pending_delays.items()))

    if not delay.condition_bound:
        pytest.skip("selected authored delay is not condition-bound")

    with pytest.raises(ValueError, match="condition not satisfied"):
        session.engine.activate_delayed_target(session.state, key, condition_satisfied=False)

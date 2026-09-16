from __future__ import annotations

from pathlib import Path

import pytest

from runtime.delays import schedule_authored_delay
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_delayed_target_uses_canonical_activation() -> None:
    session = GameSession.new(ROOT, "delay-session")
    schedule_authored_delay(session.state, "E45", "E45-B")

    key, delay = next(iter(session.state.pending_delays.items()))
    assert delay.status == "pending"
    assert delay.resolution_target == "E181"
    assert delay.scheduled_turn is not None

    session.state.turn = delay.scheduled_turn
    activated = session.engine.activate_delayed_target(session.state, key)

    assert activated.target_event_id == "E181"
    assert session.state.current_event_id == "E181"
    assert "E181" in session.state.activated_delayed_targets
    assert session.state.pending_delays[key].status == "resolved"


def test_game_session_condition_bound_delay_requires_explicit_condition() -> None:
    session = GameSession.new(ROOT, "condition-delay")
    schedule_authored_delay(session.state, "E17", "E17-A")
    key, delay = next(iter(session.state.pending_delays.items()))

    assert delay.condition_bound is True
    assert delay.scheduled_turn is None

    with pytest.raises(ValueError, match="condition not satisfied"):
        session.engine.activate_delayed_target(session.state, key, condition_satisfied=False)

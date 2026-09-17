from pathlib import Path

import pytest

from runtime.session import GameSession
from runtime.state import PendingDelay

ROOT = Path(__file__).resolve().parents[1]


def _seed_pending_delay(session: GameSession) -> str:
    key = "test.delay.terminal"
    session.state.pending_delays[key] = PendingDelay(
        exactly_once_key=key,
        source_event_id="E01",
        source_choice_id="E01-A",
        resolution_target="E02",
        scheduled_turn=session.state.turn,
    )
    return key


def test_terminal_session_cannot_activate_pending_delay():
    session = GameSession.new(ROOT, "terminal-delay-activation")
    key = _seed_pending_delay(session)
    session.state.terminal = True
    before = session.state.snapshot()

    with pytest.raises(ValueError, match="after terminal state"):
        session.activate_delayed_target(key)

    assert session.state.snapshot() == before


def test_terminal_session_cannot_execute_delayed_target():
    session = GameSession.new(ROOT, "terminal-delay-execution")
    key = _seed_pending_delay(session)
    session.state.terminal = True
    target = session.engine.event("E02")
    choice_id = target.choices[0].choice_id
    before = session.state.snapshot()

    with pytest.raises(ValueError, match="after terminal state"):
        session.execute_delayed_target(key, choice_id)

    assert session.state.snapshot() == before


def test_invalid_delayed_choice_does_not_consume_pending_delay():
    session = GameSession.new(ROOT, "invalid-delay-choice")
    key = _seed_pending_delay(session)
    before = session.state.snapshot()

    with pytest.raises(KeyError, match="E02-NOT-A-CHOICE"):
        session.execute_delayed_target(key, "E02-NOT-A-CHOICE")

    assert session.state.snapshot() == before


def test_invalid_next_due_delayed_choice_does_not_consume_pending_delay():
    session = GameSession.new(ROOT, "invalid-next-due-delay-choice")
    key = _seed_pending_delay(session)
    before = session.state.snapshot()

    with pytest.raises(KeyError, match="E02-NOT-A-CHOICE"):
        session.execute_next_due_delay("E02-NOT-A-CHOICE")

    assert session.state.snapshot() == before
    assert session.state.pending_delays[key].status == "pending"
    assert session.state.current_event_id == "E01"

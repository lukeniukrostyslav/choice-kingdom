from pathlib import Path

import pytest

from runtime.session import GameSession
from runtime.state import PendingDelay

ROOT = Path(__file__).resolve().parents[1]


def _seed_due_delay(session: GameSession) -> str:
    key = "test.delay.session-terminal"
    session.state.pending_delays[key] = PendingDelay(
        exactly_once_key=key,
        source_event_id="E01",
        source_choice_id="E01-A",
        resolution_target="E02",
        scheduled_turn=session.state.turn,
    )
    return key


def test_terminal_session_exposes_no_available_events_or_choices():
    session = GameSession.new(ROOT, "terminal-availability")
    session.state.terminal = True

    assert session.available_events() == ()
    assert session.available_choices() == ()


def test_terminal_session_rejects_event_selection_and_choice_execution():
    session = GameSession.new(ROOT, "terminal-mutation")
    session.state.terminal = True

    with pytest.raises(ValueError, match="not currently available"):
        session.select_event("E01")
    with pytest.raises(ValueError, match="cannot execute a choice after terminal state"):
        session.choose("E01-A")


def test_terminal_session_rejects_next_due_delay_before_inspecting_choice():
    session = GameSession.new(ROOT, "terminal-next-due-delay")
    key = _seed_due_delay(session)
    session.state.terminal = True
    before = session.state.snapshot()

    with pytest.raises(ValueError, match="cannot execute a choice after terminal state"):
        session.execute_next_due_delay("E02-NOT-A-CHOICE")

    assert session.state.snapshot() == before
    assert session.state.pending_delays[key].status == "pending"


def test_terminal_session_rejects_delayed_activation_without_mutation():
    session = GameSession.new(ROOT, "terminal-delayed-activation")
    key = _seed_due_delay(session)
    session.state.terminal = True
    before = session.state.snapshot()

    with pytest.raises(ValueError, match="after terminal state"):
        session.activate_next_due_delay()

    assert session.state.snapshot() == before
    assert session.state.pending_delays[key].status == "pending"

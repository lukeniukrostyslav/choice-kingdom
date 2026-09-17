from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


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

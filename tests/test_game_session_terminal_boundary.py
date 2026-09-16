from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_rejects_choices_after_terminal_state() -> None:
    session = GameSession.new(ROOT, "terminal-boundary")
    session.state.terminal = True
    with pytest.raises(ValueError, match="terminal state"):
        session.choose("E01-A")

from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_rejects_unknown_choice_id() -> None:
    session = GameSession.new(ROOT, "invalid-choice")
    with pytest.raises(KeyError):
        session.choose("E01-Z")

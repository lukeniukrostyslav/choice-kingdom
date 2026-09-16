from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_rejects_choice_from_non_selected_event() -> None:
    session = GameSession.new(ROOT, "choice-boundary")
    with pytest.raises(KeyError):
        session.choose("E02-A")

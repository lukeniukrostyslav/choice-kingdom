from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_turn_advances_once_per_choice() -> None:
    session = GameSession.new(ROOT, "turn-boundary")
    assert session.state.turn == 1
    session.choose("E01-A")
    assert session.state.turn == 2
    session.select_event("E02")
    session.choose("E02-A")
    assert session.state.turn == 3

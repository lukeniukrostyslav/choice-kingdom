from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_current_event_follows_engine_state() -> None:
    session = GameSession.new(ROOT, "current-event")
    assert session.state.current_event_id == "E01"
    session.choose("E01-A")
    assert session.state.current_event_id == "E01"
    session.select_event("E02")
    session.choose("E02-A")
    assert session.state.current_event_id == "E02"

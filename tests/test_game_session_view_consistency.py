from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_view_tracks_selected_event_after_choice() -> None:
    session = GameSession.new(ROOT, "view-consistency")
    assert session.view().event_id == "E01"
    session.choose("E01-A")
    session.select_event("E02")
    assert session.view().event_id == "E02"
    assert session.view().turn == session.state.turn

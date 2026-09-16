from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_view_exposes_relationship_state() -> None:
    session = GameSession.new(ROOT, "relationship-view")
    session.choose("E01-A")
    session.select_event("E02")
    session.choose("E02-B")
    view = session.view()
    assert dict(view.relationships)["mara"] == 0
    assert "E02" in session.state.history

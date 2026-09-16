from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_view_exposes_current_runtime_resources() -> None:
    session = GameSession.new(ROOT, "view-state")
    session.choose("E01-A")
    view = session.view()
    assert dict(view.resources)["trust"] == 54
    assert dict(view.resources)["power"] == 49
    assert "E01" in session.state.history

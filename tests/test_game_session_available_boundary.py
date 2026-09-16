from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_available_events_respects_authored_route_boundary() -> None:
    session = GameSession.new(ROOT, "available-boundary")
    assert session.available_choices() == ("E01-A", "E01-B")
    session.choose("E01-A")
    assert "E02" in session.available_events()
    with pytest.raises(ValueError, match="event is not currently available"):
        session.select_event("E03")

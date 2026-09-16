from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_state_is_presentation_independent() -> None:
    session = GameSession.new(ROOT, "presentation-independent")
    before = session.snapshot_digest()
    _ = session.view()
    _ = session.available_events()
    _ = session.available_choices()
    assert session.snapshot_digest() == before

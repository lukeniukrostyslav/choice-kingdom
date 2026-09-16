from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_terminal_state_is_persisted_in_snapshot() -> None:
    session = GameSession.new(ROOT, "terminal-snapshot")
    session.state.terminal = True
    session.state.ending_identity = "END_STEWARD"
    digest = session.snapshot_digest()
    assert session.state.snapshot()["terminal"] is True
    assert session.state.snapshot()["ending_identity"] == "END_STEWARD"
    assert session.snapshot_digest() == digest

from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_snapshot_digest_is_stable_without_mutation() -> None:
    session = GameSession.new(ROOT, "snapshot-stability")
    first = session.snapshot_digest()
    second = session.snapshot_digest()
    assert first == second

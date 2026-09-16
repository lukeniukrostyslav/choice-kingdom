from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_roundtrip_allows_empty_meta() -> None:
    session = GameSession.new(ROOT, "empty-meta-prior")
    session.state.terminal = True
    export = session.export_replay()
    replay = GameSession.new_replay(ROOT, "empty-meta-next", export)
    assert export.meta_keys == ()
    assert replay.state.imported_meta_keys == set()

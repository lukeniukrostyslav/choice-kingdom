from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_meta_does_not_copy_run_history() -> None:
    session = GameSession.new(ROOT, "meta-isolation-prior")
    session.choose("E01-A")
    session.state.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    session.state.terminal = True
    replay = GameSession.new_replay(ROOT, "meta-isolation-next", session.export_replay())
    assert replay.state.history == set()
    assert replay.state.resources["trust"] == 50
    assert replay.state.imported_meta_keys == {"meta.replay.warehouse_investigation_unlock"}

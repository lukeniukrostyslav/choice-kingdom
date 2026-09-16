from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_completed_replay_roundtrip_imports_only_canonical_meta() -> None:
    session = GameSession.new(ROOT, "completed-run")
    session.state.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    session.state.record_replay_meta("meta.replay.second_run_information_route")
    session.state.terminal = True

    export = session.export_replay()
    replay = GameSession.new_replay(ROOT, "replay-run", export)

    assert replay.state.run_id == "replay-run"
    assert replay.state.current_event_id == "E01"
    assert replay.state.turn == 1
    assert replay.state.history == set()
    assert replay.state.imported_meta_keys == {
        "meta.replay.warehouse_investigation_unlock",
        "meta.replay.second_run_information_route",
    }

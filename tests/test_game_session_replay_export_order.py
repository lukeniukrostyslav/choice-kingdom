from __future__ import annotations

from pathlib import Path

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_export_orders_meta_keys_canonically() -> None:
    session = GameSession.new(ROOT, "ordered-meta")
    session.state.record_replay_meta("meta.replay.second_run_information_route")
    session.state.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    session.state.terminal = True
    export = session.export_replay()
    assert export.meta_keys == (
        "meta.replay.second_run_information_route",
        "meta.replay.warehouse_investigation_unlock",
    )

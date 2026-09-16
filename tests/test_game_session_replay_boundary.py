from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_export_requires_terminal_run_and_preserves_only_meta() -> None:
    session = GameSession.new(ROOT, "prior-run")
    session.state.record_replay_meta("meta.replay.warehouse_investigation_unlock")

    with pytest.raises(ValueError, match="completed run"):
        session.export_replay()

    session.state.terminal = True
    export = session.export_replay()
    assert export.prior_run_id == "prior-run"
    assert export.completed is True
    assert export.meta_keys == ("meta.replay.warehouse_investigation_unlock",)

    replay = GameSession.new_replay(ROOT, "second-run", export)
    assert replay.state.run_id == "second-run"
    assert replay.state.turn == 1
    assert replay.state.current_event_id == "E01"
    assert replay.state.history == set()
    assert replay.state.resources == session.state.resources
    assert replay.state.imported_meta_keys == {"meta.replay.warehouse_investigation_unlock"}


def test_game_session_replay_rejects_same_run_identity() -> None:
    session = GameSession.new(ROOT, "prior-run")
    session.state.terminal = True
    export = session.export_replay()

    with pytest.raises(ValueError, match="must differ"):
        GameSession.new_replay(ROOT, "prior-run", export)

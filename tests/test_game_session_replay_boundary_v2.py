from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_export_requires_terminal_state() -> None:
    session = GameSession.new(ROOT, "prior-run-v2")
    session.state.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    with pytest.raises(ValueError, match="completed run"):
        session.export_replay()

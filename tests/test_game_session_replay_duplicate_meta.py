from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_rejects_duplicate_meta_keys() -> None:
    with pytest.raises(ValueError, match="duplicate"):
        GameSession.new_replay(ROOT, "new-run-duplicate", {
            "schema_version": 1,
            "run_id": "prior-run-duplicate",
            "completed": True,
            "meta_keys": [
                "meta.replay.warehouse_investigation_unlock",
                "meta.replay.warehouse_investigation_unlock",
            ],
        })

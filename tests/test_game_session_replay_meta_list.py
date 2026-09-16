from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_rejects_non_list_meta_keys() -> None:
    with pytest.raises(ValueError, match="meta_keys must be a list"):
        GameSession.new_replay(ROOT, "new-run-list", {
            "schema_version": 1,
            "run_id": "prior-run-list",
            "completed": True,
            "meta_keys": "meta.replay.warehouse_investigation_unlock",
        })

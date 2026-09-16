from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_rejects_unknown_schema() -> None:
    with pytest.raises(ValueError, match="unsupported replay export schema"):
        GameSession.new_replay(ROOT, "new-run-schema", {
            "schema_version": 999,
            "run_id": "prior-run-schema",
            "completed": True,
            "meta_keys": [],
        })

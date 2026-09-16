from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_rejects_noncanonical_meta() -> None:
    with pytest.raises(ValueError, match="non-canonical"):
        GameSession.new_replay(ROOT, "new-run-meta", {
            "schema_version": 1,
            "run_id": "prior-run-meta",
            "completed": True,
            "meta_keys": ["not.canonical"],
        })

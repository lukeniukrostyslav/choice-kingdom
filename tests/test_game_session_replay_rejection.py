from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_rejects_incomplete_prior_export() -> None:
    session = GameSession.new(ROOT, "prior-incomplete")
    with pytest.raises(ValueError, match="completed run"):
        GameSession.new_replay(ROOT, "new-run", {
            "schema_version": 1,
            "run_id": "prior-incomplete",
            "completed": False,
            "meta_keys": [],
        })

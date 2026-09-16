from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_rejects_missing_prior_identity() -> None:
    with pytest.raises(ValueError, match="prior run identity"):
        GameSession.new_replay(ROOT, "new-run-missing", {
            "schema_version": 1,
            "run_id": "",
            "completed": True,
            "meta_keys": [],
        })

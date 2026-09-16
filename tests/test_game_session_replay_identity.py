from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_replay_requires_distinct_run_identity() -> None:
    session = GameSession.new(ROOT, "same-run")
    session.state.terminal = True
    export = session.export_replay()
    with pytest.raises(ValueError, match="must differ"):
        GameSession.new_replay(ROOT, "same-run", export)

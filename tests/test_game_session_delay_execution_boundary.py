from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_delay_execution_rejects_unknown_delay_key() -> None:
    session = GameSession.new(ROOT, "delay-negative")
    with pytest.raises(KeyError):
        session.engine.execute_delayed_target(session.state, "missing-delay", "E181-A")

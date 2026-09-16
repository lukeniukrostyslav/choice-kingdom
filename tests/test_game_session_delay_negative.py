from __future__ import annotations

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_game_session_cannot_execute_missing_delay() -> None:
    session = GameSession.new(ROOT, "delay-negative-v2")
    with pytest.raises(KeyError):
        session.execute_next_due_delay("E181-A")

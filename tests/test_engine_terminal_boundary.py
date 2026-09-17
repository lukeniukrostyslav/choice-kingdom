from pathlib import Path

from runtime.engine import DecisionEngine
from runtime.state import GameState

ROOT = Path(__file__).resolve().parents[1]


def test_engine_available_is_empty_for_terminal_state():
    engine = DecisionEngine(ROOT)
    state = GameState.new("engine-terminal-availability")
    state.terminal = True

    assert engine.available(state) == ()

from pathlib import Path

import pytest

from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def _pending_delay(session: GameSession) -> str:
    for key, delay in session.state.pending_delays.items():
        if delay.status == "pending":
            return key
    pytest.fail("expected a pending delayed consequence")


def test_terminal_session_cannot_activate_pending_delay():
    session = GameSession.new(ROOT, "terminal-delay-activation")
    session.state.terminal = True
    key = _pending_delay(session) if session.state.pending_delays else None

    if key is None:
        pytest.skip("fresh state has no authored pending delay")

    before = session.state.snapshot()
    with pytest.raises(ValueError, match="after terminal state"):
        session.activate_delayed_target(key, condition_satisfied=True)
    assert session.state.snapshot() == before


def test_terminal_session_cannot_execute_delayed_target():
    session = GameSession.new(ROOT, "terminal-delay-execution")
    session.state.terminal = True
    key = _pending_delay(session) if session.state.pending_delays else None

    if key is None:
        pytest.skip("fresh state has no authored pending delay")

    delay = session.state.pending_delays[key]
    target = session.engine.event(delay.resolution_target)
    choice_id = target.choices[0].choice_id
    before = session.state.snapshot()

    with pytest.raises(ValueError, match="after terminal state"):
        session.execute_delayed_target(key, choice_id, condition_satisfied=True)
    assert session.state.snapshot() == before

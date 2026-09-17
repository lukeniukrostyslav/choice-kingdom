from __future__ import annotations

from pathlib import Path

from runtime.gameplay_state import GameplayPhase, gameplay_state
from runtime.session import GameSession, SessionView
from runtime.state import GameState, PendingDelay


ROOT = Path(__file__).resolve().parents[1]


def test_block8_new_run_and_decision_states() -> None:
    session = GameSession.new(ROOT, "block8-new")
    assert gameplay_state(session.view()).phase is GameplayPhase.NEW_RUN

    session.choose("E01-A")
    assert gameplay_state(session.view()).phase is GameplayPhase.DECISION


def test_block8_convergence_state_is_explicit() -> None:
    view = SessionView(
        run_id="block8-convergence",
        turn=4,
        event_id="E32",
        title="Convergence",
        trigger="",
        choices=(),
        resources=tuple((key, 50) for key in ("gold", "trust", "security", "power", "reputation")),
        relationships=tuple((key, 0) for key in ("mara", "rowan", "seris", "ivo", "amara", "toma")),
        history=("E31",),
        threads=(),
        pending_delays=(),
        ending_evidence=(),
        terminal=False,
        ending_identity=None,
    )
    state = gameplay_state(view)
    assert state.phase is GameplayPhase.CONVERGENCE
    assert state.has_choices is False


def test_block8_delayed_states_are_distinguished() -> None:
    waiting = GameState.fresh("block8-delay-waiting")
    waiting.pending_delays["waiting"] = PendingDelay(
        "waiting", "E17", "E17-A", "E185", None, condition_bound=True
    )
    session_view = GameSession(ROOT, waiting).view()
    assert gameplay_state(session_view).phase is GameplayPhase.DELAY_WAITING

    due = GameState.fresh("block8-delay-due")
    due.turn = 8
    due.pending_delays["due"] = PendingDelay(
        "due", "E45", "E45-B", "E181", 5
    )
    due_view = GameSession(ROOT, due).view()
    state = gameplay_state(due_view)
    assert state.phase is GameplayPhase.DELAY_DUE
    assert state.due_delay_count == 1


def test_block8_terminal_state_is_explicit_and_non_actionable() -> None:
    state = GameState.fresh("block8-ending")
    state.terminal = True
    state.ending_identity = "END_STEWARD"
    view = GameSession(ROOT, state).view()
    projected = gameplay_state(view)
    assert projected.phase is GameplayPhase.ENDING
    assert projected.ending_identity == "END_STEWARD"


def test_block8_all_phases_are_closed() -> None:
    assert {phase.value for phase in GameplayPhase} == {
        "new_run",
        "decision",
        "convergence",
        "delay_due",
        "delay_waiting",
        "ending",
    }

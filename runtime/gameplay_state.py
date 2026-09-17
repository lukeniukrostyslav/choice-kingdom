from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .delays import due_delays
from .session import SessionView


class GameplayPhase(str, Enum):
    NEW_RUN = "new_run"
    DECISION = "decision"
    CONVERGENCE = "convergence"
    DELAY_DUE = "delay_due"
    DELAY_WAITING = "delay_waiting"
    ENDING = "ending"


@dataclass(frozen=True)
class GameplayState:
    """Canonical, presentation-neutral gameplay lifecycle projection.

    This class classifies the already-owned GameSession state; it never mutates
    gameplay and never invents routing rules.
    """

    phase: GameplayPhase
    has_choices: bool
    has_pending_delays: bool
    due_delay_count: int
    ending_identity: str | None

    @classmethod
    def from_view(cls, view: SessionView) -> "GameplayState":
        if view.terminal:
            return cls(GameplayPhase.ENDING, False, False, 0, view.ending_identity)

        pending = tuple(item for item in view.pending_delays if item[2] == "pending")
        due_count = sum(
            1
            for _, _, _, scheduled_turn, _ in pending
            if scheduled_turn is not None and view.turn >= scheduled_turn
        )
        if due_count:
            phase = GameplayPhase.DELAY_DUE
        elif any(scheduled_turn is None for _, _, _, scheduled_turn, _ in pending):
            phase = GameplayPhase.DELAY_WAITING
        elif not view.history and view.turn == 1 and view.event_id == "E01":
            phase = GameplayPhase.NEW_RUN
        elif view.choices:
            phase = GameplayPhase.DECISION
        else:
            phase = GameplayPhase.CONVERGENCE

        return cls(
            phase=phase,
            has_choices=bool(view.choices),
            has_pending_delays=bool(pending),
            due_delay_count=due_count,
            ending_identity=None,
        )


def gameplay_state(view: SessionView) -> GameplayState:
    return GameplayState.from_view(view)

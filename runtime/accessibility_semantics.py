from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ActionState(str, Enum):
    IDLE = "idle"
    FOCUSED = "focused"
    PRESSED = "pressed"
    RESOLVING = "resolving"
    DISABLED = "disabled"
    RESOLVED = "resolved"


@dataclass(frozen=True)
class ActionSemantics:
    role: str
    label: str
    hint: str | None
    state: ActionState
    enabled: bool
    min_touch_target_dp: int = 48


def choice_semantics(
    label: str,
    *,
    state: ActionState = ActionState.IDLE,
    enabled: bool = True,
    hint: str | None = None,
) -> ActionSemantics:
    """Return screen-reader/action semantics without changing gameplay state."""
    if not label.strip():
        raise ValueError("accessible action label must not be empty")
    if state is ActionState.DISABLED:
        enabled = False
    return ActionSemantics(
        role="button",
        label=label,
        hint=hint,
        state=state,
        enabled=enabled,
    )

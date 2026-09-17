from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class MotionSemantic(str, Enum):
    ENTER = "enter"
    FOCUS = "focus"
    CONFIRM = "confirm"
    RESOLVE = "resolve"
    PENDING = "pending"
    ERROR = "error"


@dataclass(frozen=True)
class MotionPolicy:
    semantic: MotionSemantic
    enabled: bool
    duration_ms: int
    decorative: bool = True


def motion_policy(
    semantic: MotionSemantic,
    *,
    reduced_motion: bool = False,
) -> MotionPolicy:
    """Map semantic feedback to motion without changing gameplay state.

    Reduced motion removes decoration and shortens transitions while preserving
    the information carried by the semantic state.
    """
    durations = {
        MotionSemantic.ENTER: 280,
        MotionSemantic.FOCUS: 120,
        MotionSemantic.CONFIRM: 180,
        MotionSemantic.RESOLVE: 360,
        MotionSemantic.PENDING: 240,
        MotionSemantic.ERROR: 160,
    }
    if reduced_motion:
        return MotionPolicy(semantic, enabled=True, duration_ms=0, decorative=False)
    return MotionPolicy(semantic, enabled=True, duration_ms=durations[semantic], decorative=True)

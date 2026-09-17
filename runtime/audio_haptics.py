from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class FeedbackSemantic(str, Enum):
    CHOICE_FOCUS = "choice_focus"
    CHOICE_CONFIRM = "choice_confirm"
    CONSEQUENCE_REVEAL = "consequence_reveal"
    CONSEQUENCE_PENDING = "consequence_pending"
    ERROR = "error"
    NAVIGATE = "navigate"
    ENDING_REVEAL = "ending_reveal"


@dataclass(frozen=True)
class FeedbackPolicy:
    semantic: FeedbackSemantic
    sound_id: str | None
    haptic_id: str | None
    intensity: float = 1.0
    interruptible: bool = True


def feedback_policy(
    semantic: FeedbackSemantic,
    *,
    sound_enabled: bool = True,
    haptics_enabled: bool = True,
) -> FeedbackPolicy:
    """Map player-facing semantics to premium feedback tokens.

    This is a presentation-only vocabulary. It does not trigger gameplay,
    calculate outcomes, or require a specific Android implementation.
    """
    tokens = {
        FeedbackSemantic.CHOICE_FOCUS: ("ui_focus", "tick_soft", 0.45),
        FeedbackSemantic.CHOICE_CONFIRM: ("choice_confirm", "confirm_medium", 0.75),
        FeedbackSemantic.CONSEQUENCE_REVEAL: ("consequence_reveal", "reveal_medium", 0.85),
        FeedbackSemantic.CONSEQUENCE_PENDING: ("pending_pulse", "pulse_soft", 0.55),
        FeedbackSemantic.ERROR: ("ui_error", "error_light", 0.70),
        FeedbackSemantic.NAVIGATE: ("ui_navigate", "tick_soft", 0.35),
        FeedbackSemantic.ENDING_REVEAL: ("ending_reveal", "reveal_strong", 1.0),
    }
    sound_id, haptic_id, intensity = tokens[semantic]
    return FeedbackPolicy(
        semantic=semantic,
        sound_id=sound_id if sound_enabled else None,
        haptic_id=haptic_id if haptics_enabled else None,
        intensity=intensity,
    )

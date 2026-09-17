from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .audio_haptics import FeedbackSemantic, feedback_policy
from .motion import MotionSemantic, motion_policy


class PlayerFeedbackState(str, Enum):
    FOCUS = "focus"
    CONFIRM = "confirm"
    REVEAL = "reveal"
    PENDING = "pending"
    ERROR = "error"
    NAVIGATE = "navigate"
    ENDING = "ending"


@dataclass(frozen=True)
class PremiumFeedback:
    state: PlayerFeedbackState
    feedback: object
    motion: object


def premium_feedback(
    state: PlayerFeedbackState,
    *,
    reduced_motion: bool = False,
    sound_enabled: bool = True,
    haptics_enabled: bool = True,
) -> PremiumFeedback:
    """Compose semantic motion and audio/haptic feedback without gameplay mutation."""
    mapping = {
        PlayerFeedbackState.FOCUS: (FeedbackSemantic.CHOICE_FOCUS, MotionSemantic.FOCUS),
        PlayerFeedbackState.CONFIRM: (FeedbackSemantic.CHOICE_CONFIRM, MotionSemantic.CONFIRM),
        PlayerFeedbackState.REVEAL: (FeedbackSemantic.CONSEQUENCE_REVEAL, MotionSemantic.RESOLVE),
        PlayerFeedbackState.PENDING: (FeedbackSemantic.CONSEQUENCE_PENDING, MotionSemantic.PENDING),
        PlayerFeedbackState.ERROR: (FeedbackSemantic.ERROR, MotionSemantic.ERROR),
        PlayerFeedbackState.NAVIGATE: (FeedbackSemantic.NAVIGATE, MotionSemantic.ENTER),
        PlayerFeedbackState.ENDING: (FeedbackSemantic.ENDING_REVEAL, MotionSemantic.RESOLVE),
    }
    feedback_semantic, motion_semantic = mapping[state]
    return PremiumFeedback(
        state=state,
        feedback=feedback_policy(
            feedback_semantic,
            sound_enabled=sound_enabled,
            haptics_enabled=haptics_enabled,
        ),
        motion=motion_policy(motion_semantic, reduced_motion=reduced_motion),
    )

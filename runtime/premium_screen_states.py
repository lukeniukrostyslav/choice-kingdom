from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ScreenState(str, Enum):
    DEFAULT = "default"
    FOCUSED = "focused"
    PRESSED = "pressed"
    SELECTED = "selected"
    DISABLED = "disabled"
    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "failure"
    ERROR = "error"


class PremiumScreen(str, Enum):
    EVENT = "event"
    REALM = "realm"
    HISTORY = "history"
    PEOPLE = "people"
    INVESTIGATION = "investigation"
    ENDING = "ending"
    SETTINGS = "settings"


@dataclass(frozen=True)
class ScreenStateContract:
    screen: PremiumScreen
    state: ScreenState
    semantic_label_required: bool = True
    visual_indicator_required: bool = True
    color_only_forbidden: bool = True


def screen_state_contract(
    screen: PremiumScreen,
    state: ScreenState,
) -> ScreenStateContract:
    """Return a presentation-only state contract for a premium screen."""
    return ScreenStateContract(screen=screen, state=state)


def required_states(screen: PremiumScreen) -> tuple[ScreenState, ...]:
    """Return the minimum shared state vocabulary required for each screen."""
    base = (
        ScreenState.DEFAULT,
        ScreenState.FOCUSED,
        ScreenState.PRESSED,
        ScreenState.DISABLED,
    )
    if screen is PremiumScreen.EVENT:
        return base + (ScreenState.SELECTED, ScreenState.PENDING, ScreenState.ERROR)
    if screen is PremiumScreen.INVESTIGATION:
        return base + (ScreenState.SELECTED, ScreenState.PENDING, ScreenState.SUCCESS)
    if screen is PremiumScreen.ENDING:
        return base + (ScreenState.SUCCESS, ScreenState.FAILURE)
    if screen is PremiumScreen.SETTINGS:
        return base + (ScreenState.SELECTED, ScreenState.ERROR)
    return base + (ScreenState.SELECTED,)

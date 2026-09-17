from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class WindowWidthClass(str, Enum):
    COMPACT = "compact"
    MEDIUM = "medium"
    EXPANDED = "expanded"


class NavigationMode(str, Enum):
    BOTTOM_BAR = "bottom_bar"
    NAVIGATION_RAIL = "navigation_rail"
    TWO_PANE = "two_pane"


@dataclass(frozen=True)
class AdaptiveNavigationModel:
    """Pure presentation contract derived from the current app window width.

    The runtime receives window space, not a physical device identity. This keeps
    layout decisions adaptive for phones, foldables, tablets and resizable windows.
    """

    width_dp: int
    width_class: WindowWidthClass
    mode: NavigationMode
    content_panes: int
    safe_insets_required: bool = True


def classify_width(width_dp: int) -> WindowWidthClass:
    if width_dp < 600:
        return WindowWidthClass.COMPACT
    if width_dp < 840:
        return WindowWidthClass.MEDIUM
    return WindowWidthClass.EXPANDED


def adaptive_navigation(width_dp: int) -> AdaptiveNavigationModel:
    """Return navigation/pane presentation without touching gameplay state."""
    width_class = classify_width(width_dp)
    if width_class is WindowWidthClass.COMPACT:
        mode = NavigationMode.BOTTOM_BAR
        panes = 1
    elif width_class is WindowWidthClass.MEDIUM:
        mode = NavigationMode.NAVIGATION_RAIL
        panes = 1
    else:
        mode = NavigationMode.TWO_PANE
        panes = 2
    return AdaptiveNavigationModel(
        width_dp=width_dp,
        width_class=width_class,
        mode=mode,
        content_panes=panes,
    )

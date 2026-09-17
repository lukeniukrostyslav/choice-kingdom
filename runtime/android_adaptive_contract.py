from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .adaptive_navigation import NavigationMode, WindowWidthClass, adaptive_navigation
from .safe_area import SafeInsets, safe_content_bounds


class AndroidPaneStrategy(str, Enum):
    SINGLE = "single"
    SUPPORTING = "supporting"
    TWO_PANE = "two_pane"


@dataclass(frozen=True)
class AndroidAdaptiveContract:
    width_dp: int
    height_dp: int
    width_class: WindowWidthClass
    navigation_mode: NavigationMode
    pane_strategy: AndroidPaneStrategy
    content_panes: int
    safe_content_width_dp: int
    safe_content_height_dp: int
    preserve_session_on_resize: bool = True


def android_adaptive_contract(
    width_dp: int,
    height_dp: int,
    insets: SafeInsets | None = None,
) -> AndroidAdaptiveContract:
    """Platform-facing presentation contract; it never mutates GameSession."""
    if width_dp < 0 or height_dp < 0:
        raise ValueError("window dimensions must be non-negative")
    nav = adaptive_navigation(width_dp)
    if nav.width_class is WindowWidthClass.EXPANDED:
        pane = AndroidPaneStrategy.TWO_PANE
    elif nav.width_class is WindowWidthClass.MEDIUM:
        pane = AndroidPaneStrategy.SUPPORTING
    else:
        pane = AndroidPaneStrategy.SINGLE
    safe = safe_content_bounds(width_dp, height_dp, insets or SafeInsets())
    return AndroidAdaptiveContract(
        width_dp=width_dp,
        height_dp=height_dp,
        width_class=nav.width_class,
        navigation_mode=nav.mode,
        pane_strategy=pane,
        content_panes=nav.content_panes,
        safe_content_width_dp=safe.content_width_dp,
        safe_content_height_dp=safe.content_height_dp,
    )

from __future__ import annotations

import pytest

from runtime.adaptive_navigation import NavigationMode, WindowWidthClass
from runtime.android_adaptive_contract import AndroidPaneStrategy, android_adaptive_contract
from runtime.safe_area import SafeInsets


def test_compact_uses_single_pane_and_bottom_navigation() -> None:
    model = android_adaptive_contract(390, 844, SafeInsets(top_dp=24, bottom_dp=34))
    assert model.width_class is WindowWidthClass.COMPACT
    assert model.navigation_mode is NavigationMode.BOTTOM_BAR
    assert model.pane_strategy is AndroidPaneStrategy.SINGLE
    assert model.content_panes == 1
    assert model.safe_content_height_dp == 786


def test_medium_uses_supporting_pane_and_navigation_rail() -> None:
    model = android_adaptive_contract(720, 1024)
    assert model.width_class is WindowWidthClass.MEDIUM
    assert model.navigation_mode is NavigationMode.NAVIGATION_RAIL
    assert model.pane_strategy is AndroidPaneStrategy.SUPPORTING
    assert model.content_panes == 1


def test_expanded_uses_two_panes() -> None:
    model = android_adaptive_contract(1200, 800)
    assert model.width_class is WindowWidthClass.EXPANDED
    assert model.navigation_mode is NavigationMode.TWO_PANE
    assert model.pane_strategy is AndroidPaneStrategy.TWO_PANE
    assert model.content_panes == 2


def test_invalid_dimensions_rejected() -> None:
    with pytest.raises(ValueError):
        android_adaptive_contract(-1, 800)

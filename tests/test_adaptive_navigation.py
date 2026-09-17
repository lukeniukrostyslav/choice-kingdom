from runtime.adaptive_navigation import (
    NavigationMode,
    WindowWidthClass,
    adaptive_navigation,
    classify_width,
)


def test_window_width_classes_use_available_window_space():
    assert classify_width(599) is WindowWidthClass.COMPACT
    assert classify_width(600) is WindowWidthClass.MEDIUM
    assert classify_width(839) is WindowWidthClass.MEDIUM
    assert classify_width(840) is WindowWidthClass.EXPANDED


def test_navigation_changes_with_width_class():
    compact = adaptive_navigation(390)
    medium = adaptive_navigation(700)
    expanded = adaptive_navigation(1024)

    assert compact.mode is NavigationMode.BOTTOM_BAR
    assert compact.content_panes == 1
    assert medium.mode is NavigationMode.NAVIGATION_RAIL
    assert medium.content_panes == 1
    assert expanded.mode is NavigationMode.TWO_PANE
    assert expanded.content_panes == 2


def test_adaptive_navigation_is_presentation_only():
    before = adaptive_navigation(390)
    after = adaptive_navigation(1024)

    assert before.width_dp == 390
    assert after.width_dp == 1024
    assert before.safe_insets_required is True
    assert after.safe_insets_required is True

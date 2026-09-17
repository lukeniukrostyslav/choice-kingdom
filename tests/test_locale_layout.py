from runtime.locale_layout import TextDensity, TextDirection, locale_layout_policy


def test_ltr_locale_keeps_navigation_direction():
    policy = locale_layout_policy("en-US")
    assert policy.direction is TextDirection.LTR
    assert policy.mirror_navigation is False
    assert policy.allow_wrap is True


def test_rtl_locale_mirrors_navigation_without_changing_text_policy():
    policy = locale_layout_policy("ar")
    assert policy.direction is TextDirection.RTL
    assert policy.mirror_navigation is True
    assert policy.allow_wrap is True


def test_large_text_expands_layout_instead_of_disabling_wrapping():
    policy = locale_layout_policy("uk-UA", large_text=True)
    assert policy.text_scale == 1.25
    assert policy.density is TextDensity.EXPANDED
    assert policy.allow_wrap is True

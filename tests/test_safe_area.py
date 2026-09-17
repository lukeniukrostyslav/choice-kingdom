from __future__ import annotations

import pytest

from runtime.safe_area import SafeInsets, safe_content_bounds


def test_safe_content_bounds_subtracts_system_insets() -> None:
    bounds = safe_content_bounds(
        390,
        844,
        SafeInsets(top_dp=24, end_dp=8, bottom_dp=34, start_dp=8),
    )
    assert bounds.content_width_dp == 374
    assert bounds.content_height_dp == 786


def test_safe_content_bounds_never_goes_negative() -> None:
    bounds = safe_content_bounds(20, 20, SafeInsets(top_dp=30, bottom_dp=30))
    assert bounds.content_width_dp == 20
    assert bounds.content_height_dp == 0


def test_negative_window_dimension_rejected() -> None:
    with pytest.raises(ValueError):
        safe_content_bounds(-1, 100, SafeInsets())

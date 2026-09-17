from runtime.premium_regression_matrix import (
    build_regression_matrix,
    regression_matrix_is_safe,
)


def test_regression_matrix_covers_every_screen_and_dimension() -> None:
    cases = build_regression_matrix()
    screens = {case.screen for case in cases}
    dimensions = {case.dimension for case in cases}
    assert len(screens) == 7
    assert len(dimensions) == 6


def test_regression_matrix_preserves_primary_action() -> None:
    cases = build_regression_matrix()
    assert regression_matrix_is_safe(cases)


def test_regression_matrix_contains_all_required_states() -> None:
    cases = build_regression_matrix()
    pairs = {(case.screen, case.state) for case in cases}
    assert len(pairs) >= 36

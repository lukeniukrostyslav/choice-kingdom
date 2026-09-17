from runtime.premium_screen_states import PremiumScreen, ScreenState
from runtime.premium_surface_projection import (
    SurfaceDensity,
    project_premium_surface,
)


def test_compact_keeps_primary_action_and_hides_secondary_context() -> None:
    projection = project_premium_surface(
        PremiumScreen.EVENT,
        ScreenState.DEFAULT,
        available_width_dp=390,
    )
    assert projection.density is SurfaceDensity.COMPACT
    assert projection.preserve_primary_action
    assert not projection.show_secondary_actions
    assert not projection.show_supporting_context


def test_medium_adds_supporting_context_for_information_surfaces() -> None:
    projection = project_premium_surface(
        PremiumScreen.HISTORY,
        ScreenState.SELECTED,
        available_width_dp=720,
    )
    assert projection.density is SurfaceDensity.COMFORTABLE
    assert projection.show_secondary_actions
    assert projection.show_supporting_context


def test_expanded_exposes_full_context() -> None:
    projection = project_premium_surface(
        PremiumScreen.INVESTIGATION,
        ScreenState.PENDING,
        available_width_dp=1000,
    )
    assert projection.density is SurfaceDensity.EXPANDED
    assert projection.show_secondary_actions
    assert projection.show_supporting_context


def test_width_validation() -> None:
    try:
        project_premium_surface(
            PremiumScreen.SETTINGS,
            ScreenState.DEFAULT,
            available_width_dp=319,
        )
    except ValueError as exc:
        assert "320dp" in str(exc)
    else:
        raise AssertionError("Expected invalid width to fail")

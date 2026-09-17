from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .premium_screen_states import PremiumScreen, ScreenState, required_states
from .premium_surface_projection import SurfaceDensity, project_premium_surface


class RegressionDimension(str, Enum):
    COMPACT = "compact"
    MEDIUM = "medium"
    EXPANDED = "expanded"
    RTL = "rtl"
    LARGE_TEXT = "large_text"
    REDUCED_MOTION = "reduced_motion"


@dataclass(frozen=True)
class RegressionCase:
    screen: PremiumScreen
    state: ScreenState
    dimension: RegressionDimension
    available_width_dp: int
    density: SurfaceDensity
    primary_action_preserved: bool


def build_regression_matrix() -> tuple[RegressionCase, ...]:
    widths = {
        RegressionDimension.COMPACT: 390,
        RegressionDimension.MEDIUM: 720,
        RegressionDimension.EXPANDED: 1000,
    }
    cases: list[RegressionCase] = []
    for screen in PremiumScreen:
        for state in required_states(screen):
            for dimension in RegressionDimension:
                width = widths.get(dimension, 390)
                projection = project_premium_surface(screen, state, available_width_dp=width)
                cases.append(
                    RegressionCase(
                        screen=screen,
                        state=state,
                        dimension=dimension,
                        available_width_dp=width,
                        density=projection.density,
                        primary_action_preserved=projection.preserve_primary_action,
                    )
                )
    return tuple(cases)


def regression_matrix_is_safe(cases: tuple[RegressionCase, ...]) -> bool:
    return bool(cases) and all(case.primary_action_preserved for case in cases)

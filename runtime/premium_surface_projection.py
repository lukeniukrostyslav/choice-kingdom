from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .premium_screen_states import PremiumScreen, ScreenState


class SurfaceDensity(str, Enum):
    COMPACT = "compact"
    COMFORTABLE = "comfortable"
    EXPANDED = "expanded"


@dataclass(frozen=True)
class PremiumSurfaceProjection:
    screen: PremiumScreen
    state: ScreenState
    density: SurfaceDensity
    show_secondary_actions: bool
    show_supporting_context: bool
    preserve_primary_action: bool = True


def project_premium_surface(
    screen: PremiumScreen,
    state: ScreenState,
    *,
    available_width_dp: int,
) -> PremiumSurfaceProjection:
    """Pure presentation projection for a premium screen surface.

    The projection responds to available app-window width rather than device identity
    and never mutates gameplay state.
    """
    if available_width_dp < 320:
        raise ValueError("available_width_dp must be at least 320dp")

    if available_width_dp < 600:
        density = SurfaceDensity.COMPACT
        secondary = False
        context = False
    elif available_width_dp < 840:
        density = SurfaceDensity.COMFORTABLE
        secondary = True
        context = screen in {
            PremiumScreen.REALM,
            PremiumScreen.HISTORY,
            PremiumScreen.PEOPLE,
            PremiumScreen.INVESTIGATION,
        }
    else:
        density = SurfaceDensity.EXPANDED
        secondary = True
        context = True

    return PremiumSurfaceProjection(
        screen=screen,
        state=state,
        density=density,
        show_secondary_actions=secondary,
        show_supporting_context=context,
    )

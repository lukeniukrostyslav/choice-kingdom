from __future__ import annotations

from dataclasses import dataclass

from .consequence_screen import ConsequenceHost
from .premium_screen_states import PremiumScreen, ScreenState
from .premium_surface_projection import PremiumSurfaceProjection, project_premium_surface
from .presentation import SessionPresenter


@dataclass(frozen=True)
class PremiumConsequenceSurface:
    projection: PremiumSurfaceProjection
    model: object


class PremiumConsequenceHost:
    """Adaptive presentation boundary for the transient consequence surface.

    The host owns only presentation density. Consequence calculation, routing,
    delayed activation and gameplay mutation remain inside ConsequenceHost and
    the canonical GameSession boundary.
    """

    def __init__(self, presenter: SessionPresenter):
        self._consequence = ConsequenceHost(presenter)

    def render(
        self,
        *,
        state: ScreenState = ScreenState.SUCCESS,
        available_width_dp: int = 390,
    ) -> PremiumConsequenceSurface:
        projection = project_premium_surface(
            PremiumScreen.EVENT,
            state,
            available_width_dp=available_width_dp,
        )
        return PremiumConsequenceSurface(
            projection=projection,
            model=self._consequence.render(),
        )

    def commit(
        self,
        choice_id: str,
        *,
        available_width_dp: int = 390,
    ) -> PremiumConsequenceSurface:
        self._consequence.commit(choice_id)
        return self.render(
            state=ScreenState.PENDING if self._consequence.render().pending_delay_count else ScreenState.SUCCESS,
            available_width_dp=available_width_dp,
        )

    def dismiss(self) -> None:
        self._consequence.dismiss()

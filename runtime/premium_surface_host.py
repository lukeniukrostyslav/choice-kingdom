from __future__ import annotations

from dataclasses import dataclass

from .event_screen import EventChoiceHost
from .journey_screens import JourneyScreenHost
from .premium_screen_states import PremiumScreen, ScreenState
from .premium_surface_projection import PremiumSurfaceProjection, project_premium_surface
from .presentation import SessionPresenter


@dataclass(frozen=True)
class PremiumHostedSurface:
    projection: PremiumSurfaceProjection
    model: object


class PremiumSurfaceHost:
    """Bind adaptive premium presentation to the production screen hosts.

    This host is presentation-only: it chooses density and forwards existing
    immutable screen models. It never evaluates or mutates gameplay state.
    """

    def __init__(self, presenter: SessionPresenter):
        self._event = EventChoiceHost(presenter)
        self._screens = JourneyScreenHost(presenter)

    def render(
        self,
        screen: PremiumScreen,
        *,
        state: ScreenState = ScreenState.DEFAULT,
        available_width_dp: int = 390,
    ) -> PremiumHostedSurface:
        projection = project_premium_surface(
            screen,
            state,
            available_width_dp=available_width_dp,
        )
        models = {
            PremiumScreen.EVENT: self._event.render,
            PremiumScreen.REALM: self._screens.realm,
            PremiumScreen.HISTORY: self._screens.history,
            PremiumScreen.PEOPLE: self._screens.people,
            PremiumScreen.INVESTIGATION: self._screens.investigation,
            PremiumScreen.ENDING: self._screens.ending,
            PremiumScreen.SETTINGS: self._screens.settings,
        }
        if screen not in models:
            raise ValueError(f"screen host not available for {screen.value}")
        return PremiumHostedSurface(projection=projection, model=models[screen]())

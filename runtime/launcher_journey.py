from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .main_menu import MainMenuDestination, MainMenuScreen
from .motion import MotionSemantic, MotionPolicy, motion_policy
from .premium_journey import JourneySurface, JourneyView, PremiumJourneyHost


class LauncherRoute(str, Enum):
    MENU = "menu"
    JOURNEY = "journey"


@dataclass(frozen=True)
class LauncherView:
    route: LauncherRoute
    menu: MainMenuScreen | None = None
    journey: JourneyView | None = None
    motion: MotionPolicy | None = None


class PremiumLauncherHost:
    """Presentation-only bridge from the launcher into the premium journey."""

    def __init__(self, menu: MainMenuScreen, journey: PremiumJourneyHost):
        self.menu = menu
        self.journey = journey
        self._route = LauncherRoute.MENU

    @property
    def route(self) -> LauncherRoute:
        return self._route

    def render(self, *, reduced_motion: bool = False) -> LauncherView:
        if self._route is LauncherRoute.MENU:
            return LauncherView(
                route=self._route,
                menu=self.menu,
                motion=motion_policy(MotionSemantic.ENTER, reduced_motion=reduced_motion),
            )
        return LauncherView(
            route=self._route,
            journey=self.journey.render(),
            motion=motion_policy(MotionSemantic.ENTER, reduced_motion=reduced_motion),
        )

    def activate(self, destination: MainMenuDestination) -> LauncherView:
        if destination is MainMenuDestination.CONTINUE:
            self.journey.restore_event()
        elif destination is MainMenuDestination.NEW_RUN:
            self.journey.restore_event()
        elif destination is MainMenuDestination.HISTORY:
            self.journey.show(JourneySurface.HISTORY)
        elif destination is MainMenuDestination.SETTINGS:
            self.journey.show(JourneySurface.SETTINGS)
        else:
            raise ValueError(f"Unsupported launcher destination: {destination}")
        self._route = LauncherRoute.JOURNEY
        return self.render()

    def back_to_menu(self) -> LauncherView:
        self._route = LauncherRoute.MENU
        return self.render()

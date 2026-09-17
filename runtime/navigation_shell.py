from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .adaptive_navigation import AdaptiveNavigationModel
from .main_menu import MainMenuScreen, build_main_menu
from .premium_journey import JourneySurface, JourneyView, PremiumJourneyHost
from .presentation import SessionPresentation, SessionPresenter


class AppDestination(str, Enum):
    MENU = "menu"
    JOURNEY = "journey"


@dataclass(frozen=True)
class AppShellView:
    destination: AppDestination
    model: MainMenuScreen | JourneyView


class PremiumNavigationShell:
    """Single presentation navigation boundary for launcher and journey.

    It changes only presentation destination/surface. Gameplay mutations remain
    inside SessionPresenter/GameSession and are never duplicated here.
    """

    def __init__(self, presenter: SessionPresenter, navigation: AdaptiveNavigationModel):
        self.presenter = presenter
        self.navigation = navigation
        self.journey = PremiumJourneyHost(presenter)
        self._destination = AppDestination.MENU

    @property
    def destination(self) -> AppDestination:
        return self._destination

    def render(self) -> AppShellView:
        if self._destination is AppDestination.MENU:
            return AppShellView(
                AppDestination.MENU,
                build_main_menu(self.presenter.snapshot(), self.navigation),
            )
        return AppShellView(AppDestination.JOURNEY, self.journey.render())

    def open_journey(self, surface: JourneySurface = JourneySurface.EVENT) -> AppShellView:
        self._destination = AppDestination.JOURNEY
        self.journey.show(surface)
        return self.render()

    def open_menu(self) -> AppShellView:
        self._destination = AppDestination.MENU
        return self.render()

    def show_journey(self, surface: JourneySurface) -> AppShellView:
        return self.open_journey(surface)

    def commit_choice(self, choice_id: str) -> AppShellView:
        self._destination = AppDestination.JOURNEY
        self.journey.commit_choice(choice_id)
        return self.render()

    def dismiss_consequence(self) -> AppShellView:
        self.journey.dismiss_consequence()
        return self.render()

from __future__ import annotations

from dataclasses import dataclass

from runtime.launcher_journey import LauncherRoute, PremiumLauncherHost
from runtime.main_menu import MainMenuDestination, MainMenuScreen
from runtime.premium_journey import JourneySurface, JourneyView


@dataclass
class FakeJourney:
    surface: JourneySurface = JourneySurface.EVENT

    def restore_event(self) -> JourneyView:
        self.surface = JourneySurface.EVENT
        return JourneyView(self.surface, object())

    def show(self, surface: JourneySurface) -> JourneyView:
        self.surface = surface
        return JourneyView(self.surface, object())

    def render(self) -> JourneyView:
        return JourneyView(self.surface, object())


def menu() -> MainMenuScreen:
    return MainMenuScreen("Avelune", "", (), object(), False, None)  # type: ignore[arg-type]


def test_launcher_starts_on_menu() -> None:
    host = PremiumLauncherHost(menu(), FakeJourney())
    assert host.route is LauncherRoute.MENU
    assert host.render().menu is not None


def test_continue_and_new_run_enter_event_without_navigation_mutation() -> None:
    journey = FakeJourney()
    host = PremiumLauncherHost(menu(), journey)

    host.activate(MainMenuDestination.CONTINUE)
    assert host.route is LauncherRoute.JOURNEY
    assert journey.surface is JourneySurface.EVENT

    host.back_to_menu()
    host.activate(MainMenuDestination.NEW_RUN)
    assert journey.surface is JourneySurface.EVENT


def test_history_and_settings_are_presentation_routes() -> None:
    journey = FakeJourney()
    host = PremiumLauncherHost(menu(), journey)

    host.activate(MainMenuDestination.HISTORY)
    assert journey.surface is JourneySurface.HISTORY

    host.back_to_menu()
    host.activate(MainMenuDestination.SETTINGS)
    assert journey.surface is JourneySurface.SETTINGS

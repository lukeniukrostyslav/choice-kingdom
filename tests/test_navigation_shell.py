from dataclasses import dataclass

from runtime.adaptive_navigation import adaptive_navigation
from runtime.navigation_shell import AppDestination, PremiumNavigationShell
from runtime.presentation import (
    DelayPresentation,
    ResourcePresentation,
    RelationshipPresentation,
    SessionPresentation,
)


@dataclass
class RenderOnlyPresenter:
    model: SessionPresentation

    def snapshot(self):
        return self.model


def presenter():
    return RenderOnlyPresenter(
        SessionPresentation(
            run_id="run-1",
            turn=7,
            event_id="E07",
            title="The Eastern Gate",
            trigger="story",
            choices=(),
            resources=(ResourcePresentation("gold", 54),),
            relationships=(RelationshipPresentation("mara", 78),),
            history=("E01-A", "E04-B"),
            threads=("thread-gate",),
            pending_delays=(DelayPresentation("delay-1", "E09", "pending", 9, "E07"),),
            ending_evidence=("evidence-gate",),
            terminal=False,
            ending_identity=None,
        )
    )


def test_launcher_opens_journey_without_replacing_canonical_snapshot():
    presenter_instance = presenter()
    shell = PremiumNavigationShell(presenter_instance, adaptive_navigation(390))

    menu = shell.render()
    journey = shell.open_journey()

    assert menu.destination is AppDestination.MENU
    assert journey.destination is AppDestination.JOURNEY
    assert journey.model.model.event_id == "E07"
    assert presenter_instance.model.turn == 7


def test_return_to_menu_preserves_session_context():
    presenter_instance = presenter()
    shell = PremiumNavigationShell(presenter_instance, adaptive_navigation(840))

    shell.open_journey()
    menu = shell.open_menu()

    assert menu.destination is AppDestination.MENU
    assert menu.model.has_continue is True
    assert menu.model.last_event_id == "E07"
    assert menu.model.navigation.mode.value == "two_pane"


def test_navigation_shell_is_presentation_only():
    presenter_instance = presenter()
    shell = PremiumNavigationShell(presenter_instance, adaptive_navigation(600))

    shell.show_journey(shell.journey.surface)
    shell.open_menu()

    assert presenter_instance.model.resources[0].value == 54
    assert presenter_instance.model.history == ("E01-A", "E04-B")

from runtime.adaptive_navigation import adaptive_navigation
from runtime.main_menu import MainMenuDestination, build_main_menu
from runtime.presentation import SessionPresentation


def test_main_menu_has_continue_for_active_run_only():
    session = SessionPresentation(
        run_id="run-1",
        turn=3,
        event_id="E03",
        title="Gate",
        trigger="story",
        choices=(),
        resources=(),
        relationships=(),
        history=("E01-A",),
        threads=(),
        pending_delays=(),
        ending_evidence=(),
        terminal=False,
        ending_identity=None,
    )

    menu = build_main_menu(session, adaptive_navigation(390))

    assert menu.has_continue is True
    assert menu.last_event_id == "E03"
    assert menu.actions[0].destination is MainMenuDestination.CONTINUE
    assert menu.actions[0].enabled is True
    assert menu.navigation.content_panes == 1


def test_main_menu_never_invents_continue_after_terminal_run():
    session = SessionPresentation(
        run_id="run-1",
        turn=99,
        event_id="E272",
        title="Ending",
        trigger="ending",
        choices=(),
        resources=(),
        relationships=(),
        history=(),
        threads=(),
        pending_delays=(),
        ending_evidence=("ending-proof",),
        terminal=True,
        ending_identity="ending-a",
    )

    menu = build_main_menu(session, adaptive_navigation(1000))

    assert menu.has_continue is False
    assert menu.actions[0].enabled is False
    assert menu.navigation.mode.value == "two_pane"


def test_main_menu_without_session_stays_presentation_only():
    menu = build_main_menu(None, adaptive_navigation(700))

    assert menu.has_continue is False
    assert menu.last_event_id is None
    assert menu.actions[1].enabled is True
    assert menu.actions[2].enabled is False
    assert menu.navigation.mode.value == "navigation_rail"

from __future__ import annotations

from pathlib import Path

from runtime.event_screen import EventChoiceHost
from runtime.presentation import InteractionState, SessionPresenter, present
from runtime.session import GameSession, SessionView

ROOT = Path(__file__).resolve().parents[1]


def test_event_choice_host_renders_authored_event_and_choices() -> None:
    host = EventChoiceHost(SessionPresenter(GameSession.new(ROOT, "event-screen")))
    screen = host.render()
    assert screen.session.event_id == "E01"
    assert screen.session.title
    assert [choice.choice_id for choice in screen.session.choices] == ["E01-A", "E01-B"]
    assert screen.selected_choice_id is None
    assert screen.can_interact is True


def test_event_choice_host_maps_focus_and_press_without_mutating_gameplay() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "event-screen-interaction"))
    host = EventChoiceHost(presenter)
    before = presenter.session.snapshot_digest()
    focused = host.focus("E01-A")
    assert focused.session.choices[0].state is InteractionState.FOCUSED
    assert focused.selected_choice_id == "E01-A"
    assert presenter.session.snapshot_digest() == before
    pressed = host.press("E01-A")
    assert pressed.session.choices[0].state is InteractionState.PRESSED
    assert pressed.selected_choice_id == "E01-A"
    assert presenter.session.snapshot_digest() == before
    presenter.begin_choice("E01-A")
    resolving = host.render()
    assert resolving.session.choices[0].state is InteractionState.RESOLVING
    assert resolving.selected_choice_id == "E01-A"
    assert presenter.session.snapshot_digest() == before


def test_event_choice_host_commits_only_through_presenter_and_renders_next_event() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "event-screen-choice"))
    host = EventChoiceHost(presenter)
    result, screen = host.choose("E01-A")
    assert result.event_id == "E01"
    assert result.choice_id == "E01-A"
    assert screen.session.event_id == "E02"
    assert screen.selected_choice_id is None
    assert presenter.session.state.history == {"E01"}
    assert presenter.session.state.flags == {"open_petition_hall"}


def test_event_choice_host_rejects_unavailable_choice_before_mutation() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "event-screen-invalid"))
    host = EventChoiceHost(presenter)
    before = presenter.session.snapshot_digest()
    try:
        host.choose("NOT-A-REAL-CHOICE")
    except ValueError as exc:
        assert "not currently available" in str(exc)
    else:
        raise AssertionError("unavailable choice must be rejected")
    assert presenter.session.snapshot_digest() == before


def test_terminal_session_projects_visible_choices_as_disabled() -> None:
    view = SessionView(
        run_id="terminal-preview",
        turn=7,
        event_id="E272",
        title="Final Chronicle",
        trigger="terminal",
        choices=(("E272-A", "Archive", "Close the chronicle."),),
        resources=(),
        relationships=(),
        terminal=True,
        ending_identity="ending-alpha",
    )
    model = present(view)
    assert model.terminal is True
    assert model.choices[0].state is InteractionState.DISABLED
    assert model.ending_identity == "ending-alpha"

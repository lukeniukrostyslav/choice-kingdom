from __future__ import annotations

from pathlib import Path

from runtime.presentation import InteractionState, SessionPresenter, present
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_presentation_projects_authored_event_without_reimplementing_rules() -> None:
    session = GameSession.new(ROOT, "presentation-runtime")
    model = present(session.view())

    assert model.event_id == "E01"
    assert model.turn == 1
    assert [choice.choice_id for choice in model.choices] == ["E01-A", "E01-B"]
    assert all(choice.state is InteractionState.IDLE for choice in model.choices)
    assert dict((item.key, item.value) for item in model.resources) == dict(session.view().resources)


def test_presenter_exposes_focused_and_resolving_choice_states() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "presentation-interactions"))

    presenter.focus_choice("E01-A")
    focused = presenter.snapshot()
    assert focused.choices[0].state is InteractionState.FOCUSED
    assert focused.choices[1].state is InteractionState.IDLE

    presenter.press_choice("E01-A")
    resolving = presenter.snapshot()
    assert resolving.choices[0].state is InteractionState.RESOLVING
    assert resolving.choices[1].state is InteractionState.IDLE


def test_presenter_routes_choice_through_game_session_and_clears_transient_state() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "presentation-choice"))

    presenter.choose("E01-A")
    resolved = presenter.snapshot()

    assert resolved.event_id == "E01"
    assert all(choice.state is InteractionState.IDLE for choice in resolved.choices)
    assert presenter.session.state.history == {"E01"}
    assert presenter.session.state.flags == {"open_petition_hall", "E07_market_whispers"}
    assert presenter.session.state.current_event_id == "E01"


def test_presenter_rejects_unavailable_choice_before_runtime_mutation() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "presentation-invalid"))
    before = presenter.session.snapshot_digest()

    try:
        presenter.begin_choice("NOT-A-REAL-CHOICE")
    except ValueError as exc:
        assert "not currently available" in str(exc)
    else:
        raise AssertionError("unavailable choice must be rejected")

    assert presenter.session.snapshot_digest() == before


def test_presenter_select_event_uses_engine_qualification_and_resets_ui_state() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "presentation-navigation"))
    presenter.focus_choice("E01-A")

    presenter.session.choose("E01-A")
    presenter.select_event("E02")
    model = presenter.snapshot()

    assert model.event_id == "E02"
    assert all(choice.state is InteractionState.IDLE for choice in model.choices)

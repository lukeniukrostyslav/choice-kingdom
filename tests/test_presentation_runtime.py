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


def test_presenter_exposes_resolving_and_resolved_choice_states() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "presentation-interactions"))

    presenter.begin_choice("E01-A")
    resolving = presenter.snapshot()
    assert resolving.choices[0].state is InteractionState.RESOLVING
    assert resolving.choices[1].state is InteractionState.IDLE

    presenter.choose("E01-A")
    resolved = presenter.snapshot()
    assert resolved.event_id == "E02"
    assert resolved.choices[0].state is InteractionState.RESOLVED or all(
        choice.state is InteractionState.IDLE for choice in resolved.choices
    )


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

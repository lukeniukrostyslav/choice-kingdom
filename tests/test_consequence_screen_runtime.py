from __future__ import annotations

from pathlib import Path

from runtime.consequence_screen import ConsequenceHost
from runtime.presentation import SessionPresenter
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_consequence_host_projects_authored_choice_result_and_post_state() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "consequence-screen"))
    host = ConsequenceHost(presenter)

    screen = host.commit("E01-A")

    assert screen.event_id == "E01"
    assert screen.choice_id == "E01-A"
    assert screen.next_event_ids == ("E02",)
    assert screen.session.event_id == "E02"
    assert screen.session.history == ("E01",)
    assert screen.pending_delay_count == 0
    assert screen.terminal is False


def test_consequence_host_does_not_invent_effects_and_dismiss_is_presentation_only() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "consequence-screen-dismiss"))
    host = ConsequenceHost(presenter)

    host.commit("E01-A")
    after_commit = presenter.session.snapshot_digest()
    host.dismiss()

    assert presenter.session.snapshot_digest() == after_commit
    assert presenter.session.state.flags == {"open_petition_hall"}
    assert presenter.session.state.history == {"E01"}


def test_consequence_host_requires_a_real_engine_result_before_render() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "consequence-screen-empty"))
    host = ConsequenceHost(presenter)

    try:
        host.render()
    except RuntimeError as exc:
        assert "no consequence result" in str(exc)
    else:
        raise AssertionError("consequence screen must not fabricate a result")

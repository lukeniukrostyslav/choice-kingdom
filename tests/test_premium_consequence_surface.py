from __future__ import annotations

from pathlib import Path

from runtime.premium_consequence_surface import PremiumConsequenceHost
from runtime.premium_screen_states import PremiumScreen, ScreenState
from runtime.premium_surface_projection import SurfaceDensity
from runtime.presentation import SessionPresenter
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def test_consequence_surface_projects_a_real_authored_choice_result() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "premium-consequence"))
    host = PremiumConsequenceHost(presenter)

    surface = host.commit("E01-A", available_width_dp=390)

    assert surface.model.event_id == "E01"
    assert surface.model.choice_id == "E01-A"
    assert surface.model.next_event_ids == ("E02",)
    assert surface.model.session.event_id == "E02"
    assert surface.model.session.history == ("E01",)
    assert surface.model.pending_delay_count == 0
    assert surface.projection.screen is PremiumScreen.EVENT
    assert surface.projection.state is ScreenState.SUCCESS
    assert surface.projection.density is SurfaceDensity.COMPACT
    assert surface.projection.preserve_primary_action is True


def test_consequence_surface_adapts_without_changing_the_canonical_result() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "premium-consequence-adaptive"))
    host = PremiumConsequenceHost(presenter)

    compact = host.commit("E01-A", available_width_dp=390)
    digest = presenter.session.snapshot_digest()
    expanded = host.render(state=ScreenState.SUCCESS, available_width_dp=1000)

    assert compact.model.event_id == expanded.model.event_id == "E01"
    assert compact.model.choice_id == expanded.model.choice_id == "E01-A"
    assert compact.model.next_event_ids == expanded.model.next_event_ids == ("E02",)
    assert compact.model.session.event_id == expanded.model.session.event_id == "E02"
    assert compact.projection.density is SurfaceDensity.COMPACT
    assert expanded.projection.density is SurfaceDensity.EXPANDED
    assert expanded.projection.show_supporting_context is True
    assert expanded.projection.preserve_primary_action is True
    assert presenter.session.snapshot_digest() == digest


def test_consequence_surface_dismiss_is_presentation_only() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "premium-consequence-dismiss"))
    host = PremiumConsequenceHost(presenter)

    host.commit("E01-A")
    digest = presenter.session.snapshot_digest()
    host.dismiss()

    assert presenter.session.snapshot_digest() == digest
    assert presenter.session.state.flags == {"open_petition_hall"}
    assert presenter.session.state.history == {"E01"}


def test_consequence_surface_does_not_fabricate_a_result_before_commit() -> None:
    presenter = SessionPresenter(GameSession.new(ROOT, "premium-consequence-empty"))
    host = PremiumConsequenceHost(presenter)

    try:
        host.render()
    except RuntimeError as exc:
        assert "no consequence result" in str(exc)
    else:
        raise AssertionError("premium consequence surface must not fabricate a result")

from __future__ import annotations

from pathlib import Path

from runtime.premium_consequence_surface import PremiumConsequenceHost
from runtime.premium_screen_states import ScreenState
from runtime.presentation import SessionPresenter
from runtime.session import GameSession

ROOT = Path(__file__).resolve().parents[1]


def _host(run_id: str) -> tuple[SessionPresenter, PremiumConsequenceHost]:
    presenter = SessionPresenter(GameSession.new(ROOT, run_id))
    return presenter, PremiumConsequenceHost(presenter)


def test_consequence_surface_preserves_primary_action_across_required_widths() -> None:
    _, host = _host("premium-consequence-widths")
    host.commit("E01-A", available_width_dp=390)

    compact = host.render(state=ScreenState.SUCCESS, available_width_dp=390)
    medium = host.render(state=ScreenState.SUCCESS, available_width_dp=720)
    expanded = host.render(state=ScreenState.SUCCESS, available_width_dp=1200)

    assert compact.projection.preserve_primary_action
    assert medium.projection.preserve_primary_action
    assert expanded.projection.preserve_primary_action
    assert compact.projection.show_secondary_actions is False
    assert medium.projection.show_secondary_actions is True
    assert expanded.projection.show_supporting_context is True


def test_consequence_surface_pending_state_is_presentation_only() -> None:
    presenter, host = _host("premium-consequence-pending")
    host.commit("E01-A")
    before = presenter.session.snapshot_digest()

    pending = host.render(state=ScreenState.PENDING, available_width_dp=720)

    assert pending.projection.state is ScreenState.PENDING
    assert pending.model.event_id == "E01"
    assert pending.model.choice_id == "E01-A"
    assert pending.model.session.event_id == "E02"
    assert presenter.session.snapshot_digest() == before

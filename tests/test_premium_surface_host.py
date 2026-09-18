from runtime.premium_screen_states import PremiumScreen, ScreenState
from runtime.premium_surface_host import PremiumSurfaceHost
from runtime.premium_surface_projection import SurfaceDensity
from runtime.presentation import SessionPresentation, ChoicePresentation


class StubPresenter:
    def snapshot(self):
        return SessionPresentation(
            run_id="test", turn=1, event_id="E01", title="Test", trigger="test",
            choices=(ChoicePresentation("E01-A", "A", "Open the Hall"),),
            resources=(), relationships=(), history=(), threads=(), pending_delays=(),
            ending_evidence=(), terminal=False, ending_identity=None,
        )

    def focus_choice(self, choice_id: str):
        return None


def test_surface_host_binds_adaptive_projection_to_history() -> None:
    hosted = PremiumSurfaceHost(StubPresenter()).render(
        PremiumScreen.HISTORY,
        state=ScreenState.SELECTED,
        available_width_dp=720,
    )
    assert hosted.projection.density is SurfaceDensity.COMFORTABLE
    assert hosted.projection.preserve_primary_action
    assert hosted.model is not None


def test_surface_host_binds_expanded_investigation() -> None:
    hosted = PremiumSurfaceHost(StubPresenter()).render(
        PremiumScreen.INVESTIGATION,
        state=ScreenState.PENDING,
        available_width_dp=1000,
    )
    assert hosted.projection.density is SurfaceDensity.EXPANDED
    assert hosted.projection.show_supporting_context


def test_surface_host_binds_event_surface() -> None:
    hosted = PremiumSurfaceHost(StubPresenter()).render(
        PremiumScreen.EVENT,
        state=ScreenState.FOCUSED,
        available_width_dp=390,
    )
    assert hosted.projection.density is SurfaceDensity.COMPACT
    assert hosted.projection.preserve_primary_action
    assert hosted.model is not None

from runtime.premium_screen_states import PremiumScreen, ScreenState
from runtime.premium_surface_host import PremiumSurfaceHost
from runtime.premium_surface_projection import SurfaceDensity


class StubPresenter:
    def snapshot(self):
        return object()


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


def test_surface_host_rejects_unbound_event_surface() -> None:
    try:
        PremiumSurfaceHost(StubPresenter()).render(PremiumScreen.EVENT)
    except ValueError as exc:
        assert "event" in str(exc)
    else:
        raise AssertionError("Expected event surface to require EventChoiceHost")

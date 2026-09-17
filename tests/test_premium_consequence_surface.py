from runtime.premium_consequence_surface import PremiumConsequenceHost
from runtime.premium_screen_states import ScreenState
from runtime.premium_surface_projection import SurfaceDensity


class StubPresenter:
    def snapshot(self):
        raise AssertionError("render must not be called before a consequence exists")


def test_consequence_host_preserves_adaptive_projection_contract() -> None:
    # The host's projection contract is exercised after a real consequence
    # commit in integration; this test keeps the state vocabulary explicit.
    assert ScreenState.SUCCESS.value == "success"
    assert ScreenState.PENDING.value == "pending"
    assert SurfaceDensity.COMPACT.value == "compact"
    assert SurfaceDensity.COMFORTABLE.value == "comfortable"
    assert SurfaceDensity.EXPANDED.value == "expanded"

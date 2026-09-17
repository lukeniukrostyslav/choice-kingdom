from dataclasses import dataclass

from runtime.premium_journey import JourneySurface, PremiumJourneyHost
from runtime.presentation import (
    DelayPresentation,
    ResourcePresentation,
    RelationshipPresentation,
    SessionPresentation,
)


@dataclass
class FakePresenter:
    snapshots: list[SessionPresentation]

    def snapshot(self):
        return self.snapshots[-1]

    def choose(self, choice_id):
        raise AssertionError("choice commits must be exercised through the real presenter")


class RenderOnlyPresenter:
    def __init__(self):
        self.model = SessionPresentation(
            run_id="run-1",
            turn=7,
            event_id="E07",
            title="The Eastern Gate",
            trigger="story",
            choices=(),
            resources=(ResourcePresentation("gold", 54),),
            relationships=(RelationshipPresentation("mara", 78),),
            history=("E01-A", "E04-B"),
            threads=("thread-gate",),
            pending_delays=(DelayPresentation("delay-1", "E09", "pending", 9, "E07"),),
            ending_evidence=("evidence-gate",),
            terminal=False,
            ending_identity=None,
        )

    def snapshot(self):
        return self.model


def test_navigation_changes_surface_without_changing_snapshot():
    presenter = RenderOnlyPresenter()
    host = PremiumJourneyHost(presenter)

    event = host.render()
    realm = host.show(JourneySurface.REALM)
    history = host.show(JourneySurface.HISTORY)
    ending = host.show(JourneySurface.ENDING)

    assert event.surface is JourneySurface.EVENT
    assert realm.surface is JourneySurface.REALM
    assert realm.model.resources[0].value == 54
    assert history.model.entries == ("E01-A", "E04-B")
    assert ending.model.terminal is False
    assert presenter.model.event_id == "E07"


def test_settings_are_a_navigation_projection_not_gameplay_state():
    presenter = RenderOnlyPresenter()
    host = PremiumJourneyHost(presenter)

    view = host.settings(reduced_motion=True, large_text=True, rtl=True)

    assert view.surface is JourneySurface.SETTINGS
    assert view.model.reduced_motion is True
    assert view.model.large_text is True
    assert view.model.rtl is True
    assert presenter.model.turn == 7

from runtime.journey_screens import JourneyScreenHost
from runtime.presentation import (
    DelayPresentation,
    InteractionState,
    ResourcePresentation,
    RelationshipPresentation,
    SessionPresentation,
)


class FakePresenter:
    def snapshot(self):
        return SessionPresentation(
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


def test_journey_surfaces_share_one_canonical_snapshot():
    host = JourneyScreenHost(FakePresenter())

    assert host.realm().resources[0].value == 54
    assert host.realm().pending_consequences[0].target_event_id == "E09"
    assert host.history().entries == ("E01-A", "E04-B")
    assert host.people().relationships[0].key == "mara"
    assert host.investigation().threads == ("thread-gate",)
    assert host.investigation().evidence == ("evidence-gate",)
    assert host.ending().ending_identity is None
    assert host.ending().terminal is False


def test_settings_are_presentation_only():
    settings = JourneyScreenHost.settings(reduced_motion=True, large_text=True, rtl=True)

    assert settings.reduced_motion is True
    assert settings.large_text is True
    assert settings.rtl is True

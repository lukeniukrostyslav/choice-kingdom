from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .consequence_screen import ConsequenceHost, ConsequenceScreen
from .event_screen import EventChoiceHost, EventChoiceScreen
from .journey_screens import (
    EndingScreen,
    HistoryScreen,
    InvestigationScreen,
    PeopleScreen,
    RealmScreen,
    SettingsScreen,
    JourneyScreenHost,
)
from .presentation import SessionPresenter


class JourneySurface(str, Enum):
    EVENT = "event"
    CONSEQUENCE = "consequence"
    REALM = "realm"
    HISTORY = "history"
    PEOPLE = "people"
    INVESTIGATION = "investigation"
    ENDING = "ending"
    SETTINGS = "settings"


@dataclass(frozen=True)
class JourneyView:
    """Immutable navigation projection for the premium journey host.

    Navigation owns only which presentation surface is visible. Gameplay state,
    choice qualification, consequences, and routing remain owned by the existing
    SessionPresenter/GameSession boundary.
    """

    surface: JourneySurface
    model: Any


class PremiumJourneyHost:
    """Compose the production-facing screen hosts into one UI boundary.

    This class deliberately contains no gameplay rules. It translates navigation
    intents into screen projections and delegates choice commits to the canonical
    EventChoiceHost/ConsequenceHost pair.
    """

    def __init__(self, presenter: SessionPresenter):
        self.presenter = presenter
        self.event = EventChoiceHost(presenter)
        self.consequence = ConsequenceHost(presenter)
        self.journey = JourneyScreenHost(presenter)
        self._surface = JourneySurface.EVENT

    @property
    def surface(self) -> JourneySurface:
        return self._surface

    def show(self, surface: JourneySurface) -> JourneyView:
        """Change only the visible presentation surface and return its model."""
        self._surface = surface
        return self.render()

    def render(self) -> JourneyView:
        models = {
            JourneySurface.EVENT: self.event.render,
            JourneySurface.CONSEQUENCE: self.consequence.render,
            JourneySurface.REALM: self.journey.realm,
            JourneySurface.HISTORY: self.journey.history,
            JourneySurface.PEOPLE: self.journey.people,
            JourneySurface.INVESTIGATION: self.journey.investigation,
            JourneySurface.ENDING: self.journey.ending,
        }
        if self._surface is JourneySurface.SETTINGS:
            return JourneyView(self._surface, self.journey.settings())
        return JourneyView(self._surface, models[self._surface]())

    def commit_choice(self, choice_id: str) -> JourneyView:
        """Commit exactly once through the canonical consequence boundary."""
        model = self.consequence.commit(choice_id)
        self._surface = JourneySurface.CONSEQUENCE
        return JourneyView(self._surface, model)

    def dismiss_consequence(self) -> JourneyView:
        self.consequence.dismiss()
        self._surface = JourneySurface.EVENT
        return self.render()

    def settings(
        self,
        *,
        reduced_motion: bool = False,
        large_text: bool = False,
        rtl: bool = False,
    ) -> JourneyView:
        self._surface = JourneySurface.SETTINGS
        return JourneyView(
            self._surface,
            SettingsScreen(
                reduced_motion=reduced_motion,
                large_text=large_text,
                rtl=rtl,
            ),
        )

    def restore_event(self) -> JourneyView:
        """Return to the event surface without changing canonical gameplay state."""
        self._surface = JourneySurface.EVENT
        return self.render()

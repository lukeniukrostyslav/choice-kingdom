from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

from .session import GameSession, SessionView


class InteractionState(str, Enum):
    """UI interaction state; it never changes gameplay semantics."""

    IDLE = "idle"
    FOCUSED = "focused"
    PRESSED = "pressed"
    RESOLVING = "resolving"
    RESOLVED = "resolved"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class ChoicePresentation:
    choice_id: str
    label: str
    text: str
    state: InteractionState = InteractionState.IDLE


@dataclass(frozen=True)
class ResourcePresentation:
    key: str
    value: int


@dataclass(frozen=True)
class SessionPresentation:
    """Stable UI-facing projection of the canonical GameSession boundary.

    The presentation layer owns labels, ordering and interaction state only.
    It deliberately does not calculate triggers, effects, routing or endings.
    """

    run_id: str
    turn: int
    event_id: str
    title: str
    trigger: str
    choices: tuple[ChoicePresentation, ...]
    resources: tuple[ResourcePresentation, ...]
    relationships: tuple[ResourcePresentation, ...]
    terminal: bool
    ending_identity: str | None


_DEFAULT_CHOICE_STATE: Final = InteractionState.IDLE


def present(view: SessionView) -> SessionPresentation:
    """Convert a canonical session snapshot into a deterministic UI model."""
    return SessionPresentation(
        run_id=view.run_id,
        turn=view.turn,
        event_id=view.event_id,
        title=view.title,
        trigger=view.trigger,
        choices=tuple(
            ChoicePresentation(choice_id, label, text, _DEFAULT_CHOICE_STATE)
            for choice_id, label, text in view.choices
        ),
        resources=tuple(ResourcePresentation(key, value) for key, value in view.resources),
        relationships=tuple(ResourcePresentation(key, value) for key, value in view.relationships),
        terminal=view.terminal,
        ending_identity=view.ending_identity,
    )


class SessionPresenter:
    """Thin controller for UI intent -> GameSession operations.

    All mutations still execute through GameSession. This prevents the UI from
    acquiring a second gameplay implementation and makes resolving/disabled
    states explicit for future Android Compose integration.
    """

    def __init__(self, session: GameSession):
        self.session = session
        self._resolving_choice: str | None = None
        self._resolved_choice: str | None = None

    def snapshot(self) -> SessionPresentation:
        base = present(self.session.view())
        choices = tuple(
            choice.__class__(
                choice.choice_id,
                choice.label,
                choice.text,
                self._choice_state(choice.choice_id),
            )
            for choice in base.choices
        )
        return base.__class__(
            base.run_id,
            base.turn,
            base.event_id,
            base.title,
            base.trigger,
            choices,
            base.resources,
            base.relationships,
            base.terminal,
            base.ending_identity,
        )

    def focus_choice(self, choice_id: str) -> None:
        if choice_id not in self.session.available_choices():
            raise ValueError(f"choice is not currently available: {choice_id}")
        self._resolving_choice = None
        self._resolved_choice = choice_id

    def begin_choice(self, choice_id: str) -> None:
        if choice_id not in self.session.available_choices():
            raise ValueError(f"choice is not currently available: {choice_id}")
        self._resolving_choice = choice_id
        self._resolved_choice = None

    def choose(self, choice_id: str):
        self.begin_choice(choice_id)
        result = self.session.choose(choice_id)
        self._resolving_choice = None
        self._resolved_choice = choice_id
        return result

    def _choice_state(self, choice_id: str) -> InteractionState:
        if choice_id == self._resolving_choice:
            return InteractionState.RESOLVING
        if choice_id == self._resolved_choice:
            return InteractionState.RESOLVED
        return InteractionState.IDLE

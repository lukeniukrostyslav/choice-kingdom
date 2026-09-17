from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

from .session import GameSession, SessionView


class InteractionState(str, Enum):
    """UI interaction state; it never changes gameplay semantics."""

    IDLE = "idle"
    FOCUSED = "focused"
    SELECTED = "selected"
    PRESSED = "pressed"
    RESOLVING = "resolving"
    RESOLVED = "resolved"
    DISABLED = "disabled"
    BLOCKED = "blocked"
    ERROR = "error"


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
    """Stable UI-facing projection of the canonical GameSession boundary."""

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
    terminal_state = InteractionState.DISABLED if view.terminal else _DEFAULT_CHOICE_STATE
    return SessionPresentation(
        run_id=view.run_id,
        turn=view.turn,
        event_id=view.event_id,
        title=view.title,
        trigger=view.trigger,
        choices=tuple(
            ChoicePresentation(choice_id, label, text, terminal_state)
            for choice_id, label, text in view.choices
        ),
        resources=tuple(ResourcePresentation(key, value) for key, value in view.resources),
        relationships=tuple(ResourcePresentation(key, value) for key, value in view.relationships),
        terminal=view.terminal,
        ending_identity=view.ending_identity,
    )


class SessionPresenter:
    """Thin controller for UI intent -> GameSession operations.

    All mutations still execute through GameSession. The presenter only owns
    transient interaction state and never calculates gameplay effects/routing.
    """

    def __init__(self, session: GameSession):
        self.session = session
        self._focused_choice: str | None = None
        self._selected_choice: str | None = None
        self._pressed_choice: str | None = None
        self._resolving_choice: str | None = None
        self._resolved_choice: str | None = None
        self._error_choice: str | None = None

    def snapshot(self) -> SessionPresentation:
        base = present(self.session.view())
        choices = tuple(
            ChoicePresentation(
                choice.choice_id,
                choice.label,
                choice.text,
                self._choice_state(choice.choice_id, base.terminal),
            )
            for choice in base.choices
        )
        return SessionPresentation(
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
        self._require_available(choice_id)
        self._focused_choice = choice_id
        self._selected_choice = None
        self._pressed_choice = None
        self._resolving_choice = None
        self._resolved_choice = None
        self._error_choice = None

    def select_choice(self, choice_id: str) -> None:
        """Preview a committed selection without changing gameplay."""
        self._require_available(choice_id)
        self._focused_choice = None
        self._selected_choice = choice_id
        self._pressed_choice = None
        self._resolving_choice = None
        self._resolved_choice = None
        self._error_choice = None

    def press_choice(self, choice_id: str) -> None:
        """Record the tactile/keyboard press state without resolving gameplay."""
        self._require_available(choice_id)
        self._focused_choice = choice_id
        self._selected_choice = None
        self._pressed_choice = choice_id
        self._resolving_choice = None
        self._resolved_choice = None
        self._error_choice = None

    def begin_choice(self, choice_id: str) -> None:
        """Advance the UI-only pressed state into resolving."""
        self._require_available(choice_id)
        self._focused_choice = None
        self._selected_choice = None
        self._pressed_choice = None
        self._resolving_choice = choice_id
        self._resolved_choice = None
        self._error_choice = None

    def choose(self, choice_id: str):
        self.begin_choice(choice_id)
        try:
            result = self.session.choose(choice_id)
        except Exception:
            self._error_choice = choice_id
            self._focused_choice = None
            self._selected_choice = None
            self._pressed_choice = None
            self._resolving_choice = None
            self._resolved_choice = None
            raise
        self._focused_choice = None
        self._selected_choice = None
        self._pressed_choice = None
        self._resolving_choice = None
        self._resolved_choice = choice_id
        self._error_choice = None
        return result

    def clear_transient_state(self) -> None:
        self._focused_choice = None
        self._selected_choice = None
        self._pressed_choice = None
        self._resolving_choice = None
        self._resolved_choice = None
        self._error_choice = None

    def select_event(self, event_id: str) -> None:
        """Move UI focus to an engine-qualified event without mutating gameplay."""
        self.session.select_event(event_id)
        self.clear_transient_state()

    def _require_available(self, choice_id: str) -> None:
        if self.session.view().terminal:
            raise ValueError("choice is not currently available: terminal session")
        if choice_id not in self.session.available_choices():
            raise ValueError(f"choice is not currently available: {choice_id}")

    def _choice_state(self, choice_id: str, terminal: bool) -> InteractionState:
        if terminal:
            return InteractionState.DISABLED
        if choice_id == self._error_choice:
            return InteractionState.ERROR
        if choice_id == self._resolving_choice:
            return InteractionState.RESOLVING
        if choice_id == self._pressed_choice:
            return InteractionState.PRESSED
        if choice_id == self._selected_choice:
            return InteractionState.SELECTED
        if choice_id == self._resolved_choice:
            return InteractionState.RESOLVED
        if choice_id == self._focused_choice:
            return InteractionState.FOCUSED
        return InteractionState.IDLE

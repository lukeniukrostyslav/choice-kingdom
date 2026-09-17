from __future__ import annotations

from dataclasses import dataclass

from .presentation import InteractionState, SessionPresentation, SessionPresenter


@dataclass(frozen=True)
class EventChoiceScreen:
    """Concrete Event + Choice screen contract for a platform UI host.

    This is presentation orchestration only: the canonical GameSession remains
    the sole owner of gameplay mutation and qualification.
    """

    session: SessionPresentation
    selected_choice_id: str | None = None
    can_interact: bool = True


class EventChoiceHost:
    """Small screen host that maps user gestures to SessionPresenter intents."""

    def __init__(self, presenter: SessionPresenter):
        self.presenter = presenter

    def render(self) -> EventChoiceScreen:
        model = self.presenter.snapshot()
        return EventChoiceScreen(
            session=model,
            selected_choice_id=self._selected_choice(model),
            can_interact=not model.terminal,
        )

    def focus(self, choice_id: str) -> EventChoiceScreen:
        self.presenter.focus_choice(choice_id)
        return self.render()

    def select(self, choice_id: str) -> EventChoiceScreen:
        self.presenter.select_choice(choice_id)
        return self.render()

    def press(self, choice_id: str) -> EventChoiceScreen:
        self.presenter.press_choice(choice_id)
        return self.render()

    def block(self, choice_id: str) -> EventChoiceScreen:
        self.presenter.block_choice(choice_id)
        return self.render()

    def choose(self, choice_id: str):
        """Commit one choice through the canonical application boundary."""
        result = self.presenter.choose(choice_id)
        return result, self.render()

    def _selected_choice(self, model: SessionPresentation) -> str | None:
        for choice in model.choices:
            if choice.state in {
                InteractionState.FOCUSED,
                InteractionState.SELECTED,
                InteractionState.PRESSED,
                InteractionState.RESOLVING,
                InteractionState.BLOCKED,
            }:
                return choice.choice_id
        return None

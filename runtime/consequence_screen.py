from __future__ import annotations

from dataclasses import dataclass

from .engine import ExecutionResult
from .presentation import SessionPresentation, SessionPresenter


@dataclass(frozen=True)
class ConsequenceScreen:
    """Concrete consequence/result screen contract for a platform UI host.

    The screen exposes only the result returned by the canonical engine plus the
    post-resolution presentation projection. It does not calculate effects,
    future consequences, or routing itself.
    """

    event_id: str
    choice_id: str
    next_event_ids: tuple[str, ...]
    session: SessionPresentation

    @property
    def terminal(self) -> bool:
        return self.session.terminal

    @property
    def pending_delay_count(self) -> int:
        return len(self.session.pending_delays)


class ConsequenceHost:
    """Build a premium consequence surface after one canonical choice commit."""

    def __init__(self, presenter: SessionPresenter):
        self.presenter = presenter
        self._last_result: ExecutionResult | None = None

    def commit(self, choice_id: str) -> ConsequenceScreen:
        """Commit through SessionPresenter, then project the resulting state."""
        result = self.presenter.choose(choice_id)
        self._last_result = result
        return self.render()

    def render(self) -> ConsequenceScreen:
        if self._last_result is None:
            raise RuntimeError("no consequence result has been committed")
        return ConsequenceScreen(
            event_id=self._last_result.event_id,
            choice_id=self._last_result.choice_id,
            next_event_ids=self._last_result.next_event_ids,
            session=self.presenter.snapshot(),
        )

    def dismiss(self) -> None:
        """Clear only the transient UI result; gameplay state remains unchanged."""
        self._last_result = None

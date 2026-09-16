from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .catalog import AuthoredCatalog, Event
from .delays import schedule_authored_delay
from .state import GameState

# Only explicit immediate Unlock/Unlocks lines are executable routing signals.
# Delayed prose is handled by the canonical delayed lifecycle instead.
IMMEDIATE_UNLOCK_RE = re.compile(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", re.I | re.M)


@dataclass(frozen=True)
class ExecutionResult:
    event_id: str
    choice_id: str
    next_event_ids: tuple[str, ...]
    state_snapshot: dict


class DecisionEngine:
    """Real authored-content execution boundary with canonical delay scheduling."""

    def __init__(self, root: Path):
        self.catalog = AuthoredCatalog.from_repository(root)
        self.catalog.validate()

    def event(self, event_id: str) -> Event:
        return self.catalog.get(event_id)

    def _route_allowed(self, state: GameState, event_id: str) -> bool:
        prerequisites = self.catalog.authored_prerequisites(event_id)
        if not prerequisites:
            return True
        if not all(required in state.history for required in prerequisites):
            return False
        return state.current_event_id in prerequisites

    def available(self, state: GameState) -> tuple[Event, ...]:
        return tuple(
            event
            for event in self.catalog.events.values()
            if self.catalog.trigger_satisfied(event.event_id, state)
            and self._route_allowed(state, event.event_id)
        )

    def execute(self, state: GameState, event_id: str, choice_id: str) -> ExecutionResult:
        if state.terminal:
            raise ValueError("cannot execute a choice after terminal state")
        event = self.catalog.get(event_id)
        if not self.catalog.trigger_satisfied(event_id, state):
            raise ValueError(f"event trigger not satisfied: {event_id}")
        if not self._route_allowed(state, event_id):
            prerequisites = self.catalog.authored_prerequisites(event_id)
            raise ValueError(
                f"event route not allowed: {event_id}; current={state.current_event_id}; "
                f"prerequisites={prerequisites}"
            )
        try:
            choice = next(choice for choice in event.choices if choice.choice_id == choice_id)
        except StopIteration as exc:
            raise KeyError(choice_id) from exc

        for resource, delta in choice.resource_deltas.items():
            state.apply_delta(resource, delta)
        for character, delta in choice.relationship_deltas.items():
            state.set_relationship_delta(character, delta)
        for token in choice.clear_tokens:
            state.flags.discard(token)
            state.history.discard(token)
            state.threads.discard(token)
        for token in choice.state_tokens:
            if token.startswith("thread."):
                state.threads.add(token)
            elif token.startswith("history."):
                state.history.add(token)
            else:
                state.flags.add(token)
        state.history.add(event_id)

        # Scheduling happens only after the authored choice effects have committed.
        # Relative timing is anchored to the source turn; condition-bound delays
        # intentionally carry no invented due turn.
        schedule_authored_delay(state, event_id, choice_id)

        state.current_event_id = event_id
        state.turn += 1

        next_ids = tuple(dict.fromkeys(IMMEDIATE_UNLOCK_RE.findall(choice.body)))
        return ExecutionResult(event_id, choice_id, next_ids, state.snapshot())

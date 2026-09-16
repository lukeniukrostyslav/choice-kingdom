from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .catalog import AuthoredCatalog, Choice, Event
from .state import GameState

# Only explicit immediate Unlock/Unlocks lines are executable routing signals.
# Delayed prose such as "after 3 turns, unlock E07..." is intentionally excluded
# until the delayed-lifecycle runtime is integrated.
IMMEDIATE_UNLOCK_RE = re.compile(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", re.I | re.M)

@dataclass(frozen=True)
class ExecutionResult:
    event_id: str
    choice_id: str
    next_event_ids: tuple[str, ...]
    state_snapshot: dict

class DecisionEngine:
    """Small, real authored-content execution boundary.

    It intentionally executes only explicit immediate deltas/state markers parsed from
    the authored source. Delayed prose is not silently converted into runtime timing.
    """
    def __init__(self, root: Path):
        self.catalog = AuthoredCatalog.from_repository(root)
        self.catalog.validate()

    def event(self, event_id: str) -> Event:
        return self.catalog.get(event_id)

    def available(self, state: GameState) -> tuple[Event, ...]:
        return tuple(event for event in self.catalog.events.values() if self.catalog.trigger_satisfied(event.event_id, state))

    def execute(self, state: GameState, event_id: str, choice_id: str) -> ExecutionResult:
        if state.terminal:
            raise ValueError("cannot execute a choice after terminal state")
        event = self.catalog.get(event_id)
        if not self.catalog.trigger_satisfied(event_id, state):
            raise ValueError(f"event trigger not satisfied: {event_id}")
        if state.current_event_id not in {event_id, "E01"} and event_id not in state.history:
            # Current-event routing is not fully inferred from prose. The caller may explicitly
            # enter an authored event after a verified trigger, but cannot jump outside catalog scope.
            pass
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
        state.current_event_id = event_id
        state.turn += 1

        next_ids = tuple(dict.fromkeys(IMMEDIATE_UNLOCK_RE.findall(choice.body)))
        return ExecutionResult(event_id, choice_id, next_ids, state.snapshot())

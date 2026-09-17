from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .catalog import AuthoredCatalog, Event
from .delays import due_delays, schedule_authored_delay
from .state import GameState

# Only explicit immediate Unlock/Unlocks lines are executable routing signals.
# Delayed prose is handled by the canonical delayed lifecycle instead.
IMMEDIATE_UNLOCK_RE = re.compile(r"^-\s*\*\*Unlocks?\*\*\s+`?(E\d{2,3})", re.I | re.M)

AUTHORED_COALITION_PARTICIPANTS = {
    "E148-A": ("mara", "rowan", "seris", "ivo", "amara", "toma"),
}


@dataclass(frozen=True)
class ExecutionResult:
    event_id: str
    choice_id: str
    next_event_ids: tuple[str, ...]
    state_snapshot: dict


@dataclass(frozen=True)
class DelayedActivationResult:
    consequence_key: str
    target_event_id: str
    state_snapshot: dict


class DecisionEngine:
    """Real authored-content execution boundary with canonical delay scheduling."""

    def __init__(self, root: Path):
        self.catalog = AuthoredCatalog.from_repository(root)
        self.catalog.validate()

    def event(self, event_id: str) -> Event:
        return self.catalog.get(event_id)

    def _route_allowed(self, state: GameState, event_id: str) -> bool:
        if event_id in state.activated_delayed_targets and state.current_event_id == event_id:
            return True
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

    @staticmethod
    def _apply_authored_participant_effects(state: GameState, choice_id: str) -> None:
        for participant in AUTHORED_COALITION_PARTICIPANTS.get(choice_id, ()):
            state.record_coalition_participant(participant)

    def execute(self, state: GameState, event_id: str, choice_id: str) -> ExecutionResult:
        if state.terminal:
            raise ValueError("cannot execute a choice after terminal state")
        event = self.catalog.get(event_id)
        if not self.catalog.trigger_satisfied(event_id, state) and event_id not in state.activated_delayed_targets:
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

        if choice_id == "E192-A":
            state.flags.discard("food_logistics_stabilized")
            state.flags.add("food_logistics_unstable")
        elif choice_id == "E192-B":
            state.flags.discard("food_logistics_unstable")
            state.flags.add("food_logistics_stabilized")
        elif choice_id == "E270-A":
            pass
        elif choice_id == "E271-A":
            state.flags.add("border_crisis_declared")
            state.flags.discard("border_crisis_resolved")
            state.threads.add("thread.border_crisis")
        elif choice_id == "E271-B":
            state.flags.add("border_crisis_resolved")
            state.flags.discard("border_crisis_declared")
            state.threads.add("thread.border_crisis")
        elif choice_id in {"E272-A", "E272-B"}:
            state.flags.add("border_crisis_resolved")
            state.flags.add("border_crisis_declared")
            state.threads.add("thread.border_crisis")
            state.flags.discard("pred.border_crisis")

        state.history.add(event_id)
        self._apply_authored_participant_effects(state, choice_id)
        state.activated_delayed_targets.discard(event_id)
        schedule_authored_delay(state, event_id, choice_id)
        state.current_event_id = event_id
        state.turn += 1

        next_ids = tuple(dict.fromkeys(IMMEDIATE_UNLOCK_RE.findall(choice.body)))
        return ExecutionResult(event_id, choice_id, next_ids, state.snapshot())

    def activate_delayed_target(
        self,
        state: GameState,
        exactly_once_key: str,
        *,
        condition_satisfied: bool | None = None,
    ) -> DelayedActivationResult:
        if state.terminal:
            raise ValueError("cannot activate a delayed consequence after terminal state")
        delay = state.pending_delays.get(exactly_once_key)
        if delay is None:
            raise KeyError(exactly_once_key)
        self.event(delay.resolution_target)
        if delay.condition_bound:
            if condition_satisfied is not True:
                raise ValueError(f"condition not satisfied: {exactly_once_key}")
        elif delay.scheduled_turn is None or state.turn < delay.scheduled_turn:
            raise ValueError(f"delay is not due: {exactly_once_key}")
        resolved = state.activate_delayed_target(exactly_once_key)
        return DelayedActivationResult(
            consequence_key=resolved.exactly_once_key,
            target_event_id=resolved.resolution_target,
            state_snapshot=state.snapshot(),
        )

    def execute_delayed_target(
        self,
        state: GameState,
        exactly_once_key: str,
        choice_id: str,
        *,
        condition_satisfied: bool | None = None,
    ) -> ExecutionResult:
        if state.terminal:
            raise ValueError("cannot execute a choice after terminal state")
        delay = state.pending_delays.get(exactly_once_key)
        if delay is None:
            raise KeyError(exactly_once_key)
        if delay.status != "pending":
            raise ValueError(f"delay is not pending: {exactly_once_key}")
        target = self.event(delay.resolution_target)
        if not any(choice.choice_id == choice_id for choice in target.choices):
            raise KeyError(choice_id)
        self.activate_delayed_target(state, exactly_once_key, condition_satisfied=condition_satisfied)
        return self.execute(state, target.event_id, choice_id)

    def activate_next_due_delay(self, state: GameState) -> DelayedActivationResult:
        if state.terminal:
            raise ValueError("cannot activate a delayed consequence after terminal state")
        due = due_delays(state)
        if not due:
            raise ValueError("no due delayed consequence")
        return self.activate_delayed_target(state, due[0].exactly_once_key)

from __future__ import annotations

from dataclasses import dataclass

from .state import GameState, PendingDelay


@dataclass(frozen=True)
class DelaySpec:
    consequence_id: str
    source_event_id: str
    source_choice_id: str
    resolution_target: str
    exactly_once_key: str
    earliest_after_turns: int | None
    condition_bound: bool = False
    priority: int = 0
    cancellation_rule: str = "none_authored"
    supersedes: str | None = None


# Frozen from docs/MACHINE_DELAY_CONTRACT_01.json and its QA reconciliation.
CANONICAL_DELAY_SPECS: tuple[DelaySpec, ...] = (
    DelaySpec("E181.second_toll_increase", "E45", "E45-B", "E181", "delay.E45B.E181.second_toll_increase", 5),
    DelaySpec("E182.veteran_promise", "E117", "E117-B", "E182", "delay.E117B.E182.veteran_promise", 4),
    DelaySpec("E183.noble_exception_return", "E118", "E118-B", "E183", "delay.E118B.E183.noble_exception_return", 5),
    DelaySpec("E184.quiet_evidence", "E25", "E25-B", "E184", "delay.E25B.E184.quiet_evidence", 4),
    DelaySpec("E185.cheap_steel_failure", "E17", "E17-A", "E185", "delay.E17A.E185.cheap_steel_failure", None, condition_bound=True),
    DelaySpec("E242.renewed_exception", "E118", "E118-B", "E242", "delay.E118B.E242.renewed_exception", 6),
    DelaySpec("E243.old_bridge", "E18", "E18-B", "E243", "delay.E18B.E243.old_bridge", 5),
    DelaySpec("E244.audit_comes_due", "E09", "E09-B", "E244", "delay.E09B.E244.audit_comes_due", 5),
    DelaySpec("E245.soldiers_son_returns", "E20", "E20-A", "E245", "delay.E20A.E245.soldiers_son_returns", 6),
    DelaySpec("E246.price_ceiling_memory", "E160", "E160-A", "E246", "delay.E160A.E246.price_ceiling_memory", 5),
)

_BY_CHOICE = {(spec.source_event_id, spec.source_choice_id): spec for spec in CANONICAL_DELAY_SPECS}
_BY_KEY = {spec.exactly_once_key: spec for spec in CANONICAL_DELAY_SPECS}


def spec_for_choice(event_id: str, choice_id: str) -> DelaySpec | None:
    return _BY_CHOICE.get((event_id, choice_id))


def spec_for_key(exactly_once_key: str) -> DelaySpec | None:
    return _BY_KEY.get(exactly_once_key)


def schedule_authored_delay(state: GameState, event_id: str, choice_id: str) -> PendingDelay | None:
    spec = spec_for_choice(event_id, choice_id)
    if spec is None:
        return None
    scheduled_turn = None if spec.condition_bound else state.turn + (spec.earliest_after_turns or 0)
    delay = PendingDelay(
        exactly_once_key=spec.exactly_once_key,
        source_event_id=spec.source_event_id,
        source_choice_id=spec.source_choice_id,
        resolution_target=spec.resolution_target,
        scheduled_turn=scheduled_turn,
        condition_bound=spec.condition_bound,
        priority=spec.priority,
        supersedes=spec.supersedes,
    )
    state.schedule(delay)
    return delay


def due_delays(state: GameState) -> tuple[PendingDelay, ...]:
    due = [
        delay
        for delay in state.pending_delays.values()
        if delay.status == "pending" and delay.scheduled_turn is not None and state.turn >= delay.scheduled_turn
    ]
    return tuple(sorted(due, key=lambda delay: (delay.scheduled_turn or 0, delay.priority, delay.exactly_once_key)))


def resolve_due_delay(state: GameState, exactly_once_key: str) -> PendingDelay:
    delay = state.pending_delays.get(exactly_once_key)
    if delay is None:
        raise KeyError(exactly_once_key)
    if delay.condition_bound:
        raise ValueError(f"condition-bound delay requires authored resolution condition: {exactly_once_key}")
    if delay.status != "pending":
        raise ValueError(f"delay is not pending: {exactly_once_key}")
    if delay.scheduled_turn is None or state.turn < delay.scheduled_turn:
        raise ValueError(f"delay is not due: {exactly_once_key}")
    return state.resolve_delay(exactly_once_key)


def resolve_condition_bound_delay(state: GameState, exactly_once_key: str, condition_satisfied: bool) -> PendingDelay:
    delay = state.pending_delays.get(exactly_once_key)
    if delay is None:
        raise KeyError(exactly_once_key)
    if not delay.condition_bound:
        raise ValueError(f"delay is not condition-bound: {exactly_once_key}")
    if not condition_satisfied:
        raise ValueError(f"condition not satisfied: {exactly_once_key}")
    return state.resolve_delay(exactly_once_key)

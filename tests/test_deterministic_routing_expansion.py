from pathlib import Path

from runtime.engine import DecisionEngine
from runtime.state import GameState, EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST

ROOT = Path(__file__).resolve().parents[1]


def test_all_explicit_event_prerequisites_are_in_frozen_scope():
    engine = DecisionEngine(ROOT)
    production_ids = {f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)} - set(EXCLUDED_EVENTS)

    checked = 0
    for event_id in production_ids:
        prerequisites = engine.catalog.authored_prerequisites(event_id)
        for prerequisite in prerequisites:
            checked += 1
            assert prerequisite in production_ids
    assert checked > 0


def test_every_explicit_prerequisite_requires_the_current_authored_route():
    engine = DecisionEngine(ROOT)
    production_ids = {f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)} - set(EXCLUDED_EVENTS)

    checked = 0
    for event_id in production_ids:
        prerequisites = engine.catalog.authored_prerequisites(event_id)
        if not prerequisites:
            continue
        checked += 1
        state = GameState.fresh(f"route-{event_id}")
        state.history.update(prerequisites)
        state.current_event_id = prerequisites[-1]
        assert engine._route_allowed(state, event_id) is True

        state.current_event_id = "E01" if prerequisites[-1] != "E01" else "E02"
        assert engine._route_allowed(state, event_id) is False
    assert checked > 0


def test_missing_authored_prerequisite_blocks_route_even_if_another_prerequisite_is_present():
    engine = DecisionEngine(ROOT)
    targets = [
        event_id
        for event_id in engine.catalog.events
        if len(engine.catalog.authored_prerequisites(event_id)) >= 2
    ]
    if not targets:
        return

    target = targets[0]
    prerequisites = engine.catalog.authored_prerequisites(target)
    state = GameState.fresh("route-missing-prereq")
    state.history.add(prerequisites[0])
    state.current_event_id = prerequisites[0]
    assert engine._route_allowed(state, target) is False


def test_e148_authored_event_reference_or_branch_is_runtime_executable():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("e148-or-trigger")
    state.history.add("E146")
    state.current_event_id = "E146"

    event = engine.event("E148")
    assert "E146 or" in event.trigger
    assert engine.catalog.trigger_satisfied("E148", state) is True
    assert engine._route_allowed(state, "E148") is True


def test_e148_or_branch_does_not_treat_unrelated_event_history_as_the_authored_reference():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("e148-or-negative")
    state.history.add("E145")
    state.current_event_id = "E145"

    assert engine.catalog.trigger_satisfied("E148", state) is False
    assert engine._route_allowed(state, "E148") is True

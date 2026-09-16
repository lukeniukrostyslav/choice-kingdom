from pathlib import Path

import pytest

from runtime.catalog import AuthoredCatalog
from runtime.engine import DecisionEngine
from runtime.state import GameState, EXCLUDED_EVENTS, PRODUCTION_FIRST, PRODUCTION_LAST

ROOT = Path(__file__).resolve().parents[1]


def test_frozen_catalog_loads_exactly_and_excludes_expansion_nodes():
    catalog = AuthoredCatalog.from_repository(ROOT)
    catalog.validate()
    assert len(catalog.events) == 272
    assert "E273" not in catalog.events
    assert "E277" not in catalog.events


def test_e01_a_executes_authored_immediate_state_transition():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-e01-a")
    result = engine.execute(state, "E01", "E01-A")
    assert state.resources["trust"] == 54
    assert state.resources["power"] == 49
    assert "open_petition_hall" in state.flags
    assert "E01" in state.history
    assert result.event_id == "E01"
    assert result.next_event_ids == ()


def test_e01_b_does_not_leak_delayed_unlock_into_immediate_routing():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-e01-b")
    result = engine.execute(state, "E01", "E01-B")
    assert state.resources["power"] == 52
    assert state.relationships["seris"] == 1
    assert "court_first" in state.flags
    assert result.next_event_ids == ()


def test_explicit_event_prerequisite_is_exposed_from_authored_trigger():
    engine = DecisionEngine(ROOT)
    assert engine.catalog.authored_prerequisites("E02") == ("E01",)


def test_core_spine_routes_deterministically_through_explicit_prerequisite():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-core-spine")
    engine.execute(state, "E01", "E01-A")
    assert engine.catalog.trigger_satisfied("E02", state)
    assert "E02" in {event.event_id for event in engine.available(state)}
    assert "E03" not in {event.event_id for event in engine.available(state)}
    engine.execute(state, "E02", "E02-B")
    assert "E02" in state.history
    assert engine.catalog.trigger_satisfied("E02", state) is False
    assert "E02" not in {event.event_id for event in engine.available(state)}


def test_representative_authored_chain_executes_e01_to_e02_without_inferred_edges():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-authored-chain-e01-e02")
    first = engine.execute(state, "E01", "E01-B")
    assert first.next_event_ids == ()
    assert state.current_event_id == "E01"
    assert state.turn == 2
    assert engine.catalog.authored_prerequisites("E02") == ("E01",)
    available_ids = {event.event_id for event in engine.available(state)}
    assert "E02" in available_ids
    assert "E03" not in available_ids
    second = engine.execute(state, "E02", "E02-B")
    assert second.next_event_ids == ()
    assert state.current_event_id == "E02"
    assert state.turn == 3
    assert state.relationships["mara"] == 2
    assert state.resources["power"] == 50
    assert "decree_investigation" in state.flags
    assert "E02" in state.history


def test_authored_prerequisite_blocks_unrelated_jump_even_when_trigger_is_satisfied():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-route-guard")
    state.history.add("E01")
    state.current_event_id = "E99"
    assert engine.catalog.trigger_satisfied("E02", state)
    assert "E02" not in {event.event_id for event in engine.available(state)}
    with pytest.raises(ValueError, match="event route not allowed: E02"):
        engine.execute(state, "E02", "E02-B")


def test_authored_event_is_single_use_and_cannot_be_replayed():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-single-use")
    engine.execute(state, "E01", "E01-A")
    with pytest.raises(ValueError, match="event trigger not satisfied: E01"):
        engine.execute(state, "E01", "E01-A")


def test_unrecognized_authored_trigger_is_not_invented_as_runtime_route():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-unknown-trigger")
    assert engine.catalog.trigger_satisfied("E03", state) is False
    assert "E03" not in {event.event_id for event in engine.available(state)}


def test_fresh_runs_are_isolated_and_repeat_the_same_authored_transition():
    engine = DecisionEngine(ROOT)
    first = GameState.fresh("repeat-a")
    second = GameState.fresh("repeat-b")
    first_result = engine.execute(first, "E01", "E01-A")
    second_result = engine.execute(second, "E01", "E01-A")
    first_snapshot = first.snapshot()
    second_snapshot = second.snapshot()
    first_snapshot.pop("run_id")
    second_snapshot.pop("run_id")
    assert first_snapshot == second_snapshot
    assert first_result.state_snapshot["resources"] == second_result.state_snapshot["resources"]
    assert first_result.state_snapshot["flags"] == second_result.state_snapshot["flags"]


def test_e51_c_executes_three_way_authored_choice_without_dropping_choice_c():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-e51-c")
    state.turn = 10
    state.history.add("E47")
    state.current_event_id = "E47"
    result = engine.execute(state, "E51", "E51-C")
    assert state.resources["trust"] == 55
    assert state.resources["power"] == 47
    assert "public_renewal_rule" in state.flags
    assert "E51" in state.history
    assert result.choice_id == "E51-C"


def test_e108_c_is_loaded_as_authored_even_where_source_uses_shorthand_effects():
    engine = DecisionEngine(ROOT)
    event = engine.event("E108")
    choice = next(choice for choice in event.choices if choice.choice_id == "E108-C")
    assert choice.text.startswith("distributed draft")
    assert "+trust -power" in choice.body
    state = GameState.fresh("run-e108-c")
    state.turn = 10
    engine.execute(state, "E108", "E108-C")
    assert "E108" in state.history


def test_excluded_event_cannot_execute():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("run-excluded")
    with pytest.raises(ValueError):
        engine.execute(state, "E273", "E273-A")


def test_all_explicit_event_prerequisites_are_in_frozen_scope():
    engine = DecisionEngine(ROOT)
    production_ids = {f"E{i:02d}" for i in range(PRODUCTION_FIRST, PRODUCTION_LAST + 1)} - set(EXCLUDED_EVENTS)
    checked = 0
    for event_id in production_ids:
        for prerequisite in engine.catalog.authored_prerequisites(event_id):
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


def test_missing_authored_prerequisite_blocks_route_even_if_another_is_present():
    engine = DecisionEngine(ROOT)
    targets = [event_id for event_id in engine.catalog.events if len(engine.catalog.authored_prerequisites(event_id)) >= 2]
    if not targets:
        return
    target = targets[0]
    prerequisites = engine.catalog.authored_prerequisites(target)
    state = GameState.fresh("route-missing-prereq")
    state.history.add(prerequisites[0])
    state.current_event_id = prerequisites[0]
    assert engine._route_allowed(state, target) is False


def test_canonical_expansion_choice_rows_for_delayed_sources_are_present():
    engine = DecisionEngine(ROOT)
    expected = {
        "E117": ("E117-A", "E117-B"),
        "E118": ("E118-A", "E118-B"),
    }
    for event_id, choice_ids in expected.items():
        actual = tuple(choice.choice_id for choice in engine.event(event_id).choices)
        assert actual == choice_ids


def test_structured_or_trigger_uses_known_authored_branch_without_guessing_opaque_branch():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("structured-or")
    state.flags.add("court_first")
    assert engine.catalog.trigger_satisfied("E06", state) is True

    state = GameState.fresh("structured-or-numeric")
    state.resources["trust"] = 59
    assert engine.catalog.trigger_satisfied("E12", state) is True


def test_structured_and_trigger_requires_all_known_atoms():
    engine = DecisionEngine(ROOT)
    state = GameState.fresh("structured-and")
    state.relationships["mara"] = 1
    state.flags.add("decree_investigation")
    assert engine.catalog.trigger_satisfied("E09", state) is True
    state.flags.clear()
    assert engine.catalog.trigger_satisfied("E09", state) is False

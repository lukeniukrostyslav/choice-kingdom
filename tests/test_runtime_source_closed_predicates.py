from __future__ import annotations

from pathlib import Path

from runtime.catalog import AuthoredCatalog
from runtime.ending_sources import EndingSourceCompiler
from runtime.state import GameState

ROOT = Path(__file__).resolve().parents[1]


def test_source_closed_predicates_compile_only_from_canonical_facts() -> None:
    state = GameState.fresh("predicate-test")
    state.flags.update(
        {
            "people_charter_endorsed",
            "crown_audited",
            "auditor_independence",
            "legislative_budget_lock",
            "military_red_line",
            "systemic_explanation_convergence",
            "coalition_candidate_package",
            "guild_tribunal_independent",
            "merchant_charter",
            "guild_neutral_inspectors",
            "food_logistics_stabilized",
        }
    )
    state.history.update(
        {
            "history.house_assembly",
            "history.guild_representation",
            "history.guild_logistics_cooperation",
            "history.cross_faction_package",
        }
    )
    state.ending_evidence_families.update(
        {"warehouse_or_financial", "document_or_language", "witness_or_organizational"}
    )
    state.coalition_participants.update({"mara", "rowan", "seris"})

    predicates = EndingSourceCompiler.compile_state(state).predicates

    assert "pred.guild_influence_strong" in predicates
    assert "pred.food_stable" in predicates
    assert "pred.systemic_explanation_verified" in predicates
    assert "pred.coalition_cooperation" in predicates
    assert "pred.constitutional_prepared_strong" in predicates
    assert "pred.budget_reform" in predicates
    assert "pred.final_charter_prerequisites" in predicates


def test_coalition_predicate_rejects_noncanonical_shortcuts() -> None:
    state = GameState.fresh("coalition-negative")
    state.flags.update({"coalition_candidate_package"})
    state.history.update({"history.cross_faction_package"})
    state.coalition_participants.update({"mara", "rowan"})
    state.relationships["seris"] = 3

    predicates = EndingSourceCompiler.compile_state(state).predicates

    assert "pred.coalition_cooperation" not in predicates


def test_food_predicate_uses_the_explicit_producer_marker() -> None:
    state = GameState.fresh("food-predicate")
    catalog = AuthoredCatalog.from_repository(ROOT)

    state.flags.add("food_logistics_stabilized")
    predicates = EndingSourceCompiler.compile_state(state).predicates
    assert "pred.food_stable" in predicates
    assert catalog.trigger_satisfied("E192", state) is False

    state.flags.add("food_logistics_unstable")
    predicates = EndingSourceCompiler.compile_state(state).predicates
    assert "pred.food_stable" not in predicates
    assert catalog.trigger_satisfied("E192", state) is False


def test_predicate_trigger_atom_uses_the_same_source_compiler() -> None:
    state = GameState.fresh("predicate-trigger")
    catalog = AuthoredCatalog.from_repository(ROOT)
    event = next(event for event in catalog.events.values() if event.trigger.lower().strip() == "pred.food_stable")

    state.flags.add("food_logistics_stabilized")
    assert catalog.trigger_satisfied(event.event_id, state) is True

    state.flags.add("food_logistics_unstable")
    assert catalog.trigger_satisfied(event.event_id, state) is False

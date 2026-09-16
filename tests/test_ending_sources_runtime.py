from __future__ import annotations

import pytest

from runtime.ending_contract import EndingContractError, EndingQualification
from runtime.ending_sources import (
    CANONICAL_COALITION_PARTICIPANTS,
    EndingSourceCompiler,
)
from runtime.endings import END_STEWARD, EndingResolver
from runtime.state import GameState, SaveStore


def test_constitutional_preparation_requires_three_distinct_domains() -> None:
    facts = EndingSourceCompiler.compile(
        flags={"people_charter_endorsed", "crown_audited"},
        history={"history.house_assembly"},
    )
    assert "pred.constitutional_prepared_strong" in facts.predicates


def test_single_source_family_cannot_double_count() -> None:
    facts = EndingSourceCompiler.compile(
        flags={"people_charter_endorsed", "crown_audited"},
    )
    assert "pred.constitutional_prepared_strong" not in facts.predicates


def test_relationships_and_four_way_bargain_do_not_create_cooperation() -> None:
    facts = EndingSourceCompiler.compile(
        flags={"four_way_bargain"},
        coalition_participants=set(),
    )
    assert "pred.coalition_cooperation" not in facts.predicates


def test_coalition_requires_authored_positive_outcome_three_participants_and_no_blocker() -> None:
    canonical = {"mara", "rowan", "seris"}
    assert canonical <= CANONICAL_COALITION_PARTICIPANTS

    facts = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants=canonical,
    )
    assert "pred.coalition_cooperation" in facts.predicates

    missing_positive_outcome = EndingSourceCompiler.compile(
        history={"history.cross_faction_package"},
        coalition_participants=canonical,
    )
    assert "pred.coalition_cooperation" not in missing_positive_outcome.predicates

    insufficient = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants={"mara", "rowan"},
    )
    assert "pred.coalition_cooperation" not in insufficient.predicates

    unknown_only = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants={"commons", "guild", "houses", "border"},
    )
    assert "pred.coalition_cooperation" not in unknown_only.predicates

    blocked = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants=canonical,
        unresolved_coalition_blockers={"withdrawal_pending"},
    )
    assert "pred.coalition_cooperation" not in blocked.predicates


def test_guild_influence_requires_three_distinct_authored_domains() -> None:
    common = dict(
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
        flags={"guild_tribunal_independent", "audited_monopoly", "guild_neutral_inspectors"},
    )
    facts = EndingSourceCompiler.compile(**common)
    assert "pred.guild_influence_strong" in facts.predicates

    representation_only = EndingSourceCompiler.compile(
        history={"history.guild_representation"},
    )
    assert "pred.guild_influence_strong" not in representation_only.predicates

    relationship_only = EndingSourceCompiler.compile(
        flags={"rel.ivo"},
        history={"thread.guild"},
    )
    assert "pred.guild_influence_strong" not in relationship_only.predicates


def test_guild_logistics_immunity_invalidates_only_the_logistics_domain() -> None:
    facts = EndingSourceCompiler.compile(
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
        flags={
            "guild_tribunal_independent",
            "guild_neutral_inspectors",
            "guild_logistics_immunity_risk",
        },
    )
    assert "pred.guild_influence_strong" not in facts.predicates


def test_systemic_explanation_requires_all_evidence_families_and_convergence() -> None:
    incomplete = EndingSourceCompiler.compile(
        systemic_evidence_families={"warehouse_or_financial", "document_or_language"},
        flags={"systemic_explanation_convergence"},
    )
    assert "pred.systemic_explanation_verified" not in incomplete.predicates

    complete = EndingSourceCompiler.compile(
        systemic_evidence_families={
            "warehouse_or_financial",
            "document_or_language",
            "witness_or_organizational",
        },
        flags={"systemic_explanation_convergence"},
    )
    assert "pred.systemic_explanation_verified" in complete.predicates


def test_final_charter_requires_upstream_predicates_and_no_current_blocker() -> None:
    common = dict(
        flags={
            "people_charter_endorsed",
            "crown_audited",
            "systemic_explanation_convergence",
            "military_red_line",
            "coalition_candidate_package",
        },
        history={
            "history.house_assembly",
            "history.guild_representation",
            "history.cross_faction_package",
        },
        systemic_evidence_families={
            "warehouse_or_financial",
            "document_or_language",
            "witness_or_organizational",
        },
        coalition_participants={"mara", "rowan", "seris"},
    )
    ready = EndingSourceCompiler.compile(**common)
    assert "pred.final_charter_prerequisites" in ready.predicates

    blocked = EndingSourceCompiler.compile(
        **common,
        unresolved_mandatory_crisis_blockers={"border_crisis"},
    )
    assert "pred.final_charter_prerequisites" not in blocked.predicates


def test_live_game_state_is_the_runtime_source_boundary() -> None:
    state = GameState.fresh("ending-runtime")
    state.flags.update({
        "people_charter_endorsed",
        "crown_audited",
        "systemic_explanation_convergence",
        "military_red_line",
        "coalition_candidate_package",
    })
    state.history.update({"history.house_assembly", "history.guild_representation", "history.cross_faction_package"})
    state.threads.add("thread.military_constitutional")
    for family in ("warehouse_or_financial", "document_or_language", "witness_or_organizational"):
        assert state.record_ending_evidence(family)
    for participant in ("mara", "rowan", "seris"):
        assert state.record_coalition_participant(participant)

    facts = EndingSourceCompiler.compile_state(state)
    assert "pred.constitutional_prepared_strong" in facts.predicates
    assert "pred.systemic_explanation_verified" in facts.predicates
    assert "pred.coalition_cooperation" in facts.predicates
    assert "pred.final_charter_prerequisites" in facts.predicates


def test_live_state_rejects_stale_aliases_instead_of_promoting_them() -> None:
    state = GameState.fresh("alias-negative")
    state.flags.update({"four_way_bargain", "systemic_explanation_convergence"})
    state.threads.update({"thread.border", "thread.guild"})
    state.history.add("history.cross_faction_package")
    state.coalition_participants.update({"commons", "guild", "houses"})
    state.ending_evidence_families.update({"warehouse_or_financial", "document_or_language"})

    facts = EndingSourceCompiler.compile_state(state)
    assert "pred.coalition_cooperation" not in facts.predicates
    assert "pred.systemic_explanation_verified" not in facts.predicates
    assert "pred.final_charter_prerequisites" not in facts.predicates


def test_unscoped_second_founder_prerequisites_are_rejected() -> None:
    with pytest.raises(EndingContractError, match="unscoped systemic_explanation_verified"):
        EndingQualification.build(flags={"systemic_explanation_verified"})
    with pytest.raises(EndingContractError, match="unscoped coalition_cooperation"):
        EndingQualification.build(flags={"coalition_cooperation"})


def test_ending_resolution_is_repeatable_from_the_same_snapshot() -> None:
    state = GameState.fresh("deterministic-ending")
    state.terminal = True
    EndingResolver().resolve(state, qualified_endings=[END_STEWARD])
    snapshot = state.snapshot()

    first = snapshot["ending_identity"]
    restored = GameState.from_snapshot(snapshot)
    second = EndingResolver().resolve(restored, qualified_endings=[END_STEWARD]).ending_id
    assert first == second == END_STEWARD


def test_ending_source_facts_survive_save_load_without_leaking_to_fresh_run(tmp_path) -> None:
    state = GameState.fresh("ending-save")
    state.flags.update({"people_charter_endorsed", "crown_audited", "systemic_explanation_convergence", "coalition_candidate_package"})
    state.history.update({"history.house_assembly", "history.guild_representation", "history.cross_faction_package"})
    state.record_ending_evidence("warehouse_or_financial")
    state.record_ending_evidence("document_or_language")
    state.record_ending_evidence("witness_or_organizational")
    state.record_coalition_participant("mara")
    state.record_coalition_participant("rowan")
    state.record_coalition_participant("seris")

    path = tmp_path / "ending-state.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == state.snapshot()

    fresh = GameState.new_run_from_completed_prior("fresh-run")
    assert fresh.ending_evidence_families == set()
    assert fresh.coalition_participants == set()

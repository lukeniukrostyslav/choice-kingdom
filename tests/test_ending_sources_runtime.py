from __future__ import annotations

from runtime.ending_sources import EndingSourceCompiler
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


def test_coalition_requires_participants_and_no_blocker() -> None:
    facts = EndingSourceCompiler.compile(
        history={"history.cross_faction_package"},
        coalition_participants={"commons", "guild", "houses", "border"},
    )
    assert "pred.coalition_cooperation" in facts.predicates

    blocked = EndingSourceCompiler.compile(
        history={"history.cross_faction_package"},
        coalition_participants={"commons", "guild", "houses", "border"},
        unresolved_coalition_blockers={"withdrawal_pending"},
    )
    assert "pred.coalition_cooperation" not in blocked.predicates


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
        flags={"people_charter_endorsed", "crown_audited", "systemic_explanation_convergence", "military_red_line"},
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
        coalition_participants={"commons", "guild", "houses", "border"},
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
    state.flags.update({"people_charter_endorsed", "crown_audited", "systemic_explanation_convergence", "military_red_line"})
    state.history.update({"history.house_assembly", "history.guild_representation", "history.cross_faction_package"})
    state.threads.add("thread.military_constitutional")
    for family in ("warehouse_or_financial", "document_or_language", "witness_or_organizational"):
        assert state.record_ending_evidence(family)
    for participant in ("commons", "guild", "houses", "border"):
        assert state.record_coalition_participant(participant)

    facts = EndingSourceCompiler.compile_state(state)
    assert "pred.constitutional_prepared_strong" in facts.predicates
    assert "pred.systemic_explanation_verified" in facts.predicates
    assert "pred.coalition_cooperation" in facts.predicates
    assert "pred.final_charter_prerequisites" in facts.predicates


def test_ending_source_facts_survive_save_load_without_leaking_to_fresh_run(tmp_path) -> None:
    state = GameState.fresh("ending-save")
    state.flags.update({"people_charter_endorsed", "crown_audited", "systemic_explanation_convergence"})
    state.history.update({"history.house_assembly", "history.guild_representation", "history.cross_faction_package"})
    state.record_ending_evidence("warehouse_or_financial")
    state.record_ending_evidence("document_or_language")
    state.record_ending_evidence("witness_or_organizational")
    state.record_coalition_participant("commons")
    state.record_coalition_participant("guild")

    path = tmp_path / "ending-state.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == state.snapshot()

    fresh = GameState.new_run_from_completed_prior("fresh-run")
    assert fresh.ending_evidence_families == set()
    assert fresh.coalition_participants == set()

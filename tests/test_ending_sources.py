from runtime.ending_sources import EndingSourceCompiler


def test_constitutional_preparation_requires_three_distinct_domains():
    facts = EndingSourceCompiler.compile(
        flags={"people_charter_endorsed", "crown_audited"},
        history={"history.house_assembly"},
    )
    assert "pred.constitutional_prepared_strong" in facts.predicates


def test_one_domain_cannot_be_counted_twice():
    facts = EndingSourceCompiler.compile(
        flags={"crown_audited", "full_crown_audit_published", "people_charter_endorsed"},
    )
    assert "pred.constitutional_prepared_strong" not in facts.predicates


def test_budget_reform_requires_all_three_authored_producers():
    incomplete = EndingSourceCompiler.compile(
        flags={"auditor_independence", "crown_audited"},
    )
    assert "pred.budget_reform" not in incomplete.predicates

    complete = EndingSourceCompiler.compile(
        flags={"auditor_independence", "crown_audited", "legislative_budget_lock"},
    )
    assert "pred.budget_reform" in complete.predicates


def test_systemic_explanation_needs_three_evidence_families_and_convergence():
    incomplete = EndingSourceCompiler.compile(
        flags={"systemic_explanation_convergence"},
        systemic_evidence_families={"warehouse_or_financial", "document_or_language"},
    )
    assert "pred.systemic_explanation_verified" not in incomplete.predicates

    complete = EndingSourceCompiler.compile(
        flags={"systemic_explanation_convergence"},
        systemic_evidence_families={
            "warehouse_or_financial",
            "document_or_language",
            "witness_or_organizational",
        },
    )
    assert "pred.systemic_explanation_verified" in complete.predicates


def test_coalition_requires_authored_positive_outcome_participant_identity_and_no_blocker():
    incomplete = EndingSourceCompiler.compile(
        history={"history.cross_faction_package"},
    )
    assert "pred.coalition_cooperation" not in incomplete.predicates

    blocked = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants={"mara", "rowan", "seris"},
        unresolved_coalition_blockers={"coalition_withdrawal"},
    )
    assert "pred.coalition_cooperation" not in blocked.predicates

    insufficient = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants={"mara", "rowan"},
    )
    assert "pred.coalition_cooperation" not in insufficient.predicates

    complete = EndingSourceCompiler.compile(
        flags={"coalition_candidate_package"},
        history={"history.cross_faction_package"},
        coalition_participants={"mara", "rowan", "seris"},
    )
    assert "pred.coalition_cooperation" in complete.predicates


def test_four_way_bargain_does_not_alias_coalition_cooperation():
    facts = EndingSourceCompiler.compile(
        flags={"four_way_bargain"},
        coalition_participants={"commons", "houses", "guilds", "border"},
    )
    assert "pred.coalition_cooperation" not in facts.predicates


def test_final_charter_is_consumer_only_and_requires_all_upstream_contracts():
    facts = EndingSourceCompiler.compile(
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
        threads=set(),
        systemic_evidence_families={
            "warehouse_or_financial",
            "document_or_language",
            "witness_or_organizational",
        },
        coalition_participants={"mara", "rowan", "seris"},
    )
    assert "pred.final_charter_prerequisites" in facts.predicates


def test_final_charter_blocker_prevents_manufacture():
    facts = EndingSourceCompiler.compile(
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
        unresolved_mandatory_crisis_blockers={"pred.border_crisis"},
    )
    assert "pred.final_charter_prerequisites" not in facts.predicates

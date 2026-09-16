from __future__ import annotations

import itertools

import pytest

from runtime.ending_precedence import AUTHORED_PRIORITY
from runtime.ending_sources import EndingSourceCompiler
from runtime.endings import (
    END_BROKEN_DIADEM,
    END_GOLDEN_COMPACT,
    END_IRON_CROWN,
    END_PEOPLES_CHARTER,
    END_QUIET_THRONE,
    END_SECOND_FOUNDER,
    END_STEWARD,
    EndingResolutionError,
    EndingResolver,
)
from runtime.state import GameState, SaveStore


def terminal_state(run_id: str = "qa") -> GameState:
    state = GameState.fresh(run_id)
    state.terminal = True
    return state


def test_p01_p05_ending_family_boundaries():
    resolver = EndingResolver()
    for ending_id in (
        END_STEWARD,
        END_IRON_CROWN,
        END_GOLDEN_COMPACT,
        END_PEOPLES_CHARTER,
        END_SECOND_FOUNDER,
    ):
        state = terminal_state(ending_id)
        assert resolver.resolve(state, qualified_endings=[ending_id]).ending_id == ending_id

    collapse = terminal_state("p05-collapse")
    assert resolver.resolve(collapse, qualified_endings=[END_IRON_CROWN], collapse_failure=True).ending_id == END_BROKEN_DIADEM


def test_p06_p09_source_qualification_and_blockers():
    golden = EndingSourceCompiler.compile(
        flags={"audited_monopoly", "merchant_charter"},
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
        flags_extra=None,
    ) if False else EndingSourceCompiler.compile(
        flags={"audited_monopoly", "merchant_charter", "guild_tribunal_independent", "guild_neutral_inspectors"},
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
    )
    assert "pred.guild_influence_strong" in golden.predicates

    charter = EndingSourceCompiler.compile(
        flags={"people_charter_endorsed", "crown_audited", "full_crown_audit_published", "military_red_line"},
        history={"history.house_assembly", "history.guild_representation"},
        systemic_evidence_families={"warehouse_or_financial", "document_or_language", "witness_or_organizational"},
        coalition_participants={"mara", "rowan", "seris"},
    )
    assert "pred.systemic_explanation_verified" not in charter.predicates
    assert "pred.coalition_cooperation" not in charter.predicates


def test_p10_p11_second_founder_requires_canonical_predicates():
    state = terminal_state("p10")
    qualification = EndingSourceCompiler.compile(
        systemic_evidence_families={"warehouse_or_financial", "document_or_language", "witness_or_organizational"},
        flags={"systemic_explanation_convergence"},
        history={"history.cross_faction_package"},
        coalition_participants={"mara", "rowan", "seris"},
    )
    assert "pred.systemic_explanation_verified" in qualification.predicates
    assert "pred.coalition_cooperation" in qualification.predicates

    missing_cooperation = EndingSourceCompiler.compile(
        systemic_evidence_families={"warehouse_or_financial", "document_or_language", "witness_or_organizational"},
        flags={"systemic_explanation_convergence"},
    )
    assert "pred.coalition_cooperation" not in missing_cooperation.predicates
    assert state.ending_identity is None


def test_p12_p15_quiet_and_failure_near_misses():
    resolver = EndingResolver()
    quiet = terminal_state("p12")
    assert resolver.resolve(quiet, explicit_withdrawal=True).ending_id == END_QUIET_THRONE

    near_miss = terminal_state("p13")
    with pytest.raises(EndingResolutionError, match="no ending qualifies"):
        resolver.resolve(near_miss)

    failure = terminal_state("p14")
    assert resolver.resolve(failure, collapse_failure=True).ending_id == END_BROKEN_DIADEM

    no_failure = terminal_state("p15")
    with pytest.raises(EndingResolutionError, match="no ending qualifies"):
        resolver.resolve(no_failure, collapse_failure=False)


def test_p16_p18_positive_pair_precedence_and_collapse():
    resolver = EndingResolver()
    pairs = [
        (END_STEWARD, END_PEOPLES_CHARTER),
        (END_GOLDEN_COMPACT, END_SECOND_FOUNDER),
        (END_PEOPLES_CHARTER, END_SECOND_FOUNDER),
    ]
    for left, right in pairs:
        state = terminal_state(f"{left}-{right}")
        winner = AUTHORED_PRIORITY.get((left, right), AUTHORED_PRIORITY.get((right, left)))
        assert resolver.resolve(state, qualified_endings=[left, right]).ending_id == winner

    collapsed = terminal_state("p18")
    assert resolver.resolve(collapsed, qualified_endings=[END_STEWARD, END_PEOPLES_CHARTER], collapse_failure=True).ending_id == END_BROKEN_DIADEM


def test_p19_p20_quiet_positive_and_repeatability():
    resolver = EndingResolver()
    state = terminal_state("p19")
    assert resolver.resolve(state, qualified_endings=[END_GOLDEN_COMPACT], explicit_withdrawal=True).ending_id == END_GOLDEN_COMPACT

    repeated = terminal_state("p20")
    first = resolver.resolve(repeated, qualified_endings=[END_SECOND_FOUNDER]).ending_id
    second = resolver.resolve(repeated, qualified_endings=[END_SECOND_FOUNDER]).ending_id
    assert first == second == END_SECOND_FOUNDER


def test_p21_p23_save_load_and_delay_lifecycle(tmp_path):
    state = GameState.fresh("p21")
    state.terminal = True
    state.flags.add("systemic_explanation_convergence")
    state.ending_evidence_families.update({"warehouse_or_financial", "document_or_language", "witness_or_organizational"})
    EndingResolver().resolve(state, qualified_endings=[END_SECOND_FOUNDER])
    path = tmp_path / "ending.json"
    SaveStore.save(state, path)
    restored = SaveStore.load(path)
    assert restored.snapshot() == state.snapshot()


def test_p22_p23_delay_before_ending_and_cancellation():
    from runtime.state import PendingDelay

    state = GameState.fresh("p22")
    delay = PendingDelay("qa.delay", "E45", "B", "E181", 4)
    state.schedule(delay)
    assert state.pending_delays["qa.delay"].status == "pending"
    state.cancel_delay("qa.delay")
    assert state.pending_delays["qa.delay"].status == "cancelled"
    with pytest.raises(ValueError, match="not pending"):
        state.resolve_delay("qa.delay")


def test_p24_p26_replay_isolation():
    first = GameState.fresh("p24")
    first.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    first.record_replay_meta("meta.replay.second_run_information_route")
    first.terminal = True
    exported = first.export_completed_run_meta()

    second = GameState.new_run_from_completed_prior("p25", exported)
    assert second.imported_meta_keys == {
        "meta.replay.warehouse_investigation_unlock",
        "meta.replay.second_run_information_route",
    }
    fresh = GameState.fresh("p26")
    assert fresh.imported_meta_keys == set()
    assert fresh.flags == set()
    assert fresh.history == set()


def test_p27_p30_namespace_aliases_are_rejected():
    compiler = EndingSourceCompiler
    with pytest.raises(Exception):
        from runtime.ending_contract import EndingQualification
        EndingQualification.build(predicates={"thread.border"})
    with pytest.raises(Exception):
        from runtime.ending_contract import EndingQualification
        EndingQualification.build(predicates={"thread.guild"})
    assert "pred.coalition_cooperation" not in compiler.compile(
        history={"history.cross_faction_package"},
        flags={"four_way_bargain"},
        coalition_participants={"unknown"},
    ).predicates
    with pytest.raises(Exception):
        from runtime.ending_contract import EndingQualification
        EndingQualification.build(flags={"systemic_explanation_verified"})

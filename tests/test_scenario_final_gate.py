from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from runtime.ending_sources import EndingSourceCompiler
from runtime.endings import (
    END_BROKEN_DIADEM, END_GOLDEN_COMPACT, END_IRON_CROWN,
    END_PEOPLES_CHARTER, END_SECOND_FOUNDER, END_STEWARD,
    EndingResolver,
)
from runtime.replay import ReplayBoundary
from runtime.state import GameState, SaveStore

ROOT = Path(__file__).resolve().parents[1]


def test_replay_boundary_round_trip_isolated_and_canonical():
    prior = GameState.fresh("prior")
    prior.flags.update({"run_only", "active_crisis"})
    prior.history.add("E131")
    prior.record_replay_meta("meta.replay.warehouse_investigation_unlock")
    prior.record_replay_meta("meta.replay.second_run_information_route")
    prior.terminal = True
    export = ReplayBoundary.export(prior)

    replay = ReplayBoundary.start_new_run("replay", export)
    assert replay.run_id == "replay"
    assert replay.current_event_id == "E01"
    assert replay.turn == 1
    assert replay.flags == set()
    assert replay.history == set()
    assert replay.pending_delays == {}
    assert replay.terminal is False
    assert replay.imported_meta_keys == {
        "meta.replay.warehouse_investigation_unlock",
        "meta.replay.second_run_information_route",
    }


def test_replay_boundary_rejects_reuse_of_same_run_and_unknown_meta():
    state = GameState.fresh("same")
    state.record_replay_meta("meta.replay.callback_forgotten_favor")
    state.terminal = True
    export = ReplayBoundary.export(state)
    with pytest.raises(ValueError, match="must differ"):
        ReplayBoundary.start_new_run("same", export)
    bad = export.as_dict()
    bad["meta_keys"] = ["meta.replay.invented"]
    with pytest.raises(ValueError, match="non-canonical"):
        ReplayBoundary.start_new_run("next", bad)


def test_catalog_scope_and_reachability_contract_are_green():
    result = subprocess.run(
        [sys.executable, "tools/validate_causal_reachability_contract.py"],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads((ROOT / "docs/MACHINE_CAUSAL_REACHABILITY_01.json").read_text())
    assert report["causal_edge_count"] == report["expected_causal_edge_count"]
    assert report["causal_node_count"] == report["expected_causal_node_count"]
    assert report["causal_nodes_unreachable_from_structural_root"] == 0


def test_all_ending_runtime_boundaries_are_deterministic_and_persistent():
    resolver = EndingResolver()
    endings = [END_STEWARD, END_IRON_CROWN, END_GOLDEN_COMPACT,
               END_PEOPLES_CHARTER, END_SECOND_FOUNDER, END_BROKEN_DIADEM]
    for ending in endings:
        state = GameState.fresh(f"{ending}-run")
        state.terminal = True
        failure = ending == END_BROKEN_DIADEM
        result = resolver.resolve(state, qualified_endings=[] if failure else [ending], collapse_failure=failure)
        assert result.ending_id == ending
        path = ROOT / ".pytest-final-gate-save.json"
        try:
            SaveStore.save(state, path)
            restored = SaveStore.load(path)
            assert restored.ending_identity == ending
            assert restored.snapshot() == state.snapshot()
        finally:
            path.unlink(missing_ok=True)


def test_canonical_composite_predicates_are_runtime_derivable_without_aliases():
    facts = EndingSourceCompiler.compile(
        flags={
            "people_charter_endorsed", "crown_audited", "full_crown_audit_published",
            "military_red_line", "systemic_explanation_convergence",
            "coalition_candidate_package", "audited_monopoly", "merchant_charter",
            "guild_tribunal_independent", "guild_neutral_inspectors",
        },
        history={
            "history.house_assembly", "history.guild_representation",
            "history.cross_faction_package", "history.guild_logistics_cooperation",
        },
        systemic_evidence_families={
            "warehouse_or_financial", "document_or_language", "witness_or_organizational"
        },
        coalition_participants={"mara", "rowan", "seris"},
    )
    assert {
        "pred.constitutional_prepared_strong",
        "pred.systemic_explanation_verified",
        "pred.coalition_cooperation",
        "pred.guild_influence_strong",
    } <= facts.predicates
    assert "pred.coalition_cooperation" not in EndingSourceCompiler.compile(
        flags={"four_way_bargain"},
        history={"history.cross_faction_package"},
        coalition_participants={"mara", "rowan", "seris"},
    ).predicates

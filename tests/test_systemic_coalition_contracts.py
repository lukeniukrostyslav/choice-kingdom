from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
SYSTEMIC = ROOT / "docs" / "MACHINE_SYSTEMIC_EXPLANATION_CONTRACT_01.json"
COALITION = ROOT / "docs" / "MACHINE_COALITION_COOPERATION_CONTRACT_01.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_systemic_explanation_contract_matches_frozen_graph() -> None:
    graph = load(GRAPH)
    contract = load(SYSTEMIC)
    source = graph["composite_predicates"]["pred.systemic_explanation_verified"]
    assert contract["predicate"] == "pred.systemic_explanation_verified"
    assert contract["producer"] == "E270-A"
    assert contract["requires_distinct_evidence_domains"] == [
        "warehouse_or_financial", "document_or_language", "witness_or_organizational"
    ]
    assert source["status"] == "SOURCE-CLOSED"
    assert source["producer"] == "E270-A"
    assert source["runtime_verified"] is False


def test_coalition_contract_matches_frozen_graph_and_rejects_alias() -> None:
    graph = load(GRAPH)
    contract = load(COALITION)
    source = graph["composite_predicates"]["pred.coalition_cooperation"]
    assert contract["producer"] == "E148-A"
    assert contract["requires"] == [
        "positive_mutual_concessions",
        "coalition_candidate_package",
        "at_least_three_distinct_canonical_participant_identities",
        "no_unresolved_coalition_collapse_blocker",
    ]
    assert contract["producer_runtime_binding"]["positive_outcome_marker"] == "coalition_candidate_package"
    assert "four_way_bargain" in contract["forbidden_aliases"]
    assert source["status"] == "SOURCE-CLOSED"
    assert source["producer"] == "E148-A"
    assert source["positive_outcome_marker"] == "coalition_candidate_package"
    assert source["runtime_verified"] is False


def test_known_runtime_gaps_are_not_hidden_by_source_contracts() -> None:
    graph = load(GRAPH)
    known = set(graph["known_not_yet_verified"])
    assert "fresh_run gameplay reachability" in known
    assert "replay reachability" in known
    assert "exact replay producer/key tuples for E186/E247/E248" in known

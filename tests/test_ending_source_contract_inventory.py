from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"

CONTRACTS = {
    "pred.budget_reform": ROOT / "docs" / "MACHINE_BUDGET_REFORM_CONTRACT_01.json",
    "pred.final_charter_prerequisites": ROOT / "docs" / "MACHINE_FINAL_CHARTER_CONTRACT_01.json",
    "pred.constitutional_prepared_strong": ROOT / "docs" / "MACHINE_CONSTITUTIONAL_PREPARED_CONTRACT_01.json",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_frozen_composite_predicates_have_explicit_machine_contracts() -> None:
    graph = load(GRAPH)
    composites = graph["composite_predicates"]
    for predicate, path in CONTRACTS.items():
        assert predicate in composites
        contract = load(path)
        assert contract["scope"] == "E01-E272"
        assert contract["predicate"] == predicate
        assert contract["runtime_verified"] is False


def test_source_closed_composites_are_not_silently_runtime_closed() -> None:
    graph = load(GRAPH)
    for predicate in CONTRACTS:
        assert graph["composite_predicates"][predicate]["status"] == "SOURCE-CLOSED"
        assert graph["composite_predicates"][predicate]["runtime_verified"] is False


def test_canonical_graph_keeps_known_runtime_boundaries_visible() -> None:
    graph = load(GRAPH)
    known = set(graph["known_not_yet_verified"])
    assert "fresh_run gameplay reachability" in known
    assert "ending incoming paths and precedence" in known
    assert "runtime lifecycle persistence" in known
    assert "Decision Engine execution" in known
    assert "delayed cancellation/supersession lifecycle" in known

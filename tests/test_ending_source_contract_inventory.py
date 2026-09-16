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


def test_guild_influence_machine_contract_is_explicit_and_unverified() -> None:
    path = ROOT / "docs" / "MACHINE_GUILD_INFLUENCE_CONTRACT_01.json"
    contract = load(path)
    graph = load(GRAPH)
    graph_contract = graph["composite_predicates"]["pred.guild_influence_strong"]
    assert contract["scope"] == "E01-E272"
    assert contract["predicate"] == "pred.guild_influence_strong"
    assert contract["minimum_distinct_domains"] == 3
    assert [d["id"] for d in contract["domains"]] == [
        "representation",
        "tribunal",
        "commercial_market",
        "qualified_logistics",
    ]
    assert graph_contract["min_distinct_domains"] == contract["minimum_distinct_domains"]
    assert graph_contract["domains"] == [d["id"] for d in contract["domains"]]
    assert contract["consumer_cannot_manufacture"] is True
    assert contract["runtime_verified"] is False
    assert "rel.ivo" in contract["forbidden_aliases"]


def test_coalition_machine_contract_freezes_e148_participant_identity_boundary() -> None:
    path = ROOT / "docs" / "MACHINE_COALITION_COOPERATION_CONTRACT_01.json"
    contract = load(path)
    graph = load(GRAPH)
    graph_contract = graph["composite_predicates"]["pred.coalition_cooperation"]
    assert contract["producer"] == "E148-A"
    assert contract["minimum_distinct_participants"] == 3
    assert contract["canonical_participant_identities"] == [
        "mara",
        "rowan",
        "seris",
        "ivo",
        "amara",
        "toma",
    ]
    assert graph_contract["producer"] == contract["producer"]
    assert graph_contract["minimum_distinct_participants"] == contract["minimum_distinct_participants"]
    assert graph_contract["canonical_participant_identities"] == contract["canonical_participant_identities"]
    assert contract["producer_runtime_binding"]["choice"] == "E148-A"
    assert contract["runtime_verified"] is False


def test_canonical_graph_keeps_known_runtime_boundaries_visible() -> None:
    graph = load(GRAPH)
    known = set(graph["known_not_yet_verified"])
    assert "fresh_run gameplay reachability" in known
    assert "ending incoming paths and precedence" in known
    assert "runtime lifecycle persistence" in known
    assert "Decision Engine execution" in known
    assert "delayed cancellation/supersession lifecycle" in known

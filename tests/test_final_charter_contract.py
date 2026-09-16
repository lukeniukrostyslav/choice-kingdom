from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_FINAL_CHARTER_CONTRACT_01.json"
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_final_charter_contract_is_explicit_and_consumer_only() -> None:
    contract = load(CONTRACT)
    assert contract["scope"] == "E01-E272"
    assert contract["predicate"] == "pred.final_charter_prerequisites"
    assert contract["consumer"] == "E209"
    assert contract["consumer_cannot_manufacture"] is True
    assert contract["runtime_verified"] is False
    assert {domain["id"] for domain in contract["required_domains"]} == {
        "civic_commons_legitimacy",
        "audit_institutional_legitimacy",
        "faction_house_guild_representation",
        "military_security_constitutional_route",
        "information_evidence_legitimacy",
        "coalition_cooperation",
    }


def test_final_charter_contract_matches_canonical_graph_source_contract() -> None:
    contract = load(CONTRACT)
    graph = load(GRAPH)
    graph_contract = graph["composite_predicates"]["pred.final_charter_prerequisites"]

    assert graph_contract["status"] == "SOURCE-CLOSED"
    assert graph_contract["consumer_only"] == ["E209"]
    assert set(graph_contract["requires"]) == {
        "people_charter_endorsed",
        "crown_audited_or_full_crown_audit_published",
        "history.house_assembly_and_history.guild_representation",
        "military_constitutional_or_military_red_line",
        "evidence_legitimacy",
        "pred.coalition_cooperation",
        "no_unresolved_mandatory_crisis_blocker",
    }


def test_late_events_cannot_be_declared_as_producers() -> None:
    contract = load(CONTRACT)
    assert contract["forbidden_manufacturers"] == ["E209", "E210"]
    assert "E209" not in [source for domain in contract["required_domains"] for source in domain["canonical_sources"]]
    assert "E210" not in [source for domain in contract["required_domains"] for source in domain["canonical_sources"]]


def test_forbidden_aliases_cannot_satisfy_final_charter_gate() -> None:
    contract = load(CONTRACT)
    assert set(contract["forbidden_aliases"]) == {
        "four_way_bargain",
        "rel.ivo",
        "rel.seris",
        "security_score_alone",
    }


def test_runtime_verification_remains_explicitly_open() -> None:
    contract = load(CONTRACT)
    assert contract["runtime_verified"] is False
    assert "mandatory-crisis blocker state contract" in contract["remaining_checks"]
    assert "producer-before-consumer ordering" in contract["remaining_checks"]

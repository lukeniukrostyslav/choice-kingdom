from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_CONSTITUTIONAL_PREPARED_CONTRACT_01.json"
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_constitutional_preparation_has_four_explicit_domains_and_three_minimum() -> None:
    contract = load(CONTRACT)
    assert contract["predicate"] == "pred.constitutional_prepared_strong"
    assert contract["minimum_distinct_domains"] == 3
    assert {d["id"] for d in contract["domains"]} == {"civic", "institutional", "factional", "military"}
    assert contract["runtime_verified"] is False


def test_constitutional_preparation_matches_canonical_graph() -> None:
    contract = load(CONTRACT)
    graph = load(GRAPH)
    graph_contract = graph["composite_predicates"]["pred.constitutional_prepared_strong"]
    assert graph_contract["status"] == "SOURCE-CLOSED"
    assert graph_contract["min_distinct_domains"] == 3
    assert graph_contract["domains"] == ["E50 civic", "E154 institutional", "E161 factional", "E199 military/law"]


def test_late_consumers_cannot_manufacture_preparation() -> None:
    contract = load(CONTRACT)
    assert contract["consumer_cannot_manufacture"] is True
    assert "E197" in contract["upstream_of"]
    assert "E197-E210 outcomes cannot create this predicate retroactively" in contract["anti_double_counting"]

from __future__ import annotations

import json
from pathlib import Path

from runtime.ending_sources import EndingSourceCompiler

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_GUILD_INFLUENCE_CONTRACT_01.json"


def load() -> dict:
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def test_guild_contract_matches_runtime_source_boundary() -> None:
    contract = load()
    assert contract["predicate"] == "pred.guild_influence_strong"
    assert contract["minimum_distinct_domains"] == 3
    assert {domain["id"] for domain in contract["domains"]} == {
        "representation", "tribunal", "commercial_market", "qualified_logistics"
    }
    assert contract["domains"][3]["canonical_sources"] == [
        "history.guild_logistics_cooperation", "guild_neutral_inspectors"
    ]
    assert contract["runtime_verified"] is False


def test_three_distinct_guild_domains_compile() -> None:
    facts = EndingSourceCompiler.compile(
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
        flags={"guild_tribunal_independent", "guild_neutral_inspectors"},
    )
    assert "pred.guild_influence_strong" in facts.predicates


def test_one_guild_domain_cannot_double_count() -> None:
    facts = EndingSourceCompiler.compile(
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
        flags={"guild_neutral_inspectors"},
    )
    assert "pred.guild_influence_strong" not in facts.predicates


def test_logistics_immunity_risk_invalidates_logistics_domain() -> None:
    facts = EndingSourceCompiler.compile(
        history={"history.guild_representation", "history.guild_logistics_cooperation"},
        flags={"guild_neutral_inspectors", "guild_tribunal_independent", "guild_logistics_immunity_risk"},
    )
    assert "pred.guild_influence_strong" not in facts.predicates


def test_relationships_and_stale_guild_alias_do_not_create_influence() -> None:
    facts = EndingSourceCompiler.compile(
        flags={"guild_tribunal_independent"},
        threads={"thread.guild"},
    )
    assert "pred.guild_influence_strong" not in facts.predicates

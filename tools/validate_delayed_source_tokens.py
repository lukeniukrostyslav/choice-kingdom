#!/usr/bin/env python3
"""Validate the source-level delayed producer token contract.

This validator checks exact event+choice+token identity only. It does not
claim runtime scheduling, cancellation, save/load persistence, or reachability.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_DELAYED_SOURCE_TOKENS_01.json"
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_DELAYED_SOURCE_TOKEN_VALIDATION_01.json"

EXPECTED = {
    "E181": ("E45", "B", "infrastructure_concession", "CLOSED"),
    "E182": ("E117", "B", "veteran_patronage", "CLOSED"),
    "E183": ("E118", "B", "estate_exception", "CLOSED"),
    "E184": (None, None, None, "OPEN"),
    "E185": ("E17", "A", "cheap_weapons", "CLOSED_IDENTITY"),
    "E242": ("E118", "B", "estate_exception", "PARTIAL"),
    "E243": ("E18", "B", "public_bridge", "CLOSED"),
    "E244": ("E09", "B", "flexible_accounts", "CLOSED"),
    "E245": ("E20", "A", "soldier_compensation", "CLOSED"),
    "E246": ("E160", "A", "winter_rent_ceiling", "CLOSED"),
}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    rows = {r["consumer"]: r for r in contract.get("records", [])}
    producer_rows = {(r.get("event"), r.get("choice"), r.get("fact")) for r in graph.get("source_closed_producers", [])}
    errors: list[str] = []
    checked: dict[str, dict] = {}

    for consumer, expected in EXPECTED.items():
        row = rows.get(consumer)
        if row is None:
            errors.append(f"missing record: {consumer}")
            continue
        actual = (row.get("source_event"), row.get("source_choice"), row.get("token"), row.get("status"))
        ok = actual == expected
        checked[consumer] = {"expected": expected, "actual": actual, "ok": ok}
        if not ok:
            errors.append(f"{consumer}: expected {expected!r}, got {actual!r}")

        event, choice, token, _ = expected
        if event is not None and (event, choice, token) not in producer_rows:
            errors.append(f"{consumer}: source token is not represented by machine producer inventory: {(event, choice, token)!r}")

    # Hard-negative guard for the most dangerous compensation merge.
    e245 = rows.get("E245", {})
    if e245.get("source_event") != "E20" or e245.get("source_choice") != "A":
        errors.append("E245: canonical source must remain E20-A")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.delayed_source_token_validation",
        "readiness": "PASS_SOURCE_IDENTITY" if not errors else "FAIL",
        "runtime_verified": False,
        "reachability_verified": False,
        "checked": checked,
        "errors": errors,
        "explicit_non_claims": [
            "does not prove scheduler semantics",
            "does not prove cancellation/supersession",
            "does not prove save/load persistence",
            "does not prove fresh-run reachability",
            "does not prove replay reachability",
            "does not establish semantic equality between graph context and producer edges"
        ]
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

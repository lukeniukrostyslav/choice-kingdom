#!/usr/bin/env python3
"""Close the source-level producer semantic-equality boundary.

This gate compares the frozen delayed producer identity contract against the
canonical producer inventory. It deliberately ignores runtime lifecycle state:
expiry, cancellation, save/load, scheduling and reachability remain separate
QA blocks.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "docs" / "CANONICAL_PRODUCER_INVENTORY_01.md"
COLLISION = ROOT / "docs" / "MACHINE_PRODUCER_CONSUMER_COLLISION_01.json"
OUT = ROOT / "docs" / "MACHINE_SOURCE_PRODUCER_SEMANTIC_EQUALITY_01.json"

EXPECTED = {
    "E181": ("E45-B", "infrastructure_concession"),
    "E182": ("E117-B", "veteran_patronage"),
    "E183": ("E118-B", "estate_exception"),
    "E184": ("E25-B", "secret_evidence_route"),
    "E185": ("E17-A", "cheap_weapons"),
    "E242": ("E118-B", "estate_exception"),
    "E243": ("E18-B", "public_bridge"),
    "E244": ("E09-B", "flexible_accounts"),
    "E245": ("E20-A", "soldier_compensation"),
    "E246": ("E160-A", "winter_rent_ceiling"),
}


def main() -> int:
    inventory = INVENTORY.read_text(encoding="utf-8")
    collision = json.loads(COLLISION.read_text(encoding="utf-8"))
    rows = {row["consumer"]: row for row in collision["records"]}
    errors: list[str] = []
    checked: dict[str, dict[str, object]] = {}

    # Inventory source identity is represented as producer -> token rows. The
    # exact strings below are intentionally narrow to avoid synonym promotion.
    inventory_expectations = {
        "E45-B": "infrastructure_concession",
        "E117-B": "veteran_patronage",
        "E118-B": "estate_exception",
        "E25-B": "secret_evidence_route",
        "E17-A": "cheap_weapons",
        "E18-B": "public_bridge",
        "E09-B": "flexible_accounts",
        "E20-A": "soldier_compensation",
        "E160-A": "winter_rent_ceiling",
    }
    for producer, token in inventory_expectations.items():
        if producer not in inventory or f"`{token}`" not in inventory:
            errors.append(f"canonical inventory missing exact producer/token evidence: {producer} / {token}")

    for consumer, expected in EXPECTED.items():
        row = rows.get(consumer)
        if row is None:
            errors.append(f"missing collision record: {consumer}")
            continue
        actual = (row.get("producer"), row.get("token"))
        ok = actual == expected
        checked[consumer] = {"expected": expected, "actual": actual, "ok": ok}
        if not ok:
            errors.append(f"{consumer}: expected {expected!r}, got {actual!r}")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.source_producer_semantic_equality",
        "scope": "E01-E272",
        "readiness": "PASS_SOURCE_PRODUCER_SEMANTIC_EQUALITY" if not errors else "FAIL",
        "checked": checked,
        "errors": errors,
        "runtime_verified": False,
        "reachability_verified": False,
        "non_claims": [
            "does not prove delayed scheduler execution",
            "does not prove cancellation/supersession",
            "does not prove save/load persistence",
            "does not prove fresh-run or replay reachability",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

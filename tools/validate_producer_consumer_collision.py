#!/usr/bin/env python3
"""Validate the source-level producer/consumer collision contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_PRODUCER_CONSUMER_COLLISION_01.json"
OUT = ROOT / "docs" / "MACHINE_PRODUCER_CONSUMER_COLLISION_VALIDATION_01.json"

EXPECTED = {
    "E181": ("E45-B", "infrastructure_concession", "NO_MERGE"),
    "E182": ("E117-B", "veteran_patronage", "CLOSED_IDENTITY"),
    "E183": ("E118-B", "estate_exception", "NO_MERGE"),
    "E184": (None, None, "OPEN"),
    "E185": ("E17-A", "cheap_weapons", "SEPARATE_LIFECYCLE"),
    "E242": ("E118-B", "estate_exception", "PARTIAL_NO_ALIAS"),
    "E243": ("E18-B", "public_bridge", "NO_MERGE"),
    "E244": ("E09-B", "flexible_accounts", "CLOSED_IDENTITY"),
    "E245": ("E20-A", "soldier_compensation", "HARD_NEGATIVE"),
    "E246": ("E160-A", "winter_rent_ceiling", "NO_MERGE"),
}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    rows = {row["consumer"]: row for row in contract["records"]}
    errors: list[str] = []
    checked: dict[str, dict] = {}

    for consumer, expected in EXPECTED.items():
        row = rows.get(consumer)
        if row is None:
            errors.append(f"missing record: {consumer}")
            continue
        actual = (row.get("producer"), row.get("token"), row.get("status"))
        ok = actual == expected
        checked[consumer] = {"expected": expected, "actual": actual, "ok": ok}
        if not ok:
            errors.append(f"{consumer}: expected {expected!r}, got {actual!r}")

    e245 = rows.get("E245", {})
    if e245.get("producer") != "E20-A":
        errors.append("E245 must remain exclusively E20-A")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.producer_consumer_collision_validation",
        "readiness": "PASS_COLLISION_SCREEN" if not errors else "FAIL",
        "checked": checked,
        "errors": errors,
        "runtime_verified": False,
        "reachability_verified": False,
        "explicit_non_claims": [
            "does not prove runtime reachability",
            "does not prove scheduler semantics",
            "does not prove semantic graph equality",
            "does not promote consumer wording into producers"
        ]
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

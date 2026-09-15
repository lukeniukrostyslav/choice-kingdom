#!/usr/bin/env python3
"""Validate the conservative source-level ending prerequisite contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_ENDING_PREREQUISITE_SATISFIABILITY_01.json"
OUT = ROOT / "docs" / "MACHINE_ENDING_PREREQUISITE_SATISFIABILITY_VALIDATION_01.json"

EXPECTED = {
    "Steward": "OPEN",
    "Iron Crown": "OPEN",
    "Golden Compact": "OPEN",
    "People's Charter": "OPEN_BLOCKED_FINAL_CHARTER_PRODUCER",
    "Broken Diadem": "OPEN",
    "Quiet Throne": "OPEN",
    "Second Founder": "OPEN_BLOCKED_REPLAY_AND_CONVERGENCE",
}


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    actual = contract.get("families", {})
    errors: list[str] = []
    checked: dict[str, dict[str, str | bool]] = {}
    for family, expected in EXPECTED.items():
        got = actual.get(family)
        ok = got == expected
        checked[family] = {"expected": expected, "actual": got, "ok": ok}
        if not ok:
            errors.append(f"{family}: expected {expected!r}, got {got!r}")

    rules = set(contract.get("rules", []))
    for required in (
        "consumer_cannot_manufacture_prerequisite",
        "support_evidence_is_not_final_predicate",
        "replay_meta_requires_explicit_promotion",
        "E33_E34_quarantined",
        "E273_E277_excluded",
    ):
        if required not in rules:
            errors.append(f"missing hard rule: {required}")

    if contract.get("fresh_run_reachability_verified") is not False:
        errors.append("fresh-run reachability must remain unverified")
    if contract.get("replay_reachability_verified") is not False:
        errors.append("replay reachability must remain unverified")
    if contract.get("precedence_verified") is not False:
        errors.append("ending precedence must remain unverified")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.ending_prerequisite_satisfiability_validation",
        "readiness": "PASS_CONSERVATIVE_SCREEN" if not errors else "FAIL",
        "checked": checked,
        "errors": errors,
        "runtime_verified": False,
        "reachability_verified": False,
        "precedence_verified": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the high-risk delayed-consequence identity boundary.

This gate checks only canonical source-level identity/status facts. It does not
invent absolute turns, cancellation rules, or runtime scheduling semantics.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
OUT = ROOT / "docs" / "MACHINE_DELAYED_LIFECYCLE_GATE_01.json"

EXPECTED = {
    "E181": {"statuses": {"CLOSED"}, "required_candidate": "E45-B"},
    "E182": {"statuses": {"CLOSED"}, "required_candidate": "E117-B"},
    "E183": {"statuses": {"CLOSED"}, "required_candidate": "E118-B"},
    "E184": {"statuses": {"OPEN"}, "required_candidate": None},
    "E185": {"statuses": {"PARTIAL", "OPEN"}, "required_candidate": "E17-A"},
    "E245": {"statuses": {"CLOSED", "PARTIAL"}, "required_candidate": "E20-A"},
    "E246": {"statuses": {"CLOSED", "PARTIAL"}, "required_candidate": "E160-A"},
}


def main() -> int:
    data = json.loads(GRAPH.read_text(encoding="utf-8"))
    rows = {row.get("consumer"): row for row in data.get("delayed_consumers", [])}
    errors: list[str] = []
    warnings: list[str] = []
    checked = {}

    for consumer, rule in EXPECTED.items():
        row = rows.get(consumer)
        if row is None:
            errors.append(f"missing delayed consumer: {consumer}")
            continue
        status = row.get("status")
        candidates = " ".join(str(x) for x in row.get("candidates", []))
        ok_status = status in rule["statuses"]
        required = rule["required_candidate"]
        ok_candidate = required is None or required in candidates
        checked[consumer] = {
            "status": status,
            "required_candidate": required,
            "candidate_present": ok_candidate,
        }
        if not ok_status:
            errors.append(f"{consumer}: unexpected status {status!r}; expected one of {sorted(rule['statuses'])}")
        if not ok_candidate:
            errors.append(f"{consumer}: required source candidate {required!r} is absent")
        if status in {"OPEN", "PARTIAL"}:
            warnings.append(f"{consumer}: lifecycle remains {status}; runtime scheduling/cancellation is not closed")

    # Explicit anti-invention guard: these phrases must not become absolute due turns.
    for row in data.get("delayed_consumers", []):
        text = json.dumps(row, ensure_ascii=False).lower()
        if "absolute due" in text or "invented turn" in text:
            errors.append(f"delayed row contains prohibited invented timing language: {row.get('consumer')}")

    report = {
        "schema_version": "1.1",
        "contract": "choice_kingdom.delayed_lifecycle_gate",
        "scope": "E01-E272",
        "readiness": "BLOCKED" if errors else ("PARTIAL" if warnings else "CLOSED"),
        "gameplay_verified": False,
        "checked": checked,
        "errors": errors,
        "warnings": warnings,
        "rules": [
            "source identity and lifecycle closure are separate",
            "relative authored delays are preserved; absolute due turns are not invented",
            "OPEN/PARTIAL rows cannot be promoted by this validator",
            "E181 source identity is closed at E45-B; exact runtime scheduler semantics remain separate",
            "E185 cheap_weapons identity is distinct from the later military-crisis condition",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": report["readiness"], "errors": len(errors), "warnings": len(warnings)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

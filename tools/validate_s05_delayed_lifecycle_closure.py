#!/usr/bin/env python3
"""Validate S05 delayed-consequence lifecycle source/contract closure.

This gate is deliberately source-level. It must never promote the production
Decision Engine or runtime gameplay to READY.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "MACHINE_CANONICAL_GRAPH_01.json"
DELAY = ROOT / "docs" / "MACHINE_DELAY_CONTRACT_01.json"
OUT = ROOT / "docs" / "MACHINE_S05_DELAYED_LIFECYCLE_CLOSURE_01.json"

EXPECTED = {
    "E181": ("E45-B", "delay.E45B.E181.second_toll_increase", 5),
    "E182": ("E117-B", "delay.E117B.E182.veteran_promise", 4),
    "E183": ("E118-B", "delay.E118B.E183.noble_exception_return", 5),
    "E184": ("E25-B", "delay.E25B.E184.quiet_evidence", 4),
    "E185": ("E17-A", "delay.E17A.E185.cheap_steel_failure", None),
    "E242": ("E118-B", "delay.E118B.E242.renewed_exception", 6),
    "E243": ("E18-B", "delay.E18B.E243.old_bridge", 5),
    "E244": ("E09-B", "delay.E09B.E244.audit_comes_due", 5),
    "E245": ("E20-A", "delay.E20A.E245.soldiers_son_returns", 6),
    "E246": ("E160-A", "delay.E160A.E246.price_ceiling_memory", 5),
}
EXCLUDED = {"E273", "E274", "E275", "E276", "E277"}


def main() -> int:
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    delay = json.loads(DELAY.read_text(encoding="utf-8"))
    errors: list[str] = []
    checked: dict[str, dict[str, object]] = {}

    scope = graph.get("scope", {})
    if scope.get("first_event") != 1 or scope.get("last_event") != 272:
        errors.append("canonical graph scope drifted from E01-E272")
    if set(scope.get("excluded_events", [])) != EXCLUDED:
        errors.append("excluded event scope drifted from E273-E277")

    rows = {r.get("consumer"): r for r in graph.get("delayed_consumers", [])}
    delay_rows = {r.get("resolutionTarget"): r for r in delay.get("delays", [])}
    if set(rows) != set(EXPECTED):
        errors.append(f"canonical delayed-consumer scope drift: expected {sorted(EXPECTED)}, got {sorted(rows)}")
    if set(delay_rows) != set(EXPECTED):
        errors.append(f"machine delay scope drift: expected {sorted(EXPECTED)}, got {sorted(delay_rows)}")

    keys = [r.get("exactlyOnceKey") for r in delay.get("delays", [])]
    ids = [r.get("id") for r in delay.get("delays", [])]
    if len(keys) != len(set(keys)):
        errors.append("duplicate exactlyOnceKey")
    if len(ids) != len(set(ids)):
        errors.append("duplicate delay id")

    for consumer, (source, expected_key, relative_turns) in EXPECTED.items():
        row = rows.get(consumer)
        drow = delay_rows.get(consumer)
        if row is None or drow is None:
            continue
        candidates = row.get("candidates", [])
        checked[consumer] = {
            "source": source,
            "candidate_present": source in candidates,
            "status": row.get("status"),
            "exactlyOnceKey": drow.get("exactlyOnceKey"),
            "cancellationRule": drow.get("cancellationRule"),
            "supersedes": drow.get("supersedes"),
        }
        if row.get("status") != "CLOSED":
            errors.append(f"{consumer}: graph status is not CLOSED")
        if source not in candidates:
            errors.append(f"{consumer}: exact source {source} missing")
        if drow.get("sourceEventId") != source.split("-")[0] or drow.get("sourceChoiceId") != source.split("-")[1]:
            errors.append(f"{consumer}: sourceEventId/sourceChoiceId mismatch")
        if drow.get("exactlyOnceKey") != expected_key:
            errors.append(f"{consumer}: exactlyOnceKey mismatch")
        if drow.get("saveLoadPolicy") != "persistent":
            errors.append(f"{consumer}: saveLoadPolicy must be persistent")
        if drow.get("replayPolicy") != "run_scoped_pending_delay":
            errors.append(f"{consumer}: replayPolicy must be run_scoped_pending_delay")
        if not isinstance(drow.get("priority"), int):
            errors.append(f"{consumer}: priority must be explicit integer")
        if "cancellationRule" not in drow:
            errors.append(f"{consumer}: cancellationRule must be explicit")
        if "supersedes" not in drow:
            errors.append(f"{consumer}: supersedes must be explicit")
        if drow.get("cancellationRule") == "":
            errors.append(f"{consumer}: cancellationRule cannot be empty")
        if relative_turns is None:
            if drow.get("earliestTurn") is not None:
                errors.append("E185: condition-bound delay must keep earliestTurn=null")
            if "military crisis" not in str(drow.get("cancellationRule", "")).lower():
                errors.append("E185: explicit later military-crisis qualification is required")
        else:
            earliest = drow.get("earliestTurn")
            if not isinstance(earliest, dict) or earliest.get("relativeToSource") != relative_turns:
                errors.append(f"{consumer}: relative earliestTurn must be +{relative_turns}")
        for field in ("id", "sourceEventId", "sourceChoiceId", "resolutionTarget", "exactlyOnceKey", "auditLabel"):
            if not drow.get(field):
                errors.append(f"{consumer}: missing required lifecycle field {field}")
        for value in (drow.get("sourceEventId"), drow.get("resolutionTarget")):
            if value in EXCLUDED:
                errors.append(f"{consumer}: excluded event {value} entered delay contract")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.s05_delayed_lifecycle_closure",
        "scope": "E01-E272",
        "closed_delayed_consumers": sorted(EXPECTED),
        "checked": checked,
        "source_contract_closed": not errors,
        "runtime_verified": False,
        "readiness": "CLOSED_SOURCE_CONTRACT" if not errors else "BLOCKED",
        "errors": errors,
        "rules": [
            "all ten canonical delayed callbacks are exact-source closed",
            "cancellation and supersession are explicit, including none_authored/null",
            "no invented cancellation edge is permitted",
            "relative timing is source-relative; E185 is condition-bound",
            "pending state is persistent and replay-scoped",
            "E273-E277 are excluded",
            "source closure never implies runtime Decision Engine readiness",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

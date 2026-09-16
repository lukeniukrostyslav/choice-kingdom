#!/usr/bin/env python3
"""Audit authored triggers against the runtime trigger interpreter."""
from __future__ import annotations

import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.catalog import (  # noqa: E402
    EVENT_OR_RE,
    NUMERIC_RE,
    REL_COND_RE,
    TOKEN_RE,
    AuthoredCatalog,
)

OUT = ROOT / "docs" / "MACHINE_RUNTIME_TRIGGER_SEMANTICS_AUDIT_01.json"


SAFE_ALIAS_PHRASES = {
    "high trust", "high civic trust", "civic/public trust",
    "low trust", "public distrust", "low security", "strong security",
    "low gold", "treasury pressure", "strong treasury pressure",
    "high power", "high reputation", "food shortage", "food-price pressure",
    "food pressure", "severe winter", "winter pressure", "border tension",
    "border pressure", "low army readiness", "strong market oversight",
    "market pressure", "guild labor tension", "apprentice pressure",
    "high information pressure", "high reform spending", "audit reform",
    "document audit route", "institutional reform", "deep investigation",
    "advanced investigation",
}


def classify(trigger: str) -> str:
    low = trigger.lower().strip().rstrip(".")
    if not trigger:
        return "EMPTY"
    if "first turn" in low:
        return "FIRST_TURN"
    if low == "severe winter":
        return "SEVERE_WINTER"
    if low in SAFE_ALIAS_PHRASES:
        return "SAFE_CANONICAL_ALIAS"
    if NUMERIC_RE.search(trigger) or REL_COND_RE.search(trigger) or TOKEN_RE.search(trigger):
        # If a trigger also contains prose, it is only partially executable.
        residue = NUMERIC_RE.sub(" ", trigger)
        residue = REL_COND_RE.sub(" ", residue)
        residue = TOKEN_RE.sub(" ", residue)
        residue = EVENT_OR_RE.sub(" ", residue)
        residue = re.sub(r"\b(?:and|or|after|at least|turns?|later|from|through|with|plus)\b", " ", residue, flags=re.I)
        residue = re.sub(r"[+<>=`'(),.-]", " ", residue)
        if re.search(r"[A-Za-z]{3,}", residue):
            return "PARTIAL_PROSE"
        return "CANONICAL_TOKEN_OR_THRESHOLD"
    if EVENT_OR_RE.search(trigger):
        return "EVENT_REFERENCE"
    return "OPAQUE_PROSE"


def main() -> int:
    catalog = AuthoredCatalog.from_repository(ROOT)
    rows = []
    for event in catalog.events.values():
        classification = classify(event.trigger)
        if classification == "OPAQUE_PROSE":
            refs = catalog.authored_prerequisites(event.event_id)
            normalized = event.trigger.lower().strip().rstrip(".")
            if refs and normalized in {f"after {ref.lower()}" for ref in refs}:
                classification = "EVENT_PREREQUISITE"
        rows.append({
            "event": event.event_id,
            "trigger": event.trigger,
            "classification": classification,
        })
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["classification"]] = counts.get(row["classification"], 0) + 1
    opaque = [row for row in rows if row["classification"] in {"OPAQUE_PROSE", "PARTIAL_PROSE"}]
    report = {
        "schema_version": "1.0",
        "scope": "E01-E272",
        "audit_only": True,
        "counts": counts,
        "opaque_or_partial_count": len(opaque),
        "opaque_or_partial": opaque,
        "semantic_boundary": "Opaque prose is not converted into runtime truth. Each such trigger requires an authoritative canonical producer/predicate/route contract before engine implementation.",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", **counts, "opaque_or_partial_count": len(opaque)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate the frozen ending identifier namespace and stale-alias boundary.

The boundary is about runtime identifiers, not prose describing forbidden aliases.
Authoritative machine sources may legitimately mention an old alias inside an
explicit negative/documentation field; those mentions must not be interpreted
as runtime state names.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_01.json"
OUT = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_VALIDATION_01.json"
EXPECTED_SCOPE = "E01-E272"

NON_RUNTIME_KEYS = {
    "forbidden_alias", "forbidden_runtime_aliases", "hard_negatives",
    "canonical_source_rules", "rules", "qa_note", "note", "reason",
    "description", "semantic_boundary", "known_not_yet_verified",
    "validation_gates",
}


def _contains_exact_identifier(text: str, identifier: str) -> bool:
    pattern = rf"(?<![A-Za-z0-9_.]){re.escape(identifier)}(?![A-Za-z0-9_])"
    return re.search(pattern, text) is not None


def _runtime_strings(value: Any, key: str | None = None) -> list[str]:
    """Extract namespace-qualified runtime identifiers from structured JSON."""
    if key in NON_RUNTIME_KEYS:
        return []
    if isinstance(value, dict):
        result: list[str] = []
        for child_key, child_value in value.items():
            result.extend(_runtime_strings(child_value, child_key))
        return result
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(_runtime_strings(item, key))
        return result
    if isinstance(value, str) and value.startswith(("thread.", "pred.", "meta.")):
        return [value]
    return []


def _markdown_runtime_identifiers(text: str) -> list[str]:
    """Read only canonical-key cells from the registry, not explanatory prose."""
    identifiers: list[str] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if cells and cells[0].startswith(("thread.", "pred.", "meta.")):
            identifiers.append(cells[0])
    return identifiers


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    aliases = contract.get("forbidden_runtime_aliases", [])
    canonical = contract.get("canonical_identifiers", {})
    sources = [ROOT / path for path in contract.get("authoritative_machine_sources", [])]
    allowlist = {ROOT / path for path in contract.get("documentation_allowlist", [])}
    errors: list[str] = []
    source_texts: dict[str, str] = {}
    runtime_source_ids: dict[str, list[str]] = {}

    if contract.get("scope") != EXPECTED_SCOPE:
        errors.append(f"unexpected contract scope: {contract.get('scope')!r}")
    if not aliases:
        errors.append("forbidden alias inventory is empty")
    if not canonical:
        errors.append("canonical identifier inventory is empty")
    if len(set(aliases)) != len(aliases):
        errors.append("forbidden alias inventory contains duplicates")
    if len(set(canonical.values())) != len(canonical):
        errors.append("canonical identifier inventory contains duplicate values")

    for key, value in canonical.items():
        if not isinstance(value, str) or not value:
            errors.append(f"canonical identifier {key!r} has invalid value")
        elif not (value.startswith("thread.") or value.startswith("pred.")):
            errors.append(f"canonical identifier {key!r} is not namespace-qualified: {value!r}")

    for path in sources:
        rel = str(path.relative_to(ROOT))
        if not path.exists():
            errors.append(f"missing authoritative machine source: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        source_texts[rel] = text
        if path.suffix == ".json":
            try:
                parsed = json.loads(text)
                identifiers = _runtime_strings(parsed)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid authoritative JSON source {rel}: {exc}")
                identifiers = []
        else:
            identifiers = _markdown_runtime_identifiers(text)
        runtime_source_ids[rel] = identifiers
        for alias in aliases:
            if any(_contains_exact_identifier(identifier, alias) for identifier in identifiers):
                errors.append(
                    f"forbidden runtime alias {alias!r} appears as an exact runtime identifier in authoritative machine source {rel}"
                )

    combined_runtime_identifiers = [
        identifier for identifiers in runtime_source_ids.values() for identifier in identifiers
    ]
    for key, value in canonical.items():
        if not any(_contains_exact_identifier(identifier, value) for identifier in combined_runtime_identifiers):
            errors.append(
                f"canonical identifier {key!r}={value!r} is absent from all authoritative runtime identifier fields"
            )

    for path in allowlist:
        if not path.exists():
            errors.append(f"missing documentation allowlist entry: {path.relative_to(ROOT)}")

    result = {
        "schema_version": "1.4",
        "contract": "choice_kingdom.ending_alias_boundary_validation",
        "scope": EXPECTED_SCOPE,
        "readiness": "PASS" if not errors else "FAIL",
        "forbidden_alias_count": len(aliases),
        "canonical_identifier_count": len(canonical),
        "authoritative_sources_checked": len(sources),
        "documentation_allowlist_entries": len(allowlist),
        "canonical_namespace_qualified": all(
            isinstance(v, str) and (v.startswith("thread.") or v.startswith("pred."))
            for v in canonical.values()
        ),
        "canonical_presence_verified_across_sources": not any(
            "absent from all authoritative runtime identifier fields" in error
            for error in errors
        ),
        "exact_identifier_matching": True,
        "runtime_identifier_extraction": True,
        "prose_alias_mentions_ignored": True,
        "errors": errors,
        "runtime_verified": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

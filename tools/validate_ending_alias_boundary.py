#!/usr/bin/env python3
"""Validate the frozen ending identifier namespace and stale-alias boundary."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_01.json"
OUT = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_VALIDATION_01.json"
EXPECTED_SCOPE = "E01-E272"


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    aliases = contract.get("forbidden_runtime_aliases", [])
    canonical = contract.get("canonical_identifiers", {})
    sources = [ROOT / path for path in contract.get("authoritative_machine_sources", [])]
    allowlist = {ROOT / path for path in contract.get("documentation_allowlist", [])}
    errors: list[str] = []
    source_texts: dict[str, str] = {}

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
        for alias in aliases:
            if alias in text:
                errors.append(f"forbidden runtime alias {alias!r} appears in authoritative machine source {rel}")

    combined = "\n".join(source_texts.values())
    for key, value in canonical.items():
        if value not in combined:
            errors.append(f"canonical identifier {key!r}={value!r} is absent from all authoritative machine sources")

    for path in allowlist:
        if not path.exists():
            errors.append(f"missing documentation allowlist entry: {path.relative_to(ROOT)}")

    result = {
        "schema_version": "1.2",
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
            f"canonical identifier {key!r}=" in error and "absent from all" in error
            for error in errors for key in canonical
        ),
        "errors": errors,
        "runtime_verified": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

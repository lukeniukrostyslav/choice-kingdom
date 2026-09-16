#!/usr/bin/env python3
"""Validate that stale ending aliases cannot leak into authoritative runtime contracts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_01.json"
OUT = ROOT / "docs" / "MACHINE_ENDING_ALIAS_BOUNDARY_VALIDATION_01.json"


def main() -> int:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    aliases = contract.get("forbidden_runtime_aliases", [])
    canonical = contract.get("canonical_identifiers", {})
    sources = [ROOT / path for path in contract.get("authoritative_machine_sources", [])]
    allowlist = {ROOT / path for path in contract.get("documentation_allowlist", [])}
    errors: list[str] = []

    if not aliases:
        errors.append("forbidden alias inventory is empty")
    if not canonical:
        errors.append("canonical identifier inventory is empty")

    for path in sources:
        if not path.exists():
            errors.append(f"missing authoritative machine source: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for alias in aliases:
            if alias in text:
                errors.append(
                    f"forbidden runtime alias {alias!r} appears in authoritative machine source {path.relative_to(ROOT)}"
                )

    for alias, value in canonical.items():
        if not isinstance(value, str) or not value:
            errors.append(f"canonical identifier {alias!r} has invalid value")

    result = {
        "schema_version": "1.0",
        "contract": "choice_kingdom.ending_alias_boundary_validation",
        "readiness": "PASS" if not errors else "FAIL",
        "forbidden_alias_count": len(aliases),
        "canonical_identifier_count": len(canonical),
        "authoritative_sources_checked": len(sources),
        "documentation_allowlist_entries": len(allowlist),
        "errors": errors,
        "runtime_verified": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"readiness": result["readiness"], "errors": len(errors)}, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

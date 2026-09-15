#!/usr/bin/env python3
"""Validate the authored ending QA matrix without pretending runtime exists."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "ENDING_PRECEDENCE_TEST_MATRIX_01.md"

FAMILIES = {
    "END_STEWARD",
    "END_IRON_CROWN",
    "END_GOLDEN_COMPACT",
    "END_PEOPLES_CHARTER",
    "END_BROKEN_DIadem".upper(),
    "END_QUIET_THRONE",
    "END_SECOND_FOUNDER",
}

REQUIRED_TESTS = {f"P{i:02d}" for i in range(1, 31)}
REQUIRED_ORDER = [
    "Validate terminal state and save version.",
    "Evaluate collapse/failure predicates.",
    "Evaluate explicit withdrawal / Quiet Throne condition.",
    "Evaluate all positive ending qualification predicates.",
    "If multiple positive endings qualify, apply an explicit authored priority table.",
    "Record one immutable ending identity.",
    "Never mutate prior history or invent a prerequisite to force an ending.",
]


def main() -> int:
    text = MATRIX.read_text(encoding="utf-8")
    errors: list[str] = []

    if "Scope: seven current ending families and E265–E270." not in text:
        errors.append("matrix scope header missing")

    test_ids = set(re.findall(r"\|\s*(P\d{2})\s*\|", text))
    if test_ids != REQUIRED_TESTS:
        missing = sorted(REQUIRED_TESTS - test_ids)
        extra = sorted(test_ids - REQUIRED_TESTS)
        if missing:
            errors.append("missing tests: " + ", ".join(missing))
        if extra:
            errors.append("unexpected tests: " + ", ".join(extra))

    if "## Deterministic precedence order" not in text:
        errors.append("deterministic precedence section missing")
    else:
        section = text.split("## Deterministic precedence order", 1)[1].split("## Test matrix", 1)[0]
        for fragment in REQUIRED_ORDER:
            if fragment not in section:
                errors.append("missing precedence rule: " + fragment)

    for family in ("END_STEWARD", "END_IRON_CROWN", "END_GOLDEN_COMPACT", "END_PEOPLES_CHARTER", "END_BROKEN_DIADEM", "END_QUIET_THRONE", "END_SECOND_FOUNDER"):
        if family not in text:
            errors.append("missing ending family: " + family)

    for forbidden in ("E273", "E274", "E275", "E276", "E277"):
        # Expansion events are allowed only as explicit exclusion language.
        for line in text.splitlines():
            if forbidden in line and "excluded" not in line.lower() and "cannot" not in line.lower():
                errors.append(f"forbidden production use of {forbidden}")
                break

    for required in (
        "authored priority table",
        "Near-miss state",
        "Delayed-consequence interaction",
        "Replay interaction",
        "save/load",
        "stale alias",
    ):
        if required.lower() not in text.lower():
            errors.append("missing QA requirement: " + required)

    print(f"ENDING_TEST_MATRIX_CONTRACT: {'PASS' if not errors else 'FAIL'}")
    print(f"tests={len(test_ids)}")
    print(f"errors={len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

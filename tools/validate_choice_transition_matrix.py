#!/usr/bin/env python3
"""Validate the authored A/B choice transition matrix against canonical event sources.

This is a QA contract: it does not invent effects. Every matrix row must point to
an authored event choice and carry explicit state/effect evidence copied from the
canonical source. Production scope is frozen to E01-E272.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = [ROOT / "docs" / "EVENT_CATALOG_EXPANSION_151_210.md", ROOT / "docs" / "EVENT_CATALOG_EXPANSION_211_272.md"]
MATRIX = ROOT / "docs" / "CANONICAL_CHOICE_TRANSITION_MATRIX_01.md"

EVENT_RE = re.compile(r"^###\\s+(E(\\d{2,3}))\\b", re.I | re.M)
CHOICE_RE = re.compile(r"(?:^|\\n)\\s*(?:[-*]\\s*)?([AB])\\s*[:—-]\\s*(.+)", re.I)
TOKEN_RE = re.compile(r"`[^`]+`")
EFFECT_WORDS = re.compile(r"\\b(establish|produce|set|mark|clear|reset|resolve|cancel|schedule|record|preserve|trigger|route|effect|state|predicate|flag|history|thread|condition|evidence|ending|cycle|meta)\\b", re.I)


def read_catalog() -> dict[str, str]:
    events: dict[str, str] = {}
    for path in CATALOGS:
        text = path.read_text(encoding="utf-8")
        matches = list(EVENT_RE.finditer(text))
        for i, m in enumerate(matches):
            eid = m.group(1).upper()
            if not 1 <= int(eid[1:]) <= 272:
                continue
            body = text[m.end(): matches[i + 1].start() if i + 1 < len(matches) else len(text)]
            if eid in events:
                raise SystemExit(f"duplicate canonical event: {eid}")
            events[eid] = body
    return events


def main() -> int:
    events = read_catalog()
    expected = {f"E{i:02d}" for i in range(1, 273)}
    missing = sorted(expected - events, key=lambda x: int(x[1:]))
    if missing:
        print("MISSING_CANONICAL_EVENTS", ",".join(missing))
        return 1

    if not MATRIX.exists():
        print(f"MISSING_MATRIX {MATRIX}")
        return 1
    matrix = MATRIX.read_text(encoding="utf-8")
    errors: list[str] = []

    for eid in sorted(expected, key=lambda x: int(x[1:])):
        if not re.search(rf"\\b{eid}\\b", matrix):
            errors.append(f"matrix missing {eid}")
            continue
        body = events[eid]
        choices = {m.group(1).upper(): m.group(2).strip() for m in CHOICE_RE.finditer(body)}
        if set(choices) != {"A", "B"}:
            errors.append(f"{eid}: canonical choices are not exactly A+B")
            continue
        for label, choice in choices.items():
            if not (TOKEN_RE.search(choice) or EFFECT_WORDS.search(choice)):
                errors.append(f"{eid}-{label}: no explicit authored effect/state signal")
            if not (TOKEN_RE.search(choice) or EFFECT_WORDS.search(choice)):
                errors.append(f"{eid}-{label}: no explicit state/evidence marker")

    # Matrix must explicitly declare frozen scope and one row per event.
    if "E01–E272" not in matrix and "E01-E272" not in matrix:
        errors.append("matrix missing frozen E01-E272 scope declaration")
    rows = set(re.findall(r"\\bE(\\d{2,3})\\s*[-–]\\s*([AB])\\b", matrix, re.I))
    for eid in sorted(expected, key=lambda x: int(x[1:])):
        n = str(int(eid[1:]))
        for label in ("A", "B"):
            if (n, label) not in {(a, b.upper()) for a, b in rows}:
                errors.append(f"matrix missing transition row {eid}-{label}")

    if errors:
        print("FAIL")
        for e in errors[:200]:
            print(e)
        print(f"errors={len(errors)}")
        return 1
    print("PASS")
    print("scope=E01-E272")
    print("events=272")
    print("choices=544")
    print("authored_transition_rows=544")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

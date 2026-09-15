#!/usr/bin/env python3
"""Static linter for the Choice Kingdom authored markdown catalog.

This is QA tooling only. It does not execute gameplay and must never be treated
as proof of runtime reachability. It extracts event/choice IDs plus explicit
Trigger/Flag/History/Thread/Immediate/Delayed lines and reports structural gaps.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CATALOGS = sorted(DOCS.glob("EVENT_CATALOG*.md")) + sorted(DOCS.glob("E*_*.md"))
CATALOGS = sorted(set(p for p in CATALOGS if "AUDIT" not in p.name and "CONTRACT" not in p.name))

EVENT_RE = re.compile(r"^###\s+(E\d{2,3})\s+[—-]\s+(.+?)\s*$")
CHOICE_RE = re.compile(r"^\*\*([AB])\s+[—-]\s+(.+?)\*\*\s*$")
TOKEN_RE = re.compile(r"`([^`]+)`")

KEYWORDS = ("Flag:", "History:", "Thread:", "Unlock:", "Delayed:", "Trigger:", "Immediate:")


def main() -> int:
    events: dict[str, dict] = {}
    occurrences: defaultdict[str, list[str]] = defaultdict(list)
    warnings: list[str] = []

    for path in CATALOGS:
        text = path.read_text(encoding="utf-8")
        current = None
        choice = None
        for lineno, raw in enumerate(text.splitlines(), 1):
            line = raw.strip()
            m = EVENT_RE.match(line)
            if m:
                current, title = m.groups()
                events.setdefault(current, {"title": title, "file": path.name, "line": lineno, "choices": []})
                choice = None
                continue
            m = CHOICE_RE.match(line)
            if m and current:
                choice = m.group(1)
                events[current]["choices"].append(choice)
                continue
            if current and any(line.startswith(k) for k in KEYWORDS):
                for token in TOKEN_RE.findall(line):
                    occurrences[token].append(f"{current}-{choice or '?'}@{path.name}:{lineno}")

    for eid, info in sorted(events.items(), key=lambda x: int(x[0][1:])):
        if set(info["choices"]) != {"A", "B"}:
            warnings.append(f"{eid}: expected A/B choices, found {sorted(set(info['choices']))}")

    duplicate_tokens = {k: v for k, v in occurrences.items() if len(v) > 1}

    print(f"catalog_files={len(CATALOGS)}")
    print(f"events={len(events)}")
    print(f"token_occurrences={sum(len(v) for v in occurrences.values())}")
    print(f"unique_tokens={len(occurrences)}")
    print(f"duplicate_token_mentions={len(duplicate_tokens)}")
    print(f"choice_shape_warnings={len(warnings)}")

    if warnings:
        print("\nCHOICE SHAPE WARNINGS")
        print("\n".join(warnings[:50]))

    if duplicate_tokens:
        print("\nREPEATED TOKENS (review required; repetition is not automatically an error)")
        for token, refs in sorted(duplicate_tokens.items()):
            print(f"{token}: {', '.join(refs[:12])}")

    # Current catalogs are prose-oriented, so a non-zero exit is reserved for
    # malformed event structure, not for unresolved canonical semantics.
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())

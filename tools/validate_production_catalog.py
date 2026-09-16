#!/usr/bin/env python3
"""Validate the deterministic machine production catalog projection."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.compile_production_catalog import compile_catalog  # noqa: E402


def main() -> int:
    catalog = compile_catalog()
    events = catalog["events"]
    if catalog["event_count"] != 272:
        print("PRODUCTION CATALOG VALIDATION: FAIL\n- expected 272 events")
        return 1
    if sum(len(event["choices"]) for event in events) != 520:
        print("PRODUCTION CATALOG VALIDATION: FAIL\n- expected 520 choices")
        return 1
    if sum(not event["choices"] for event in events) != 13:
        print("PRODUCTION CATALOG VALIDATION: FAIL\n- expected 13 no-choice nodes")
        return 1
    if catalog["scope"]["excluded_events"] != ["E273", "E274", "E275", "E276", "E277"]:
        print("PRODUCTION CATALOG VALIDATION: FAIL\n- invalid frozen scope")
        return 1
    print("PRODUCTION CATALOG VALIDATION: PASS")
    print(f"events={len(events)}")
    print(f"choices={sum(len(e['choices']) for e in events)}")
    print(f"no_choice_events={sum(not e['choices'] for e in events)}")
    print("source_of_truth=authored markdown")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

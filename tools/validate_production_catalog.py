#!/usr/bin/env python3
"""Verify the committed machine production catalog exactly matches authored data."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.compile_production_catalog import OUT, compile_catalog  # noqa: E402


def main() -> int:
    expected = compile_catalog()
    if not OUT.exists():
        print("PRODUCTION CATALOG VALIDATION: FAIL")
        print(f"- missing {OUT.relative_to(ROOT)}")
        return 1
    actual = json.loads(OUT.read_text(encoding="utf-8"))
    if actual != expected:
        print("PRODUCTION CATALOG VALIDATION: FAIL")
        print("- committed artifact differs from deterministic authored projection")
        return 1
    events = actual["events"]
    print("PRODUCTION CATALOG VALIDATION: PASS")
    print(f"events={len(events)}")
    print(f"choices={sum(len(e['choices']) for e in events)}")
    print(f"no_choice_events={sum(not e['choices'] for e in events)}")
    print("source_of_truth=authored markdown")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

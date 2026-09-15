from __future__ import annotations

import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/MACHINE_DELAY_CONTRACT_01.json"


class ReferenceDelayRuntime:
    """Deterministic QA model for the frozen delay contract.

    This is intentionally a test/reference model, not the production Decision Engine.
    It proves the lifecycle invariants the future engine must implement.
    """

    def __init__(self, rows):
        self.rows = rows
        self.pending = {}
        self.resolved = set()

    def schedule(self, row, source_turn):
        key = row["exactlyOnceKey"]
        if key in self.resolved or key in self.pending:
            return False
        earliest = row["earliestTurn"].get("relativeToSource") if row.get("earliestTurn") else None
        due = None if earliest is None else source_turn + earliest
        self.pending[key] = {"row": row, "source_turn": source_turn, "due": due}
        return True

    def due(self, turn, *, military_crisis=False):
        fired = []
        for key, item in list(self.pending.items()):
            row = item["row"]
            if row["resolutionTarget"] == "E185" and not military_crisis:
                continue
            if item["due"] is not None and turn < item["due"]:
                continue
            fired.append(row["resolutionTarget"])
            self.resolved.add(key)
            del self.pending[key]
        return fired

    def save_load_roundtrip(self):
        payload = json.dumps(self.pending, sort_keys=True)
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "pending.json"
            p.write_text(payload, encoding="utf-8")
            restored = json.loads(p.read_text(encoding="utf-8"))
        self.pending = restored

    def fresh_run(self):
        self.pending = {}
        self.resolved = set()


contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
rows = contract["delays"]
errors = []

if len(rows) != 10:
    errors.append(f"expected 10 delayed rows, got {len(rows)}")
if len({r["exactlyOnceKey"] for r in rows}) != len(rows):
    errors.append("exactlyOnceKey values are not unique")

# Isolate each delay for its earliest-turn proof so a later delay cannot be
# consumed by an unrelated earlier assertion.
for index, row in enumerate(rows, start=1):
    isolated = ReferenceDelayRuntime(rows)
    source_turn = 10 + index
    if not isolated.schedule(row, source_turn):
        errors.append(f"initial scheduling rejected for {row['exactlyOnceKey']}")
    if isolated.schedule(row, source_turn):
        errors.append(f"duplicate scheduling accepted for {row['exactlyOnceKey']}")

    item = isolated.pending[row["exactlyOnceKey"]]
    due = item["due"]
    if due is not None and isolated.due(due - 1):
        errors.append(f"delay fired before earliestTurn: {row['exactlyOnceKey']}")

# Run the complete set together for persistence and eventual execution checks.
rt = ReferenceDelayRuntime(rows)
for index, row in enumerate(rows, start=1):
    source_turn = 10 + index
    rt.schedule(row, source_turn)
    if rt.schedule(row, source_turn):
        errors.append(f"duplicate scheduling accepted for {row['exactlyOnceKey']}")

pending_before = set(rt.pending)
rt.save_load_roundtrip()
if set(rt.pending) != pending_before:
    errors.append("pending delay state changed across save/load roundtrip")

# E185 is condition-bound: no crisis means no execution; crisis permits execution.
fired_without_crisis = rt.due(999, military_crisis=False)
if "E185" in fired_without_crisis:
    errors.append("E185 fired without the authored later military crisis")
fired_with_crisis = rt.due(999, military_crisis=True)
if "E185" not in fired_with_crisis:
    errors.append("E185 did not execute when the authored military-crisis condition became true")

# All other delays should resolve once their authored due condition is satisfied.
remaining_non_e185 = [
    item for item in rt.pending.values() if item["row"]["resolutionTarget"] != "E185"
]
if remaining_non_e185:
    errors.append("one or more due non-E185 delays remained pending")

# Completed keys cannot execute twice or remain pending.
for row in rows:
    key = row["exactlyOnceKey"]
    if key in rt.resolved and key in rt.pending:
        errors.append(f"resolved key still pending: {key}")

# Fresh run must not inherit prior-run pending or resolved state.
rt.fresh_run()
if rt.pending or rt.resolved:
    errors.append("fresh run inherited prior-run delay/meta state")

if errors:
    print("DELAY_RUNTIME_REFERENCE: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("DELAY_RUNTIME_REFERENCE: PASS")
print("rows=10")
print("schedule=deduplicated")
print("earliest_turn=isolated_and_honored")
print("condition_bound=E185 military_crisis")
print("save_load=persistent_pending_state")
print("fresh_run=reset")
print("production_runtime=NOT_CLAIMED")

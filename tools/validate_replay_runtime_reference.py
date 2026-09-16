from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs/MACHINE_REPLAY_CONTRACT_01.json"


class ReferenceReplayRuntime:
    """Deterministic reference model for the frozen replay reset/import contract.

    QA evidence only; not the production Decision Engine.
    """

    def __init__(self, contracts):
        self.contracts = {row["canonical_meta_key"]: row for row in contracts}
        self.run_state = set()
        self.pending_delays = set()
        self.terminal_state = None
        self.imported_meta = set()

    def complete_run(self, terminal: str) -> dict[str, object]:
        self.terminal_state = terminal
        return {"meta": set(self.run_state), "terminal": terminal}

    def new_run_from_prior(self, export: dict[str, object]) -> None:
        self.run_state = set()
        self.pending_delays = set()
        self.terminal_state = None
        self.imported_meta = set(export.get("meta", set())) & set(self.contracts)

    def import_meta(self, key: str) -> bool:
        if key not in self.contracts or key in self.imported_meta:
            return False
        self.imported_meta.add(key)
        return True


contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
rows = contract["contracts"]
errors: list[str] = []

if {r["event_id"] for r in rows} != {"E186", "E247", "E248"}:
    errors.append("unexpected replay event scope")
if len({r["canonical_meta_key"] for r in rows}) != 3:
    errors.append("replay meta keys are not unique")
if any(r.get("exactly_once_import") is not True for r in rows):
    errors.append("not every replay meta route is exactly-once")

rt = ReferenceReplayRuntime(rows)
rt.run_state.update({"open_petition_hall", "ordinary_run_flag"})
rt.pending_delays.add("delay.prior.run")
export = rt.complete_run("Steward")

rt.new_run_from_prior(export)
if rt.run_state or rt.pending_delays or rt.terminal_state is not None:
    errors.append("fresh run inherited run-specific state, pending delays, or terminal state")
if rt.imported_meta:
    errors.append("ordinary run state was incorrectly promoted to replay metadata")

# Exactly-once import for every canonical key.
for key in sorted(rt.contracts):
    if not rt.import_meta(key):
        errors.append(f"first import rejected for {key}")
    if rt.import_meta(key):
        errors.append(f"duplicate import accepted for {key}")

# A terminal identity is never an active-run producer.
no_prior = ReferenceReplayRuntime(rows)
no_prior.new_run_from_prior({"meta": set(), "terminal": "Steward"})
if no_prior.imported_meta:
    errors.append("terminal state was promoted into active replay state")
if rt.terminal_state is not None:
    errors.append("terminal state crossed replay reset boundary")

if errors:
    print("REPLAY_RUNTIME_REFERENCE: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("REPLAY_RUNTIME_REFERENCE: PASS")
print("events=3")
print("meta_keys=3")
print("exactly_once_import=true")
print("run_state_reset=true")
print("pending_delay_reset=true")
print("terminal_state_reset=true")
print("production_runtime=NOT_CLAIMED")

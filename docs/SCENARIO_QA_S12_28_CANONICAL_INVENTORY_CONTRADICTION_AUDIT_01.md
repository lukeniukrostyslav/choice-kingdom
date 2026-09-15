# Choice Kingdom — S12.28 Canonical Inventory Contradiction Audit

Date: 2026-09-15
Status: **AUDIT — STALE RECORDS IDENTIFIED, NO UNSUPPORTED CLOSURE**
Frozen production scope: E01–E272

## Finding

The current `docs/CANONICAL_PRODUCER_INVENTORY_01.md` is stale relative to the later S12 source reconciliations.

Two concrete discrepancies are confirmed:

1. `pred.budget_reform` is marked `OPEN` in the inventory even though S12.25 re-read authoritative E142-A/E154-A/E198-A and closed the source set.
2. E245 is represented only as E125-A + E156-A candidates in the inventory, while S12.24 records an earlier delayed-graph audit candidate E20-A `soldier_compensation`. The correct current state is therefore **OPEN pending authoritative reconciliation**, not a closed two-source union.

## Correct canonical status

### Budget reform
Source set:

`E142-A → auditor_independence`

`E154-A → crown_audited`

`E198-A → legislative_budget_lock`

Negative blockers:

`E142-B`, `E154-B`, `E198-B`

Source identity: **CLOSED**.

Runtime lifecycle, invalidation and reachability: **OPEN**.

### E245
Known authored compensation candidates:

- E20-A `soldier_compensation` — earlier delayed-graph candidate requiring source re-read;
- E125-A `border_compensation` — source-closed;
- E156-A `requisition_compensation` — source-closed.

Current machine rule: **do not union these candidates without an explicit authored family/composite rule**.

## Why this matters

The producer inventory is intended to be the machine-facing working record. Leaving stale `OPEN`/candidate classifications there while newer QA artifacts have more authoritative source findings creates a dangerous false graph if implementation begins from the inventory.

Therefore production-schema promotion remains blocked until the inventory is reconciled against the latest authoritative QA artifacts.

## Acceptance

PASS — contradiction identified.
PASS — no unsupported E245 closure introduced.
PASS — budget source closure preserved.
BLOCKED — canonical producer inventory rewrite required before machine graph generation.

# Choice Kingdom — Scenario QA S12.40 — Canonical Graph Drift Audit 01

Date: 2026-09-15
Status: QA AUDIT — DRIFT IDENTIFIED / CORRECTION REQUIRED
Frozen scope: E01–E272

## Finding

The authoritative `CANONICAL_PRODUCER_INVENTORY_01.md` now records `soldier_compensation` as source-closed at E20-A and explicitly maps it to delayed consumer E245. The machine graph `MACHINE_CANONICAL_GRAPH_01.json` still contains an older E245 candidate set (`E20-A`, `E125-A`, `E156-A`) and marks the consumer OPEN.

This is machine-source drift, not a new narrative gap.

## Required correction

1. Add `soldier_compensation` / E20-A to the machine graph source-closed producer registry.
2. Normalize E245 to canonical producer E20-A.
3. Remove E125-A and E156-A from E245's producer set; they remain distinct compensation producers and must not be unioned without authored evidence.
4. Mark E245 source identity CLOSED while retaining any separate runtime timing/cancellation lifecycle questions.
5. Re-run canonical graph validation and producer/consumer compilation after the correction.

## Safety rule

The stale machine graph must not be treated as authoritative over the newer producer inventory. No Decision Engine contract should consume the stale E245 union.

## Gate

S12.40 identifies a concrete machine-data consistency defect and defines a deterministic correction. This is a source-of-truth synchronization issue, not permission to raise runtime readiness.

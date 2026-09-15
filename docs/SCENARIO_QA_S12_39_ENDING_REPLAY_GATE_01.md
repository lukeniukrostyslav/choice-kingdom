# Choice Kingdom — Scenario QA S12.39 — Ending / Replay Gate 01

Date: 2026-09-15  
Status: SOURCE-LEVEL QA — RECONCILED / RUNTIME BLOCKED  
Frozen production scope: E01–E272

## Objective

Reconcile the ending producer gap register with the replay meta source closure and define the exact blockers that prevent deterministic ending resolution and replay transfer.

## Ending families

| Ending | Current producer state | Blocking contract |
|---|---|---|
| Steward | PARTIAL | institutional thread, emergency-power restraint, terminal blockers |
| Iron Crown | PARTIAL | machine qualification + negative constitutional blockers |
| Golden Compact | PARTIAL | guild influence + economic stability + commercial producer set |
| People's Charter | PARTIAL | civic participation + blocker closure |
| Broken Diadem | OPEN | failure predicate + two independent authored failure paths |
| Quiet Throne | OPEN | explicit withdrawal producer + precedence |
| Second Founder | PARTIAL | systemic convergence + coalition + constitutional prerequisite + replay metadata |

## Replay boundary

- E186 ordinary `warehouse_arson` remains distinct from previous-run informational unlock.
- E247 has no source-closed `meta.*` producer/key.
- E248 has no source-closed `meta.*` producer/key.
- E270 produces ordinary `dual_witness_account`; it is not promoted to replay metadata.

## Deterministic resolver requirements

1. Ending prerequisites must have canonical incoming producers.
2. Positive endings require explicit precedence data where conflicts are possible.
3. Failure endings require deterministic terminal predicates, not score shortcuts.
4. Quiet Throne requires explicit authored withdrawal evidence.
5. Replay metadata must be isolated from current-run state.
6. No ending may manufacture its own prerequisite.

## Gate

The reconciliation confirms that ending and replay gaps are independent but intersect at Second Founder and precedence. Runtime ending resolver and replay-transfer runtime remain blocked. No completion percentage is increased solely from this reconciliation artifact.

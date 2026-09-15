# Choice Kingdom — Scenario QA Worklog

Frozen scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**  
Purpose: durable handoff ledger so completed QA work is not repeated.

## Working rule
Every substantive scenario-QA batch must leave a durable GitHub commit and update this ledger. A later session must read this file and `PROJECT_STATE.md` before repeating any gate.

## Completed batches

### Batch 01 — Reporting contract
- Scenario QA reporting metric frozen at 65%.
- E01–E272 frozen denominator.
- Engine/UI/Android/APK explicitly excluded from this phase.

### Batch 02 — Static closure reconciliation
- Added `docs/SCENARIO_QA_PASS_02_STATIC_CLOSURE.md`.
- Reconciled transport lifecycle wording: E32 establishes `pred.transport_disruption(active)`; E136-A/B clear it.
- Preserved unresolved runtime lifecycle semantics instead of inventing producers.
- Reconfirmed delayed callback closure matrix.
- Reconfirmed replay boundary and hard-negative predicate rules.
- Reconfirmed seven ending families and remaining incoming-path/precedence gap.

## Active gates — NOT YET CLOSED

1. Exhaustive concrete output-token inventory E01–E272.
2. Exhaustive trigger-token inventory E01–E272.
3. Duplicate semantic writer detection.
4. Contradictory writer detection.
5. Undefined producer/consumer detection.
6. Predicate dependency-cycle detection.
7. Exact delayed callback identity + cancellation/supersession matrix.
8. Exhaustive ending incoming paths + deterministic precedence.
9. Exact replay `meta.*` producer/key closure.
10. Fresh-run causal reachability simulation.
11. Representative replay reachability simulation.
12. Graph-vs-catalog edge reconciliation.

## Source-of-truth rule

Authoritative event catalogs are the narrative source. `EVENT_GRAPH.md` is a reconciliation target, not an independent producer. E273–E277 must not satisfy E01–E272 consumers until formally admitted.

## Anti-duplication rule

Before starting a QA batch:
1. read this worklog;
2. read `PROJECT_STATE.md`;
3. inspect the latest commits listed there;
4. only work on gates still listed as active;
5. after completing a substantive batch, update this file and commit it.

## Current status

Scenario QA remains **65%** until the active gates above are actually checked and closed. Do not increase the percentage for documentation-only progress.

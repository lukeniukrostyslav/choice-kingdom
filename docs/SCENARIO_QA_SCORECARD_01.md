# Choice Kingdom — Scenario QA Scorecard 01

Date: 2026-09-16  
Frozen authored scope: **E01–E272**  
Status: **SCENARIO QA REPORTING CONTRACT — SOURCE LEVEL**

Percentages increase only on verified source changes and green relevant gates. This scorecard does not claim runtime gameplay, APK readiness, Android UI, or engine readiness.

## Current 12-block scorecard

| Scenario block | Completion | Current gate |
|---|---:|---|
| S01 — Canonical Event Coverage | 84% | ADVANCED — E01–E272 exhaustive authored-event scope is structurally validated; semantic/reachability closure remains |
| S02 — Choice / State Transitions | 70% | OPEN — complete authored transition/effect closure remains |
| S03 — Producer / Consumer Closure | 100% | SOURCE-CLOSED — exhaustive inventory reports zero undefined consumers after frozen source contracts and canonical trigger normalization |
| S04 — Predicate Contracts | **100%** | **SOURCE-CLOSED — all production predicates have an in-scope authored/deterministic source contract or an explicit frozen-scope exclusion; the two formerly open names are formally excluded and machine-gated; E275-B/E276-B remain expansion-only** |
| S05 — Delayed Consequences | 60% | OPEN — complete consequence and cancellation closure remains |
| S06 — Replay / Meta State | 65% | ADVANCED — explicit replay meta-state bindings for E186/E247/E248 are frozen and pass the dedicated machine gate; runtime replay execution remains open |
| S07 — Event Graph / Causality | **100%** | **SOURCE-CLOSED — every explicit E01–E272 causal edge is rooted in a structural causal component; every event is classified; scope leakage and self-loops are machine-gated; feedback components are reported without being misclassified as runtime loops** |
| S08 — Source / Producer QA | 100% | CLOSED — canonical delayed producer identities are semantically reconciled with the source inventory; collision and dedicated source-producer equality gates are green |
| S09 — Canonical Graph | 100% | SOURCE-CLOSED — E01–E272 catalog/graph node parity, scope integrity, canonical edge inventory and explicit design-vs-runtime semantic boundary are machine-gated; runtime gameplay reachability remains downstream |
| S10 — Delayed Lifecycle | 83% | ADVANCED — delayed lifecycle gate is green; exact cancellation/supersession/save-load semantics remain |
| S11 — Replay / Ending QA | 72% | OPEN — deterministic ending precedence and replay reachability remain |
| S12 — Scope / Integrity Gates | 100% | CLOSED — E01–E272 scope, exclusions, contract readiness, source inventory and integrity gates are green |

## Aggregate scenario score

**86.17% — scenario QA / verification progress.**  
Exact arithmetic mean: **86.1667%**, displayed as **86.17%**.

The aggregate increased from 84.75% because S07 was formally closed at source level; no runtime readiness is implied.

## Verified autonomous work — latest blocks

### S40 — S07 causal reachability source closure
- Added `tools/validate_causal_reachability_contract.py` as a dedicated S07 machine gate.
- Validates the frozen E01–E272 scope and rejects excluded/out-of-scope event leakage from explicit causal chains.
- Requires every event to be either part of an explicit causal edge or explicitly classified in the graph's coverage inventory.
- Proves every event participating in a causal edge is reachable from a structural causal root.
- Rejects self-loops.
- Detects directed feedback components and reports them separately; feedback is not treated as proof of a runtime gameplay loop.
- Explicitly preserves the boundary between source-level causal reachability and conditional gameplay/runtime reachability.
- Wired the gate into `.github/workflows/canonical-graph.yml` and uploads `MACHINE_CAUSAL_REACHABILITY_01.json` with the canonical QA artifacts.
- S07 is therefore closed at **source level** without inventing prerequisites or runtime semantics.
- Commits: `0954e25717e9bc95cc03ee2f9e9b757070150a1b`, `5e36bb5c7f5d674eab41abb7df05f5faa7c6d339`, `bf3f8b2765d747438e0650b7659f3915f56950d9`.

### S39 — S04 predicate production boundary closure
- Formally closed the two previously open predicate names without inventing scenario semantics.
- `pred.guild_labor_tension` is now explicitly **EXCLUDED / NOT-A-PRODUCTION-PREDICATE**; E275-B remains expansion-only.
- `pred.information_pressure_high` is now explicitly **EXCLUDED / NOT-A-PRODUCTION-PREDICATE**; E276-B remains expansion-only.
- Added a hard production-boundary rule: formally excluded predicates cannot become production inputs, consumer triggers, derived state, or reachability conditions.
- Hardened `tools/validate_predicate_open_boundary.py` so it checks the actual `source_closed_producers` and `derived_source_contracts` inventories rather than treating mere contract documentation as production leakage.
- S04 is therefore closed by **formal semantic exclusion**, not by inventing E01–E272 producers.
- Commits: `7247474f5302e094dead0b931ceb2f74bc3920d4`, `cc11b4a88d5b1136333823d9471529138c91e5e5`.

### S38 — producer/consumer registry reconciliation
- Reconciled `docs/CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md` with the current canonical predicate contract and machine graph.
- Corrected stale source-level rows for market pressure, winter severity, food stability, transport disruption, border crisis, guild logistics cooperation, guild influence, systemic explanation, coalition cooperation, constitutional preparation, budget reform and final-charter prerequisites.
- Explicitly quarantined `pred.guild_labor_tension` and `pred.information_pressure_high` from frozen production semantics rather than inventing E01–E272 producers.
- Commit: `26699823a6babec40d0ea2d7580d67eb05b6aba5`.

### S37 — predicate producer open-boundary enforcement
- Added `tools/validate_predicate_open_boundary.py` and its CI integration.
- The gate originally proved that the two unresolved names could not leak from E275/E276 into frozen production semantics.
- This boundary was subsequently upgraded by S39 into formal exclusion, allowing S04 source-level closure without fabricating authored producers.
- Commits: `451440af0ea68b0528a0d0721e9c4a1c4aaac2a0`, `be435cd244f212009f5ef836003077cb95e85627`.

### S36 — canonical graph source-closure
- Added `tools/validate_canonical_graph_closure.py` as a dedicated S09 closure gate.
- Proves the frozen source-level graph contract: E01–E272 node coverage, scope integrity, exclusion quarantine and design-vs-runtime semantic boundary.
- Commits: `67f80194f7d5aa623ce42d7b4e6c3c73831a91d9`, `c1f4410b45a5377028d9e60856e5368ace5e9214`.

### S35 — source producer semantic equality closure
- Reconciled E184 explicitly and exclusively to E25-B → `secret_evidence_route`.
- Added source-producer semantic equality validation and CI coverage.
- Commit chain includes `5ec089fa2a6dc07c3597154791003d47f853c43a`, `4f7b389ff40b4e18513330a0eead60749750ebce`, `ba5d623f9845095aed230d6d13fd657e9e56fe9d`, `4da5da1fb441789ab9ae7245e977bfcc3d024bc9`, `48fd61bb6b86ea9a581d6bbb9d27afb26ebab73d`.

## Remaining gates to 100%

1. Complete authored choice/effect transition closure (S02).
2. Complete delayed consequence cancellation/supersession, persistence and exactly-once semantics (S05/S10).
3. Prove replay execution/reset semantics beyond the frozen source contract (S06).
4. Complete exact ending positive prerequisites, negative blockers and deterministic precedence (S11).
5. Prove fresh-run and replay **gameplay** reachability beyond the source-level S07 causal graph contract (S01/S11 and runtime implementation).
6. Freeze the production schema and prove final runtime graph/catalog semantic execution against the engine; this is downstream of source-level S04/S07/S09 closure.

## Scope / exclusions

E01–E272 are the production denominator. E273–E277 are expansion candidates and cannot contribute producers, consumers, predicates, delayed sources or reachability edges.

### S04 closure rule

A predicate contract reaches source-level CLOSED status when every production predicate has either:
1. an authoritative E01–E272 producer, or
2. a deterministic in-scope derived contract, or
3. an explicit frozen-scope exclusion enforced by machine QA.

The third case is now used only for the two names that had no authored production source. This does not create runtime semantics for them.

**S04 — SOURCE-LEVEL CLOSED: 100%.**

### S07 closure rule

S07 reaches source-level CLOSED status when:
1. every explicit causal edge is within E01–E272;
2. no explicit causal edge contains a self-loop;
3. every E01–E272 event is either present in an explicit causal edge or explicitly classified by the graph's coverage inventory;
4. every event participating in an explicit causal edge is reachable from a structural causal root;
5. feedback components, if present, are reported separately and are not interpreted as runtime gameplay loops.

This is a **source-level causal graph closure**, not a claim that every conditional branch is playable from a fresh run. Runtime gameplay reachability, replay reachability, timing/state feasibility and ending precedence remain downstream gates.

**S07 — SOURCE-LEVEL CLOSED: 100%.**

Historical scorecard states remain available through Git history; this file records the current reporting contract.

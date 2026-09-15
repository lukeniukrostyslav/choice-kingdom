# Choice Kingdom — Scenario QA Producer→Graph Reconciliation Audit 01

Status: **SOURCE-LEVEL QA — RECONCILIATION GATE**  
Scope: E01–E272 production semantics only.  
Date: 2026-09-15.

## Purpose

Reconcile facts whose source-level producer identity is already closed with the separate causal-graph representation. This audit deliberately does **not** promote a producer→consumer relationship merely because both records exist. A source producer proves origin; a graph edge proves only a design-level causal candidate; executable reachability still requires a satisfiable trigger, timing/lifecycle contract and fresh-run/replay verification.

## 1. Closed producer identities that require graph reconciliation

| Canonical fact / delayed source | Producer | Consumer / use | Source status | Graph status | Promotion |
|---|---|---|---|---|---|
| `public_bridge` | E18-B | E243 | CLOSED | candidate route visible through E126/E129 family | HOLD until exact edge semantics are reconciled |
| `flexible_accounts` | E09-B | E244 | CLOSED | candidate institutional route | HOLD until exact edge semantics are reconciled |
| `veteran_patronage` | E117-B | E182/E222/E245 family | CLOSED | graph has E117→E182/E222/E245 | edge existence is not scheduler proof |
| `estate_exception` | E118-B | E183/E242 | CLOSED / PARTIAL for broad E242 wording | graph has E118→E183/E242 | E242 remains partial because authored consumer says any prior noble exception |
| `cheap_weapons` | E17-A | E185 | CLOSED at source identity | graph has E128→E185 | later military-crisis lifecycle remains open |
| `winter_rent_ceiling` | E160-A | E246 | CLOSED at source identity | graph candidate is visible in constitutional/crisis layer | timing and lifecycle remain open |
| `soldier_compensation` | E20-A | E245 | CLOSED | graph consumer route must be treated as source-backed only after exact choice identity is preserved | no union with E125/E156 |

## 2. Hard reconciliation rules

1. A producer record does not automatically create a graph edge.
2. A graph edge does not prove gameplay reachability.
3. A delayed consumer cannot infer its producer from thematic similarity.
4. E245 must retain E20-A as its canonical source identity; E125-A and E156-A are distinct compensation routes and must not be merged without an explicit authored rule.
5. E242 cannot be normalized to E118-B as a universal alias while its authored wording remains “any prior noble exception”.
6. Relative timing such as `5+ turns` or `6+ turns` remains non-executable until the scheduler anchor and exactly-once identity are authored/verified.
7. Replay state cannot be introduced into a fresh-run graph through ordinary history markers.
8. E33/E34 remain quarantined and cannot be used to repair missing graph edges.

## 3. Required closure record for every delayed edge

Before promotion into production semantics, each delayed relation must have:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule + graph edge + reachability evidence`

The current source work closes only some source identities. It does not yet close the complete tuple.

## 4. Scenario-specific reconciliation targets

### E181 / E45-B

The authored catalog identifies a toll-concession delay. E45-B is the source-identified producer. The remaining work is to bind the relative delay to a deterministic scheduler anchor and prove the resolution path is satisfiable without silently treating the graph edge as execution proof.

### E182 / E117-B

Producer identity is closed. The remaining scenario work is lifecycle qualification and ensuring the delayed callback resolves exactly once under save/load and competing state changes.

### E183 / E118-B

Producer identity is closed. The remaining work is the same lifecycle closure; no broader noble-exception alias should be invented.

### E185 / E17-A

The source producer is closed, but the authored semantics include a separate later military crisis. Therefore the producer→consumer relation is not complete until the crisis resolution, cancellation/supersession and exactly-once semantics are explicit.

### E243 / E18-B

The graph/source vocabulary differs (`public bridge investment` vs `public_bridge`). Normalize vocabulary without changing authored meaning. The `5+ turns later` delay remains a runtime contract blocker.

### E244 / E09-B

The source identity is closed. The remaining work is exact delay scheduling, resolution target and lifecycle persistence.

### E245 / E20-A

The source audit explicitly identifies E20-A as the canonical compensation route for the Soldier's Son callback. E125-A and E156-A remain separate facts. Any graph simplification that merges them would be a semantic regression.

### E246 / E160-A

The source identity is closed. Relative timing, exactly-once behavior, invalidation and graph-to-runtime reachability remain open.

## 5. Current conclusion

The producer inventory and event graph are **compatible but not yet semantically equivalent**. The correct next step is not to invent edges or close all delayed callbacks mechanically. The next scenario gate is to reconcile each closed producer with its exact consumer contract and then run satisfiability/reachability analysis over the resulting candidate graph.

No Decision Engine promotion is authorized by this audit.

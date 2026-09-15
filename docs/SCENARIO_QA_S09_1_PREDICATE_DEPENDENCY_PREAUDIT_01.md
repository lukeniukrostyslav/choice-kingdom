# Choice Kingdom — S09.1 Predicate Dependency Pre-Audit 01

Date: 2026-09-15  
Scope: frozen production **E01–E272 only**  
Status: **SOURCE-LEVEL QA — PREDICATE DEPENDENCY PRE-AUDIT**

## Purpose

Start the S09 predicate dependency gate using only source-closed facts already admitted by the canonical producer/consumer registry and chronology pre-audit. This document does not promote design-level graph edges into runtime truth.

## Dependency rules

1. A predicate may consume only source-backed facts or independently qualified predicates.
2. A consumer cannot manufacture the predicate it consumes.
3. A recovery/clear fact is not equivalent to the active predicate it clears.
4. Historical evidence is not automatically an active predicate.
5. Independent-domain qualification must not count aliases of the same domain twice.
6. E273–E277 are rejected from every production dependency edge.
7. Any cycle requires an authored upstream seed or is rejected as self-satisfaction.

## Current dependency dispositions

| Predicate | Upstream dependency shape | Status |
|---|---|---|
| `pred.gold_low` | `resource.gold` threshold | PROVISIONAL; threshold verification open |
| `pred.security_high` | `resource.security` threshold | OPEN; threshold not frozen |
| `pred.food_stable` | exact durable food-stability producer | **BLOCKED**; no in-scope producer verified |
| `pred.transport_disruption` | E32 active marker; E136-A/B clear/recovery | PARTIAL; lifecycle semantics open |
| `pred.border_crisis` | E271-A declaration; E272-A/B resolution | SOURCE LIFECYCLE CLOSED / RUNTIME OPEN |
| `pred.guild_logistics_cooperation` | E136-B cooperation + E194-A inspection | SOURCE CHAIN CLOSED / RUNTIME OPEN |
| `pred.guild_influence_strong` | independent institutional guild domains | PARTIAL; exact producer chronology open |
| `pred.systemic_explanation_verified` | three evidence domains + convergence decision | CONTRACT FROZEN / PRODUCERS OPEN |
| `pred.coalition_cooperation` | cross-faction package + distinct positive faction evidence | CONTRACT FROZEN / PRODUCERS OPEN |
| `pred.constitutional_prepared_strong` | three independent preparation domains | PARTIAL; chronology/independence open |
| `pred.budget_reform` | auditor independence + crown audit + legislative budget lock | OPEN; chronology/reachability open |
| `pred.final_charter_prerequisites` | multiple independent endgame domains + no mandatory blocker | CONTRACT FROZEN / PRODUCERS OPEN |
| `pred.faction_routes_4` | four distinct route identities | OPEN |

## Cycle/self-satisfaction checks

No source-closed evidence currently justifies accepting any of the following patterns:

- `E209 -> pred.final_charter_prerequisites -> E209`;
- `E200 -> pred.guild_influence_strong -> E200`;
- `E197 -> pred.constitutional_prepared_strong -> E197`;
- `E207 -> pred.systemic_explanation_verified -> E207`;
- `thread.coalition -> pred.coalition_cooperation -> thread.coalition`;
- recovery marker -> active predicate without an independent reactivation producer.

These are hard-rejected as self-satisfaction unless an earlier authored producer is explicitly proven.

## Event-graph reconciliation observations

`EVENT_GRAPH.md` is explicitly design-level and states that its edges are not verified runtime edges. Therefore an edge such as `E200 -> E261` does not itself prove `pred.guild_influence_strong`, and `E209 -> ending qualification` does not prove that E209 produced its own prerequisites. The canonical registry remains authoritative for source-level producer qualification.

## Hard negatives

- `rel.ivo` cannot alone produce `pred.guild_influence_strong`.
- `thread.coalition` cannot alone produce `pred.coalition_cooperation`.
- `pred.faction_routes_4` cannot be reused as coalition evidence.
- `resource.security` cannot substitute for `pred.border_crisis`.
- `food_logistics_stabilized` cannot silently become `pred.food_stable`.
- E273-A cannot produce `pred.food_stable`.
- E277 cannot produce transport recovery.

## Gate result

**S09.1: PARTIAL PASS.**

The dependency boundaries and self-satisfaction negatives are explicit, but exhaustive token-level dependency extraction and machine cycle detection are still required before S09 can close.

## Next machine-checkable batch

1. Enumerate every predicate token consumed by E01–E272.
2. Map each token to its earliest admitted producer.
3. Detect cycles and same-event self-satisfaction.
4. Detect duplicate semantic aliases that could double-count one domain.
5. Reconcile predicate dependencies with delayed callback eligibility and replay boundaries.
6. Build the S11 ending prerequisite matrix only after the S09 dependency inventory is sufficiently complete.

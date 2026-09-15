# Choice Kingdom — Scenario QA S09.4 Predicate Cycle / Self-Satisfaction Audit 01

Date: 2026-09-15
Status: **PARTIAL PASS — SOURCE-LEVEL QA**
Frozen production scope: **E01–E272**
Expansion candidates: **E273–E277 excluded**

## Purpose

Audit the current canonical derived-predicate contract against the canonical producer/consumer registry for direct self-satisfaction, downstream-to-upstream leakage, and obvious predicate dependency cycles. This is a source-level QA artifact; it is not engine validation.

## Rules applied

1. A consumer cannot create a predicate it consumes.
2. A downstream outcome cannot become an upstream prerequisite for the same event.
3. A convergence event cannot manufacture missing prerequisites.
4. Relationship scores and route cardinality cannot substitute for independently authored institutional predicates.
5. E273–E277 cannot contribute production dependency edges.
6. Historical evidence and current predicates remain distinct unless a lifecycle rule explicitly connects them.

## Audited composite predicates

### `pred.guild_influence_strong`

Status: **PARTIAL PASS**.

Allowed independent domains are frozen as representation, tribunal, commercial/market-credit, and qualified logistics cooperation. `rel.ivo` is explicitly rejected as a standalone producer. E200 consumes the predicate and therefore cannot be used as its producer.

No direct E200 self-satisfaction edge is admitted.

### `pred.constitutional_prepared_strong`

Status: **PARTIAL PASS**.

The frozen upstream domains are civic, institutional/audit, factional/house, and military/law. E197 consumes the predicate. The contract explicitly forbids E197–E210 outcomes from retroactively satisfying it.

No direct E197 self-satisfaction edge is admitted.

### `pred.systemic_explanation_verified`

Status: **PARTIAL PASS**.

The predicate requires three distinct evidence domains plus an explicit convergence decision. E207 is a consumer and cannot itself create the evidence predicate.

No direct E207 self-satisfaction edge is admitted by the frozen contract.

### `pred.coalition_cooperation`

Status: **PARTIAL PASS**.

Qualification requires an explicit positive cooperation package and participant identity. `thread.coalition` and route-count alone are insufficient. E207/E201/E261 are consumers/candidate downstream users and cannot manufacture cooperation retroactively.

No direct consumer self-satisfaction edge is admitted.

### `pred.final_charter_prerequisites`

Status: **BLOCKED — SELF-SATISFACTION RISK REQUIRES SOURCE ENUMERATION**.

The contract says E209 consumes already-established prerequisites and must not manufacture them. However, the producer/consumer registry currently lists `E197/E198/E199/E202–E209 candidates` as possible producers for this predicate. The inclusive `E209` reference is therefore unsafe until the concrete source inventory proves that E209 is excluded from the predicate's upstream producer set.

Required disposition: **E209 must be consumer-only for `pred.final_charter_prerequisites`; no E209 outcome may be an upstream producer of that predicate.**

### `pred.budget_reform`

Status: **OPEN**.

The registry identifies E142/E154/E198 as candidate institutional layers. E198 appears in the consumer/proposer surface and therefore requires exact source-role separation before closure. The current audit does not promote E198 as a producer without the explicit source closure proof.

### `pred.food_stable`

Status: **BLOCKED / SAFE AGAINST E273 CONTAMINATION**.

No E01–E272 producer is verified. E273-A is excluded. The predicate cannot be manufactured by E192 merely because E192 produces `food_logistics_stabilized`; that source must be explicitly promoted only if the authoritative production contract confirms the intended lifecycle semantics.

### `pred.transport_disruption`

Status: **PARTIAL PASS**.

E32 is the active source. E136-A/B are clear/recovery semantics and cannot be treated as active producers. E277 is excluded. No later in-scope reactivation producer is currently source-closed.

## Hard negatives confirmed

- E273–E277 cannot enter production dependency graphs.
- `rel.ivo` cannot satisfy guild influence by itself.
- `thread.coalition` cannot satisfy coalition cooperation by itself.
- A recovery/clear marker cannot silently become an active predicate.
- A consumer cannot manufacture its prerequisite.
- E210 is convergence-only and cannot create missing prerequisites.
- E209 cannot create `pred.final_charter_prerequisites` while consuming it.

## Gate result

**S09.4 PARTIAL PASS.**

One concrete registry-level self-satisfaction risk was isolated: the generic `E197/E198/E199/E202–E209 candidates` wording for `pred.final_charter_prerequisites` must be refined so E209 is unambiguously excluded as an upstream producer.

This finding does not justify increasing the S09 percentage yet. Full token-level dependency extraction, complete event-by-event producer enumeration, and machine cycle detection remain open.

## Next required work

1. Enumerate every concrete producer token for each composite predicate.
2. Remove ambiguous inclusive ranges and consumer IDs from producer sets.
3. Build a normalized dependency edge list from only source-backed producers.
4. Run cycle detection and transitive self-satisfaction checks.
5. Reconcile the resulting edge list against delayed callback identities and the event graph.

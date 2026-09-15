# Choice Kingdom — Scenario QA S09.6 Composite Predicate Producer Enumeration 01

Date: 2026-09-15  
Status: **PARTIAL PASS — SOURCE-LEVEL QA**  
Frozen production scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**

## Purpose

Enumerate the currently source-supported producer surfaces for composite predicates and remove ambiguous consumer-as-producer references before any production schema or engine implementation.

## 1. `pred.guild_influence_strong`

Required qualification surface:

- representation: `history.guild_representation` / `guild_political_representation`; E49/E144 are one institutional domain;
- tribunal: independently authored guild-tribunal evidence;
- commercial/market governance: `official_credit_disclosure` / `audited_monopoly` as one commercial domain;
- qualified logistics: `history.guild_logistics_cooperation` followed by E194-A neutral-inspection qualification and no unresolved immunity-risk blocker.

`rel.ivo`, raw event count and E49+E144 double counting are rejected.

Disposition: **PARTIAL**. Domain identities are frozen, but the exact minimum-domain formula and exhaustive producer IDs remain open.

## 2. `pred.constitutional_prepared_strong`

Source domains:

- civic/commons: `people_charter_endorsed`;
- institutional/audit: `crown_audited` / `full_crown_audit_published`;
- factional/house: `house_assembly`;
- military/law: `military_red_line` / authored military constitutional route.

E197 is consumer-only for this predicate. Its downstream outcome cannot satisfy its own prerequisite.

Disposition: **PARTIAL**. Three independent domains are required by the current contract, but exact source IDs, ordering and negative-branch semantics remain open.

## 3. `pred.systemic_explanation_verified`

Required independent evidence families:

1. warehouse/financial;
2. document/language;
3. witness/organizational;
4. explicit convergence decision.

E207 is convergence/consumer surface and cannot manufacture missing evidence families.

Disposition: **PARTIAL**. Evidence-family shape is closed; immutable authored evidence IDs remain to be compiled.

## 4. `pred.coalition_cooperation`

Required:

- explicit participant/faction identities;
- positive cooperation outcome;
- no unresolved coalition-collapse blocker;
- deterministic invalidation/supersession.

`history.cross_faction_package` is evidence, not an automatic perpetual predicate. `thread.coalition`, route cardinality and `four_way_bargain` are insufficient alone.

Disposition: **PARTIAL**.

## 5. `pred.budget_reform`

Candidate institutional layers:

- E142-A `auditor_independence`;
- E154-A `crown_audited`;
- E198-A `legislative_budget_lock`.

E198 must not be promoted from consumer/proposer surface without exact source-role verification.

Disposition: **OPEN**.

## 6. `pred.final_charter_prerequisites`

The predicate is a convergence of already-established civic, institutional/audit, faction/house/guild, military/security, information/evidence, coalition and crisis-resolution facts.

**E209 is explicitly consumer-only.** No E209 outcome is an upstream producer for `pred.final_charter_prerequisites`.

E210 is convergence-only and cannot manufacture missing prerequisites.

Disposition: **BLOCKED pending exhaustive source enumeration**.

## 7. `pred.food_stable`

No E01–E272 producer is currently verified. E192 `food_logistics_stabilized` is not silently aliased to kingdom-wide `pred.food_stable`; E273-A remains excluded.

Disposition: **BLOCKED**.

## 8. `pred.transport_disruption`

E32 is the explicit active producer. E136-A/B are clear/recovery sources. E277 is excluded. No later in-scope reactivation producer is currently source-closed.

Disposition: **PARTIAL** pending current-cycle persistence, ordering, expiry and reactivation semantics.

## Dependency hard negatives

- no consumer may manufacture its prerequisite;
- no downstream outcome may become an upstream prerequisite;
- no recovery marker may become an active predicate without explicit reactivation;
- no relationship score may substitute for an authored institutional predicate;
- no expansion event E273–E277 may enter production dependency edges;
- no historical evidence becomes current state without an authored lifecycle rule.

## Gate result

**S09.6 PARTIAL PASS.**

The composite predicate surface is now enumerated at contract level and the known E209 self-satisfaction ambiguity is explicitly removed. Full token-level extraction and machine cycle detection remain open.

## Next

1. Extract exact producer tokens from authoritative E01–E272 catalogs.
2. Normalize producer → predicate → consumer edges.
3. Run transitive cycle detection.
4. Reconcile delayed callback source/target identities against the same producer chronology.
5. Promote only evidence-backed rows to CLOSED.

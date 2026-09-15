# Choice Kingdom — S08.9 Source Reconciliation 01

Date: 2026-09-15  
Scope: frozen production E01–E272 only  
Status: **SOURCE-LEVEL QA — RECONCILIATION PASS**

## Purpose
Reconcile the S08.8 unresolved food/transport families against the authoritative late-predicate audit and prevent false closure from downstream consumers.

## 1. Food stability

Authoritative late audit confirms:
- E167/E218 handle import/grain responses but do not provide a safe kingdom-wide `pred.food_stable` producer.
- E192-A/B produce `food_logistics_unstable` / `food_logistics_stabilized`, not a generic kingdom-wide stability fact.
- E225/E251/E254 consume food-pressure context and therefore cannot manufacture the missing prerequisite.
- E273-A remains outside frozen scope.

Decision: **OPEN**.

Required before schema freeze: an exact E01–E272 choice-level durable producer or an explicit authored catalog edit. The engine must not invent a sixth resource or silently promote `food_logistics_stabilized` into `pred.food_stable`.

## 2. Transport disruption

Authoritative source reconciliation confirms:
- E32 is the established active disruption producer.
- E136-A/B clear the active disruption and establish `transport_network_stable` recovery evidence.
- E167/E170/E192/E251 are consumers/context nodes and do not safely provide a later active disruption producer.
- E192 cannot self-produce the predicate it consumes.
- E277 is excluded from production.

Decision: **PARTIAL — active lifecycle producer is E32; recovery/clear is E136-A/B; later reactivation producer is not yet source-closed.**

Required before schema freeze: determine whether the authored campaign intentionally permits reactivation and, if so, identify the exact E01–E272 choice. If no such source exists, the production contract must explicitly model one-shot lifecycle semantics rather than inventing a producer.

## 3. Guild influence

E165 credit/debt, E168 independent tribunal, E166 market/merchant domain and E194 qualified logistics cooperation remain candidate institutional domains. The frozen contract requires distinct domains and rejects `rel.ivo` as sufficient evidence.

Decision: **PARTIAL**. Exact source IDs and chronological availability still require exhaustive producer mapping.

## 4. Constitutional preparation

E154/E155 audit legitimacy, E161 house assembly and E227 military-red-line evidence remain candidate independent domains. Late E256–E260 stress tests are downstream and cannot retroactively manufacture preparation before E197.

Decision: **PARTIAL**. Exact pre-E197 source set and failed-branch exclusions remain open.

## 5. Coalition cooperation

E148-A provides `history.cross_faction_package`; E261-A provides explicit cooperation-package evidence. Four active routes, `thread.coalition`, or `four_way_bargain` alone do not satisfy the complete predicate. Participant identity, positive outcome and blocker semantics remain required.

Decision: **PARTIAL**.

## 6. Hard negatives retained

1. Downstream consumers cannot manufacture their prerequisites.
2. `food_logistics_stabilized` is not automatically `pred.food_stable`.
3. E192 cannot create the `pred.transport_disruption` state it consumes.
4. Recovery evidence does not imply a later reactivation producer.
5. `rel.ivo` cannot independently qualify guild influence.
6. One institutional domain cannot be counted twice through aliases.
7. E197–E210 cannot retroactively satisfy `pred.constitutional_prepared_strong` or `pred.final_charter_prerequisites`.
8. E273–E277 cannot enter frozen production semantics.

## Gate decision

S08 remains **IN PROGRESS**.  
S09 remains **IN PROGRESS**.  
S10 remains **IN PROGRESS**.  
Production schema remains **BLOCKED**.  
Runtime/reachability remains **NOT VERIFIED**.

## Next machine-checkable batch

1. Enumerate every E01–E272 producer token and consumer token from the authoritative catalogs.
2. Build a producer-before-consumer chronology table.
3. Detect duplicate semantic writers and contradictory writers.
4. Detect predicate cycles/self-satisfaction.
5. Reconcile delayed source/target identities with the same frozen-scope filter.
6. Begin exact ending/replay prerequisite matrix only after producer chronology is clean.

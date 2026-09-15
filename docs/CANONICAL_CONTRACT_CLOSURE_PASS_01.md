# Choice Kingdom — Canonical Contract Closure Pass 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — CONTRACT CLOSURE WORKING RECORD
Scope: E01–E272

## Purpose

This pass consolidates the current canonical closure audit into an actionable contract table. It does not create runtime state, thresholds, or hidden fallback behavior. A contract is marked CLOSED only where the authoritative authored source already establishes an unambiguous producer and semantic identity.

## Closure table

| Contract | Current state | Canonical decision / blocker |
|---|---|---|
| `history.guild_representation` | CLOSED | E144 is authoritative producer; legacy wording must normalize to this history marker. |
| `history.guild_logistics_cooperation` | CLOSED | E136-B is the upstream immutable producer; E194 consumes it. |
| `pred.border_crisis` | CLOSED at source lifecycle | E271 declares; E272 resolves; active predicate is derived from declaration minus resolution. Security alone cannot create it. |
| `pred.guild_logistics_cooperation` | CLOSED at source chain | Requires E136-B history plus E194-A neutral-inspection qualification and no immunity-risk blocker. |
| `pred.food_stable` | OPEN | Requires exact durable producer set, invalidation/expiry semantics, and deterministic derivation. Food remains non-resource. |
| `pred.transport_disruption` | OPEN | E136 proves recovery/clear semantics but no authoritative upstream disruption producer is yet closed. |
| `pred.winter_severe` | OPEN | Consumer vocabulary is normalized, but authoritative producer and severity rule remain unspecified. |
| `pred.market_pressure` | OPEN | Consumer vocabulary exists; durable producer set and threshold/derivation remain unspecified. |
| `pred.guild_labor_tension` | OPEN | Producer set and persistence rule remain unspecified. |
| `pred.information_pressure_high` | OPEN | Must be based on information-state evidence, not `rel.toma`; cardinality/source identity remains open. |
| `pred.guild_influence_strong` | PARTIAL | Institutional-domain model is frozen conceptually, but exact minimum producer set must be enumerated and made machine-checkable. |
| `pred.systemic_explanation_verified` | PARTIAL | Requires distinct warehouse/financial, document/language, and witness/organizational evidence IDs plus explicit convergence choice. |
| `pred.coalition_cooperation` | CLOSED at authored source semantics | E148-A is the authoritative cooperation package producer and records participation from all six named faction identities; the qualified predicate still requires explicit compilation into machine-readable membership plus absence of an unresolved collapse/invalidation marker. E146 route-count alone and E148-B selective coalition do not satisfy it. |
| `pred.constitutional_prepared_strong` | OPEN | Must be established before E197 from three independent legitimacy domains; no circular endgame producer allowed. |
| `pred.budget_reform` | OPEN | Audit independence, crown audit, and legislative budget lock must remain distinct. |
| `thread.military_constitutional` | STRONG | E199-A's constitutional army oath provides explicit route evidence; final activation contract still needs compilation. |
| `thread.coalition` | STRONG | E148-A provides the authored cross-faction package and named participation evidence; exact immutable membership/package representation still needs compilation. |
| `thread.amara_civic` | PARTIAL | Multiple authored Amara choices exist; one explicit route activation contract remains necessary. |
| `thread.toma_information` | PARTIAL | Multiple authored Toma/information choices exist; explicit activation contract remains necessary. |
| `thread.final_constitutional_phase` | OPEN | Must activate deterministically before E208 without using late consumers as producers. |
| `pred.final_charter_prerequisites` | OPEN | Exact prerequisite set and mandatory-crisis blockers must be frozen before E209. |
| Delayed consequence identity | OPEN | Every prose delay needs source choice, exact identity, timing window/condition, cancellation/supersession and exactly-once semantics. |
| Replay metadata | OPEN | Only `meta.*` facts intentionally persistent across runs may qualify future replay behavior. |
| Ending qualification | OPEN | E61–E67 are distinct ending resolvers; independent prerequisites and precedence still require explicit contract. |
| Route identity | CLOSED as semantic rule | Relationship values cannot substitute for explicit historical/flag/thread route identity. See `docs/CANONICAL_ROUTE_CONTRACT_01.md`. Exact machine-readable route producer inventory remains part of schema compilation. |
| Evidence convergence | PARTIAL | Required evidence families are fixed conceptually; exact source IDs and convergence-choice representation still require compilation. |

## Hard invariants carried forward

1. Five numeric resources only: gold, trust, security, power, reputation.
2. Contextual pressures such as food, winter, border, guild influence and information pressure are derived predicates or durable state, never silent sixth resources.
3. Historical decisions are immutable; current-state predicates cannot be satisfied merely by historical wording unless the contract explicitly says so.
4. Relationship values cannot substitute for route identity or institutional evidence.
5. Consumer events cannot manufacture their own prerequisites.
6. Endgame consumers cannot retroactively manufacture preparation predicates.
7. Replay metadata cannot satisfy current-run state unless the authored contract explicitly makes it a cross-run discovery mechanic.
8. Delayed consequences must survive save/load and resolve exactly once.
9. Coalition cooperation is distinct from route count and requires explicit authored cooperation evidence.
10. Evidence convergence requires distinct evidence families and an explicit convergence decision.

## P0 closure blockers

The production schema remains blocked until these are resolved and reconciled against the complete E01–E272 authored catalog:

- food stability producer/clear contract;
- transport disruption producer;
- winter severity producer;
- market pressure producer;
- guild labor tension producer;
- information pressure producer/cardinality;
- exact guild influence institutional set;
- independent evidence route IDs and systemic convergence;
- coalition machine-readable membership and collapse/invalidation semantics;
- constitutional preparation upstream producers;
- final charter prerequisite closure;
- delayed consequence source identity/timing/cancellation/exactly-once extraction;
- replay meta-state contract;
- ending qualification and precedence.

## Gate result

**Canonical contract closure: IN PROGRESS.**

**Production schema: BLOCKED.**

**Validator: intentionally not implemented yet.**

**Decision Engine/runtime: intentionally not implemented yet.**

The next pass should convert the remaining OPEN contracts into exact producer/consumer inventories from the authoritative event catalog, then perform a contradiction/cycle/reachability check before schema freeze.

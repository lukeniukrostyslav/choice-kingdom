# Choice Kingdom — Scenario QA Predicate Dependency / Cycle Audit 01

Status: **SOURCE-LEVEL QA — PREDICATE DEPENDENCY GATE**  
Scope: canonical predicates referenced by delayed callbacks, endgame qualification and replay-sensitive routes; frozen production E01–E272.

## Purpose

Audit predicate dependencies without promoting narrative consumers into producers. A predicate is not considered executable merely because an event mentions it or because the causal graph contains a nearby node.

## Dependency rules

1. A predicate consumer cannot manufacture the prerequisite it consumes.
2. A delayed callback cannot create the predicate that makes its own callback eligible unless an explicit authored producer exists outside that callback lifecycle.
3. Composite predicates require their authored component evidence; one support flag cannot silently substitute for a missing domain.
4. `history.*` does not become replay `meta.*` without an explicit promotion contract.
5. `food_logistics_stabilized` is not `pred.food_stable`.
6. `four_way_bargain` is not `pred.coalition_cooperation`.
7. Security evidence is not interchangeable with border-crisis state.
8. E33/E34 remain quarantined; E273–E277 remain excluded.

## Current dependency screen

| Predicate / state | Dependency | Cycle risk | Current result |
|---|---|---|---|
| `pred.guild_influence_strong` | at least two distinct authored domains | composite/self-manufacture risk | **OPEN** |
| `pred.systemic_explanation_verified` | warehouse/financial + document/language + witness/organizational convergence | convergence self-reference risk | **OPEN** |
| `pred.coalition_cooperation` | positive cooperation + participant identity + no unresolved collapse blocker | support/final predicate confusion | **OPEN** |
| `pred.constitutional_prepared_strong` | three distinct domains | component substitution risk | **OPEN** |
| `pred.budget_reform` | `auditor_independence` + `crown_audited` + `legislative_budget_lock` | no direct cycle identified at source-contract level | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.final_charter_prerequisites` | explicit producer required; E209 is consumer-only | self-manufacture risk | **OPEN/BLOCKED** |
| `pred.food_stable` | no in-scope producer currently closed | accidental alias risk | **OPEN/BLOCKED** |
| `pred.border_crisis` | E271-A declaration, E272 resolution clears active state | lifecycle re-entry risk | **SOURCE-CLOSED / RUNTIME OPEN** |

## Delayed dependency checks

- E181 consumes a toll-concession condition sourced to E45-B; the callback does not itself manufacture that source.
- E243 consumes `public_bridge` sourced to E18-B; E18-A is not merged into the producer.
- E245 remains exclusively sourced to E20-A and cannot union E125-A/E156-A compensation evidence.
- E242 remains partial because its authored wording covers any prior noble exception; E118-B is not promoted as a universal alias.
- E184 remains producer-open; no downstream graph edge is promoted into a producer.
- E185 source identity is closed to E17-A, but the later military-crisis lifecycle remains separately unresolved.

## Replay dependency boundary

Replay-sensitive E186/E247/E248/E249/E250/E270 remain consumer-side until a complete `metaKey + sourceEvent/sourceChoice + promotionTiming + isolationRule + persistenceScope` tuple is authored and machine-closed.

## Result

**Conservative PASS for dependency-boundary screening.** No new executable predicate cycle is promoted from narrative proximity. This is not a proof of runtime reachability or engine correctness.

## Remaining closure gates

- exact producers for open composite predicates;
- delayed cancellation/supersession and scheduler lifecycle;
- replay producer inventory;
- ending precedence;
- fresh-run and replay reachability;
- machine semantic equality with authoritative catalog.

**No Decision Engine promotion is authorized by this audit.**

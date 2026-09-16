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
5. Current food stability is established by E192-B and explicitly cleared by E192-A; historical evidence is not silently treated as current stability.
6. `four_way_bargain` is not `pred.coalition_cooperation`.
7. Security evidence is not interchangeable with border-crisis state.
8. E33/E34 are canonical production events; E273–E277 remain excluded.

## Current dependency screen

| Predicate / state | Dependency | Cycle risk | Current result |
|---|---|---|---|
| `pred.guild_influence_strong` | at least two distinct authored domains | composite/self-manufacture risk | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.systemic_explanation_verified` | warehouse/financial + document/language + witness/organizational + E270-A convergence | convergence self-reference risk | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.coalition_cooperation` | E148-A cooperation package + participant identity + no unresolved collapse blocker | support/final predicate confusion | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.constitutional_prepared_strong` | three distinct domains from E50/E154/E161/E199 | component substitution risk | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.budget_reform` | E142-A + E154-A + E198-A | no direct cycle identified at source-contract level | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.final_charter_prerequisites` | explicit derived gate; E209 is consumer-only | self-manufacture risk | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.food_stable` | E192-B current-cycle producer; E192-A clear | accidental alias / stale-cycle risk | **SOURCE-CLOSED / RUNTIME OPEN** |
| `pred.border_crisis` | E271-A declaration, E272-A/B resolution clears active state | lifecycle re-entry risk | **SOURCE-CLOSED / RUNTIME OPEN** |

## Delayed dependency checks

- E181 consumes the toll-concession condition sourced to E45-B; the callback does not manufacture that source.
- E243 consumes `public_bridge` sourced to E18-B; E18-A is not merged into the producer.
- E245 is currently source-closed to E20-A in the machine canonical graph; union with E125-A/E156-A remains forbidden without an authored family rule.
- E242 is sourced to E118-B for the canonical machine contract while preserving the authored timing constraint.
- E184 is sourced to E25-B at source identity level; lifecycle semantics remain separate.
- E185 source identity is E17-A; later military-crisis lifecycle remains separately unresolved.

## Replay dependency boundary

Replay-sensitive E186/E247/E248 remain subject to exact `metaKey + sourceEvent/sourceChoice + promotionTiming + isolationRule + persistenceScope` closure. Ordinary E249/E250/E270 authored history must not be promoted to replay metadata without an explicit contract.

## Result

**Conservative PASS for dependency-boundary screening.** No executable predicate cycle is promoted from narrative proximity. Source-level closures are distinguished from runtime qualification.

## Remaining closure gates

- runtime qualification/invalidation for composite predicates;
- delayed cancellation/supersession and scheduler lifecycle;
- replay producer execution/reset/isolation;
- ending precedence;
- fresh-run and replay reachability;
- machine semantic equality with authoritative catalog.

**No Decision Engine promotion is authorized by this audit.**

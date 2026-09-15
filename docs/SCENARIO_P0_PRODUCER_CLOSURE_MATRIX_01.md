# Choice Kingdom — Scenario P0 Producer Closure Matrix 01

Status: **SOURCE-LEVEL P0 CLOSURE GATE — NOT RUNTIME CLOSED**  
Scope: E01–E272 only.

## Purpose

Freeze the exact distinction between an authored event that **supports** a prerequisite and an authored event that actually **produces** it. This prevents the scenario from reaching 100% through graph proximity or downstream self-qualification.

| Predicate | Candidate producer | Current authoritative status | Closure required |
|---|---|---|---|
| `pred.guild_influence_strong` | E49 / E165 / E168-A / E136-B | composite source contract exists | executable ordering + fresh-run reachability + blocker evaluation |
| `pred.constitutional_prepared_strong` | E50-A / E154-A / E161-A / E199-A | composite source contract exists | deterministic domain aggregation + blocker evaluation + fresh-run reachability |
| `pred.coalition_cooperation` | E148-A candidate | **NOT CLOSED** | exact participant identities, positive outcome, collapse blockers, canonical key |
| `pred.systemic_explanation_verified` | no exact producer frozen | **OPEN** | authoritative producer + key + convergence rule + anti-circularity |
| `pred.final_charter_prerequisites` | no exact producer frozen; E209 is consumer | **OPEN** | authoritative producer + key + upstream chain |

## Non-circularity rules

1. A consumer cannot manufacture a predicate it consumes.
2. A trigger string is not evidence of the predicate.
3. Support evidence is not equivalent to a composite predicate.
4. One authored domain cannot count twice unless an explicit canonical independence rule exists.
5. Downstream consequences cannot retroactively become upstream prerequisites.
6. Replay-only evidence cannot be promoted to ordinary same-run history.

## Required scenario-100 gates

A predicate is scenario-closed only when its source producer/key, consumer contract, ordering, contradiction/cycle behavior, save/load semantics, and fresh-run reachability are all verified. Runtime verification remains a separate gate.

## Current result

The matrix itself is closed as a QA artifact, but the five predicate rows above remain source/runtime work items. No scenario percentage is raised merely because this matrix exists.

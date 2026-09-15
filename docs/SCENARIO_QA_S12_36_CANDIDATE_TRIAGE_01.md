# Scenario QA S12.36 — Candidate Triage Contract 01

## Purpose

Define the next semantic QA gate for the machine graph candidates without treating graph degree as proof of orphanhood.

## Frozen scope

Production scope remains E01–E272. E273–E277 are excluded.

## Candidate classes

A candidate is promoted only when authoritative source evidence supports the classification:

| Class | Required evidence | Runtime meaning |
|---|---|---|
| ROOT/SOURCE | explicit campaign entry/source semantics | can start a causal chain |
| PRODUCER | explicit authored effect/state mutation | writes a durable key/state |
| CONSUMER-ONLY | explicit prerequisite read with no authored write | cannot satisfy itself |
| TERMINAL/ENDING | explicit terminal or ending qualification semantics | ends a route/result |
| QUALIFICATION | explicit formula/domain rule | evaluates prior evidence; does not invent it |
| DELAYED CALLBACK | explicit delayed identity and source producer | scheduled consequence |
| REPLAY-ONLY | explicit meta-state semantics | must not contaminate fresh-run state |
| TRUE ORPHAN | no valid source, consumer, terminal, delayed, replay, or root role after reconciliation | source/graph defect |

## Hard anti-false-positive rules

- No outbound edge does not prove terminality.
- No inbound edge does not prove orphanhood.
- A relationship is not automatically an institutional state.
- A QA summary cannot become an authored producer.
- A candidate producer cannot be admitted only because it makes a downstream ending reachable.
- `meta.*` must remain outside ordinary fresh-run causal state.
- E273–E277 cannot be used to repair missing E01–E272 reachability.

## Current priority candidates

1. The 54 unreferenced catalog candidates.
2. The 69 no-outbound candidates.
3. The 15 inbound-only candidates.
4. E265–E270 ending qualification and incoming paths.
5. E247–E250 replay/meta boundary.

## Current unresolved source gates

- E33/E34 exact authored recovery;
- `pred.food_stable` producer;
- exact guild influence qualification;
- systemic explanation convergence identity;
- coalition cooperation qualification;
- constitutional preparation ordering;
- final charter prerequisite producer set;
- delayed cancellation/supersession;
- E184/E185 lifecycle;
- ending precedence;
- fresh-run/replay reachability.

## Gate

**S12.36 = semantic candidate-triage contract defined; candidate-by-candidate closure remains OPEN.**

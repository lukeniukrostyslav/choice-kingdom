# Choice Kingdom — Canonical Delayed Consequence Contract

Status: **DESIGN / QA — NOT ENGINE RUNTIME**

Delayed consequences are a first-class part of Choice Kingdom. Narrative prose is not sufficient for implementation.

## Required production representation

Every delayed consequence must define:

- `id`: globally unique delay identity;
- `sourceEventId`;
- `sourceChoiceId`;
- `earliestTurn`;
- `latestTurn` or an explicit condition-based resolution rule;
- `resolutionTarget` (event, state effect, flag, thread, or ending pressure);
- `exactlyOnceKey`;
- `priority` when multiple delays compete;
- `cancellationRule` when a later decision invalidates the premise;
- `supersedes` when this delay replaces an earlier pending consequence;
- `saveLoadPolicy` = persistent;
- `auditLabel` for narrative QA.

## Timing rules

1. A delay is scheduled only after the source choice is successfully committed.
2. Scheduling is deterministic from the same state/history/seed.
3. A pending delay survives save/load.
4. A delay may resolve at most once.
5. If a cancellation condition becomes true, the delay is marked cancelled rather than silently deleted.
6. If a latest-turn boundary exists and no resolution occurs, QA must classify the case as an authored defect; the engine must not silently invent an outcome.
7. Multiple delayed effects resolving on the same turn must use deterministic ordering.

## QA cases

For every delayed consequence, future tests must cover:

- normal scheduling;
- save/load while pending;
- exact earliest-turn behavior;
- late-boundary behavior;
- cancellation/supersession;
- duplicate-resolution attempt;
- competing delays on the same turn;
- replay isolation;
- deterministic outcome from identical initial conditions.

## Narrative normalization examples

Prose such as:

- “after 3 turns” → explicit `earliestTurn` relative to source;
- “5+ turns later” → explicit earliest turn plus resolution condition/window;
- “during a later crisis” → named crisis condition plus deterministic resolution policy;
- “schedules severe delayed loss” → explicit state effect and exactly-once identity.

No production event may retain an ambiguous timing phrase as its only executable specification.

## Gate

The existence of this contract does **not** mean delayed consequences are implemented. They remain pending canonical data extraction, engine implementation and automated verification.

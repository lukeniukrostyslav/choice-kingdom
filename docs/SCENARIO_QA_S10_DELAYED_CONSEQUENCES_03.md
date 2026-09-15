# Choice Kingdom — Scenario QA S10 — Delayed Consequences 03

Date: 2026-09-15  
Frozen scope: **E01–E272**  
Status: **IN PROGRESS — E185 CRISIS RESOLUTION / ORDERING CONTRACT**

## Purpose

Close the remaining static ambiguity around E185 without inventing an authored producer, crisis identity, or consequence payload. This checkpoint defines the minimum contract the runtime must satisfy once the authoritative source identity is fully reconciled.

## 1. Known authored source

The current canonical delayed-consequence matrix identifies:

- source event: **E17**
- source choice: **E17-A**
- source condition: **`cheap_weapons`**
- later eligibility: **a military crisis**
- delayed resolution: an authored military-loss consequence whose exact runtime payload remains source-dependent.

No new producer is created by this document.

## 2. Required two-stage eligibility

E185 must not be represented as a simple N-turn timer.

A pending E185 instance becomes eligible only when both conditions hold:

1. its minimum delay boundary has been reached; and
2. the later military-crisis condition is true according to a canonical, independently produced crisis state.

Conceptually:

`eligible(E185) = pending(sourceIdentity) AND turn >= earliestTurn AND militaryCrisisActive`

The exact crisis predicate/key remains subject to the canonical producer inventory. A consumer must not manufacture the crisis state.

## 3. Source provenance and instance identity

Every E185 pending instance must preserve:

- `runId`
- `sourceEventId = E17`
- `sourceChoiceId = E17-A`
- stable `consequenceId`
- `sourceTurn`
- `earliestTurn`
- lifecycle status

The authored event ID `E185` is not a sufficient unique instance key.

Repeated evaluation of E17-A, save/load, or a new military-crisis check must never create a duplicate instance for the same qualifying source choice.

## 4. Crisis ordering contract

When the minimum delay has elapsed but the military crisis is not active, the callback remains pending.

When the crisis becomes active after the delay boundary, E185 becomes eligible at the first valid evaluation point.

If the crisis is already active when the delay boundary is crossed, E185 becomes eligible at the first evaluation point at or after `earliestTurn`.

The callback must not resolve before `earliestTurn` merely because the crisis is active.

## 5. Multiple eligible callbacks

The runtime must use a deterministic ordering key when multiple delayed callbacks become eligible in the same turn.

The ordering key must be stable across save/load and replay. It must not depend on hash-map iteration order, wall-clock time, or nondeterministic collection ordering.

The exact production ordering field is not frozen by this document; the runtime contract must expose one before implementation is admitted.

## 6. Crisis lifecycle and cancellation

E185 must distinguish:

- crisis declaration/activation;
- crisis resolution/clear;
- delayed callback eligibility;
- callback resolution;
- explicit supersession/cancellation, if authored.

A later crisis clear must not retroactively erase the fact that the callback became eligible. Conversely, no consequence may be applied merely because a historical crisis existed if the authored rule requires an active crisis at resolution time.

The authoritative content must decide this distinction before runtime behavior is frozen.

## 7. Exactly-once invariant

For E185:

`E17-A qualifying source -> zero/one pending instance -> zero/one resolution`

A resolved instance cannot resolve again. A cancelled/superseded instance cannot later resolve unless an explicit authored transition reopens it.

Save/load must restore the existing lifecycle state rather than recreate it from `cheap_weapons`.

## 8. Replay boundary

E185 pending state is run-local. A fresh run starts with no E185 instance inherited from another run.

Only explicitly authored replay metadata may cross runs. The existence of `cheap_weapons`, a prior crisis, or a prior E185 resolution must not implicitly become `meta.*` state.

## 9. Remaining source-level blocker

The phrase “military crisis” still requires exact canonical producer identity and resolution semantics in the exhaustive producer/consumer closure.

Therefore this checkpoint **does not** mark E185 runtime-ready and does not freeze a new predicate alias.

## 10. Gate result

Closed at static contract level:

- E17-A source provenance retained;
- two-stage delay + crisis eligibility established;
- pre-delay resolution forbidden;
- deterministic same-turn ordering required;
- run-local exactly-once identity preserved;
- save/load duplication forbidden;
- replay inheritance forbidden;
- crisis lifecycle and supersession ambiguity explicitly isolated.

Still open:

- exact canonical producer for the military-crisis condition;
- exact authored delayed-loss payload;
- final cancellation/supersession rule;
- production ordering field/value.

**S10 remains IN PROGRESS.**

Global Scenario QA remains unchanged until global gates close.

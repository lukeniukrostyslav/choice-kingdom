# Choice Kingdom — S12.24 E245 Compensation Source Reconciliation

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — OPEN / RECONCILIATION REQUIRED**
Frozen production scope: **E01–E272**

## Purpose

Reconcile the delayed callback E245 (`The Soldier's Son Returns`) against every compensation producer already identified by source-level QA, without inventing a generic compensation alias.

## E245 authored trigger

E245 is triggered by:

`compensation route, 6+ turns later`

The callback itself is not an executable predicate until the authored meaning of `compensation route` is normalized.

## Confirmed compensation facts already present in QA evidence

- **E20-A → `soldier_compensation`** — identified in the earlier delayed-graph audit as an authored compensation fact.
- **E125-A → `border_compensation`** — source-closed producer in the canonical producer inventory.
- **E156-A → `requisition_compensation`** — source-closed producer in the canonical producer inventory.

These facts are semantically distinct. Their common English description (“compensation”) is not sufficient to create a machine-level union.

## Current contradiction / reconciliation point

The current canonical producer inventory narrowed E245's candidate set to E125-A + E156-A, while the earlier delayed-graph audit also records E20-A `soldier_compensation` as an authored compensation fact.

Therefore E245 cannot currently be marked source-closed.

The correct state is:

`E245 producer = OPEN`

with candidate source set requiring authoritative catalog re-read:

`E20-A`, `E125-A`, `E156-A`

No candidate is promoted merely because it contains the word “compensation”.

## Negative boundaries

The following are not producers of E245 merely by semantic proximity:

- E117-B `veteran_patronage`;
- E222 veteran-family social-pressure consequences;
- unrelated compensation-like resource/economic effects.

## Required closure decision

One of the following must be established from authoritative authored text before runtime registration:

1. **Single-source closure:** one exact event+choice is explicitly the intended source for E245.
2. **Explicit authored composite:** the catalog explicitly defines a composite compensation predicate and names its constituent sources.
3. **Explicit source-family rule:** the catalog explicitly states that multiple named compensation contexts qualify for E245.

Absent one of these, no `compensation_route = A OR B OR C` implementation is permitted.

## Delayed lifecycle remains separate

Even after producer identity is closed, E245 still requires:

`sourceEventId + sourceChoiceId + consequenceId=E245 + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`

The authored `6+ turns later` wording must not be converted into a guessed exact turn.

## Gate

- E245 producer identity: **OPEN**
- E20-A candidate: **requires authoritative reconciliation**
- E125-A candidate: **confirmed authored compensation producer**
- E156-A candidate: **confirmed authored compensation producer**
- Generic compensation union: **FORBIDDEN until explicitly authored**
- Runtime delay registration: **BLOCKED**
- Decision Engine promotion: **BLOCKED by canonical contract gate**

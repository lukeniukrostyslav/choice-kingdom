# Choice Kingdom — Delayed Source Closure 03

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — NOT RUNTIME DATA**

## Purpose

This pass closes only delayed-consequence producer identity that is explicitly supported by the authoritative authored catalog. It deliberately does **not** infer source choices, delay IDs, callback keys, cancellation rules, or runtime persistence from prose alone.

## E181 — The Second Toll Increase

**Consumer condition:** 5+ turns after a toll concession.

The canonical delayed inventory identifies the upstream concession as the authored `infrastructure_concession` route. The authoritative E151–E210 catalog confirms E181 consumes the prior concession rather than manufacturing it.

**Verified upstream producer:** E45-B → `infrastructure_concession` → delayed E181 route.

**Still open:**
- exact executable `sourceEventId/sourceChoiceId` representation in production data;
- unique `delayId` / `exactlyOnceKey`;
- whether the callback is cancelled, superseded, or merely becomes ineligible after another policy decision;
- save/load representation;
- deterministic same-turn ordering.

## E182 — The Veteran's Promise

**Consumer condition:** `veteran_patronage`, 4+ turns later.

The trigger vocabulary is explicit in the authored E182 node. The current source inventory does not provide enough evidence in the available canonical excerpts to freeze a unique producer event/choice without inference.

**Status:** trigger and timing source-verified; producer identity remains OPEN.

No relationship score or generic veteran event may be promoted into `veteran_patronage` without an explicit authored producer.

## E183 — The Noble Exception Returns

**Consumer condition:** `estate_exception`, 5+ turns later.

The trigger vocabulary and timing are explicit. A unique producer event/choice is not frozen by this pass because the current canonical evidence does not establish it unambiguously.

**Status:** trigger and timing source-verified; producer identity remains OPEN.

A noble relationship, route count, or other similar state must not silently manufacture `estate_exception`.

## E184 — The Quiet Evidence

**Consumer condition:** secret evidence route, 4+ turns later.

The authored node establishes the delayed timing and the two downstream choices. The source evidence currently available does not establish a unique machine-level producer identity or canonical predicate for the secret evidence route.

**Status:** timing source-verified; trigger normalization and producer identity remain OPEN.

## E185 — The Cheap Steel Remembered

**Consumer condition:** `cheap_weapons` plus a later military crisis.

The canonical foundational catalog establishes `cheap_weapons` through E17-A. Therefore the first half of E185's trigger is source-closed:

**Verified producer:** E17-A → `cheap_weapons` → E185 eligibility.

The second half — the later military crisis — is intentionally not treated as an implicit alias for any generic crisis/security state. Its exact canonical predicate/event identity and resolution target remain OPEN.

E185 therefore remains **HIGH PRIORITY OPEN** for machine-contract closure because choice B schedules a severe delayed loss and choice A explicitly prevents a later disaster.

## Machine-contract gate

For E181–E185, an authored trigger/timing statement is not sufficient for executable runtime data. Each admitted delay must eventually contain:

`delayId`, `sourceEventId`, `sourceChoiceId`, `earliestTurn`, `latestTurnOrResolutionCondition`, `resolutionTarget`, `exactlyOnceKey`, `priority`, `cancellationRule`, `supersedes`, `saveLoadPolicy`, `auditLabel`.

Pending callbacks remain run-local and must not cross replay boundaries except through explicitly authored `meta.*` transfer data.

## Result

- E181: **producer source-closed** through E45-B; lifecycle still open.
- E182: **producer open**.
- E183: **producer open**.
- E184: **trigger normalization + producer open**.
- E185: **`cheap_weapons` producer source-closed through E17-A; military-crisis half and delayed lifecycle open**.

This document is a QA artifact only. It does not claim runtime implementation or readiness.

# Choice Kingdom — Delayed Source Closure 04

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — NOT RUNTIME DATA**

## Scope

This pass reconciles the authored trigger/timing statements for E242–E246 against the canonical E211–E270 source. It does not invent upstream producers where the catalog does not explicitly identify one.

## E242 — The Renewed Exception

**Authored trigger:** any prior noble exception; 6+ turns later.

The node explicitly depends on an earlier noble-exception precedent. The current source excerpt does not uniquely identify which event/choice establishes that precedent.

**Status:** timing and semantic dependency verified; producer identity OPEN.

The production engine must not synthesize this trigger from Seris relationship, noble route count, or another generic exception state.

## E243 — The Old Bridge

**Authored trigger:** public bridge investment; 5+ turns later.

The delayed dependency is explicit, but the current canonical excerpt does not uniquely identify the investment event/choice or a machine-level callback identity.

**Status:** timing and semantic dependency verified; producer identity OPEN.

The storm/convoy occurrence is also a later resolution condition rather than an implicit generic crisis alias.

## E244 — The Audit Comes Due

**Authored trigger:** flexible accounts; 5+ turns later.

The callback represents a later accounting failure: the missing trail becomes impossible to reconstruct. The authored node does not identify a unique upstream event/choice in this pass.

**Status:** trigger and timing verified; producer identity and exact failure-resolution contract OPEN.

## E245 — The Soldier's Son Returns

**Authored trigger:** compensation route; 6+ turns later.

The node explicitly consumes a prior compensation route. The exact producer event/choice and route identity are not frozen by the available canonical excerpt.

**Status:** trigger and timing verified; producer identity OPEN.

## E246 — The Price Ceiling Memory

**Authored trigger:** price ceiling; 5+ turns later.

The node explicitly consumes a prior temporary price-ceiling decision and checks whether it ended on schedule. The exact ceiling producer, expiry state, extension callback and exactly-once identity remain OPEN.

**Status:** trigger and timing verified; lifecycle contract OPEN.

## Cross-cutting machine contract

The five nodes require explicit production fields before engine integration:

`delayId`, `sourceEventId`, `sourceChoiceId`, `earliestTurn`, `latestTurnOrResolutionCondition`, `resolutionTarget`, `exactlyOnceKey`, `priority`, `cancellationRule`, `supersedes`, `saveLoadPolicy`, `auditLabel`.

A delayed callback is not considered executable merely because the authored text contains a turn count. Pending callbacks remain run-local and must not cross a replay boundary without explicit authored `meta.*` transfer.

## Result

E242–E246 now have a verified source-level trigger/timing inventory, but none is promoted to a fully closed executable delay. Producer identity and lifecycle fields remain explicit QA work rather than inferred data.

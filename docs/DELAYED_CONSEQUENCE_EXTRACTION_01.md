# Choice Kingdom — Delayed Consequence Extraction 01

Date: 2026-09-15  
Status: **SOURCE EXTRACTION — NOT RUNTIME DATA**

## Purpose

The authored catalog contains delayed effects in several forms: explicit timed callback nodes, prose callbacks, delayed resource changes and future unlocks. This pass separates them so the future engine cannot mistake narrative prose for executable timing.

## Explicit timed callback groups found in the authored sources

### E111–E150

- E127 — 4+ turns after `hereditary_seats_limited` or `temporary_noble_exemption`
- E128 — `cheap_weapons`, 3+ turns later
- E129 — festival-held callback, 3+ turns later
- E130 — `infrastructure_concession`, 4+ turns later
- E141 — `emergency_renewal_possible`, 5+ turns later

These are the clearest candidates for direct machine-readable delay records. They still require exact source choice IDs and resolution targets.

### E151–E210

- E181 — 5+ turns after a toll concession
- E182 — `veteran_patronage`, 4+ turns later
- E183 — `estate_exception`, 5+ turns later
- E184 — secret evidence route, 4+ turns later
- E185 — `cheap_weapons` plus a later military crisis; choice B explicitly schedules a severe delayed loss

E185 is especially important because the delay is authored by a choice and therefore must carry a stable `sourceChoiceId` and exactly-once identity.

### E211–E270

- E242 — any prior noble exception, 6+ turns later
- E243 — public bridge investment, 5+ turns later
- E244 — flexible accounts, 5+ turns later
- E245 — compensation route, 6+ turns later
- E246 — price ceiling, 5+ turns later

E246 also contains a choice-level delayed effect: extending the price ceiling causes a later Ivo penalty. This must not be encoded as a generic future modifier without a source choice identity.

## Non-timed delayed prose requiring normalization

The earlier event catalogs also contain phrases such as:

- “later”;
- “delayed”;
- “during a later crisis”;
- “if winter hits”;
- “after another emergency”;
- “if no oversight”;
- “later evidence becomes available”.

These statements are narrative requirements, not sufficient production timing specifications.

## Required normalization record

For every executable delayed effect, the future production catalog must contain:

`delayId`  
`sourceEventId`  
`sourceChoiceId`  
`earliestTurn`  
`latestTurnOrResolutionCondition`  
`resolutionTarget`  
`exactlyOnceKey`  
`priority`  
`cancellationRule`  
`supersedes`  
`saveLoadPolicy`  
`auditLabel`

## Replay isolation rule

A pending delay belongs to one run. It must not leak into a replay unless an explicit `meta.*` transfer rule authorizes that transfer. A replay must never inherit a pending callback merely because it originated from the same account/device/save slot.

## Same-turn ordering rule

If multiple delays become eligible on the same turn, ordering must be deterministic and data-defined. Suggested canonical ordering key:

1. earliest scheduled turn;
2. explicit priority;
3. stable delay ID.

The engine must not depend on hash-map iteration or file order.

## Current gate

**Timed callback candidates identified:** YES  
**Exact source choice IDs extracted for all candidates:** NO  
**Cancellation/supersession fully specified:** NO  
**Production delay schema frozen:** NO  
**Runtime implementation:** NOT STARTED

This extraction increases QA coverage but does not claim implementation.
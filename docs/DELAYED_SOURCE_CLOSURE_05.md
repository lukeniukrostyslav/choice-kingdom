# Choice Kingdom — Delayed Source Closure 05

Status: **SOURCE-LEVEL QA — PARTIAL CLOSURE**
Scope: E181–E185 and E242–E246.

## Purpose

Close producer identity only where the authored catalog provides an exact source choice. Do not infer a producer from a vague semantic similarity. Timing, target and lifecycle fields remain separate from producer identity.

## Closure matrix

| Delayed node | Trigger | Exact producer | Producer choice | Timing | Lifecycle status |
|---|---|---|---|---|---|
| E181 Second Toll Increase | infrastructure/toll concession | E45 | B — concession route | 5+ turns | OPEN: exact delay key, cancellation/supersession, save/load and exactly-once |
| E182 Veteran's Promise | `veteran_patronage` | E117 | B — reserve posts for veterans | 4+ turns | OPEN: exact delay key, cancellation/supersession, save/load and exactly-once |
| E183 Noble Exception Returns | `estate_exception` | E118 | B — transitional exception | 5+ turns | OPEN: exact delay key, cancellation/supersession, save/load and exactly-once |
| E184 Quiet Evidence | secret evidence route | **NOT SOURCE-CLOSED** | **NOT IDENTIFIED** | 4+ turns | OPEN: trigger normalization + producer + lifecycle |
| E185 Cheap Steel Remembered | `cheap_weapons` + later military crisis | E17 | A — cheap weapons procurement | later crisis; no fixed numeric delay | OPEN: crisis-resolution condition, exactly-once, cancellation/supersession, deterministic target |
| E242 Renewed Exception | prior noble exception | E118-B is an explicit candidate source; other exception producers may exist | transitional exception | 6+ turns | OPEN: complete producer set and whether any other producer creates same semantic fact |
| E243 Old Bridge | public bridge investment | **NOT SOURCE-CLOSED** | **NOT IDENTIFIED** | 5+ turns | OPEN: exact source event/choice + lifecycle |
| E244 Audit Comes Due | flexible accounts | **NOT SOURCE-CLOSED** | **NOT IDENTIFIED** | 5+ turns | OPEN: exact producer + failure-resolution semantics + lifecycle |
| E245 Soldier's Son Returns | compensation route | **NOT SOURCE-CLOSED** | **NOT IDENTIFIED** | 6+ turns | OPEN: exact compensation producer + lifecycle |
| E246 Price Ceiling Memory | price ceiling | E160 | A — temporary rent/price ceiling route | 5+ turns | OPEN: verify semantic identity of `price ceiling` vs authored `winter_rent_ceiling`; do not alias without normalization |

## Important distinctions

### E181
The event graph and earlier source audit identify the infrastructure concession path as the upstream route. The engine must preserve the exact source event and choice rather than storing only a generic `toll_concession` flag.

### E182
E117-B explicitly produces `veteran_patronage`, making E117-B the current source-closed producer for E182.

### E183
E118-B explicitly produces `estate_exception`, making E118-B the current source-closed producer for E183.

### E184
The phrase `secret evidence route` is a semantic description, not a machine-safe producer. A future closure must identify the exact event and choice that establishes the route and must not pick a producer merely because it contains secret/evidence language.

### E185
E17-A is the known producer of `cheap_weapons`. The second half of the trigger is a later military-crisis condition, so the callback is not a simple fixed-turn flag. The runtime contract must define when the crisis condition is evaluated, how the callback resolves, and how the prevention route suppresses the severe-loss route.

### E242
E118-B is an explicit source of `estate_exception`, but the phrase "any prior noble exception" is broader than one producer. Before runtime, the producer registry must decide whether E242 intentionally consumes only `estate_exception` or a closed set of additional canonical exception facts. No generic "noble exception" alias should be invented.

### E243
`public bridge investment` is not yet mapped to an exact canonical source choice in this closure pass. Do not use E224 merely because it mentions bridge safety; semantic proximity is insufficient.

### E244
`flexible accounts` requires an exact source. It must not be manufactured from any event that merely discusses auditing, borrowing or accounting.

### E245
`compensation route` requires an exact source. Border compensation, requisition compensation and other compensation outcomes must be distinguished before a single producer is selected.

### E246
The authored event E160 uses `winter_rent_ceiling`, while E246 says `price ceiling`. These are not automatically identical. Trigger normalization must explicitly decide whether E246 is intended to consume E160-A or another canonical price-control producer.

## Executable delay contract required for every closed producer

Each delayed callback must eventually carry:

- `delayId`
- `sourceEventId`
- `sourceChoiceId`
- `earliestTurn`
- `latestTurnOrResolutionCondition`
- `resolutionTarget`
- `exactlyOnceKey`
- `priority`
- `cancellationRule`
- `supersedes`
- `saveLoadPolicy`
- `auditLabel`

No callback is runtime-ready merely because producer identity and timing are known.

## Gate result

**Producer identity fully closed:** E181, E182, E183, E185.

**Producer identity partially closed:** E242 (known explicit source, complete producer set still open).

**Producer identity open:** E184, E243, E244, E245, E246 semantic normalization.

**Runtime implementation:** not started.

This document is intentionally conservative: unresolved producer identity remains OPEN rather than being guessed.

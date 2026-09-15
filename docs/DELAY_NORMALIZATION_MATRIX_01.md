# Choice Kingdom — Delayed Consequence Normalization Matrix 01

Date: 2026-09-15
Status: **SOURCE-LEVEL NORMALIZATION — NO RUNTIME IMPLEMENTATION**

## Purpose

Normalize only fields that are explicitly supported by the authored catalog. Unknown fields remain OPEN. This document is not executable game data and must not be treated as a substitute for the production schema.

## E127–E130 / E141

| Consumer | delay timing | verified source | explicit source choice | resolution target | exactly-once | cancellation/supersession |
|---|---|---|---|---|---|---|
| E127 | 4+ turns | E06-B and/or E38-A | E06-B / E38-A | E127 | OPEN | OPEN |
| E128 | 3+ turns | E17-A | E17-A | E128 | OPEN | OPEN |
| E129 | 3+ turns | E22-A | E22-A | E129 | OPEN | OPEN |
| E130 | 4+ turns | E45-B | E45-B | E130 | OPEN | OPEN |
| E141 | 5+ turns | E48-B | E48-B | E141 | OPEN | E48-A opposing block must supersede/negate eligibility |

## E181–E185

| Consumer | timing/condition | source identity | resolution target | exactly-once | cancellation/supersession |
|---|---|---|---|---|---|
| E181 | 5+ turns after toll concession | OPEN | E181 | OPEN | OPEN |
| E182 | 4+ turns after `veteran_patronage` | OPEN | E182 | OPEN | OPEN |
| E183 | 5+ turns after `estate_exception` | OPEN | E183 | OPEN | OPEN |
| E184 | 4+ turns after secret-evidence route | OPEN | E184 | OPEN | OPEN |
| E185 | later military crisis; no numeric delay | OPEN | later severe-loss resolution | OPEN | OPEN |

## E242–E246

| Consumer | timing/condition | source identity | resolution target | exactly-once | cancellation/supersession |
|---|---|---|---|---|---|
| E242 | 6+ turns after prior noble exception | OPEN | E242 | OPEN | OPEN |
| E243 | 5+ turns after public bridge investment | OPEN | E243 storm/convoy outcome | OPEN | OPEN |
| E244 | 5+ turns after flexible accounts | OPEN | E244 accounting failure | OPEN | OPEN |
| E245 | 6+ turns after compensation route | OPEN | E245 civil-service outcome | OPEN | OPEN |
| E246 | 5+ turns after prior price ceiling | OPEN | E246 expiry/extension outcome | OPEN | OPEN |

## Mandatory machine fields

Every production delay must eventually define:

`delayId`, `sourceEventId`, `sourceChoiceId`, `earliestTurn`, `latestTurnOrResolutionCondition`, `resolutionTarget`, `exactlyOnceKey`, `priority`, `cancellationRule`, `supersedes`, `saveLoadPolicy`, `auditLabel`.

No field is marked CLOSED merely because a narrative sentence suggests it. Source identity, timing and target are separated from runtime lifecycle semantics.

## Gate result

- Producer identity for E127–E130/E141: **CLOSED at source level**.
- Timing extraction for all listed groups: **CLOSED where explicit in source**.
- Executable delay identity: **OPEN**.
- Cancellation/supersession: **OPEN**, with the E141 opposing block explicitly identified.
- Save/load persistence: **OPEN**.
- Replay isolation: **DESIGN CLOSED / RUNTIME OPEN**.
- Same-turn deterministic ordering: **OPEN**.
- Runtime implementation: **NOT STARTED**.

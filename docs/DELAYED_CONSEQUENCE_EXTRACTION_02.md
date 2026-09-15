# Choice Kingdom — Delayed Consequence Extraction 02

## Purpose

This pass converts authored delayed-callback prose into production QA records without inventing missing timing, cancellation, or resolution semantics.

Status: **QA extraction only — not runtime data and not engine implementation.**

## Extraction rules

A delayed consequence is not considered production-complete until the source identifies, directly or through an unambiguous upstream contract:

- `delayId`
- `sourceEventId`
- `sourceChoiceId`
- `earliestTurn` or equivalent delay condition
- `latestTurn` or explicit terminal condition, when applicable
- `resolutionTarget`
- `exactlyOnceKey`
- `priority` when same-turn ordering can matter
- `cancellationRule`
- `supersedes` / conflict rule where applicable
- persistent save/load policy
- audit label

Where the authored source only says “later”, “delayed”, “5+ turns later”, etc., the explicit information is recorded and the missing machine contract remains OPEN.

## E181–E185

| Event | Source condition | Timing | Delayed target / outcome | Production status |
|---|---|---|---|---|
| E181 | Prior toll concession | **5+ turns after concession** | Follow-up request for a second toll increase. A enforces original terms; B sells the right to increase tolls. | Timing is explicit. Source concession event/choice, delay identity, exactly-once key, cancellation/supersession and save/load contract remain OPEN. |
| E182 | `veteran_patronage` | **4+ turns later** | Veterans demand promised administrative positions. A uses examinations; B honors promise. | Timing and trigger flag explicit. Source event/choice and callback identity remain OPEN; exactly-once/cancellation/save-load remain OPEN. |
| E183 | `estate_exception` | **5+ turns later** | Another family cites the precedent. A closes exception precedent; B extends it. | Timing and trigger flag explicit. Source event/choice and exact callback identity remain OPEN; cancellation/supersession remain OPEN. |
| E184 | Secret evidence route | **4+ turns later** | Witness asks why preserved evidence was not published. A publishes; B keeps confidentiality. | Timing explicit only at prose level. Source event/choice, exact condition, delay identity, exactly-once and cancellation remain OPEN. |
| E185 | `cheap_weapons` + later military crisis | **No numeric delay** | A halts deployment and prevents later disaster; B deploys and schedules severe delayed loss. | **OPEN HIGH PRIORITY:** “later military crisis” and the scheduled loss need a deterministic resolution target, timing/condition, cancellation and exactly-once semantics. |

### E185 special QA gate

E185 must not be encoded as a generic timer. The source defines a conditional military-crisis callback. The production contract must identify the exact crisis resolution target and the condition that makes the delayed loss eligible. If the condition can become false after scheduling, cancellation/supersession semantics must be explicit.

## E242–E246

| Event | Source condition | Timing | Delayed target / outcome | Production status |
|---|---|---|---|---|
| E242 | Any prior noble exception | **6+ turns later** | New family cites precedent. A closes precedent; B extends it. | Timing explicit. Source event/choice scope, exactly-once key, cancellation and save/load remain OPEN. |
| E243 | Public bridge investment | **5+ turns later** | Bridge saves a convoy during a storm. A credits investment; B claims emergency leadership credit. | Timing explicit. Triggering investment event/choice, callback identity, storm/convoy condition, exactly-once and cancellation remain OPEN. |
| E244 | Flexible accounts | **5+ turns later** | Missing accounting trail becomes impossible to reconstruct. A admits gap; B reconstructs plausible account. | Timing explicit. Source event/choice, exact failure condition, callback identity and exactly-once remain OPEN. |
| E245 | Compensation route | **6+ turns later** | Compensated family member enters civil service. A uses merit; B favors family. | Timing explicit. Source event/choice, identity of compensation route, callback identity, exactly-once and cancellation remain OPEN. |
| E246 | Prior price ceiling | **5+ turns later** | Merchants remember whether temporary measure ended on time. A ends it; B extends it and creates later Ivo loss. | Timing explicit. The source does not yet define the exact owner of the ceiling, expiry contract, extension callback, or exactly-once/cancellation semantics. |

## Earlier delayed groups — extraction status

The canonical delayed-consequence inventory already identifies E127–E130 and E141 as a separate callback group. This pass deliberately does not infer their exact contracts from filenames or downstream effects. They remain part of the open event-by-event extraction queue until their complete source text is available in the same QA pass.

## Cross-cutting production findings

1. **Numeric delays are mostly authored but not machine-complete.** “5+ turns later” is enough to establish an earliest-turn boundary, but not enough to establish identity, persistence, duplicate prevention or cancellation.
2. **Conditional callbacks are higher risk than numeric callbacks.** E185 is the clearest example because its resolution depends on a later military crisis rather than a fixed turn count.
3. **Replay isolation is mandatory.** A scheduled callback from one run must never resolve in another run unless the callback is explicitly represented as `meta.*` replay state.
4. **Save/load must preserve pending callbacks.** A callback cannot disappear because the game was saved before its earliest turn.
5. **Same-turn ordering must be deterministic.** If multiple callbacks become eligible on one turn, their priority/order must be defined before engine implementation.
6. **Cancellation must be observable.** If a later choice makes a callback irrelevant, the production state should record cancellation/supersession rather than silently deleting the pending item.

## QA gate result

**Delayed consequence authored coverage:** substantial.

**Machine-contract closure:** NOT VERIFIED.

The next authoritative step is to extract the remaining E127–E130/E141 source text and then run one unified duplicate, conflict, cancellation and replay-isolation pass across all delayed callbacks before creating runtime schema.

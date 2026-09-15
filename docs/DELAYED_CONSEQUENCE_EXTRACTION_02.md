# Choice Kingdom — Delayed Consequence Extraction 02

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — NOT RUNTIME DATA**

## Scope
This pass freezes only what the authored text explicitly proves for the delayed callback groups. It does not invent source choice IDs, resolution targets, cancellation rules, or persistence semantics where the source is silent.

## E127–E130 / E141

| Event | Authored trigger / timing | Explicit source choices | Producer/source closure |
|---|---|---|---|
| E127 — Renewal Petition | `hereditary_seats_limited` **or** `temporary_noble_exemption`; **4+ turns** | A refuse; B renew once | `temporary_noble_exemption` is explicitly produced by E06-B. `hereditary_seats_limited` has no verified producer in the currently read canonical source set. Therefore E127 has one verified upstream route and one OPEN route. |
| E128 — Cheap Steel Bill | `cheap_weapons`; **3+ turns** | A replace; B repair locally | `cheap_weapons` is produced by E17-A in the foundational catalog. Exact source choice identity can therefore be frozen as E17-A for this route. |
| E129 — Festival Memory | festival was held; **3+ turns** | A publish report; B keep secret | E22-A explicitly holds the festival. This closes the primary source route as E22-A. |
| E130 — Bridge Toll Returns | `infrastructure_concession`; **4+ turns** | A enforce ceiling; B renegotiate | The trigger producer is not yet verified in the currently read source slice. Keep source event/choice OPEN rather than guessing. |
| E141 — Emergency Clause Returns | `emergency_renewal_possible`; **5+ turns** | A public vote; B council renewal | Producer of `emergency_renewal_possible` is not yet verified in the currently read source slice. Keep OPEN. |

### Source-level conclusions

1. **E127 is multi-source.** E06-B is a confirmed producer of `temporary_noble_exemption`; the alternate `hereditary_seats_limited` route remains unresolved.
2. **E128 is source-closed for the known route:** E17-A → `cheap_weapons` → E128 after 3+ turns.
3. **E129 is source-closed for the known route:** E22-A → festival held → E129 after 3+ turns.
4. E130 and E141 remain intentionally open until their producer choices are verified.

## E181–E185

| Event | Source condition | Timing | Delayed target / outcome | Production status |
|---|---|---|---|---|
| E181 | Prior toll concession | **5+ turns after concession** | Follow-up request for a second toll increase. A enforces original terms; B sells the right to increase tolls. | Timing explicit. Source concession event/choice, delay identity, exactly-once key, cancellation/supersession and save/load contract remain OPEN. |
| E182 | `veteran_patronage` | **4+ turns later** | Veterans demand promised administrative positions. A uses examinations; B honors promise. | Timing and trigger flag explicit. Source event/choice and callback identity remain OPEN; exactly-once/cancellation/save-load remain OPEN. |
| E183 | `estate_exception` | **5+ turns later** | Another family cites the precedent. A closes exception precedent; B extends it. | Timing and trigger flag explicit. Source event/choice and exact callback identity remain OPEN; cancellation/supersession remain OPEN. |
| E184 | Secret evidence route | **4+ turns later** | Witness asks why preserved evidence was not published. A publishes; B keeps confidentiality. | Timing explicit only at prose level. Source event/choice, exact condition, delay identity, exactly-once and cancellation remain OPEN. |
| E185 | `cheap_weapons` + later military crisis | **No numeric delay** | A halts deployment and prevents later disaster; B deploys and schedules severe delayed loss. | **OPEN HIGH PRIORITY:** later military crisis and scheduled loss need deterministic resolution target, condition, cancellation and exactly-once semantics. |

## E242–E246

| Event | Source condition | Timing | Delayed target / outcome | Production status |
|---|---|---|---|---|
| E242 | Any prior noble exception | **6+ turns later** | New family cites precedent. A closes precedent; B extends it. | Timing explicit. Source event/choice scope, exactly-once key, cancellation and save/load remain OPEN. |
| E243 | Public bridge investment | **5+ turns later** | Bridge saves a convoy during a storm. A credits investment; B claims emergency leadership credit. | Timing explicit. Triggering investment event/choice, callback identity, storm/convoy condition, exactly-once and cancellation remain OPEN. |
| E244 | Flexible accounts | **5+ turns later** | Missing accounting trail becomes impossible to reconstruct. A admits gap; B reconstructs plausible account. | Timing explicit. Source event/choice, exact failure condition, callback identity and exactly-once remain OPEN. |
| E245 | Compensation route | **6+ turns later** | Compensated family member enters civil service. A uses merit; B favors family. | Timing explicit. Source event/choice, identity of compensation route, callback identity, exactly-once and cancellation remain OPEN. |
| E246 | Prior price ceiling | **5+ turns later** | Merchants remember whether temporary measure ended on time. A ends it; B extends it and creates later Ivo loss. | Timing explicit. Ceiling owner, expiry contract, extension callback and exactly-once/cancellation remain OPEN. |

## Required machine fields still open

For every executable delay: `delayId`, `sourceEventId`, `sourceChoiceId`, `earliestTurn`, `latestTurnOrResolutionCondition`, `resolutionTarget`, `exactlyOnceKey`, `priority`, `cancellationRule`, `supersedes`, persistent `saveLoadPolicy`, `auditLabel`.

## Replay / save-load rules

A pending delay belongs to one run and must not leak into replay without explicit `meta.*` authorization. Pending callbacks must survive save/load. Cancellation or supersession must be recorded rather than silently deleting a scheduled item. Same-turn resolution ordering must be deterministic.

## Gate

**Delayed consequence authored coverage:** substantial  
**Timing reconciliation:** improved; E128 and E129 now have verified upstream producers, E127 has one verified route and one open route.  
**Machine-contract closure:** NOT VERIFIED.  
**Runtime implementation:** NOT STARTED.

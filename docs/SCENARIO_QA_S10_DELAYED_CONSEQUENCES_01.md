# Choice Kingdom — Scenario QA S10 — Delayed Consequences 01

Date: 2026-09-15  
Frozen scope: **E01–E272**  
Status: **IN PROGRESS — STATIC CONTRACT EXTRACTION**

## Purpose

Normalize the authored delayed-consequence nodes into an executable-contract checklist without inventing missing identifiers. S10 covers delayed callbacks explicitly identified in the frozen QA catalog: E181–E185 and E242–E246.

The source catalogs establish event identity, trigger conditions, delay windows and authored outputs. They do **not** yet define a runtime callback schema. Therefore this checkpoint separates **source-closed facts** from **machine-contract gaps**.

## Required delayed-consequence contract

Every delayed consequence must eventually carry:

1. `sourceEventId` — exact originating event;
2. `sourceChoiceId` — exact originating choice/branch;
3. `consequenceId` — stable callback identity;
4. `earliestTurn` or equivalent exact timing rule;
5. trigger/eligibility condition at resolution time;
6. target event/resolution identity;
7. exactly-once identity key;
8. cancellation/supersession rule;
9. persistence/save-load behavior;
10. replay/run boundary rule;
11. resolution provenance for history/audit;
12. deterministic behavior when prerequisites are no longer true.

No runtime-ready callback should be inferred merely from prose such as “5+ turns later”.

## E181–E185 — first delayed family

| Callback | Source event / choice | Authored timing | Authored output | Static status | Runtime gap |
|---|---|---|---|---|---|
| E181 | E45-B toll concession | 5+ turns | `toll_terms_enforced` / `toll_escalation_sold` | SOURCE CLOSED | exact sourceChoiceId, consequence identity, expiry/supersession, exactly-once |
| E182 | E117-B `veteran_patronage` | 4+ turns | `veteran_positions_examined` / `veteran_positions_granted` | SOURCE CLOSED | same contract gaps |
| E183 | E118-B `estate_exception` | 5+ turns | `exception_precedent_closed` / `exception_precedent_extended` | SOURCE CLOSED | same contract gaps |
| E184 | secret-evidence route | 4+ turns | `quiet_evidence_published` / `quiet_evidence_kept` | SOURCE IDENTITY OPEN | producer/choice identity must be resolved before runtime contract |
| E185 | E17-A `cheap_weapons` + later military crisis | later crisis | `steel_failure_prevented` / `steel_failure_delayed` | SOURCE CLOSED / CONDITIONAL | crisis-resolution identity, exactly-once, cancellation/supersession, delayed loss identity |

### E181

Authoritative source QA already identifies E45-B as the source route. The five-turn condition is an authored minimum delay, not an exact scheduled turn. The runtime contract must therefore distinguish `earliestTurn = sourceTurn + 5` from the later eligibility predicate.

### E182

E117-B establishes `veteran_patronage`; the callback is authored at 4+ turns. The callback must remain linked to the exact originating choice, not to a generic “veteran route” state, otherwise multiple possible veteran routes could collapse into one callback identity.

### E183

E118-B establishes `estate_exception`; E183 is a later precedent request at 5+ turns. The callback must preserve source-choice provenance so an unrelated noble event cannot satisfy it accidentally.

### E184

The existing static closure explicitly leaves the secret-evidence producer unresolved. No producer is invented here. E184 remains **BLOCKED for executable contract** until an authoritative source choice is identified or the consumer is removed/reworded.

### E185

E17-A establishes `cheap_weapons`; E185 additionally requires a later military crisis. This is not equivalent to a simple timer. The callback identity must encode both the originating choice and the later crisis eligibility. Branch B schedules a severe delayed loss, so that loss requires its own stable consequence identity and exactly-once rule.

## E242–E246 — second delayed family

| Callback | Source event / choice | Authored timing | Authored output/effect | Static status | Runtime gap |
|---|---|---|---|---|---|
| E242 | E118-B / prior noble exception route | 6+ turns | close/extend precedent | SOURCE CLOSED | exact source-choice identity, repeated-exception semantics, exactly-once |
| E243 | E18-B `public_bridge` | 5+ turns | public credit / emergency-credit branch | SOURCE CLOSED | exact callback identity, persistence, supersession |
| E244 | E09-B `flexible_accounts` | 5+ turns | admit accounting gap / `reconstructed_accounts` | SOURCE CLOSED | exact callback identity, persistence, exactly-once |
| E245 | compensation route | 6+ turns | merit / family-favor branch | SOURCE IDENTITY OPEN | cannot silently union E125-A and E156-A compensation facts |
| E246 | E160-A `winter_rent_ceiling` | 5+ turns | end / extend branch | CONDITIONAL | exact canonical price-ceiling vocabulary + callback identity |

### E242 vs E183

E183 and E242 both concern noble exceptions but are distinct authored delayed nodes with different timing and downstream context. They must not be collapsed into one generic `estate_exception_callback` without explicit authored equivalence.

### E245 compensation boundary

The source QA deliberately prevents silent union of distinct compensation facts. `border_compensation` from E125-A and `requisition_compensation` from E156-A are not automatically the same producer. E245 therefore remains contract-open until the canonical compensation route is explicitly defined.

### E246 price-ceiling boundary

E160-A explicitly authors `winter_rent_ceiling`. E246 refers to a prior price ceiling in prose. The machine contract must first decide whether E246 consumes exactly `winter_rent_ceiling` or another canonical price-control fact. No generic alias is invented in S10.

## Exactly-once / cancellation model — required, not yet implemented

The eventual runtime contract must answer:

- Can the same source choice schedule more than one callback instance?
- If a later choice reverses the underlying policy, is the callback cancelled, superseded, or still resolved?
- If the game is saved before eligibility and loaded later, is the same callback instance restored exactly once?
- If multiple conditions become true on the same turn, what is deterministic resolution order?
- Can an already-resolved callback ever fire again after replay/load?
- Does a callback belong exclusively to one run and disappear at a fresh run boundary?
- For callbacks depending on a later crisis (E185), which event establishes the crisis and what happens if that crisis is resolved before callback execution?

These are machine-contract questions, not assumptions.

## Static disposition

**SOURCE-CLOSED:** E181, E182, E183, E185, E242, E243, E244.  
**CONDITIONAL / vocabulary open:** E246.  
**SOURCE IDENTITY OPEN:** E184, E245.  
**RUNTIME CONTRACT OPEN:** all delayed callbacks.

## S10 gate

- Source/timing inventory: **PARTIAL CLOSED**
- Exact callback identity: **OPEN**
- Exactly-once identity: **OPEN**
- Cancellation/supersession: **OPEN**
- Save/load persistence: **OPEN**
- Resolution ordering: **OPEN**
- Replay isolation: **OPEN**

**S10: 65% / IN PROGRESS.**

Global Scenario QA remains **65%**. No runtime readiness is claimed.

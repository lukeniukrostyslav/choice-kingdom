# Choice Kingdom — Scenario QA S10 — Delayed Consequences 02

Date: 2026-09-15  
Frozen scope: **E01–E272**  
Status: **IN PROGRESS — EXACT IDENTITY / LIFECYCLE MATRIX**

## Purpose

This checkpoint converts the source-closed delayed callbacks into an explicit identity/lifecycle matrix. It does not invent runtime identifiers where the authored catalog does not provide them.

The authoritative catalog confirms the originating choices for E181, E182, E183, E185, E242, E243, E244 and E246. E184 and E245 remain source-identity gaps. filecite references are intentionally not embedded in repository artifacts; source evidence is recorded in the QA worklog and prior closure documents.

## 1. Exact source identity matrix

| Callback | sourceEventId | sourceChoiceId | Authored condition | Stable consequenceId required | Static disposition |
|---|---|---|---|---|---|
| E181 | E45 | E45-B | 5+ turns after long-term concession | YES | SOURCE-CLOSED |
| E182 | E117 | E117-B | 4+ turns after `veteran_patronage` | YES | SOURCE-CLOSED |
| E183 | E118 | E118-B | 5+ turns after `estate_exception` | YES | SOURCE-CLOSED |
| E184 | UNRESOLVED | UNRESOLVED | secret evidence route, 4+ turns | YES | BLOCKED — source identity open |
| E185 | E17 | E17-A | `cheap_weapons` + later military crisis | YES, including delayed-loss identity | CONDITIONAL |
| E242 | E118 | E118-B | 6+ turns after noble exception | YES | SOURCE-CLOSED |
| E243 | E18 | E18-B | 5+ turns after public bridge choice | YES | SOURCE-CLOSED |
| E244 | E09 | E09-B | 5+ turns after flexible accounts | YES | SOURCE-CLOSED |
| E245 | UNRESOLVED | UNRESOLVED | compensation route, 6+ turns | YES | BLOCKED — source identity open |
| E246 | E160 | E160-A | 5+ turns after `winter_rent_ceiling` if that is the canonical price-ceiling vocabulary | YES | CONDITIONAL |

## 2. Important distinction: event ID is not callback ID

A delayed event such as E181 must not be scheduled merely because E45-B was seen. The runtime identity must distinguish at least:

`runId + sourceEventId + sourceChoiceId + consequenceId`

The event ID (`E181`) identifies the authored resolution node. It is not by itself a unique scheduled instance. Two separate runs may legitimately encounter E45-B and therefore create two distinct run-local callback instances.

Within one run, a callback instance must not be duplicated by save/load or repeated evaluation of the same source choice.

## 3. Exactly-once invariant

For source-closed callbacks, the minimum invariant is:

`one qualifying source choice -> zero or one scheduled callback instance -> zero or one resolution`

A callback may remain pending across turns and saves, but loading a save must restore the same identity rather than schedule a second instance.

A resolution must be idempotent with respect to its callback identity. A second attempt using the same identity must be rejected/no-op rather than applying the consequence twice.

## 4. Timing semantics

The authored `N+ turns` language is a **minimum eligibility boundary**, not a promise that resolution occurs at exactly `sourceTurn + N`.

Required runtime representation:

- `sourceTurn`
- `earliestTurn = sourceTurn + N`
- resolution eligibility predicate
- deterministic ordering key for multiple eligible callbacks

Therefore E181/E183/E242/E243/E244/E246 must not be implemented as a generic “fire after N turns” timer detached from eligibility.

E185 is more complex: its later military crisis is an additional eligibility condition, so a timer alone is insufficient.

## 5. Cancellation / supersession matrix

| Callback family | Can later state invalidate the callback? | Required contract decision |
|---|---|---|
| E181 toll concession | Potentially | distinguish still-valid concession from explicitly superseded policy |
| E182 veteran patronage | Potentially | preserve source-choice identity even if later veteran policy changes |
| E183 estate exception | Potentially | later law cannot silently erase provenance; define whether callback resolves or is superseded |
| E184 secret evidence | Unknown | blocked until source identity is closed |
| E185 cheap weapons | Yes, materially | later crisis must be identified; resolved/replaced armaments may prevent or alter delayed loss |
| E242 noble exception | Potentially | separate instance from E183; repeated exceptions cannot collapse identities |
| E243 public bridge | Potentially | preserve original investment/concession provenance |
| E244 flexible accounts | Potentially | preserve original accounting-policy choice |
| E245 compensation | Unknown | blocked until canonical compensation source is selected |
| E246 winter rent ceiling | Potentially | define whether later policy reversal supersedes or merely changes resolution context |

**No cancellation behavior is promoted to runtime truth yet.** This table records the required decisions and prevents accidental default semantics.

## 6. Save/load contract

Pending callbacks are run-local state. A save/load cycle must preserve:

- callback identity;
- source provenance;
- earliest eligible turn;
- current pending/resolved/cancelled/superseded status;
- any required resolution ordering key.

Save/load must never recreate a callback from the source flag alone if that callback instance already exists.

## 7. Replay boundary

Delayed callbacks are not `meta.*` state. A fresh run starts with no pending callbacks from a previous run.

Replay-specific informational nodes such as E247/E248 belong to S11 and must not be used as an implicit delayed-callback persistence mechanism.

## 8. E184 and E245 blocking rules

### E184
The source catalog says “secret evidence route” but the current canonical QA record has no safe producer/choice identity. No event or choice is invented here. E184 remains **BLOCKED** for executable scheduling.

### E245
The callback says “compensation route”, but the canonical QA record explicitly distinguishes `border_compensation` (E125-A) from `requisition_compensation` (E156-A). They cannot be silently unioned. E245 remains **BLOCKED** until an authored qualification rule identifies the source.

## 9. E246 vocabulary rule

E160-A explicitly produces `winter_rent_ceiling`. E246 says “price ceiling” in prose. Until canonical vocabulary says these are identical, the runtime must not introduce a generic `price_ceiling` alias.

## 10. Gate result

Closed at static contract level:
- exact authored source choices for 7 of 10 delayed callbacks;
- run-local identity requirement;
- exactly-once invariant;
- minimum-delay semantics;
- save/load and replay boundary rules;
- explicit blockers for E184/E245;
- explicit vocabulary blocker for E246.

Still open:
- actual runtime schema implementation;
- deterministic callback ordering;
- concrete cancellation/supersession policies;
- callback state persistence implementation;
- E184 producer closure;
- E245 source closure;
- E246 vocabulary closure;
- E185 later-crisis identity and delayed-loss resolution semantics.

**S10: 72% / IN PROGRESS.**

Global Scenario QA remains **65%**. This is static contract progress only; no runtime readiness is claimed.

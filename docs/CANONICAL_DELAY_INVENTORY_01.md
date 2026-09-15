# Choice Kingdom — Canonical Delayed Consequence Inventory 01

Status: **QA EXTRACTION — NOT ENGINE IMPLEMENTATION**
Scope: known delayed-consequence callbacks in E01–E272.

## Purpose

Convert the existing narrative QA finding into an explicit extraction checklist. This inventory does not invent runtime values where the authored catalog has not yet supplied them.

## Required identity for each callback

Each row must eventually resolve to:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`

## Known callback families requiring extraction

| Source area | Known delayed callback | Required canonical extraction | Status |
|---|---|---|---|
| E01–E10 | E01/E02/E03/E05/E06/E07/E08/E09/E10 follow-up effects | exact source choice, due timing, target, invalidation | OPEN |
| E12 | welfare-cut → later winter effect | source choice + winter predicate + exact timing | OPEN |
| E17 | armaments choice → later failure | source choice + failure identity + timing | OPEN |
| E18 | bridge/toll decision → later toll escalation | source choice + transport/economic condition + timing | OPEN |
| E21 | evidence destruction → later investigation effect | source choice + investigation target + timing | OPEN |
| E22 | festival → later assassination risk | source choice + crisis/assassination resolution + timing | OPEN |
| E23 | ledger choice → later inquiry/legitimacy effect | source choice + target + timing | OPEN |
| E27 | decoy/scandal → delayed branch | source choice + target + cancellation | OPEN |
| E29–E30 | winter/granary and warehouse consequences | exact severity/state identity + timing | OPEN |
| E31–E32 | war/emergency consequences | exact current source choice + crisis resolution/timing | OPEN |
| E39 | credit/bond choice → later leverage/repayment | source choice + economic target + due rule | OPEN |
| E40 | relief governance → later distribution effect | source choice + current-state condition + timing | OPEN |
| E41–E43 | customs/witness/ledger network callbacks | independent source identity + target + timing | OPEN |
| E44–E48 | house/military/emergency callbacks | exact source choice + invalidation | OPEN |
| E51–E60 | constitutional/endgame delayed consequences | exact source choice + endgame resolution condition | OPEN |
| E071/E076/E082/E085/E086/E087/E092/E093 | documented delayed callbacks | source-choice identity, due turn, cancellation, exactly-once | OPEN |
| E181–E185 | 5+ turn / veteran patronage / estate exception / secret evidence / cheap weapons callbacks | exact timing window + resolution predicate + supersession | OPEN |
| E192 | food logistics unstable/stabilized path | current-state derivation + invalidation after stabilization | OPEN |
| E194 | guild logistics cooperation / immunity-risk consequence | cooperation qualification + unresolved-risk cancellation | OPEN |
| E218/E225 | food-pressure consequences | explicit food-pressure producer/severity + timing | OPEN |
| E242–E246 | long-delay callbacks (6+/5+ turns) | exact relative turn semantics + exactly-once | OPEN |
| E248 | replay callback / forgotten favor | `meta.*` identity + replay isolation + exact trigger | OPEN |
| E251–E272 | late crisis consequences | explicit crisis predicates and resolution lifecycle | PARTIAL |

## Canonical scope reconciliation

Historical references to **E33–E35 are intentionally excluded from this runtime-oriented inventory**. The current canonical boundary does not admit those IDs as production source events. Their historical presence is retained only by the dedicated reconciliation record `docs/CANONICAL_DELAY_SCOPE_RECONCILIATION_02.md`. They must not enter engine data, save-state identity, exactly-once keys, or replay metadata unless explicitly reintroduced into the authoritative catalog.

## Hard QA rules

1. “Later”, “5+ turns”, or “during a crisis” is not executable timing until normalized.
2. A delayed callback must identify the exact source choice, not merely the source event.
3. Resolution must be idempotent through an exactly-once key.
4. Cancellation must be observable state, not silent deletion.
5. Save/load must preserve pending delays.
6. Replay must not inherit pending delays from a prior run unless explicitly designed as profile metadata.
7. A delayed callback cannot manufacture the predicate that caused it to become eligible.
8. Historical/draft source IDs must never enter production runtime identity without explicit canonical reintroduction.

## Current blocker

The catalog must be re-read event-by-event for the affected ranges before these rows can be promoted from `OPEN` to `CLOSED`. No guessed due turns or targets are permitted.

## Gate

After extraction is complete, this inventory becomes an input to the production delay schema and validator. Until then, the Decision Engine remains blocked by the canonical contract gate.

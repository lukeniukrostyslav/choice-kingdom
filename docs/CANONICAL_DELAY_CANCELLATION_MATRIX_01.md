# Choice Kingdom — Canonical Delay Cancellation / Supersession Matrix 01

Status: **QA EXTRACTION — BOUNDARY AUDIT**  
Scope: high-risk delayed consumers E181–E185 and E242–E246.  
This document records only source-backed identity and explicitly known gaps. It does not invent runtime cancellation, due turns, persistence, or resolution semantics.

## Contract

A delayed consequence is not production-ready until its canonical row can resolve:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersessionRule`

The matrix deliberately separates **source identity closure** from **runtime lifecycle closure**.

| Consumer | Source identity | Timing evidence | Cancellation / supersession | Exactly-once | Status |
|---|---|---|---|---|---|
| E181 | E45-B | Authored: `5+ turns after a toll concession` | Not canonically extracted | Not canonically extracted | PARTIAL — identity closed, lifecycle open |
| E182 | E117-B / `veteran_patronage` | Authored: `4+ turns later` | Not canonically extracted | Not canonically extracted | PARTIAL — identity closed, lifecycle open |
| E183 | E118-B / `estate_exception` | Authored: `5+ turns later` | Not canonically extracted | Not canonically extracted | PARTIAL — identity closed, lifecycle open |
| E184 | No safe canonical producer alias | Authored: `4+ turns later` / secret evidence route | Producer itself unresolved | Not canonically extracted | OPEN |
| E185 | E17-A / `cheap_weapons` plus later military crisis | Delayed severe-loss branch is authored; exact executable timing not normalized | A prevents later failure; B schedules severe delayed loss; supersession identity unresolved | Not canonically extracted | PARTIAL / OPEN |
| E242 | E118-B candidate | Long-delay callback; exact runtime scheduling open | Trigger says any prior noble exception; selection/lifecycle unresolved | Not canonically extracted | PARTIAL / OPEN |
| E243 | E18-B / `public_bridge` | Authored: `5+ turns later` | Not canonically extracted | Not canonically extracted | PARTIAL — identity closed, lifecycle open |
| E244 | E09-B / `flexible_accounts` | Authored: `5+ turns later` | Not canonically extracted | Not canonically extracted | PARTIAL — identity closed, lifecycle open |
| E245 | E20-A / `soldier_compensation` | Authored: `6+ turns later` | Absolute cancellation/supersession semantics unresolved | Not canonically extracted | PARTIAL — identity closed, lifecycle open |
| E246 | E160-A / `winter_rent_ceiling` | Authored relative timing; runtime scheduler open | Not canonically extracted | Not canonically extracted | PARTIAL — identity closed, lifecycle open |

## Hard negatives

1. No absolute due turn is inferred from relative prose.
2. A consumer cannot manufacture the prerequisite that makes itself eligible.
3. E245 cannot silently union E20/E125/E156 as interchangeable source families without an authored rule.
4. A cancellation rule cannot be inferred merely because a later state appears to make an outcome unlikely.
5. Replay/meta-state is not a cancellation mechanism unless the authored contract explicitly promotes it.
6. E273–E277 are excluded from production semantics.

## Promotion gate

A row may be promoted from this matrix to an executable production delay schema only after the authoritative catalog supplies the missing consequence identity, target, lifecycle rule, and exactly-once semantics. Source identity closure alone is insufficient.

## Current conclusion

The audit closes no new runtime lifecycle gate. The useful result is a bounded, machine-oriented list of what is known versus still absent, preventing accidental promotion of narrative timing into executable scheduling.

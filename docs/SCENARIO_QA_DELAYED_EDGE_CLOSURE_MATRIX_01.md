# Choice Kingdom — Scenario QA Delayed Edge Closure Matrix 01

Status: **SOURCE-LEVEL QA — DELAYED EDGE CLOSURE GATE**  
Scope: E181–E185 and E242–E246.  
Date: 2026-09-15.

## Purpose

Turn producer→graph reconciliation findings into a bounded closure matrix. This document does not invent missing scheduler semantics. It distinguishes source identity, exact source-choice evidence, graph/context evidence, authored timing, and remaining executable contract fields.

## Required executable tuple

A delayed callback is not production-closed until all of the following are known:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule + graph relation + reachability evidence`

## Matrix

| Consumer | Source producer | Exact source choice | Authored timing | Graph/context evidence | Remaining blocker | Status |
|---|---|---|---|---|---|---|
| E181 | E45-B | **CLOSED: E45-B `Grant long-term concession`** | `5+ turns after a toll concession` | E126/E130/E181 contextual route | scheduler anchor, consequence/callback key, cancellation, resolution contract, reachability | **SOURCE-CLOSED / RUNTIME OPEN** |
| E182 | E117-B | CLOSED | `4+ turns later` | E117→E182 | scheduler anchor, exactly-once, cancellation, reachability | OPEN |
| E183 | E118-B | CLOSED | `5+ turns later` | E118→E183 | scheduler anchor, exactly-once, cancellation, reachability | OPEN |
| E184 | none safely identified | OPEN | `4+ turns later` | E184→E234/E244 context | authoritative producer identity | OPEN |
| E185 | E17-A | CLOSED / consumer lifecycle partial | later military crisis | E128→E185→E253 | crisis resolution, supersession/cancellation, exactly-once, reachability | PARTIAL |
| E242 | E118-B candidate | PARTIAL | `5+ turns later` / authored broad noble-exception wording | E118→E242 and E127/E160 contextual routes | exact source-choice selection for “any prior noble exception”, lifecycle | PARTIAL |
| E243 | E18-B | **CLOSED: E18-B `Keep the bridge public`** | `5+ turns later` | E126/E129/E181 family; E224→E243 | exact source-choice binding is now source-supported; scheduler, lifecycle, reachability | OPEN |
| E244 | E09-B | CLOSED | `5+ turns later` | E184→E244; E216/E258 downstream | exact source-choice binding, scheduler, lifecycle, reachability | OPEN |
| E245 | E20-A | CLOSED | `6+ turns later` | E117/E156/E222→E245 context | preserve E20-A exclusively, scheduler, cancellation, reachability | OPEN |
| E246 | E160-A | CLOSED | relative delay | E140→E246 and E245→E246 context | exact timing, scheduler, cancellation, reachability | OPEN |

## Reconciliation decisions

1. A contextual graph edge is retained as design evidence only; it is not upgraded to a producer edge unless the authored source establishes that relation.
2. `E245` remains sourced to **E20-A**. E125-A and E156-A remain distinct compensation facts.
3. `E242` remains PARTIAL because “any prior noble exception” is broader than the currently identified E118-B source.
4. `E184` remains OPEN; no producer alias is invented from the downstream E184→E244 relationship.
5. E181 is now source-choice closed to **E45-B**, because the authoritative E45 catalog explicitly contains the long-term bridge concession and the E181 timing explicitly refers to a toll concession.
6. E243 remains distinct: E18-A grants a toll, while E18-B keeps the bridge public and explicitly establishes `public_bridge`; the existing E243 producer is E18-B.
7. Relative timing remains authored evidence, not an executable due-turn calculation.
8. E33/E34 remain quarantined and are excluded from all closure decisions.
9. No delayed callback is allowed to manufacture the predicate that makes it eligible.

## Next closure gate

Continue event-by-event extraction for E182–E185 and E242–E246. Only fields directly supported by the authoritative catalogs may be promoted. After extraction, resulting rows can be checked against the causal graph and fresh-run reachability candidates.

**No Decision Engine promotion is authorized by this matrix.**

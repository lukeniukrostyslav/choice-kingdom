# Choice Kingdom — Scenario QA Delayed Edge Closure Matrix 01

Status: **SOURCE-LEVEL QA — DELAYED EDGE CLOSURE GATE**  
Scope: E181–E185 and E242–E246.  
Date: 2026-09-15.

## Purpose

Turn the current producer→graph reconciliation findings into a bounded closure matrix. This document does not invent missing scheduler semantics. It distinguishes source identity, graph/context evidence, authored timing, and the remaining executable contract fields.

## Required executable tuple

A delayed callback is not production-closed until all of the following are known:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule + graph relation + reachability evidence`

## Matrix

| Consumer | Source producer | Source identity | Authored timing | Graph/context evidence | Remaining blocker | Status |
|---|---|---|---|---|---|---|
| E181 | E45-B | CLOSED | `5+ turns after a toll concession` | E126/E130/E181 contextual route | scheduler anchor, exact callback key, cancellation, reachability | OPEN |
| E182 | E117-B | CLOSED | `4+ turns later` | E117→E182 | scheduler anchor, exactly-once, cancellation, reachability | OPEN |
| E183 | E118-B | CLOSED | `5+ turns later` | E118→E183 | scheduler anchor, exactly-once, cancellation, reachability | OPEN |
| E184 | none safely identified | OPEN | `4+ turns later` | E184→E234/E244 context | authoritative producer identity | OPEN |
| E185 | E17-A | CLOSED / consumer lifecycle partial | later military crisis | E128→E185→E253 | crisis resolution, supersession/cancellation, exactly-once, reachability | PARTIAL |
| E242 | E118-B candidate | PARTIAL | `5+ turns later` / authored broad noble-exception wording | E118→E242 and E127/E160 contextual routes | exact source-choice selection for “any prior noble exception”, lifecycle | PARTIAL |
| E243 | E18-B | CLOSED | `5+ turns later` | E126/E129/E181 family; E224→E243 | exact source-choice binding, scheduler, lifecycle, reachability | OPEN |
| E244 | E09-B | CLOSED | `5+ turns later` | E184→E244; E216/E258 downstream | exact source-choice binding, scheduler, lifecycle, reachability | OPEN |
| E245 | E20-A | CLOSED | `6+ turns later` | E117/E156/E222→E245 context | preserve E20-A exclusively, scheduler, cancellation, reachability | OPEN |
| E246 | E160-A | CLOSED | relative delay | E140→E246 and E245→E246 context | exact timing, scheduler, cancellation, reachability | OPEN |

## Reconciliation decisions

1. A contextual graph edge is retained as design evidence only; it is not upgraded to a producer edge unless the authored source establishes that relation.
2. `E245` remains sourced to **E20-A**. E125-A and E156-A remain distinct compensation facts.
3. `E242` remains PARTIAL because “any prior noble exception” is broader than the currently identified E118-B source.
4. `E184` remains OPEN; no producer alias is invented from the downstream E184→E244 relationship.
5. Relative timing remains authored evidence, not an executable due-turn calculation.
6. E33/E34 remain quarantined and are excluded from all closure decisions.
7. No delayed callback is allowed to manufacture the predicate that makes it eligible.

## Next closure gate

The next safe scenario task is event-by-event extraction of the affected source choices and explicit callback targets. Only fields directly supported by the authoritative catalogs may be promoted. After extraction, the resulting rows can be checked against the causal graph and fresh-run reachability candidates.

**No Decision Engine promotion is authorized by this matrix.**

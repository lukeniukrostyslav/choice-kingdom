# Choice Kingdom — S12.22 Delayed Source Closure

Status: **QA SOURCE CLOSURE — NOT ENGINE IMPLEMENTATION**
Scope: authored delayed callbacks E181–E185 and E242–E246.

## Purpose

Reconcile the latest delayed-consequence inventory against authoritative catalog wording without inventing timing, source identity, or cancellation semantics.

## Closed source mappings

| Consumer | Authored source identity | Timing | Canonical status |
|---|---|---|---|
| E181 | toll concession | 5+ turns after concession | SOURCE-CLOSED; exact producer choice still requires catalog extraction |
| E182 | `veteran_patronage` | 4+ turns later | SOURCE-CLOSED |
| E183 | `estate_exception` | 5+ turns later | SOURCE-CLOSED |
| E184 | secret evidence route | 4+ turns later | SOURCE-CLOSED; producer remains OPEN |
| E185 | `cheap_weapons` | later military crisis | SOURCE-CLOSED; resolution timing remains OPEN |
| E242 | noble exception | 6+ turns later | SOURCE-CLOSED via E118-B candidate |
| E243 | `public_bridge` | 5+ turns later | SOURCE-CLOSED via E18-B |
| E244 | `flexible_accounts` | 5+ turns later | SOURCE-CLOSED via E09-B |
| E245 | compensation route | 6+ turns later | SOURCE-CLOSED as two distinct candidates: E125-A / E156-A |
| E246 | price ceiling | 5+ turns later | SOURCE-CLOSED at consumer wording; producer identity remains OPEN |

## Hard boundaries

1. A timing phrase such as `5+ turns later` is an authored constraint, not yet a runtime scheduling algorithm.
2. E245 candidates E125-A and E156-A must not be merged until the catalog proves a common canonical producer.
3. E184 remains open because the exact secret-evidence producer is not yet source-closed.
4. E246 remains open at producer level because no authoritative `price_ceiling` producer has been recovered in the inspected source.
5. E185 cannot be promoted to a deterministic delayed schedule until the later military-crisis resolution target and cancellation/supersession behavior are extracted.
6. No callback may manufacture the predicate that made it eligible.

## Exactly-once contract

All rows require the eventual runtime identity:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersession rule`

This document closes source-language identity only where evidence is present. It does **not** invent missing exactly-once keys or cancellation rules.

## Acceptance

PASS: source wording reconciled for E181–E185 and E242–E246.
PARTIAL: executable delay identity, cancellation/supersession, and remaining producer closure.

Next QA: expand the same source-first reconciliation to the remaining E01–E180 delayed families, then reconcile ending incoming paths and fresh-run reachability.

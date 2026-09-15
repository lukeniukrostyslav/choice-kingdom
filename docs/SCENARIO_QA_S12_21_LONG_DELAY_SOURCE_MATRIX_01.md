# Choice Kingdom — S12.21 Long-Delay Source Matrix 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — LONG-DELAY RECONCILIATION
Scope: E242–E246, frozen production E01–E272

## Purpose

Reconcile the five late long-delay consumers against their authored source families without inventing timing, source choices, or cancellation semantics.

## Matrix

| Consumer | Authored trigger | Source identity status | Timing status | Resolution status | QA decision |
|---|---|---|---|---|---|
| E242 Renewed Exception | prior noble exception, 6+ turns later | **CLOSED candidate:** E118-B `estate_exception` | **PARTIAL:** authored `6+ turns`; exact executable earliest/latest window still open | OPEN | May bind only to E118-B once exact delay contract is normalized; no generic noble-history alias |
| E243 Old Bridge | public bridge investment, 5+ turns later | **CLOSED:** E18-B `public_bridge` | **PARTIAL:** authored `5+ turns`; exact executable window still open | OPEN | Source identity is fixed; preserve sourceChoiceId and do not substitute another bridge-like event |
| E244 Audit Comes Due | flexible accounts, 5+ turns later | **CLOSED:** E09-B `flexible_accounts` | **PARTIAL:** authored `5+ turns`; exact executable window still open | OPEN | Source identity is fixed; callback cannot be satisfied by generic audit history |
| E245 Soldier's Son Returns | compensation route, 6+ turns later | **OPEN:** E125-A `border_compensation` and E156-A `requisition_compensation` remain distinct authored candidates | **PARTIAL:** authored `6+ turns` | OPEN | Do not merge the two routes. Runtime source identity must remain explicit until authoritative catalog disambiguates whether one or both routes qualify |
| E246 Price Ceiling Memory | price ceiling, 5+ turns later | **OPEN:** exact canonical producer/choice not yet closed | **PARTIAL:** authored `5+ turns` | OPEN | No guessed producer or alias. `price_ceiling` must be normalized from exact authored source before promotion |

## Hard invariants

1. `sourceEventId + sourceChoiceId` is mandatory for every delayed callback.
2. Relative prose such as `5+ turns` / `6+ turns` is authored evidence, but is not by itself a complete machine timing contract.
3. E245's two compensation routes remain separate until exact source semantics are resolved.
4. E246 cannot use generic price-control vocabulary as a substitute for an exact authored producer.
5. No delayed consumer may manufacture its own prerequisite.
6. Exactly-once identity, cancellation/supersession and save/load persistence remain required before runtime promotion.
7. E273–E277 are excluded from this production matrix.

## Acceptance

Source identity is closed for E242–E244. E245 remains deliberately multi-candidate and E246 remains open. Timing and lifecycle are not falsely marked executable merely because the prose contains relative-turn language.

## Next gate

Resolve E245 route semantics and recover the exact E246 price-ceiling producer, then extract executable timing and cancellation rules for E242–E246 before they enter the production delay schema.

# Choice Kingdom — Producer / Consumer Audit E251–E272

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — EXACT AUTHORED OUTPUTS RECORDED; PRODUCTION SCHEMA BLOCKED**

## Purpose

Audit the final authored range E251–E272 for concrete durable outputs, consumer prerequisites, lifecycle boundaries, delayed/replay identity and producer/consumer correctness. This is not a runtime reachability claim.

## E251–E260

- **E251 — The Frozen Treasury Road**: winter + low transport. Choices are resource/trust/power effects only; no explicit durable flag is authored. Open question: `low transport` needs a canonical derived predicate and an upstream active transport-disruption producer.
- **E252 — The Hospital Bell**: illness + Amara route. Resource/trust/power effects only. `illness` and `Amara route` require canonical predicates.
- **E253 — The Border Fire**: consumes active `border crisis`; no producer output. Correct consumer-only role.
- **E254 — The Grain Warehouse Vote**: food crisis + local governance. Resource/trust/power effects only; both trigger families require canonical derived predicates.
- **E255 — The Three-Crisis Budget**: simultaneous food, border and civic pressure. Resource/trust/power effects only; requires an explicit multi-crisis predicate contract and must consume, not manufacture, border crisis.
- **E256 — The Bad Successor**: succession route. Resource/trust/power effects only; succession route requires canonical ending/replay-safe route identity.
- **E257 — The Emergency Clock**: emergency powers. Resource/trust effects only; must consume the canonical emergency-power state and cannot silently create it.
- **E258 — The Independent Purse**: budget reform. Resource/trust/power effects only; `budget reform` remains an unresolved canonical producer/derived predicate.
- **E259 — The Military Appeal**: army constitutional route. Resource/trust effects only; route must be tied to canonical military-constitutional history/thread.
- **E260 — The Public Archive Law**: archive reform. Resource/trust/power effects only; `archive reform` requires canonical producer mapping.

## E261–E270

- **E261 — The Four-Way Bargain**: >=4 faction routes. A produces `four_way_bargain`; B produces `two_faction_bargain`. The four faction route identities require canonical thread/predicate definitions.
- **E262 — The Fifth Voice**: consumes `four_way_bargain`; choices have resource effects only. No durable marker is authored.
- **E263 — The Coalition Audit**: coalition route. Resource/trust/power effects only; `coalition route` must be canonical and distinguishable from `pred.coalition_cooperation`.
- **E264 — The Coalition Breaks**: low coalition trust. Resource/trust/power effects only; requires explicit coalition trust calculation and collapse/invalidation semantics.
- **E265 — The Coalition Holds**: high coalition trust. Resource/trust effects only; requires the same canonical coalition trust contract as E264, with mutually exclusive qualification.
- **E266 — Mara's Last Report**: Mara active. Resource/relationship effects only; route identity must be canonical.
- **E267 — Rowan's Last Order**: Rowan active. Resource/trust effects only; must remain distinct from E204/E227 military constitutional commitments.
- **E268 — Seris's Last Bargain**: Seris active. Resource/relationship effects only; must consume established property-rights/house route rather than restate it.
- **E269 — Ivo's Late Account**: late commercial evidence node; no new durable flag. Explicitly distinct from E55. Its downstream evidence contribution must be represented as an authored source identity if later qualification depends on this handoff.
- **E270 — Amara and Toma at Dawn**: A produces `dual_witness_account`; B produces `single_witness_account`. This is a distinct convergence choice and must not be treated as equivalent to E207's broader systemic evidence convergence.

## E271–E272 border lifecycle

### E271 — The Border Council Alarm
E271-A is the canonical producer of active border crisis:
- `border_crisis_declared = true`
- `border_crisis_resolved = false`
- `thread.border_crisis = active`
- `pred.border_crisis` becomes eligible.

E271-B explicitly resolves the warning without declaration and must not satisfy `pred.border_crisis`.

### E272 — The Border Crisis Accord
E272 is the canonical active-crisis resolution producer. Both A and B preserve the historical declaration and set the crisis thread to a resolved state while clearing the active predicate. A creates `history.border_crisis_resolved_diplomatically`; B creates `history.border_crisis_resolved_by_guarantee`.

The lifecycle is therefore:

`warning → E271-A declaration → active crisis → E272-A/B resolution`

and must not be shortcut by E195/E253/E255. This distinction is explicitly authored in the source. fileciteturn310file0L2-L2

## Main blockers discovered

1. `low transport` / active transport disruption still lacks a distinct canonical producer.
2. `illness`, food crisis/pressure/severity, local governance and civic pressure need frozen derived predicates.
3. `budget reform`, `archive reform`, succession route and army-constitutional route need canonical route identities.
4. Four faction routes and coalition trust require explicit machine-readable formulas and invalidation semantics.
5. E269 has no durable flag by design, but its late evidence handoff needs explicit source identity if consumed by later qualification.
6. E270 must remain a distinct evidence-convergence artifact from E207.
7. E271/E272 lifecycle is source-level closed but runtime graph integration remains unverified.

## Gate

E251–E272 authored output audit: **SOURCE-LEVEL PASS**.

Production schema: **BLOCKED** by unresolved canonical predicates/contracts.

Runtime reachability: **NOT VERIFIED**.

Validator: intentionally **NOT BUILT** until contract freeze.

# Choice Kingdom — E211–E270 Trigger Normalization Audit 01

Status: SOURCE-LEVEL QA / PRE-SCHEMA

Scope: every trigger family visible in the E211–E270 authored expansion. This pass does not silently invent engine predicates; it separates already-known canonical concepts from prose/alias triggers that must be normalized before schema freeze.

## A. Triggers that already map cleanly to frozen domains

| Authored trigger | Canonical treatment | Status |
|---|---|---|
| low gold | `pred.gold_low` | canonical concept |
| food pressure | derived food-pressure predicate; never a sixth resource | needs exact formula/marker |
| strong market oversight | derived market-oversight predicate | needs producer closure |
| winter | campaign/durable winter thread | needs exact lifecycle contract |
| border crisis | `pred.border_crisis` | canonical after E271-A; active lifecycle resolved by E272-A/B |
| succession route | succession-route thread/marker | needs exact canonical name |
| army constitutional route | military constitutional thread | canonical domain, exact producer inventory still required |
| budget reform | `pred.budget_reform` or canonical institutional reform route | alias needs normalization |
| archive reform | archive/information institutional route | exact canonical producer required |
| coalition route | `thread.coalition` / `pred.coalition_cooperation` depending on consumer | must not conflate route existence with cooperation qualification |
| high coalition trust | derived coalition durability predicate | exact formula required |
| low coalition trust | derived coalition instability predicate | exact formula required |
| four faction routes | route-count condition only | cannot substitute for `pred.coalition_cooperation` |
| Amara route | `thread.amara_civic` | canonical domain |
| Toma route | `thread.toma_information` | canonical domain |
| guild logistics route | `thread.ivo_market` plus guild-logistics qualification | route alone is insufficient for `pred.guild_logistics_cooperation` |
| border route | border thread | route alone is insufficient for `pred.border_crisis` |

## B. Prose/alias triggers requiring canonical replacement

### Public institutions
- `full_crown_audit_published` — must map to the canonical audit-publication history marker.
- `tax_transparency` — must map to an explicit institutional/public-accountability marker.
- `clerks_oath_public` — must map to a durable clerical-law marker; do not infer it from generic trust.
- `regional_courts` — must map to a canonical courts/institutional route marker.
- `institutional reform` — prose alias; must resolve to the frozen institutional reform predicate/markers.
- `law_notices_public` — must map to a canonical public-law-information marker.

### Economic/social pressure
- `high reform spending` — derived from actual resource/economic state; must not become a hidden resource.
- `trade_risk_insurance` — must have a concrete producer and lifecycle if it remains a trigger.
- `winter_rent_ceiling` — must have an explicit producer; cannot be inferred from generic winter.
- `high civic trust` — must use the canonical trust resource threshold/derived predicate, not a second trust variable.
- `veteran route` — must map to a durable military/veteran route marker.
- `river compact` — must map to a concrete civic/infrastructure marker.
- `severe food pressure` — derived condition; exact threshold/producer contract required.
- `illness` — must map to a canonical health/relief pressure marker if retained.
- `local governance` — must map to a durable civic/local-government marker.

### Character pressure
- `Mara active` — must map to Mara route/thread state, not simply relationship >= 0.
- `Rowan active` — must map to Rowan route/thread state.
- `Seris active` — must map to Seris route/thread state.
- `Ivo active` — must map to Ivo/guild route state.
- `Amara and Toma both active` — composite route predicate; exact canonical conjunction required.
- `repeated executive overrides` — needs a durable counter/history marker with exact increment semantics.
- `Mara <= -1` — relationship threshold is valid only if this event is intentionally relationship-driven; do not substitute it for route qualification.
- `Ivo >= 1` — same rule: relationship threshold does not equal guild institutional qualification.
- `Amara >= 1` — same rule: relationship threshold does not equal civic institutional qualification.

### Investigation network
- `at least two procurement clues` — must become an explicit evidence-set predicate with stable evidence IDs.
- `forgery route` — must map to `royal_forgery_proven` / canonical forgery evidence route.
- `payment_date_crosscheck` — requires an exact producer and stable evidence marker.
- `witness route` — must map to a canonical witness/evidence route.
- `at least three related clues` — must not substitute for the frozen systemic-evidence contract.

### Faction credibility
- `public accountability route` — map to civic/accountability route marker.
- `noble constitutional route` — map to House/constitutional route marker.
- `guild logistics route` — route marker only; not proof of guild influence or cooperation by itself.
- `border route` — route marker only; not proof of active border crisis.

### Replay/delayed callbacks
- `replay callback` — must be under `meta.*` replay state and never mutate first-run state implicitly.
- `second-run information route` — must use explicit replay metadata plus the information route.
- `archive route` — must map to canonical information/archive route.
- `5+ turns later` / `6+ turns later` — narrative timing must become explicit delayed-effect/event-window contracts, not free-form prose.

## C. P0 semantic rules confirmed

1. A relationship threshold is not an institutional qualification.
2. A route name is not automatically a predicate producer.
3. A clue count is not systemic explanation verification.
4. Four faction routes are not coalition cooperation.
5. Border tension/warning is not an active border crisis.
6. Contextual food/winter/transport pressure is not a sixth numeric resource.
7. Replay triggers must remain isolated under `meta.*`.
8. Delayed callbacks require stable source choice, consequence identity, turn bounds, exactly-once semantics and cancellation/supersession rules.

## D. Next normalization gate

Before production schema generation, every E211–E270 trigger must be converted to exactly one of:

- canonical resource threshold;
- canonical relationship threshold;
- canonical flag/history marker;
- canonical thread state;
- canonical derived predicate with frozen formula;
- explicit delayed-event window;
- explicit replay `meta.*` predicate;
- explicit conjunction/disjunction of the above.

No prose trigger may survive into production data contracts.

Runtime implementation remains 0%; this audit is source-level only.

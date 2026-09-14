# Choice Kingdom — Derived Predicate Contract 01

Status: DESIGN / QA — NOT ENGINE RUNTIME
Scope: E01–E270

The authored catalog uses human-readable trigger phrases. Before runtime integration, these phrases must resolve to deterministic predicates over canonical state, history, relationships, threads, and replay metadata.

## Rules

1. A predicate must have one stable ID.
2. A predicate must define exact inputs and thresholds.
3. A predicate must be deterministic for the same state/history/seed.
4. A predicate must not silently create durable state.
5. A durable fact belongs in `flag.*`, `history.*`, `thread.*`, or `meta.*`; a computed condition belongs here.
6. Predicate definitions must be versioned with the production catalog.

## Initial canonical predicates

### Resources

- `pred.trust_high`: `resource.trust >= 6`
- `pred.security_low`: `resource.security <= 3`
- `pred.gold_low`: `resource.gold <= 5`
- `pred.power_high`: `resource.power >= 6`
- `pred.reputation_high`: `resource.reputation >= 6`

Thresholds are provisional design values and must be balance-tested before engine lock.

### Food / winter

Food-pressure language must not become a new hidden resource. Until a separate food system is intentionally designed, derive pressure from canonical history/flags and current resources.

- `pred.food_shortage`: requires an explicit authored food-crisis marker OR the canonical food-pressure history/thread contract once defined.
- `pred.severe_food_pressure`: requires `pred.food_shortage` plus the authored severity marker/condition.
- `pred.severe_winter`: requires an explicit winter-severity marker; do not infer it from prose alone.

**Open QA:** identify every food/winter producer in E01–E270 and map it to one of these deterministic definitions.

### Border / security

- `pred.border_tension`: requires an explicit border-crisis history/thread marker OR a canonical derived formula approved by balance QA.
- `pred.low_army_readiness`: derived only from canonical `resource.security` plus approved military-history markers; exact formula remains a balance gate.
- `pred.strong_security_route`: requires the canonical security-route history/thread definition, not a free-text trigger.

### Economy / guild

- `pred.commercial_route`: true only when the canonical commercial thread/history prerequisites are met.
- `pred.strong_market_oversight`: true only when the canonical audit/market-oversight prerequisites are met.
- `pred.strong_treasury_pressure`: must be derived from canonical `resource.gold` and approved economic history; exact threshold remains a balance gate.

### Information / investigation

- `pred.information_route`: true when at least one approved information route is active.
- `pred.high_information_pressure`: derived from the canonical information thread plus approved evidence/pressure markers.
- `pred.at_least_two_procurement_clues`: count approved `history.*` evidence markers; do not count arbitrary flags by prefix.
- `pred.three_or_more_related_clues`: count only evidence markers belonging to the canonical investigation thread.
- `pred.secret_evidence_route`: true when an approved secret-evidence route is active.

### Constitutional / civic

- `pred.civic_route`: canonical civic thread/history definition.
- `pred.noble_route`: canonical noble thread/history definition.
- `pred.constitutional_reform`: requires the approved constitutional thread marker.
- `pred.simultaneous_crisis`: true only when the canonical food, border, and civic pressure predicates are simultaneously true.

## Non-canonical trigger phrases requiring migration

The following phrases must not be used directly by the future engine until mapped:

`high trust`
`strong treasury pressure`
`food shortage`
`winter severity`
`border tension`
`low security`
`strong market oversight`
`severe winter`
`low army readiness`
`guild labor tension`
`information route`
`high information pressure`
`simultaneous food, border and civic pressure`
`at least two procurement clues`
`three or more related clues`
`Seris >= 0`

## QA requirement

This contract is intentionally not marked runtime-ready. Each predicate needs a producer inventory, boundary-case tests, reachability impact, and balance validation before being promoted into the machine-readable production schema.

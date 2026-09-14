# Choice Kingdom — Canonical State Vocabulary

Status: **DESIGN / QA — NOT ENGINE RUNTIME**
Scope: E01–E270

This document is the normalization contract for narrative QA before decision-engine implementation. It does not make the engine complete.

## 1. State namespaces

| Namespace | Purpose | Persistence |
|---|---|---|
| `resource.*` | Numeric kingdom pressures | current run |
| `rel.*` | Character relationship values | current run |
| `flag.*` | Current durable facts | current run |
| `history.*` | Immutable decision/evidence markers | current run |
| `thread.*` | Active narrative routes | current run |
| `delay.*` | Scheduled consequences | current run + save/load |
| `ending.*` | Ending qualification facts | current run |
| `meta.*` | Intentionally persistent cross-run knowledge | profile |

## 2. Canonical resources

The five primary resources remain:

- `resource.gold`
- `resource.trust`
- `resource.security`
- `resource.power`
- `resource.reputation`

Expansion prose must not silently introduce a sixth resource. Contextual terms such as food pressure, winter severity, border tension, guild leverage and information trust must be represented as either:

1. a documented derived condition with deterministic inputs/formula; or
2. a durable flag/thread/history marker.

Until formulas exist, QA should treat these terms as unresolved normalization findings rather than runtime resources.

## 3. Relationships

Canonical character keys:

- `rel.mara`
- `rel.rowan`
- `rel.seris`
- `rel.ivo`
- `rel.amara`
- `rel.toma`

Relationship gates must use explicit numeric ranges. A trigger such as `Seris >= 0` is legal syntax only if intentionally broad; otherwise it should be replaced by a meaningful threshold.

## 4. Flag rules

Every durable flag must have exactly one semantic definition. Names must describe a fact, not a vague intention.

Examples:

- `flag.audit_office`
- `flag.crown_audited`
- `flag.cheap_weapons`
- `flag.quality_armaments`
- `flag.warehouse_arson`
- `flag.emergency_powers_expire`
- `flag.emergency_powers_inherit`

A flag may have multiple producers only when all producers establish the exact same fact. If two choices use the same name for different meanings, rename them during canonicalization.

## 5. History markers

History records immutable choices/evidence that should not be removed by later state changes.

Examples:

- `history.open_petition_hall`
- `history.emergency_decree_used`
- `history.ledger_public`
- `history.evidence_destroyed`
- `history.cheap_weapons_purchased`

A history marker is not a substitute for a current-state fact when an event must know whether the condition still holds.

## 6. Thread identifiers

Threads represent active narrative routes rather than facts. Suggested canonical families:

- `thread.mara_audit`
- `thread.rowan_security`
- `thread.seris_houses`
- `thread.ivo_market`
- `thread.amara_civic`
- `thread.toma_information`
- `thread.ledger_investigation`
- `thread.winter_crisis`
- `thread.border_crisis`
- `thread.constitutional_endgame`

Threads may activate/deactivate, but a historical decision should remain available through `history.*`.

## 7. Delayed consequences

Every delayed consequence must have a stable identity:

`delay.<source-choice-id>.<consequence-id>`

Required fields in the future machine-readable schema:

- source choice/event;
- earliest turn;
- latest turn or resolution condition;
- target event/effect;
- exactly-once key;
- cancellation/supersession rule;
- save/load persistence.

Prose-only phrases such as “later” or “during a crisis” are not sufficient for runtime data.

## 8. Replay metadata

Cross-run information must use `meta.*` and must never be inferred from arbitrary prior-run save state.

Initial candidates requiring explicit design:

- `meta.information_seen.*`
- `meta.route_discovered.*`
- `meta.ending_seen.*`
- `meta.evidence_reinterpretation.*`

The exact list should be minimized: only information intentionally preserved between runs belongs here.

## 9. Ending qualification

Ending eligibility should be composed from multiple canonical facts/resources rather than one character relationship.

Target endings:

- Steward
- Iron Crown
- Golden Compact
- People's Charter
- Broken Diadem
- Quiet Throne
- Second Founder

Each ending must eventually document at least two recognizable prerequisite configurations where the design promises independent routes.

## 10. Normalization policy

Before engine implementation, static QA must report:

- undefined producers;
- undefined consumers;
- duplicate semantics;
- conflicting semantics;
- impossible prerequisites;
- mutually exclusive locks;
- delayed effects without resolution;
- replay references without `meta.*` definitions;
- contextual resources without formulas;
- ending routes with no viable configuration.

No unresolved vocabulary should be hidden behind fallback behavior in the engine.

# Choice Kingdom — Trigger Normalization Audit 02

Date: 2026-09-14
Scope: verified authored sources E71–E270
Status: **IN PROGRESS — NOT RUNTIME**

## Purpose

Extend the initial trigger audit with source-verified trigger families observed in the E71–E270 expansion. This is an audit artifact, not executable data.

## 1. Relationship shorthand

Observed forms include `Mara >= 1`, `Rowan >= 1`, `Seris >= 0`, `Ivo >= 1`, `Amara >= 1`, and `Toma >= 1`.

Canonical form must use `rel.<character>` and preserve the authored threshold exactly. `Seris >= 0` is intentionally broader than a positive relationship gate and must not be silently rewritten.

## 2. Route shorthand

Observed forms include:
- `institutional reform`
- `document audit route`
- `commercial route`
- `guild leverage`
- `guild labor tension`
- `veteran route`
- `border route`
- `military route`
- `Amara route`
- `Toma route`
- `Seris route`
- `Rowan route`
- `information route`
- `witness route`
- `archive route`
- `coalition route`
- `succession route`
- `budget reform`
- `archive reform`

These cannot remain free-form executable strings. Each must resolve to an explicit `thread.*`, `flag.*`, `history.*`, derived predicate, or boolean expression over those namespaces.

## 3. Contextual pressure families

Observed variants require canonical predicate families:

### Food
`food shortage`, `food-price pressure`, `food pressure`, `severe food pressure`, `food crisis`, and E192's `food stability` effect.

The project has five canonical primary numeric resources. `food stability` must not silently become a sixth numeric resource.

### Winter
`winter`, `winter severity`, `severe winter`, `winter illness`, `winter mortality risk`, and related crisis language.

Define an explicit winter-state/predicate model rather than parsing prose.

### Border/security
`border tension`, `border pressure`, `border escalation`, `border crisis`, `low security`, `low army readiness`, `strong security route`, and `military route`.

These represent related but non-identical concepts and must not be collapsed into one boolean without preserving meaning.

### Market/information
`strong market oversight`, `market tension`, `information route`, `high information pressure`, `low information trust`, `guild leverage`.

Each requires a deterministic source and threshold/thread definition.

### Multi-crisis
`simultaneous food, border and civic pressure`, `at least two unresolved pressures`, and `at least two strong relationships` require explicit conjunction/cardinality rules.

## 4. Delayed wording

Expansion sources contain exact-looking delays such as:
- 3+ turns later
- 4+ turns later
- 5+ turns later
- 6+ turns later

They must compile to exact source-turn + target-turn semantics under the canonical delayed contract. Prose such as `later` or `during a later crisis` needs an explicit resolution window.

## 5. Replay metadata

E131, E186, E247, E248 and related callbacks refer to information from previous runs. These facts must live under versioned `meta.*` state and must never be confused with current-run `flag.*` or `history.*` state.

## 6. Concrete source defects / ambiguities verified

- E25 has ambiguous boolean precedence in the original prose trigger.
- E31 has ambiguous grouping between winter/security and military escalation.
- E212 uses `clerk_discipled`, which should be normalized to the intended spelling before schema lock.
- E214/E216 and several later nodes use `institutional reform`/`low gold + high reform spending` without a fully defined canonical predicate.
- E255 requires a three-way simultaneous pressure predicate that must be derived from canonical food, border and civic pressure states.
- E261 uses `at least four faction routes`; cardinality and qualifying route identities must be explicit.

## 7. Producer/consumer implication

A trigger is considered canonical only when one of these is true:

1. it is a stable flag with a verified producer;
2. it is immutable history with a verified producer;
3. it is an active thread with a deterministic activation rule;
4. it is a deterministic derived predicate over canonical state;
5. it is versioned replay metadata;
6. it is an explicit event completion or turn-window condition.

A prose trigger without one of these definitions is a QA blocker, not an implementation shortcut.

## Gate status

The expansion has enough authored causal material to proceed to exhaustive normalization. It is **not** yet suitable for automatic schema generation because the source-level ID conflict and derived-trigger vocabulary remain unresolved.

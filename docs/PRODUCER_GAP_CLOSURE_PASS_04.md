# Choice Kingdom — Producer Gap Closure Pass 04

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — PRE-SCHEMA**
Scope: remaining P0 canonical producers and their consumers.

## Purpose

This pass converts the remaining producer gaps into explicit authoring contracts. It does not create hidden engine fallback rules and does not claim runtime reachability.

## P0 closure contracts

### 1. `pred.food_stable`

Canonical meaning: the current run has an authored, durable state indicating that food distribution is stable enough for events that explicitly require stability.

Allowed evidence:
- an authored choice that explicitly establishes food stability; or
- a deterministic derived formula using already-canonical state, once the formula is frozen.

Forbidden:
- inventing `resource.food`;
- treating `+4 food stability` prose as a numeric resource mutation;
- deriving stability solely from `resource.gold` or `resource.trust` without a documented formula.

E192-B is therefore a **source correction candidate**, not a valid producer yet.

### 2. `pred.transport_disruption`

Canonical meaning: durable road/transport disruption currently affects the kingdom.

Minimum producer contract:
- source event/choice;
- durable marker or deterministic formula;
- persistence interval or clear condition;
- at least one explicit clearing action or expiry.

E136 is the primary authoring candidate because it directly describes frozen roads. E192 consumes the condition but must not manufacture it.

### 3. `pred.border_crisis` / `thread.border_crisis`

Canonical meaning: an authored escalation has moved border tension into a crisis route.

Minimum producer contract:
- escalation choice/history marker;
- activation of `thread.border_crisis`;
- deterministic de-escalation/terminal handling.

`resource.security` alone is not sufficient. Border crisis must remain semantically distinct from ordinary low/high security.

### 4. `pred.guild_logistics_cooperation`

E194-A is the strongest authored producer candidate: guild merchants offer a convoy and the ruler accepts with neutral inspectors.

Canonical producer requirement:
- `history.guild_logistics_cooperation` or equivalent canonical history marker;
- optional activation of `thread.ivo_market` if route semantics require it;
- no derivation from `rel.ivo` alone.

### 5. `pred.guild_influence_strong`

Must represent institutional guild influence, not affection toward Ivo.

Required minimum: at least two independent authored guild/institutional facts, one of which must concern durable political or commercial authority. The exact combination must be frozen during source QA.

Forbidden: `rel.ivo >= threshold` as the sole predicate.

### 6. `pred.systemic_explanation_verified`

Requires convergence of distinct investigation evidence, not evidence-count arithmetic.

Minimum contract:
- at least three distinct canonical evidence IDs from independent investigation stages;
- an authored convergence choice/event that explicitly verifies the systemic explanation;
- durable history marker or thread state consumed by downstream events.

E132–E135 and E232–E236 provide candidate evidence sources, but their semantic IDs must be normalized before this predicate is production-eligible.

### 7. `pred.coalition_cooperation`

Must represent actual cooperation across distinct faction routes.

Required:
- explicit cross-faction authored package;
- at least three distinct participating route identities;
- durable marker such as `history.cross_faction_package` plus a cooperation result;
- no equivalence with merely having four character relationships above threshold.

E148-A is the verified upstream producer for the cross-faction package; a separate cooperation qualification still needs explicit source semantics.

### 8. `pred.constitutional_prepared_strong`

Must be assembled from independent constitutional preparation domains, for example:
- institutional/audit reform;
- civic/commons reform;
- factional or house reform;
- military constitutional preparation.

The predicate cannot include itself or a downstream ending predicate as an input.

### 9. `pred.final_charter_prerequisites`

Must be a deterministic pre-E209 package. Candidate inputs include:
- constitutional preparation;
- coalition cooperation;
- house/faction representation;
- required civic/information/military safeguards.

E209 must consume this package; E210 remains convergence-only and cannot manufacture missing prerequisites.

## Explicit source defects found

1. E192-B writes `+4 food stability` without a canonical state target. This is invalid for the future machine-readable contract until rewritten as an existing marker/resource-safe consequence.
2. Several E170/E173/E174–E180 relationship/route triggers remain shorthand candidates and require canonical `thread.*` activation rather than raw relationship checks where the event is intended to represent a route.
3. E201–E210 contain several canonical-looking triggers whose producers remain incomplete; they cannot be treated as runtime-valid merely because the names exist in documentation.

## Gate

**P0 producer closure: still OPEN.**

The correct next step is source correction/authoring for the explicit defects above, followed by a complete producer-consumer inventory and reachability pre-audit. Production schema remains blocked until that pass succeeds.

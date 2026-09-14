# Choice Kingdom — Producer Gap Closure Pass 03

**Status:** SOURCE-LEVEL QA / AUTHORED-BRIDGE SPECIFICATION
**Runtime:** not implemented
**Production schema:** not frozen
**Scope:** remaining P0 producer gaps after Pass 02

## Purpose

Pass 02 verified `hist.guild_representation` at E144-A and identified nine remaining P0 gaps. This pass turns those gaps into concrete, reviewable authored bridge requirements. It deliberately does not hide unresolved semantics inside the future engine.

## Canonical rule

A producer is closed only when an authored choice or an explicitly frozen deterministic rule establishes the exact semantic fact. A prose condition, graph edge, relationship value, or unrelated resource change is not sufficient.

## 1. `pred.food_stable`

### Source defect
E192-B currently says `+4 food stability`, but the canonical state vocabulary has no numeric food resource. E138, E157, E167 and E193 expose food pressure without establishing one shared durable food-state contract.

### Required authored bridge
At the resolution of the first major food-logistics crisis, introduce one explicit choice outcome:

- `food_logistics_stabilized`
- `food_logistics_unstable`

The marker is a current-run durable fact. `pred.food_stable` is true only when `food_logistics_stabilized` is present and no later authored event has explicitly invalidated it.

### Required corrections
- Replace E192-B's undefined `+4 food stability` with `food_logistics_stabilized` plus its authored relationship/economic consequences.
- A later food-disruption event may clear/invalidate the stability marker explicitly.
- No sixth numeric resource.

**Status:** BRIDGE REQUIRED

## 2. `pred.transport_disruption`

### Source defect
E136 and E192 describe road pressure but do not establish one durable canonical fact.

### Required authored bridge
E136 must record one of:

- `transport_network_stable`
- `transport_disruption_active`

E192 may reinforce or clear the same fact depending on the chosen logistics response. The predicate is true only while `transport_disruption_active` remains current.

### Clear rule
A later explicit road-repair/infrastructure choice must clear the disruption. Merely waiting turns must not silently clear it.

**Status:** BRIDGE REQUIRED

## 3. `pred.border_crisis`

### Source defect
E139/E170–E172 create border escalation ingredients, while E195 consumes `border escalation`; no exact durable producer is currently named.

### Required authored bridge
At the authored escalation point, record:

- `border_crisis_declared`
- `border_crisis_resolved` when a later explicit resolution occurs.

`pred.border_crisis` is true only after `border_crisis_declared` and before explicit resolution.

Security changes must never create or clear this predicate by themselves.

**Status:** BRIDGE REQUIRED

## 4. `pred.guild_logistics_cooperation`

### Source defect
E124/E140 establish market/trade choices, while E194 consumes `guild cooperation`. No exact cooperation producer is frozen.

### Required authored bridge
E194-A (neutral inspectors) becomes the canonical cooperation producer:

`history.guild_logistics_cooperation = true`

E194-B is not cooperation; it is a separate immunity/political-risk outcome.

Earlier E124/E140 choices remain prerequisite evidence where the narrative requires them, but do not silently produce the final cooperation marker.

**Status:** SOURCE CANDIDATE — FINALIZE AT CATALOG FREEZE

## 5. `pred.guild_influence_strong`

### Required authored combination
Do not use `rel.ivo`.

Canonical qualification requires at least two distinct institutional guild outcomes from the following families:

- political representation (`hist.guild_representation`);
- commercial institutional influence (`guild_binding_seat` or equivalent);
- market/credit leverage (`official_credit_disclosure` / `private_credit_protected` path as appropriate);
- guild tribunal outcome;
- durable guild logistics cooperation.

The exact minimum set must be frozen before E200 becomes production-eligible. A single choice cannot satisfy the predicate by itself.

**Status:** COMBINATION RULE REQUIRED

## 6. `pred.systemic_explanation_verified`

### Required evidence model
The investigation must use distinct evidence IDs, not a raw count.

Minimum structure:

- at least one warehouse/financial evidence item;
- at least one document/language evidence item;
- at least one witness/organizational evidence item;
- one explicit convergence decision establishing the systemic explanation.

E207 may consume the predicate but cannot manufacture it.

**Status:** CONVERGENCE RULE REQUIRED

## 7. `pred.coalition_cooperation`

### Required qualification
The predicate requires:

1. `history.cross_faction_package` from E148-A;
2. explicit cooperation evidence from at least three distinct faction identities;
3. no unresolved coalition collapse marker.

Four active relationships/routes alone are insufficient.

E201 can modify coalition durability but must not create the predicate retroactively.

**Status:** COMBINATION RULE REQUIRED

## 8. `pred.constitutional_prepared_strong`

### Required non-circular qualification
Minimum authored preparation should combine three independent institutional domains chosen before E197:

- civic/commons preparation;
- audit/institutional preparation;
- cross-faction or constitutional preparation.

The predicate must not depend on E197–E210 ending outcomes, `ending.*`, or E210.

E150 and E196 can consume/strengthen preparation but must not create it from an already-qualified ending.

**Status:** COMBINATION RULE REQUIRED

## 9. `pred.final_charter_prerequisites`

### Required upstream package
The final package must be established before E209 and must explicitly validate the authored constitutional domains:

- civic/commons legitimacy;
- institutional/audit legitimacy;
- faction/house/guild representation;
- military/security constitutional route where applicable;
- information/evidence legitimacy;
- coalition cooperation;
- no unresolved mandatory crisis blocker.

E209 consumes this package. E210 only converges the resulting state into ending qualification.

**Status:** COMBINATION RULE REQUIRED

## Source defects discovered during this pass

1. **E192-B undefined state:** `+4 food stability` has no canonical resource/marker yet.
2. **E136/E192 road pressure:** no durable transport producer/clear rule.
3. **E195 border escalation:** consumer exists without an explicit durable escalation producer.
4. **E194 guild cooperation:** consumer semantics can be closed by E194-A, but the marker is not yet encoded in the authored catalog.
5. **E200 guild influence:** relationship shorthand would be an invalid shortcut.
6. **E207 systemic evidence:** requires distinct evidence identities and convergence, not count alone.
7. **E209 final prerequisites:** must be upstream and non-circular.

## Gate result

The nine remaining P0 gaps are now converted from vague names into concrete authored closure specifications. No runtime inference has been invented. The production catalog remains **BLOCKED** until these bridge semantics are either inserted into the authored event catalog or explicitly accepted as deterministic canonical rules during schema freeze.

## Next pass

1. Apply/author the smallest meaningful bridge choices in the affected narrative locations.
2. Re-run E01–E270 producer/consumer reconciliation.
3. Resolve the E192 undefined food-state consequence.
4. Freeze predicate thresholds only after source and balance review.
5. Build the static catalog validator only against the resulting canonical contract.

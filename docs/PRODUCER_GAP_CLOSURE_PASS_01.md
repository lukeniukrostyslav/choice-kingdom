# Choice Kingdom — Producer Gap Closure Pass 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — NOT PRODUCTION SCHEMA**

## Purpose

This pass converts the currently known producer gaps into an evidence-backed closure queue. It does not invent producers and does not promote thematic similarity, relationship values, graph edges, or event proximity into canonical state.

## P0 gaps

| Canonical state | Current evidence | Status | Required closure |
|---|---|---|---|
| `hist.guild_representation` | E203 consumes guild representation, but reviewed source has no exact authored producer | OPEN | identify an existing exact choice or author one explicit representation choice before schema freeze |
| `pred.food_stable` | E138/E167/E192 are candidate inputs | OPEN | define deterministic authored-state rule or explicit marker; never create a numeric food resource solely for this predicate |
| `pred.transport_disruption` | E136/E192 expose road/transport pressure | OPEN | define durable producer, persistence, and clear semantics |
| `pred.border_crisis` | E139/E170–E172 provide escalation ingredients | OPEN | define explicit escalation producer; security alone is insufficient |
| `pred.guild_logistics_cooperation` | E124/E140/E148/E194 candidates | OPEN | freeze exact authored combination and producer identity |
| `pred.guild_influence_strong` | E165/E168/E169/E194 ingredients | OPEN | define exact canonical combination; `rel.ivo` alone is prohibited |
| `pred.systemic_explanation_verified` | E132–E135 and E232–E236 evidence chain | OPEN | define distinct evidence-ID set plus explicit convergence rule |
| `pred.coalition_cooperation` | E146/E148 coalition evidence | OPEN | define cooperation semantics; route count alone is insufficient |
| `pred.constitutional_prepared_strong` | E142/E145/E146/E148/E150 candidates | OPEN | freeze minimum authored combination without circular dependency |
| `pred.final_charter_prerequisites` | E197–E209 candidates | OPEN | define exact prerequisite set and dependency direction |

## P1 gaps

- `thread.constitutional_late`
- `thread.final_constitutional_phase`
- `thread.amara_civic`
- `thread.toma_information`
- `thread.border_crisis`
- `thread.coalition`
- `thread.archive`
- `thread.winter_crisis`
- `thread.mara_audit`
- `thread.rowan_security`
- `thread.seris_houses`
- `thread.ivo_market`
- `pred.security_high`
- `pred.gold_low` threshold validation
- `pred.budget_reform`
- `pred.faction_routes_4`

These are route/predicate compilation contracts, not reasons to add filler events.

## Verified producers that must not be reopened without contradictory source evidence

- `history.cross_faction_package` ← E148-A
- `history.house_assembly` ← E161-A
- military constitutional route ← E199-A
- investigation evidence markers ← E132-A through E135-A and later investigation choices

## Forbidden shortcuts

1. Do not derive `hist.guild_representation` from `rel.ivo`.
2. Do not derive `pred.border_crisis` from `resource.security`.
3. Do not derive `pred.food_stable` from an invented sixth resource.
4. Do not treat four active faction routes as equivalent to `pred.coalition_cooperation`.
5. Do not treat evidence count without distinct IDs as systemic proof.
6. Do not use E210 as an ending resolver.
7. Do not use legacy E35–E40 as runtime IDs.
8. Do not turn replay `meta.*` into current-run `hist.*`, `thread.*`, or `pred.*` without an explicit transfer rule.

## Next execution pass

1. Resolve each P0 row from exact source text where possible.
2. Where no producer exists, flag the exact narrative insertion point rather than fabricating state.
3. Build one-row-per-key registry covering E01–E270.
4. Detect producer collisions and circular predicate dependencies.
5. Run static reachability pre-analysis from first-turn entry points to E265–E270.
6. Only then freeze the machine-readable schema.

## Gate

Production schema: **BLOCKED**.

The project remains content-first. Engine implementation must wait until this closure queue is resolved or every remaining OPEN item is explicitly represented as a deliberate authored requirement.

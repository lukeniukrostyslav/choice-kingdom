# Choice Kingdom — Canonical Closure Audit 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — NOT ENGINE INPUT**
Scope: exact producer closure for the currently open canonical consumers identified in `CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md`.

## Purpose

This pass deliberately does not invent missing producers. It distinguishes exact authored outputs from semantic candidates and records which gaps require a real authored choice, a deterministic derived predicate, or only a canonical compilation rule.

## Exact closure findings

| Consumer / key | Exact source evidence | Status | Required canonical action |
|---|---|---|---|
| `history.guild_representation` / E203 | E203 consumes `guild representation`; reviewed E151–E210 catalog contains no authored `guild_political_representation` output | **OPEN** | add/identify one explicit authored producer before schema freeze; do not infer from `rel.ivo` |
| `pred.food_stable` / E192+ | E192 choice B describes `+4 food stability`; E138 has grain recount; E167 has import risk; no canonical durable food-stability marker is authored | **OPEN** | define one deterministic authored marker or derived predicate with explicit source set; no sixth numeric resource |
| `pred.transport_disruption` / road pressure | E136 creates road responses; E192 consumes road pressure; no exact durable disruption marker in reviewed source | **OPEN** | define producer + persistence/clear rule; distinguish from a one-turn consequence |
| `pred.border_crisis` / E195+ | E139/E170–E172 provide border tension/watch decisions; no explicit `border_crisis` output found | **OPEN** | author explicit escalation state or deterministic derived escalation from frozen history; security alone is insufficient |
| `pred.guild_logistics_cooperation` / E194 | E124/E140/E148/E194 contain cooperation ingredients; E194 itself consumes cooperation | **OPEN** | freeze exact combination/history contract; do not use relationship alone |
| `pred.guild_influence_strong` / E200 | E165/E168/E169 provide guild leverage/tribunal/labor outcomes; E194 adds convoy route; no exact strong-influence producer | **OPEN** | define minimum distinct guild route/history set and exact source choices |
| `pred.systemic_explanation_verified` / E207 | E132–E135 + E232–E236 form evidence chain | **PARTIAL** | compile explicit evidence-ID set and convergence rule; count alone cannot qualify |
| `pred.coalition_cooperation` / E207 | E146/E148 establish coalition/signature/package choices | **PARTIAL** | freeze cooperation membership criteria distinct from `pred.faction_routes_4` |
| `pred.constitutional_prepared_strong` / E197 | E142/E145/E146/E148/E150 are candidates | **OPEN** | freeze minimum independent authored prerequisites and avoid circular dependency on E197 |
| `pred.budget_reform` / E198 | E142/E154/E198 are related institutional/audit choices | **OPEN** | distinguish audit-office independence, crown audit, and actual legislative budget lock |
| `thread.military_constitutional` / E204 | E199-A explicitly authors `army_constitution_oath` | **STRONG** | compile exact route marker; E204 must consume this route, not Rowan relationship/security |
| `thread.coalition` / E201+ | E146-A/B + E148-A/B | **STRONG/PARTIAL** | compile immutable membership/package history; E148-A is verified producer of package |
| `thread.amara_civic` / E205 | E120/E139/E174/E176 contain authored Amara route choices | **PARTIAL** | choose explicit route activation marker; relationship remains separate |
| `thread.toma_information` / E206 | E121/E131/E135/E177/E180 | **PARTIAL** | choose explicit route activation marker; relationship remains separate |
| `thread.final_constitutional_phase` / E208 | E150/E196–E210 are late-stage candidates | **OPEN** | establish one deterministic activation contract before E208 |
| `pred.final_charter_prerequisites` / E209 | E197/E198/E199/E202–E208 candidate ingredients | **OPEN** | publish exact prerequisite set, blockers, and minimum viable paths |

## Important source-level correction

The registry must not treat `history.guild_representation` as merely missing documentation. E203 is a real consumer and currently has no exact producer in the reviewed E151–E210 catalog. Therefore this is a genuine content/contract gap, not a wording problem.

Similarly, `pred.food_stable` must not become an implicit resource. E192's authored `+4 food stability` is a semantic output, but the canonical state model separates numeric resources from contextual pressures. The final implementation must either record an explicit history/flag marker or derive a deterministic predicate from declared authored state.

## Circularity hazards identified

1. `pred.constitutional_prepared_strong` cannot depend on E197 because E197 is the consumer of that predicate.
2. `pred.final_charter_prerequisites` cannot include E209 itself.
3. `pred.coalition_cooperation` cannot be defined merely as `pred.faction_routes_4`; the project explicitly requires cooperation to remain distinct from four route activations.
4. `pred.systemic_explanation_verified` cannot be `evidence_count >= N` without a distinct evidence-ID set and convergence rule.
5. `pred.guild_influence_strong` cannot be `rel.ivo >= threshold`.
6. `pred.border_crisis` cannot be `resource.security <= threshold`.
7. `thread.military_constitutional` cannot be inferred from `rel.rowan`.

## E203 producer requirement

A future producer must have an explicit authored semantic such as a choice granting a permanent commercial/political seat or representation. The source must identify the exact choice ID and output marker. A graph edge to E203 is not sufficient.

## Food stability contract candidate

The cleanest canonical form is a non-resource durable marker, for example `hist.food_stability_established` or an equivalent `pred.food_stable` derived from a declared set of food-security outputs. The exact name remains uncommitted until all E01–E270 food consumers are audited. The contract must define:

- qualifying outputs;
- whether they stack or are alternatives;
- expiry/clear conditions;
- whether delayed consequences can invalidate stability;
- whether replay metadata can affect it (default: no).

## Border crisis contract candidate

Border tension, military watch, and security are distinct. The eventual contract should require explicit escalation evidence, such as a combination of border-pressure history plus a qualifying escalation choice, and should specify when the crisis clears. It must not silently convert any low-security state into a border crisis.

## Guild cooperation contract candidate

A valid cooperation predicate should reference explicit guild logistics/convoy/infrastructure choices, not merely positive Ivo relationship. A possible future compilation set includes authored trade standards, risk-sharing/convoy decisions and coalition package participation, but the final minimum set must be chosen from exact source IDs and tested for reachability.

## Constitutional prerequisite contract

E197–E209 form a late-stage dependency chain. The implementation must distinguish:

- preparation (`pred.constitutional_prepared_strong`);
- route activation (`thread.constitutional_late`);
- institutional reforms (`pred.budget_reform`, audit route, house assembly, military route);
- final phase (`thread.final_constitutional_phase`);
- final prerequisites (`pred.final_charter_prerequisites`);
- convergence (`thread.endgame_convergence` / E210);
- ending qualification (E265–E270).

No layer should derive itself from a later layer.

## Next machine-checkable pass

Before production schema:

1. enumerate every concrete output token from E01–E270;
2. map every trigger token to its exact source choice(s);
3. detect consumer-without-producer;
4. detect producer-without-consumer;
5. detect duplicate semantic outputs;
6. detect contradictory writers to one canonical key;
7. detect predicate cycles;
8. detect delayed consequences whose source or target is undefined;
9. detect ending prerequisites with no independent producer path;
10. build reachability matrix and classify each event as reachable / conditionally reachable / unresolved / unreachable.

## Gate

**Production schema remains BLOCKED.** This audit closes source-level knowledge gaps and defines the exact static checks required next. No runtime claim is made.

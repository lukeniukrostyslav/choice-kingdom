# Choice Kingdom — Unified Producer / Consumer Registry 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA / PRE-SCHEMA
Scope: E01–E270 canonical producer/consumer closure.

## Purpose

This registry is the bridge between authored narrative and the future machine-readable catalog. It does not implement runtime behavior and must not manufacture state from thematic similarity.

## Canonical rules

- Exact authored choice output is the preferred producer evidence.
- Relationship values (`rel.*`) never substitute for route/history predicates.
- Graph edges and event proximity are not producers by themselves.
- Resources remain resources; pressure/stability concepts become derived predicates or explicit authored markers.
- `meta.*` replay state cannot satisfy current-run `hist.*`, `thread.*`, or `pred.*` without an explicit transfer rule.
- E210 is a convergence node, not an ending resolver.
- Legacy E35–E40 ending material is not a runtime ID namespace.

## Canonical registry — high-impact keys

| Key | Kind | Verified producer evidence | Consumer range | Status |
|---|---|---|---|---|
| `history.cross_faction_package` | history | E148-A | E149, E201, E207, E270 | VERIFIED |
| `history.house_assembly` | history | E161-A | E162, E268 | VERIFIED |
| `history.guild_representation` | history | none found in reviewed source | E203, constitutional/endgame consumers | OPEN |
| `thread.mara_audit` | thread | E81/E85/E95 candidate chain | E116, E142, E154+, ending layer | PARTIAL |
| `thread.rowan_security` | thread | E77/E88/E96 candidate chain | E117, E143, E170+, ending layer | PARTIAL |
| `thread.seris_houses` | thread | E74/E89/E97 candidate chain | E118, E161+, E203+, ending layer | PARTIAL |
| `thread.ivo_market` | thread | E75/E79/E84/E94 candidate chain | E124, E140, E165+, E194, E269 | PARTIAL |
| `thread.amara_civic` | thread | E80/E90/E103 candidate chain | E120, E139, E174+, ending layer | PARTIAL |
| `thread.toma_information` | thread | E82/E84/E93/E98 candidate chain | E121, E131, E177+, investigation | PARTIAL |
| `thread.ledger_investigation` | thread | E81/E85/E86/E91/E93/E94/E99/E100 | E132–E135, E184–E190, E232+ | STRONG CANDIDATE |
| `thread.archive` | thread | E91/E93/E99/E100 candidate chain | E153, E190, E207, E268, E270 | PARTIAL |
| `thread.winter_crisis` | thread | E101–E103/E109 | E136, E160, E175, E191–E195 | PARTIAL |
| `thread.border_crisis` | thread | E92/E107/E110 and E171–E172 inputs | E139, E170–E172, E195, E267 | PARTIAL |
| `thread.coalition` | thread | E146/E148 candidate chain | E148–E150, E201, E207, E270 | PARTIAL |
| `thread.budget_reform` | thread | E76/E81/E94/E95 candidates | E198, ending qualification | PARTIAL |
| `pred.food_stable` | predicate | E192-B explicitly describes +4 food stability; no canonical durable marker frozen | E167/E192 and downstream food consumers | OPEN |
| `pred.transport_disruption` | predicate | E136/E192 road pressure | E192 and downstream crisis logic | OPEN |
| `pred.border_crisis` | predicate | E139/E170–E172 escalation ingredients | E195, E267, ending qualification | OPEN |
| `pred.guild_logistics_cooperation` | predicate | E124/E140/E148/E194 candidates | E194, E207, E269 | OPEN |
| `pred.guild_influence_strong` | predicate | E165/E168/E169/E194 ingredients | E200, E269 | OPEN |
| `pred.systemic_explanation_verified` | predicate | E132–E135 + E232–E236 evidence chain | E207, E270, Second Founder | OPEN |
| `pred.coalition_cooperation` | predicate | E146/E148 | E207, E270 | OPEN |
| `pred.constitutional_prepared_strong` | predicate | E142/E145/E146/E148/E150 candidates | E150, E197, endgame | OPEN |
| `pred.final_charter_prerequisites` | predicate | E197–E209 candidates | E210, E265–E270 | OPEN |
| `pred.security_high` | predicate | resource/security choices provide candidates | E193, E200+, ending layer | OPEN — threshold |
| `pred.gold_low` | predicate | resource gold | E193 and crisis logic | OPEN — threshold |
| `pred.budget_reform` | predicate | audit/reform choices | E198 and ending layer | PARTIAL |
| `pred.faction_routes_4` | predicate | four route families are candidates | E146/E148/endgame | OPEN |

## Event-band producer coverage

### E01–E70
Early campaign establishes base resources, relationships, first institutional choices, emergency arc and original ending concepts. Exact route activation remains to be normalized against canonical thread markers.

### E71–E110
Strong source-level evidence exists for investigation, audit, merchant, military, noble, civic, information, winter and border routes. These outputs remain source facts until each is mapped to a canonical key.

### E111–E150
This band supplies late-route choices and explicit markers such as `guild_political_representation`, `people_charter_endorsed`, `auditor_independence`, `cross_faction_package`, and constitutional preparation evidence. `hist.guild_representation` remains OPEN because the reviewed canonical source does not yet establish an exact producer contract for that key.

### E151–E210
This band deepens audit, archive, noble, market, military, border, investigation and constitutional routes. E201/E202 are verified historical producers; E203–E210 contain several consumer/convergence contracts that must not be treated as automatically produced state.

### E211–E270
Downstream events consume audit, treasury/food, character routes, investigation evidence, faction credibility, winter crisis, constitutional stress tests and endgame qualification inputs. These remain design-level until static reachability and producer closure are executed.

## Collision / cycle review

No producer may be accepted merely because it is downstream of the predicate it supposedly produces. In particular:

1. `pred.final_charter_prerequisites` must not depend on `E210` if E210 depends on that predicate.
2. `pred.coalition_cooperation` must not be defined as `pred.faction_routes_4` if either is intended to consume the other.
3. `pred.systemic_explanation_verified` must consume distinct evidence IDs, not a count produced by itself.
4. `pred.border_crisis` must not be derived from `resource.security`.
5. `pred.food_stable` must not introduce a sixth resource.
6. `pred.guild_influence_strong` must not reduce to `rel.ivo`.
7. `thread.archive` must have a durable source marker before it can qualify Second Founder.

## Legacy ending namespace

The old E35–E40 ending titles in legacy documentation are review-only concepts. Canonical Act V uses E35 onward for continuing campaign events. Ending resolution is now represented by the E265–E270 qualification layer and the seven canonical ending families. Legacy ending IDs must therefore never be emitted by the runtime catalog.

## Gate

Production schema remains BLOCKED until the OPEN P0 keys have either:

- an exact existing authored producer;
- a deliberately authored narrative insertion point; or
- an explicit derived-predicate formula whose inputs are independently produced and acyclic.

Next pass: exact source reconciliation for each OPEN P0 key, then static graph/reachability analysis.

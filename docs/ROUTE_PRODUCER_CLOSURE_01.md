# Choice Kingdom — Canonical Route Producer Closure 01

Date: 2026-09-15
Status: **QA CLOSURE CHECKPOINT — NOT ENGINE INPUT**
Scope: route/thread producer closure from verified E01–E270 audit artifacts.

## Purpose

Convert the previously broad producer/consumer inventory into a stricter rule: a narrative route must be activated by an explicit, semantically stable producer. A relationship value, graph edge, thematic event, or raw resource threshold is not itself a route producer.

This document is a QA contract and does not implement runtime behavior.

## Canonical route families

| Route | Canonical identity | Verified producer anchors | Major consumers | Closure state |
|---|---|---|---|---|
| Mara / institutional | `thread.mara_audit` + `thread.institutional_reform` | E09 `audit_office`; E35–E36 institutional/emergency decisions; E46–E48 constitutional/institutional choices; E214/E226 | E152/E154/E155, E214/E216/E226/E258/E263, endings | **PARTIAL** |
| Rowan / security | `thread.rowan_security` | E05/E10 military authority; E17 armaments; E20 compensation; E31 mobilization; E37 army oath; E52 military audit; E227/E259 | E164/E170–E172/E185/E227/E240/E253/E255/E259 | **PARTIAL** |
| Seris / houses | `thread.seris_houses` | E06 noble pressure; E11 council; E26 witness; E38 house reform; E44/E54 constitutional house decisions | E161–E163/E183/E228/E238/E242/E265/E268 | **PARTIAL** |
| Ivo / market | `thread.ivo_market` | E08 merchant charter; E14 market reform; E18 toll/bridge policy; E19 price ceiling/guild policy; E39 credit; E49/E55 guild representation/books | E165–E169/E194/E219/E239/E246/E261/E269 | **PARTIAL** |
| Amara / civic | `thread.amara_civic` | E12 Lantern funding/clinic policy; E40 relief policy; E50 civic charter; E56 relief guarantee; E223/E230/E241 | E174–E176/E223/E230/E241/E252/E262/E270 | **PARTIAL** |
| Toma / information | `thread.toma_information` | E13 recruitment/rejection; E21 ledger investigation; E24 search; E42 witnesses; E43 ledger network; E57 systemic corruption/mystery route; E231 | E178–E190/E231/E236/E247/E249/E250/E269/E270 | **PARTIAL** |
| Ledger investigation | `thread.ledger_investigation` | E09/E21/E23/E28 audit/evidence choices; E41–E43 network; E53 ledger publication; E57 systemic confirmation | E152–E155/E187/E189/E211–E235/E250/E270 | **PARTIAL** |
| Winter crisis | `thread.winter_crisis` | E03 grain decisions; E12 relief/health; E29 granary/rationing; later winter policy nodes | E157/E160/E173/E175/E192/E225/E251/E252 | **OPEN PREDICATE CLOSURE** |
| Border crisis | `thread.border_crisis` | E10/E16 border command; E15 diplomacy; E31 border response; E37/E52 military law; later border events | E164/E170–E172/E195/E240/E253/E255/E259 | **OPEN PREDICATE CLOSURE** |
| Archive | `thread.archive` + `thread.archive_reform` | E153/E190/E249/E260 and earlier evidence access decisions | E249/E250/E256/E260/E265/E270 | **PARTIAL** |
| Coalition | `thread.coalition` | E32 shared crisis command; later faction credibility; E261/E262/E263 | E263/E265/E269/E270 | **PARTIAL** |
| Succession | `thread.succession` | E37/E47/E48 constitutional choices; E59 succession limits; E197/E256/E257 | E256–E270 ending qualification | **PARTIAL** |
| Budget reform | `thread.budget_reform` | E198/E258 and earlier fiscal reform choices | E216/E258/E263/endings | **OPEN** |
| Document audit | `thread.document_audit` | E09 audit office; E21/E23 ledger evidence; E152/E154/E155 | E213/E260 and investigation nodes | **PARTIAL** |

## Hard separation rules

1. `rel.*` values never activate a route by themselves. A relationship threshold may be a gate for an already activated route, but the route must have a producer.
2. `pred.security_low` is not `thread.border_crisis`.
3. `pred.border_tension` is not `pred.security_low`.
4. `pred.market_pressure` is not `rel.ivo` and is not automatically `thread.ivo_market`.
5. `pred.information_pressure_high` is not `rel.toma` and is not automatically `thread.toma_information`.
6. `thread.institutional_reform` is not equivalent to `resource.trust >= 6`.
7. Replay metadata (`meta.*`) cannot satisfy a current-run route unless an explicit replay-transfer rule exists.
8. A graph edge such as E214 → E216 is not a producer unless the source choice establishes the exact state consumed by E216.
9. A numeric consequence without a later semantic consumer does not need to become a history marker merely because it is numerically meaningful.
10. Every delayed route activation must retain source event/choice identity and exact-once resolution data.

## Producer quality test

A producer is **CLOSED** only when all five are known:

- stable canonical identifier;
- exact source event/choice;
- semantic meaning that matches every consumer;
- persistence model (`history`, `flag`, `thread`, `delay`, `meta` or derived predicate);
- no competing producer with a different meaning under the same identifier.

Current route families fail closure primarily where the source catalog still uses prose conditions such as food pressure, winter severity, institutional reform, budget reform, border crisis, or information pressure without a deterministic compiled definition.

## Highest-risk unresolved producers

- food pressure / severe food pressure / food crisis;
- winter pressure / severe winter / winter illness / transport disruption;
- border tension / border crisis / army readiness;
- market pressure / guild labor tension / guild logistics;
- information pressure / evidence cardinality / systemic explanation;
- institutional reform / budget reform / archive reform;
- E261 four-faction cardinality;
- E265–E270 ending qualification inputs;
- legacy E35–E40 semantic mappings after the ID reconciliation decision.

## QA result

The route producer inventory is now substantially more constrained than the earlier broad inventory, but it is **not yet production-frozen**. The next machine-verifiable gate is a complete producer/consumer table for every canonical identifier plus an undefined-consumer/undefined-producer scan. Only after that should the production data schema be frozen.

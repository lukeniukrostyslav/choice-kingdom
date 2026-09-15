# Choice Kingdom — Reachability Pre-Audit E211–E250

Status: **STATIC PRE-AUDIT — NOT RUNTIME VERIFIED**

This pass converts the E211–E250 authored trigger/output relationships into explicit QA obligations. It does not claim a playable graph because the production data representation and engine do not yet exist.

## Consumer → upstream requirement map

| Consumer | Required upstream evidence | Current status |
|---|---|---|
| E211 | `full_crown_audit_published` or `tax_transparency` | upstream source exists; runtime path unverified |
| E212 | `clerks_oath_public` | upstream E151; runtime path unverified |
| E213 | `regional_courts` | upstream E145-A; runtime path unverified |
| E214 | canonical institutional-reform predicate | **OPEN contract** |
| E215 | `law_notices_public` | upstream E159-A; runtime path unverified |
| E216 | low gold + high reform spending | **OPEN derived contract** |
| E217 | `quiet_treasury_loan` | upstream E216-B; runtime path unverified |
| E218 | food pressure | **OPEN derived contract** |
| E219 | strong market oversight | **OPEN derived contract** |
| E220 | `trade_risk_insurance` | upstream E140-A; runtime path unverified |
| E221 | `winter_rent_ceiling` or high civic trust | upstream/derived; runtime path unverified |
| E222 | veteran route | **OPEN route predicate** |
| E223 | Amara route | **OPEN route predicate** |
| E224 | `river_compact` | upstream E126-A; runtime path unverified |
| E225 | severe food pressure | **OPEN derived contract** |
| E226 | Mara <= -1 or repeated executive overrides | relationship/aggregate contract needed |
| E227 | Rowan route + constitutional reform | **OPEN route/constitutional predicate** |
| E228 | noble constitutional route | **OPEN route predicate** |
| E229 | Ivo >= 1 | direct relationship threshold; runtime path unverified |
| E230 | Amara >= 1 | direct relationship threshold; runtime path unverified |
| E231 | Toma route + high information pressure | **OPEN route/predicate contract** |
| E232 | >=2 procurement clues | **OPEN evidence-cardinality contract** |
| E233 | forgery route | canonical forgery route mapping required |
| E234 | `payment_date_crosscheck` | upstream E187-A; runtime path unverified |
| E235 | `intermediary_chain_traced` | upstream E232-A; runtime path unverified |
| E236 | witness route | canonical witness route mapping required |
| E237 | public accountability route | **OPEN route predicate** |
| E238 | noble constitutional route | **OPEN route predicate** |
| E239 | guild logistics route | canonical guild-logistics route mapping required |
| E240 | border route | canonical border route mapping required |
| E241 | Amara route | **OPEN route predicate** |
| E242 | prior noble exception + 6 turns | delayed source identity required |
| E243 | public bridge investment + 5 turns | delayed source identity required |
| E244 | flexible accounts + 5 turns | delayed source identity required |
| E245 | compensation route + 6 turns | delayed source identity required |
| E246 | price ceiling + 5 turns | delayed source identity required |
| E247 | second-run information route | explicit `meta.*` replay gate required |
| E248 | replay callback | explicit `meta.*` replay identity required |
| E249 | archive route | canonical archive route required |
| E250 | >=3 related clues | explicit evidence-cardinality contract required |

## Findings

1. The range has substantial upstream references, but reachability cannot be proven from prose alone.
2. The most important blockers are not ordinary event IDs; they are unresolved derived predicates and route concepts: institutional reform, food pressure/severity, market oversight, veteran/Amara/Toma/border/noble/guild routes, evidence cardinality and constitutional reform.
3. E242–E246 are structurally delayed callbacks. They require source-choice identity, due-turn calculation, cancellation rules and exactly-once semantics before they can be considered reachable runtime nodes.
4. E247–E248 explicitly require replay metadata and must not be satisfied by ordinary current-run flags.
5. E226 must consume accumulated institutional strain and remain semantically distinct from E36. This requires graph-level verification, not just title/source text.
6. E232/E250 require independent evidence counting; duplicate aliases must not inflate the count.

## P0 checks to perform when production schema is frozen

- enumerate all producers of each trigger token;
- enumerate all consumers of each output token;
- reject consumer-without-producer unless trigger is a primitive/resource/relationship predicate with a frozen formula;
- reject producer-without-consumer only after determining whether the output is intentionally terminal or presentation-only;
- detect duplicate semantic outputs and contradictory writers;
- detect delayed source IDs that do not correspond to authored choices;
- detect replay consumers lacking explicit `meta.*` prerequisites;
- compute incoming/outgoing edges and strongly connected components;
- verify each ending has at least one independent producer path;
- verify mutually exclusive outcomes are not simultaneously active;
- simulate branch convergence after the engine exists.

## Gate

E211–E250 static pre-audit: **RECORDED**.

Production schema: **BLOCKED**.

Runtime reachability: **NOT VERIFIED**.

No validator is created in this pass because the canonical data contract is not yet frozen, consistent with project engineering gates.

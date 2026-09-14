# Choice Kingdom — Canonical Producer / Consumer Registry 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — WORKING REGISTRY, NOT ENGINE INPUT**
Scope: canonical state families identified across E01–E270.

## Purpose

This registry consolidates the separate producer audits into one QA surface. A row is considered **VERIFIED** only when an authored source choice establishes the exact semantic state consumed downstream. A candidate, graph edge, relationship value, or thematic similarity is not sufficient.

The registry deliberately records OPEN rows instead of inventing producers.

## Canonical namespaces

The repository defines separate namespaces for numeric resources, relationships, flags, immutable history/evidence, narrative threads, delayed effects, endings and replay metadata. Contextual pressures must not silently become a sixth numeric resource.

## Registry

| Canonical key / family | Type | Known producer(s) | Known consumer(s) | Status | QA note |
|---|---|---|---|---|---|
| `resource.gold` | resource | authored choices throughout campaign | treasury/market/food events | VERIFIED FAMILY | numeric resource |
| `resource.trust` | resource | authored choices throughout campaign | civic/institutional/ending gates | VERIFIED FAMILY | numeric resource |
| `resource.security` | resource | authored choices throughout campaign | security/border events | VERIFIED FAMILY | never substitutes for border crisis |
| `resource.power` | resource | authored choices throughout campaign | political/constitutional events | VERIFIED FAMILY | numeric resource |
| `resource.reputation` | resource | authored choices throughout campaign | information/ending gates | VERIFIED FAMILY | numeric resource |
| `rel.mara` | relationship | Mara choices | Mara route events | VERIFIED FAMILY | relationship != institutional reform |
| `rel.rowan` | relationship | Rowan choices | Rowan route events | VERIFIED FAMILY | relationship != military constitutional route |
| `rel.seris` | relationship | Seris choices | house/noble events | VERIFIED FAMILY | relationship != house route itself |
| `rel.ivo` | relationship | Ivo choices | guild/market events | VERIFIED FAMILY | relationship != guild influence |
| `rel.amara` | relationship | Amara choices | civic/medical events | VERIFIED FAMILY | relationship != civic route activation |
| `rel.toma` | relationship | Toma choices | information events | VERIFIED FAMILY | relationship != information pressure |
| `flag.audit_office` | flag | E142/E151 lineage candidates | E154/E155 and audit chain | PARTIAL | exact canonical first producer needs freeze |
| `flag.crown_audited` | flag | E154-A | E155 | VERIFIED | durable audit fact |
| `flag.cheap_weapons` | flag | E128 lineage | E185 | VERIFIED FAMILY | delayed callback exists |
| `flag.warehouse_arson` | flag | earlier warehouse crisis choice(s) | E186/E191 | VERIFIED FAMILY | exact producer audit still required |
| `flag.emergency_powers_expire` | flag | E197-A | constitutional endgame | VERIFIED | explicit authored output |
| `flag.emergency_powers_inherit` | flag | E197-B | constitutional endgame | VERIFIED | explicit authored output |
| `history.cross_faction_package` | history | E148-A | E149/E201/E261+ | VERIFIED PRODUCER | canonical immutable marker still needs compilation contract |
| `history.house_assembly` | history | E161-A | E162/E202/E261+ | VERIFIED PRODUCER | exact authored output |
| `history.guild_representation` | history | no exact producer found | E203+ | OPEN | do not infer from guild relationship |
| `history.six_signatures_public` | history | E146-A | coalition/endgame | VERIFIED | authored marker |
| `history.six_signatures_private` | history | E146-B | coalition/endgame | VERIFIED | authored marker |
| `history.redaction_reconstructed` | history | E132-A | investigation chain | VERIFIED | evidence marker |
| `history.form_pattern_tested` | history | E133-A | investigation chain | VERIFIED | evidence marker |
| `history.office_network_mapped` | history | E134-A | E153/E190 | VERIFIED | evidence/route marker |
| `history.conflicting_testimony_recorded` | history | E135-A | E189/E236 | VERIFIED | evidence marker |
| `history.payment_date_crosscheck` | history | E187-A | E234 | VERIFIED | explicit callback input |
| `history.emergency_language_compared` | history | E131-A | E188 | VERIFIED | replay/evidence marker |
| `thread.mara_audit` | thread | E116/E142 plus E81/E85/E95 evidence | E151–E155 and later | PARTIAL | exact activation rule must be frozen |
| `thread.rowan_security` | thread | E117/E137/E143 and earlier Rowan decisions | E170–E173/E182/E227 | PARTIAL | must remain separate from security resource |
| `thread.seris_houses` | thread | E118/E127/E161 lineage | E162–E164/E183/E228 | PARTIAL | exact route activation still required |
| `thread.ivo_market` | thread | E124/E140/E148 and E165–E169 evidence | E194/E216+ | PARTIAL | route activation != rel.ivo |
| `thread.amara_civic` | thread | E120/E139/E174/E176 | E205/E223/E230/E241 | PARTIAL | exact activation marker required |
| `thread.toma_information` | thread | E121/E131/E135/E177/E180 | E206/E231+ | PARTIAL | route activation separate from relationship |
| `thread.ledger_investigation` | thread | E132–E135 plus E232–E236 | E207/E261+ | STRONG CANDIDATE | needs explicit chain activation and evidence set |
| `thread.archive` | thread | E131/E134/E153 | archive callbacks | PARTIAL | archive access != archive reform |
| `thread.winter_crisis` | thread | E101–E103 and winter callbacks | E136/E160/E192/E225/E251+ | PARTIAL | severity formula/history producer unresolved |
| `thread.border_crisis` | thread | E139/E170–E172 candidates | E195/E240/E251+ | PARTIAL | border escalation must be explicit |
| `thread.coalition` | thread | E146/E148 | E149/E201/E261+ | PARTIAL | coalition membership semantics not frozen |
| `thread.military_constitutional` | thread | E199-A | E204/E227/E256+ | STRONG CANDIDATE | direct constitutional oath producer |
| `thread.constitutional_late` | thread | E146/E148/E150 candidates | E196/E208 | OPEN | timing/activation contract unresolved |
| `thread.final_constitutional_phase` | thread | E150/E196–E210 candidates | E208/E209/E210 | OPEN | no single durable producer frozen |
| `thread.endgame_convergence` | thread | E210 candidate convergence node | E265–E270 | OPEN/CONVERGENCE ONLY | never independently resolves ending |
| `pred.gold_low` | predicate | `resource.gold` threshold candidate | E193+ | PROVISIONAL | threshold must be balance-verified |
| `pred.security_high` | predicate | `resource.security` threshold candidate | E193+ | OPEN | threshold not frozen |
| `pred.food_stable` | predicate/marker | E138/E167/E192 candidates | E192/E216/E225 | OPEN | exact deterministic definition required |
| `pred.transport_disruption` | predicate | E136/E192 candidates | road/food/medicine events | OPEN | persistence/clear rule required |
| `pred.border_crisis` | predicate | E139/E170–E172 candidates | E195/E240+ | OPEN | escalation producer required |
| `pred.guild_logistics_cooperation` | predicate | E124/E140/E148/E194 candidates | E194 | OPEN | exact cooperation combination required |
| `pred.guild_influence_strong` | predicate | E165/E168/E169/E194 candidates | E200 | OPEN | cannot derive from rel.ivo alone |
| `pred.systemic_explanation_verified` | predicate | E132–E135 + E232–E236 evidence chain | E207/endgame | OPEN | explicit convergence rule required |
| `pred.coalition_cooperation` | predicate | E146/E148 candidates | E207/E261+ | OPEN | cooperation != merely four routes |
| `pred.constitutional_prepared_strong` | predicate | E142/E145/E146/E148/E150 candidates | E197 | OPEN | minimum authored combination required |
| `pred.budget_reform` | predicate | E142/E154/E198 candidates | E198 | OPEN | audit reform vs budget reform must remain distinct |
| `pred.final_charter_prerequisites` | predicate | E197/E198/E199/E202–E209 candidates | E209/E210 | OPEN | exact prerequisite set not frozen |
| `pred.faction_routes_4` | predicate | distinct faction route activations | coalition/endgame | OPEN | distinct route identities required |
| `ending.*` | ending | E265–E270 qualification layer | final result | DESIGN CONTRACT | deterministic multi-input qualification required |

## Verified producer principles

1. E148-A is the authored producer for `cross_faction_package`.
2. E161-A is the authored producer for `house_assembly`.
3. E199-A is the strongest direct producer for the military constitutional route.
4. E132–E135 and E232–E236 form an authored multi-stage investigation/evidence chain.
5. E210 is a convergence node and not an ending resolver.

## Static QA rules for next pass

A registry row fails closure when:

- a consumer exists without an exact producer;
- a producer has incompatible meanings under the same key;
- a predicate derives itself or creates a circular dependency;
- a relationship is used as a substitute for a route/state that has stronger authored semantics;
- a contextual pressure is treated as a numeric resource without an explicit contract;
- a delayed callback has no stable source/consequence identity;
- an ending prerequisite has no demonstrably viable producer path.

## Next closure pass

1. Expand this registry to every concrete durable flag/history marker used by E01–E270.
2. Add exact consumer event IDs for all rows currently summarized by ranges.
3. Resolve `history.guild_representation`, food stability, border escalation and guild cooperation.
4. Freeze constitutional prerequisite composition.
5. Run contradiction and reachability checks from the registry.
6. Audit duplicate semantic events E73/E156 and E99/E173.
7. Reconcile legacy E35–E40 aliases before schema freeze.

## Gate

**Production schema: BLOCKED.** This registry is the first unified source-of-truth QA layer; it is not runtime data and does not imply reachability has been proven.

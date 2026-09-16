# Choice Kingdom — Canonical Producer / Consumer Registry 01

Date: 2026-09-16  
Status: **SOURCE-LEVEL QA — CANONICAL WORKING REGISTRY, NOT ENGINE INPUT**  
Scope: **frozen production E01–E272 only**.

## Scope-integrity rule

Only event IDs `E01..E272` may contribute production producers, consumers, predicates, delayed sources, or reachability edges. E273–E277 are expansion candidates and are excluded from the frozen production catalog.

This registry records unresolved runtime/source gaps explicitly and never invents producers, aliases, timing, or consumer semantics.

## Registry

| Canonical key / family | Type | Known producer(s) | Known consumer(s) | Status | QA note |
|---|---|---|---|---|---|
| `resource.gold` | resource | authored choices throughout campaign | treasury/market/food events | VERIFIED FAMILY | numeric resource |
| `resource.trust` | resource | authored choices throughout campaign | civic/institutional/ending gates | VERIFIED FAMILY | numeric resource |
| `resource.security` | resource | authored choices throughout campaign | security/border events | VERIFIED FAMILY | numeric resource; never substitutes for border crisis |
| `resource.power` | resource | authored choices throughout campaign | political/constitutional events | VERIFIED FAMILY | numeric resource |
| `resource.reputation` | resource | authored choices throughout campaign | information/ending gates | VERIFIED FAMILY | numeric resource |
| `rel.mara` | relationship | Mara choices | Mara route events | VERIFIED FAMILY | relationship != institutional reform |
| `rel.rowan` | relationship | Rowan choices | Rowan route events | VERIFIED FAMILY | relationship != military constitutional route |
| `rel.seris` | relationship | Seris choices | house/noble events | VERIFIED FAMILY | relationship != house route itself |
| `rel.ivo` | relationship | Ivo choices | guild/market events | VERIFIED FAMILY | relationship != guild influence |
| `rel.amara` | relationship | Amara choices | civic/medical events | VERIFIED FAMILY | relationship != civic route activation |
| `rel.toma` | relationship | Toma choices | information events | VERIFIED FAMILY | relationship != information pressure |
| `history.cross_faction_package` | history | E148-A | E149/E201/E261+ | VERIFIED PRODUCER | package != cooperation qualification |
| `history.house_assembly` | history | E161-A | E162/E202/E261+ | VERIFIED PRODUCER | durable house representation |
| `history.guild_representation` | history | E144-A/E144-B | E203+ | VERIFIED PRODUCER | one representation domain; not a second guild domain |
| `guild_political_representation` | state/history source | E49-A | guild-influence consumers | VERIFIED SOURCE | E49-B is opposing `guild_political_exclusion` |
| `people_charter_endorsed` | state/history source | E50-A | E114/E122/E145/E197/E209+ | VERIFIED SOURCE | one civic domain only |
| `history.guild_logistics_cooperation` | history | E136-B | E194+ | VERIFIED PRODUCER | E194 consumes upstream marker |
| `history.winter_severity_declared` | history | E29-A/E29-B | E136/E160/E251+ | VERIFIED PRODUCER | immutable history; active predicate needs cycle validity |
| `thread.border_crisis` | thread | E271-A declaration; E272-A/B resolution | E195/E240/E251/E253+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | declaration and resolution are separate stages |
| `history.border_crisis_resolved_diplomatically` | history | E272-A | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration |
| `history.border_crisis_resolved_by_guarantee` | history | E272-B | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration |
| `thread.coalition` | thread | E146/E148 | E149/E201/E261+ | PARTIAL | package exists; cooperation qualification is separate |
| `thread.military_constitutional` | thread | E199-A | E204/E227/E256+ | SOURCE-CLOSED CANDIDATE | direct constitutional oath producer; runtime qualification remains open |
| `thread.endgame_convergence` | thread | E210 candidate convergence node | E265–E270 | OPEN / CONVERGENCE ONLY | never independently resolves missing prerequisites |
| `pred.gold_low` | predicate | `resource.gold` threshold candidate | E193+ | PROVISIONAL | threshold must be balance-verified |
| `pred.security_high` | predicate | `resource.security` threshold candidate | E193+ | OPEN | threshold not frozen |
| `pred.market_pressure` | predicate | E19-B | E216/E219/E246+ | SOURCE-CLOSED / RUNTIME OPEN | E19-A clears active cycle |
| `pred.winter_severe` | predicate | E29-A/E29-B | winter/crisis consumers | SOURCE-CLOSED / RUNTIME OPEN | current winter cycle expiry remains open |
| `pred.food_stable` | predicate | E192-B | downstream food/logistics consumers | SOURCE-CLOSED / RUNTIME OPEN | E192-A explicitly clears active stability; E273-A excluded |
| `pred.transport_disruption` | predicate | E32 explicit active producer; E136-A/B recovery/clear | E192/E251+ | SOURCE-CLOSED / RUNTIME OPEN | lifecycle/persistence/ordering remain open |
| `pred.border_crisis` | predicate | E271-A; E272-A/B clear | E195/E253/E255+ | SOURCE-CLOSED / RUNTIME OPEN | active only between declaration and resolution |
| `pred.guild_logistics_cooperation` | predicate | E136-B upstream marker + E194-A neutral inspection | downstream guild/ending consumers | SOURCE-CLOSED / RUNTIME OPEN | requires prior cooperation + inspection + no unresolved immunity-risk blocker |
| `pred.guild_influence_strong` | predicate | representation + tribunal + commercial/credit + qualified logistics domains | E200 | SOURCE CONTRACT CLOSED / RUNTIME OPEN | at least two distinct domains; `rel.ivo` alone forbidden |
| `pred.systemic_explanation_verified` | predicate | E232–E236 evidence families + E270-A convergence | E207/endgame | SOURCE-CLOSED / RUNTIME OPEN | E270-A cannot manufacture missing evidence families |
| `pred.coalition_cooperation` | predicate | E148-A cross-faction package | E201/E207/E261+ | SOURCE CONTRACT CLOSED / RUNTIME OPEN | named participants + positive mutual concessions + no unresolved collapse blocker; E261-A alone is insufficient |
| `pred.constitutional_prepared_strong` | predicate | E50 + E154 + E161 + E199 independent domains | E197 | SOURCE CONTRACT CLOSED / RUNTIME OPEN | any 3 distinct domains; downstream evidence cannot double-count |
| `pred.budget_reform` | predicate | E142-A + E154-A + E198-A | E258+ | SOURCE CONTRACT CLOSED / RUNTIME OPEN | explicit negative blockers; E155-A same-domain evidence cannot count twice |
| `pred.final_charter_prerequisites` | predicate | deterministic derived gate from canonical upstream inputs | E209/E210 | SOURCE CONTRACT CLOSED / RUNTIME OPEN | E209 is consumer-only; exact runtime aggregation/invalidation remains open |
| `pred.faction_routes_4` | predicate | distinct faction route activations | E261+ | OPEN | distinct route identities required |
| `ending.*` | ending | E265–E270 qualification layer | final result | DESIGN CONTRACT | deterministic multi-input qualification required |

## Explicitly excluded predicate candidates

The following predicates are **not production semantics in E01–E272** because no authoritative in-scope producer or production consumer has been verified. Their named E275/E276 producer candidates are expansion-only and remain quarantined:

- `pred.guild_labor_tension` — **EXCLUDED / BLOCKED**; E275-B cannot satisfy the production contract.
- `pred.information_pressure_high` — **EXCLUDED / BLOCKED**; E276-B cannot satisfy the production contract.

They must not be promoted into production by prose, aliases, relationship scores, consumer reachability, or expansion events. Re-admission requires an explicit production-scope change and a fresh producer/consumer audit.

## Excluded-source contamination audit

The following references are explicitly rejected from the frozen production registry:

- E273-A as a producer for `pred.food_stable`.
- E274-A as a production market-pressure producer.
- E275-A/B as production guild-labor predicate sources.
- E276-A/B as production information-pressure predicate sources.
- E277 as a production transport-recovery producer.
- Any E273–E277 producer, consumer, delayed source, predicate source or reachability edge introduced by future QA work.

## Current source-level closure boundary

- Source-level producer/consumer closure is green for the frozen canonical inventory.
- Source-level composite predicate contracts are closed where an in-scope authored producer or deterministic derived contract exists.
- The two explicitly excluded predicates above are quarantined rather than silently promoted.
- Runtime lifecycle, persistence, contradiction invalidation, fresh-run gameplay reachability, replay reachability and Decision Engine execution remain downstream work.

## Remaining P0 closure work

1. Complete authored choice/effect transition closure across E01–E272.
2. Complete delayed cancellation/supersession, exactly-once runtime scheduling, persistence and replay isolation.
3. Close replay producer/key tuples for E186/E247/E248 without inference.
4. Close deterministic ending prerequisites, negative blockers, precedence and terminal order.
5. Prove fresh-run and replay causal reachability beyond structural 272/272 graph reachability.
6. Reconcile catalog ↔ graph semantic equality beyond event-ID parity.
7. Freeze production schema and implement/verify the Decision Engine only after the canonical source contracts are sufficiently closed.

## Gate

**Source-level producer/consumer registry: RECONCILED 2026-09-16.**  
**Production schema: BLOCKED.**  
**Runtime/reachability: NOT VERIFIED.**

This registry is the canonical QA surface, not runtime data.

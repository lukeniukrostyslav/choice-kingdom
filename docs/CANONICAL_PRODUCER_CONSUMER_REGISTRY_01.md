# Choice Kingdom — Canonical Producer / Consumer Registry 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — WORKING REGISTRY, NOT ENGINE INPUT**
Scope: canonical state families identified across E01–E272.

## Purpose

This registry consolidates the producer audits into one QA surface. A row is **VERIFIED** only when an authored source choice establishes the exact semantic state consumed downstream. A candidate, graph edge, relationship value, or thematic similarity is not sufficient.

The registry deliberately records OPEN rows instead of inventing producers.

## Current canonical status

The E211–E270 expansion received a dedicated producer/consumer audit. E271 explicitly separates border-crisis declaration from prior warning infrastructure, and E272 now provides the missing authored resolution producer for an active declared crisis. Runtime validation is still absent.

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
| `history.cross_faction_package` | history | E148-A | E149/E201/E261+ | VERIFIED PRODUCER | package != cooperation qualification |
| `history.house_assembly` | history | E161-A | E162/E202/E261+ | VERIFIED PRODUCER | durable house representation |
| `history.guild_representation` | history | E144-A/E144-B | E203+ | VERIFIED PRODUCER | both E144 choices establish same representation fact |
| `history.guild_logistics_cooperation` | history | E194-A | E194+ | VERIFIED SOURCE MARKER | predicate combination rule frozen; runtime producer still pending |
| `thread.border_crisis` | thread | E271-A declaration; E272-A/B resolution | E195/E240/E251/E253+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | declaration and resolution are distinct authored stages |
| `history.border_crisis_resolved_diplomatically` | history | E272-A | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration while recording diplomatic resolution |
| `history.border_crisis_resolved_by_guarantee` | history | E272-B | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration while recording security resolution |
| `thread.coalition` | thread | E146/E148 | E149/E201/E261+ | PARTIAL | package exists; cooperation qualification is separate |
| `thread.military_constitutional` | thread | E199-A | E204/E227/E256+ | STRONG CANDIDATE | direct constitutional oath producer |
| `thread.endgame_convergence` | thread | E210 candidate convergence node | E265–E270 | OPEN / CONVERGENCE ONLY | never independently resolves missing prerequisites |
| `pred.gold_low` | predicate | `resource.gold` threshold candidate | E193+ | PROVISIONAL | threshold must be balance-verified |
| `pred.security_high` | predicate | `resource.security` threshold candidate | E193+ | OPEN | threshold not frozen |
| `pred.food_stable` | predicate/marker | E138/E167/E192 candidates | E192/E216/E225 | OPEN | deterministic definition required |
| `pred.transport_disruption` | predicate | E136 repair producer + disruption source required | E192/E251+ | PARTIAL | E136 clears active disruption and establishes stable transport; disruption source remains open |
| `pred.border_crisis` | predicate | E271-A declaration; E272-A/B resolution | E195/E253/E255+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | active only after declaration and before resolution |
| `pred.guild_logistics_cooperation` | predicate | E194-A `history.guild_logistics_cooperation` | E194+ | CONTRACT FROZEN / SOURCE GAP | requires neutral-inspector safeguard and no unresolved immunity-risk blocker |
| `pred.guild_influence_strong` | predicate | E144/E165/E168/E194 candidate domains | E200 | CONTRACT FROZEN / PRODUCERS OPEN | at least two distinct institutional guild domains; `rel.ivo` alone forbidden |
| `pred.systemic_explanation_verified` | predicate | E132–E135/E232–E236 evidence candidates | E207/endgame | CONTRACT FROZEN / PRODUCER OPEN | three evidence domains plus explicit convergence decision |
| `pred.coalition_cooperation` | predicate | E148-A + distinct faction evidence candidates | E201/E207/E261+ | CONTRACT FROZEN / PRODUCERS OPEN | package + 3 distinct faction identities + no collapse blocker |
| `pred.constitutional_prepared_strong` | predicate | E142/E145/E146/E148/E150 candidates | E197 | CONTRACT FROZEN / PRODUCERS OPEN | three independent upstream institutional domains |
| `pred.budget_reform` | predicate | E142/E154/E198 candidates | E198 | OPEN | audit reform vs budget reform must remain distinct |
| `pred.final_charter_prerequisites` | predicate | E197/E198/E199/E202–E209 candidates | E209/E210 | CONTRACT FROZEN / PRODUCERS OPEN | deterministic upstream set; E209 consumes only |
| `pred.faction_routes_4` | predicate | distinct faction route activations | E261+ | OPEN | distinct route identities required |
| `ending.*` | ending | E265–E270 qualification layer | final result | DESIGN CONTRACT | deterministic multi-input qualification required |

## E211–E272 audit result

E211–E270 contain useful authored markers but still require normalization of prose triggers, explicit producer enumeration, delayed/replay metadata, and graph/reachability reconciliation. E251–E255 remain crisis consumers. E271 closes the declaration source gap and E272 closes the authored active-crisis resolution gap. E256–E260 are constitutional stress tests and cannot retroactively create prerequisites. E261–E265 keep coalition cooperation distinct from route count and durability. E266–E270 are endgame character/evidence nodes, not automatic prerequisite producers.

## Frozen combination rules

### Guild logistics cooperation
Minimum qualification: E194-A source marker + `guild_neutral_inspectors` safeguard + no unresolved `guild_logistics_immunity_risk`. It is route/history state, not `rel.ivo`.

### Strong guild influence
At least two distinct institutional domains among guild representation, commercial institutional influence, market/credit leverage, guild tribunal outcome and durable guild logistics cooperation. Relationship level alone cannot qualify it.

### Systemic explanation verified
Requires warehouse/financial evidence + document/language evidence + witness/organizational evidence + explicit convergence decision. Raw clue count is insufficient.

### Coalition cooperation
Requires E148-A package + cooperation evidence from at least three distinct faction identities + no unresolved coalition-collapse marker. E261 cannot manufacture this retroactively.

### Strong constitutional preparation
Requires three independent upstream domains: civic/commons legitimacy, audit/institutional legitimacy, and cross-faction or constitutional legitimacy. E197–E210 outcomes cannot serve as their own prerequisite.

### Final charter prerequisites
Before E209, as applicable: civic/commons legitimacy, institutional/audit legitimacy, faction/house/guild representation, military/security constitutional route where required, information/evidence legitimacy, coalition cooperation, and no unresolved mandatory crisis blocker. E209 consumes this qualification; E210 only converges.

### Border crisis
E271-A is the explicit authored declaration producer. It requires an already active border thread, border tension, and corroborated frontier-warning infrastructure. E271-B explicitly resolves/de-escalates without satisfying the crisis predicate. E195/E253/E255 are consumers and must not manufacture the crisis through reachability alone. E272-A/B are the canonical active-crisis resolution producers. Resolution preserves `border_crisis_declared` as history while clearing the active `pred.border_crisis` through `border_crisis_resolved`.

## Remaining P0 work

1. Enumerate exact durable producers for every domain used by the frozen combination rules.
2. Expand this registry to every concrete durable flag/history marker in E01–E272 with exact consumers.
3. Normalize remaining prose triggers and aliases.
4. Reconcile graph/catalog references and reachability.
5. Audit duplicate semantic events E73/E156 and E99/E173.
6. Reconcile E35–E40 legacy aliases before schema freeze.
7. Verify delayed/replay source identities and exactly-once semantics across the full catalog.

## Gate

**Production schema: BLOCKED.**

**Runtime/reachability: NOT VERIFIED.**

This registry is the source-of-truth QA layer, not runtime data.

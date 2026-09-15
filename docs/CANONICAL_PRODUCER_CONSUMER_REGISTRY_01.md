# Choice Kingdom — Canonical Producer / Consumer Registry 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — WORKING REGISTRY, NOT ENGINE INPUT**
Scope: canonical state families identified across E01–E272.

## Purpose

This registry consolidates the producer audits into one QA surface. A row is **VERIFIED** only when an authored source choice establishes the exact semantic state consumed downstream. A candidate, graph edge, relationship value, or thematic similarity is not sufficient.

The registry deliberately records OPEN rows instead of inventing producers.

## Current canonical status

E271/E272 close the authored border-crisis declaration/resolution lifecycle. The latest QA pass identified and corrected a circular guild-logistics dependency: E136-B is the earlier cooperation source, E194 consumes its history marker, and E194-A supplies the later neutral-inspector qualification. The authoritative catalogs now contain that source correction and have been re-read. Semantic collision distinctions for E55/E269 and E36/E226 have also been applied directly to the authoritative E211–E270 catalog without renumbering IDs.

The latest closure reconciliation also corrected two stale registry/audit interpretations: `history.guild_representation` is explicitly produced by E144-A and E144-B, and `pred.border_crisis` has an authored declaration/resolution lifecycle through E271/E272. These are source-level closures only; runtime evaluation and reachability remain unimplemented.

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
| `history.guild_representation` | history | E144-A/E144-B | E203+ | VERIFIED PRODUCER | both E144 choices establish same representation fact; legacy trigger is alias only |
| `history.guild_logistics_cooperation` | history | E136-B | E194+ | VERIFIED PRODUCER | immutable upstream cooperation marker; E194 consumes it and later supplies neutral inspection |
| `thread.border_crisis` | thread | E271-A declaration; E272-A/B resolution | E195/E240/E251/E253+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | declaration and resolution are distinct authored stages |
| `history.border_crisis_resolved_diplomatically` | history | E272-A | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration while recording diplomatic resolution |
| `history.border_crisis_resolved_by_guarantee` | history | E272-B | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration while recording security resolution |
| `thread.coalition` | thread | E146/E148 | E149/E201/E261+ | PARTIAL | package exists; cooperation qualification is separate |
| `thread.military_constitutional` | thread | E199-A | E204/E227/E256+ | STRONG CANDIDATE | direct constitutional oath producer |
| `thread.endgame_convergence` | thread | E210 candidate convergence node | E265–E270 | OPEN / CONVERGENCE ONLY | never independently resolves missing prerequisites |
| `pred.gold_low` | predicate | `resource.gold` threshold candidate | E193+ | PROVISIONAL | threshold must be balance-verified |
| `pred.security_high` | predicate | `resource.security` threshold candidate | E193+ | OPEN | threshold not frozen |
| `pred.food_stable` | predicate/marker | E138/E167/E192 candidates | E192/E216/E225 | OPEN | deterministic definition required |
| `pred.transport_disruption` | predicate | E136-A/B recovery/clear producer; active disruption source still unidentified | E192/E251+ | PARTIAL | clear/recovery verified; a separate authored active-disruption producer remains open |
| `pred.border_crisis` | predicate | E271-A declaration; E272-A/B resolution | E195/E253/E255+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | active only after declaration and before resolution |
| `pred.guild_logistics_cooperation` | predicate | E136-B upstream marker + E194-A neutral-inspector qualification | downstream guild/ending consumers | VERIFIED SOURCE CHAIN / RUNTIME OPEN | qualification requires prior cooperation marker, neutral inspection, and no unresolved immunity-risk blocker; E194 no longer self-produces its prerequisite |
| `pred.guild_influence_strong` | predicate | E144/E165/E168/E169 + logistics chain candidates | E200 | CONTRACT FROZEN / PRODUCERS OPEN | at least two distinct institutional guild domains; `rel.ivo` alone forbidden |
| `pred.systemic_explanation_verified` | predicate | E132–E135/E232–E236 evidence candidates | E207/endgame | CONTRACT FROZEN / PRODUCER OPEN | three evidence domains plus explicit convergence decision |
| `pred.coalition_cooperation` | predicate | E148-A + distinct faction evidence candidates | E201/E207/E261+ | CONTRACT FROZEN / PRODUCERS OPEN | package + 3 distinct faction identities + no collapse blocker |
| `pred.constitutional_prepared_strong` | predicate | E142/E145/E146/E148/E150 candidates | E197 | CONTRACT FROZEN / PRODUCERS OPEN | three independent upstream institutional domains |
| `pred.budget_reform` | predicate | E142/E154/E198 candidates | E198 | OPEN | audit-office independence, crown audit and legislative budget lock are separate semantics; no exact qualifying combination frozen yet |
| `pred.final_charter_prerequisites` | predicate | E197/E198/E199/E202–E209 candidates | E209/E210 | CONTRACT FROZEN / PRODUCERS OPEN | deterministic upstream set; E209 consumes only |
| `pred.faction_routes_4` | predicate | distinct faction route activations | E261+ | OPEN | distinct route identities required |
| `ending.*` | ending | E265–E270 qualification layer | final result | DESIGN CONTRACT | deterministic multi-input qualification required |

## Verified source closures in latest pass

### Guild representation
E144-A and E144-B explicitly establish the immutable `history.guild_representation` marker consumed by E203. The source trigger `guild_political_representation` is legacy/source-language vocabulary and must be normalized as an alias rather than treated as a second runtime fact.

### Border crisis
E271-A explicitly establishes `border_crisis_declared = true`, `border_crisis_resolved = false`, and `thread.border_crisis = active`. E271-B explicitly de-escalates without satisfying the active crisis predicate. E272-A/B resolve the active crisis while preserving the historical declaration. E195/E253/E255 remain consumers only.

### Guild logistics cooperation
E136-B establishes the immutable upstream `history.guild_logistics_cooperation` marker. E194 consumes that marker. E194-A establishes `guild_neutral_inspectors`; the qualified `pred.guild_logistics_cooperation` requires the prior marker, neutral inspection, and no unresolved immunity-risk blocker. E194 must not self-produce its prerequisite.

## Remaining P0 work

1. Enumerate exact durable producers for every remaining domain used by the frozen combination rules.
2. Expand this registry to every concrete durable flag/history marker in E01–E272 with exact consumers.
3. Normalize remaining prose triggers and aliases.
4. Reconcile graph/catalog references and reachability.
5. Verify delayed/replay source identities and exactly-once semantics across the full catalog.
6. Apply downstream verification for the E55/E269, E36/E226, E37/E227, E39/E229 and E40/E241 distinctions.
7. Resolve remaining OPEN contracts: food stability, active transport disruption, strong guild influence, systemic evidence convergence, coalition cooperation, constitutional preparation, budget reform and final charter prerequisites.

## Gate

**Production schema: BLOCKED.**

**Runtime/reachability: NOT VERIFIED.**

This registry is the source-of-truth QA layer, not runtime data.

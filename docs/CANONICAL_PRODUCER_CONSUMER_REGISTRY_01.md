# Choice Kingdom — Canonical Producer / Consumer Registry 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — WORKING REGISTRY, NOT ENGINE INPUT**
Scope: canonical state families identified across E01–E272.

## Purpose

This registry consolidates the producer audits into one QA surface. A row is **VERIFIED** only when an authored source choice establishes the exact semantic state consumed downstream. A candidate, graph edge, relationship value, or thematic similarity is not sufficient.

The registry deliberately records OPEN rows instead of inventing producers.

## Current canonical status

E271/E272 close the authored border-crisis declaration/resolution lifecycle. The latest QA pass corrected the guild-logistics dependency: E136-B is the earlier cooperation source, E194 consumes its history marker, and E194-A supplies the later neutral-inspector qualification. E144 explicitly establishes the immutable guild-representation history marker. E49's exact representation output is confirmed as `guild_political_representation`, and E50's exact civic/commons output is confirmed as `people_charter_endorsed` from the authoritative E01–E70 producer inventory. These are source-level closures only; runtime evaluation and reachability remain unimplemented.

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
| `guild_political_representation` | state/history source | E49-A | later guild-influence consumers | VERIFIED SOURCE | E49-B `guild_political_exclusion` is the opposing outcome; this is the exact early representation source, not a second domain beyond representation history |
| `people_charter_endorsed` | state/history source | E50-A | E114/E122/E145/E197/E209+ | VERIFIED SOURCE | frozen civic/commons preparation source; later charter consequences are not independent domains |
| `history.guild_logistics_cooperation` | history | E136-B | E194+ | VERIFIED PRODUCER | immutable upstream cooperation marker; E194 consumes it and later supplies neutral inspection |
| `history.winter_severity_declared` | history | E29-A/E29-B | E136/E160/E251+ | VERIFIED PRODUCER | immutable declaration for severe current winter cycle; active severity requires deterministic cycle validity/expiry |
| `thread.border_crisis` | thread | E271-A declaration; E272-A/B resolution | E195/E240/E251/E253+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | declaration and resolution are distinct authored stages |
| `history.border_crisis_resolved_diplomatically` | history | E272-A | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration while recording diplomatic resolution |
| `history.border_crisis_resolved_by_guarantee` | history | E272-B | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration while recording security resolution |
| `thread.coalition` | thread | E146/E148 | E149/E201/E261+ | PARTIAL | package exists; cooperation qualification is separate |
| `thread.military_constitutional` | thread | E199-A | E204/E227/E256+ | STRONG CANDIDATE | direct constitutional oath producer |
| `thread.endgame_convergence` | thread | E210 candidate convergence node | E265–E270 | OPEN / CONVERGENCE ONLY | never independently resolves missing prerequisites |
| `pred.gold_low` | predicate | `resource.gold` threshold candidate | E193+ | PROVISIONAL | threshold must be balance-verified |
| `pred.security_high` | predicate | `resource.security` threshold candidate | E193+ | OPEN | threshold not frozen |
| `pred.food_stable` | predicate/marker | E273-A explicit source candidate | E192/E216/E225 | PARTIAL | source producer identified; later invalidation/expiry still required |
| `pred.transport_disruption` | predicate | E32 explicit active producer; E136/E277 recovery/clear | E192/E251+ | PARTIAL | active producer now closed at source level; lifecycle/persistence still open |
| `pred.border_crisis` | predicate | E271-A declaration; E272-A/B resolution | E195/E253/E255+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | active only after declaration and before resolution |
| `pred.guild_logistics_cooperation` | predicate | E136-B upstream marker + E194-A neutral-inspector qualification | downstream guild/ending consumers | VERIFIED SOURCE CHAIN / RUNTIME OPEN | qualification requires prior cooperation marker, neutral inspection, and no unresolved immunity-risk blocker; E194 no longer self-produces its prerequisite |
| `pred.guild_influence_strong` | predicate | representation=`guild_political_representation`/`history.guild_representation`; tribunal=`guild_tribunal_independent`; market/credit=`official_credit_disclosure`/`audited_monopoly` as one domain; logistics=qualified cooperation | E200 | PARTIAL / SOURCES FROZEN | at least two distinct institutional domains; `rel.ivo` alone forbidden; full producer-before-consumer reconciliation remains open |
| `pred.systemic_explanation_verified` | predicate | E132–E135/E232–E236 evidence candidates | E207/endgame | CONTRACT FROZEN / PRODUCERS OPEN | three evidence domains plus explicit convergence decision |
| `pred.coalition_cooperation` | predicate | E148-A + distinct faction evidence candidates | E201/E207/E261+ | CONTRACT FROZEN / PRODUCERS OPEN | package + explicit participant identities + positive cooperation outcome + no collapse blocker |
| `pred.constitutional_prepared_strong` | predicate | civic=`people_charter_endorsed`; institutional=`crown_audited`/`full_crown_audit_published`; factional=`house_assembly`; military=`military_red_line` | E197 | PARTIAL / SOURCES FROZEN | any 3 independent preparation domains; full anti-double-counting and ordering reconciliation remains open |
| `pred.budget_reform` | predicate | E142/E154/E198 candidates | E198 | OPEN | audit-office independence, crown audit and legislative budget lock are separate semantics; no exact qualifying combination frozen yet |
| `pred.final_charter_prerequisites` | predicate | E197/E198/E199/E202–E209 candidates | E209/E210 | CONTRACT FROZEN / PRODUCERS OPEN | deterministic upstream set; E209 consumes only |
| `pred.faction_routes_4` | predicate | distinct faction route activations | E261+ | OPEN | distinct route identities required |
| `ending.*` | ending | E265–E270 qualification layer | final result | DESIGN CONTRACT | deterministic multi-input qualification required |

## Verified source closures in latest pass

### Guild representation
E49-A is confirmed as `guild_political_representation`; E49-B is `guild_political_exclusion`. E144-A/E144-B later establish immutable `history.guild_representation`. E49 and E144 are therefore the same institutional representation domain across campaign time, not two independent guild domains.

### Civic / commons preparation
E50-A is confirmed as `people_charter_endorsed`. This is the frozen civic/commons preparation source for `pred.constitutional_prepared_strong`. Later civic consequences from the same charter decision cannot be double-counted as independent preparation domains.

### Border crisis
E271-A explicitly establishes `border_crisis_declared = true`, `border_crisis_resolved = false`, and `thread.border_crisis = active`. E271-B explicitly de-escalates without satisfying the active crisis predicate. E272-A/B resolve the active crisis while preserving the historical declaration. E195/E253/E255 remain consumers only.

### Guild logistics cooperation
E136-B establishes the immutable upstream `history.guild_logistics_cooperation` marker. E194 consumes that marker. E194-A establishes `guild_neutral_inspectors`; the qualified `pred.guild_logistics_cooperation` requires the prior marker, neutral inspection, and no unresolved immunity-risk blocker. E194 must not self-produce its prerequisite.

### Winter severity
E29-A and E29-B are the explicit authored producer for `pred.winter_severe` during the severe winter cycle. They retain `history.winter_severity_declared` as immutable history. The active predicate must later be represented with deterministic cycle identity and explicit expiry/recovery; downstream consumers cannot manufacture it.

## Remaining P0 work

1. Enumerate exact durable producers for every remaining domain used by the frozen combination rules.
2. Expand this registry to every concrete durable flag/history marker in E01–E272 with exact consumers.
3. Normalize remaining prose triggers and aliases.
4. Reconcile graph/catalog references and reachability.
5. Verify delayed/replay source identities and exactly-once semantics across the full catalog.
6. Apply downstream verification for the E55/E269, E36/E226, E37/E227, E39/E229 and E40/E241 distinctions.
7. Resolve remaining OPEN contracts: food stability, active transport lifecycle, strong guild influence, systemic evidence convergence, coalition cooperation, constitutional preparation, budget reform and final charter prerequisites.

## Gate

**Production schema: BLOCKED.**

**Runtime/reachability: NOT VERIFIED.**

This registry is the source-of-truth QA layer, not runtime data.

# Choice Kingdom — Canonical Producer / Consumer Registry 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — WORKING REGISTRY, NOT ENGINE INPUT**
Scope: **frozen production E01–E272 only**.

## Scope-integrity rule

Only event IDs `E01..E272` may contribute production producers, consumers, predicates, delayed sources, or reachability edges. E273–E277 are expansion candidates and are excluded from the frozen production catalog.

This registry deliberately records OPEN rows instead of inventing producers or aliases.

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
| `history.guild_representation` | history | E144-A/E144-B | E203+ | VERIFIED PRODUCER | same institutional domain; not a second guild domain |
| `guild_political_representation` | state/history source | E49-A | later guild-influence consumers | VERIFIED SOURCE | E49-B is opposing `guild_political_exclusion` |
| `people_charter_endorsed` | state/history source | E50-A | E114/E122/E145/E197/E209+ | VERIFIED SOURCE | later civic consequences must not double-count this domain |
| `history.guild_logistics_cooperation` | history | E136-B | E194+ | VERIFIED PRODUCER | E194 consumes upstream marker |
| `history.winter_severity_declared` | history | E29-A/E29-B | E136/E160/E251+ | VERIFIED PRODUCER | immutable history; active predicate needs cycle validity |
| `thread.border_crisis` | thread | E271-A declaration; E272-A/B resolution | E195/E240/E251/E253+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | declaration and resolution are separate stages |
| `history.border_crisis_resolved_diplomatically` | history | E272-A | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration |
| `history.border_crisis_resolved_by_guarantee` | history | E272-B | later callbacks/ending QA | VERIFIED PRODUCER | preserves historical declaration |
| `thread.coalition` | thread | E146/E148 | E149/E201/E261+ | PARTIAL | package exists; cooperation qualification is separate |
| `thread.military_constitutional` | thread | E199-A | E204/E227/E256+ | STRONG CANDIDATE | direct constitutional oath producer |
| `thread.endgame_convergence` | thread | E210 candidate convergence node | E265–E270 | OPEN / CONVERGENCE ONLY | never independently resolves missing prerequisites |
| `pred.gold_low` | predicate | `resource.gold` threshold candidate | E193+ | PROVISIONAL | threshold must be balance-verified |
| `pred.security_high` | predicate | `resource.security` threshold candidate | E193+ | OPEN | threshold not frozen |
| `pred.food_stable` | predicate | **NO IN-SCOPE PRODUCER VERIFIED** | E192/E216/E225 | OPEN / BLOCKED | E273-A excluded; no E01–E272 producer admitted |
| `pred.transport_disruption` | predicate | E32 active producer; E136-A/B recovery/clear | E192/E251+ | PARTIAL | lifecycle/persistence/ordering still open |
| `pred.border_crisis` | predicate | E271-A declaration; E272-A/B resolution | E195/E253/E255+ | VERIFIED SOURCE LIFECYCLE / RUNTIME OPEN | active only between declaration and resolution |
| `pred.guild_logistics_cooperation` | predicate | E136-B upstream marker + E194-A neutral inspection | downstream guild/ending consumers | VERIFIED SOURCE CHAIN / RUNTIME OPEN | requires prior cooperation + inspection + no unresolved immunity-risk blocker |
| `pred.guild_influence_strong` | predicate | representation=`guild_political_representation`/`history.guild_representation`; tribunal=`guild_tribunal_independent`; market/credit=`official_credit_disclosure`/`audited_monopoly` as one domain; logistics=qualified cooperation | E200 | PARTIAL / SOURCES FROZEN | at least two distinct institutional domains; `rel.ivo` alone forbidden |
| `pred.systemic_explanation_verified` | predicate | E232–E236 evidence families + E270-A explicit convergence (`systemic_explanation_convergence`) | E207/endgame | SOURCE-CLOSED / RUNTIME OPEN | E270-A requires the three evidence families to already exist; it cannot manufacture missing evidence |
| `pred.coalition_cooperation` | predicate | E148-A + E261-A cooperation-package candidates | E201/E207/E261+ | PARTIAL / SOURCES FROZEN | positive cooperation, participant identity and blocker lifecycle required |
| `pred.constitutional_prepared_strong` | predicate | civic=`people_charter_endorsed`; institutional=`crown_audited`/`full_crown_audit_published`; factional=`house_assembly`; military=`army_constitution_oath` | E197 | PARTIAL / SOURCES FROZEN | any 3 independent preparation domains; anti-double-counting and reachability remain open |
| `pred.budget_reform` | predicate | E142-A `auditor_independence` + E154-A `crown_audited` + E198-A `legislative_budget_lock` | E258+ | SOURCE CLOSED / EXECUTABLE QUALIFICATION PARTIAL | E142-B/E154-B/E198-B are explicit blockers; E155-A same audit domain; E258 consumer-only |
| `pred.final_charter_prerequisites` | predicate | E197/E198/E199/E202–E209 candidates | E209/E210 | CONTRACT FROZEN / PRODUCERS OPEN | E209 consumes only |
| `pred.faction_routes_4` | predicate | distinct faction route activations | E261+ | OPEN | distinct route identities required |
| `ending.*` | ending | E265–E270 qualification layer | final result | DESIGN CONTRACT | deterministic multi-input qualification required |

## Excluded-source contamination audit

The following references are explicitly rejected from the frozen production registry:

- `E273-A` as a producer for `pred.food_stable`.
- `E277` as a transport-recovery producer.
- Any E273–E277 producer, consumer, delayed source, predicate source or reachability edge introduced by future QA work.

## Remaining P0 closure work

1. Exhaustively enumerate concrete durable producers for E01–E272.
2. Resolve undefined producers/consumers without invented aliases.
3. Detect duplicate semantic writers and contradictory writers.
4. Normalize prose-derived predicates into deterministic formulas or explicit source-backed markers.
5. Reconcile `EVENT_GRAPH.md` against actual authored trigger/effect relationships.
6. Close E184/E185/E242–E246 delayed lifecycle contracts.
7. Close replay `meta.*` producers/keys for E186/E247/E248; E270 ordinary convergence is not replay promotion.
8. Verify downstream distinctions for E55/E269, E36/E226, E37/E227, E39/E229 and E40/E241.
9. Run fresh-run reachability only after the source contract inventory is sufficiently closed.

## Gate

**S08: IN PROGRESS.**

**Production schema: BLOCKED.**

**Runtime/reachability: NOT VERIFIED.**

This registry is the canonical QA surface, not runtime data.
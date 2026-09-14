# Choice Kingdom — Producer / Consumer Closure Matrix 01

Date: 2026-09-15
Status: **CANONICAL QA MATRIX — NOT ENGINE INPUT**

## Purpose

This matrix turns the current producer/consumer registry into an actionable closure order. A state key is CLOSED only when an exact authored producer exists, its semantics are unambiguous, all known consumers are identified, and no circular derivation is introduced.

## Closure priorities

| Priority | State family | Current status | Closure requirement |
|---|---|---|---|
| P0 | `history.guild_representation` | OPEN | exact authored choice must create durable representation history |
| P0 | `pred.food_stable` | OPEN | deterministic authored/derived definition; no new resource |
| P0 | `pred.transport_disruption` | OPEN | source event, persistence, clear rule |
| P0 | `pred.border_crisis` | OPEN | explicit escalation producer distinct from security-low |
| P0 | `pred.guild_logistics_cooperation` | OPEN | exact cooperation combination and source |
| P0 | `pred.guild_influence_strong` | OPEN | explicit authored combination; never `rel.ivo` alone |
| P0 | `pred.systemic_explanation_verified` | OPEN | explicit evidence set and conclusion rule |
| P0 | `pred.coalition_cooperation` | OPEN | authored cooperation semantics; not route-count shorthand |
| P0 | `pred.constitutional_prepared_strong` | OPEN | exact minimum history/route combination |
| P0 | `pred.final_charter_prerequisites` | OPEN | non-circular final prerequisite set |
| P0 | `thread.constitutional_late` | OPEN | explicit activation source and timing semantics |
| P0 | `thread.final_constitutional_phase` | OPEN | one durable activation rule |
| P1 | `pred.security_high` | OPEN | balance-tested numeric threshold |
| P1 | `pred.gold_low` | PROVISIONAL | balance-test current candidate threshold |
| P1 | `pred.faction_routes_4` | OPEN | distinct route identity definition |
| P1 | `pred.budget_reform` | OPEN | distinguish audit reform from budget reform |
| P1 | `thread.border_crisis` | PARTIAL | reconcile candidate producers into one canonical activation |
| P1 | `thread.coalition` | PARTIAL | freeze membership/cooperation semantics |
| P1 | `thread.ivo_market` | PARTIAL | exact activation marker and route lifetime |
| P1 | `thread.mara_audit` | PARTIAL | exact activation marker |
| P1 | `thread.rowan_security` | PARTIAL | exact route marker distinct from security resource |
| P1 | `thread.seris_houses` | PARTIAL | exact route marker |
| P1 | `thread.amara_civic` | PARTIAL | exact activation marker |
| P1 | `thread.toma_information` | PARTIAL | exact activation marker |
| P1 | `thread.archive` | PARTIAL | distinguish access, investigation and reform |
| P1 | `thread.winter_crisis` | PARTIAL | severity/history source and clear rule |
| P1 | `thread.ledger_investigation` | STRONG CANDIDATE | explicit chain activation and evidence-set contract |
| P1 | `thread.military_constitutional` | STRONG CANDIDATE | preserve E199-A semantics and verify consumers |
| P2 | `history.cross_faction_package` | VERIFIED | E148-A; compile immutable marker |
| P2 | `history.house_assembly` | VERIFIED | E161-A; compile immutable marker |
| P2 | `history.six_signatures_public` | VERIFIED | E146-A |
| P2 | `history.six_signatures_private` | VERIFIED | E146-B |
| P2 | `history.redaction_reconstructed` | VERIFIED | E132-A |
| P2 | `history.form_pattern_tested` | VERIFIED | E133-A |
| P2 | `history.office_network_mapped` | VERIFIED | E134-A |
| P2 | `history.conflicting_testimony_recorded` | VERIFIED | E135-A |
| P2 | `history.payment_date_crosscheck` | VERIFIED | E187-A |
| P2 | `history.emergency_language_compared` | VERIFIED | E131-A |
| P2 | `flag.crown_audited` | VERIFIED | E154-A |
| P2 | `flag.emergency_powers_expire` | VERIFIED | E197-A |
| P2 | `flag.emergency_powers_inherit` | VERIFIED | E197-B |

## Producer rules

### Rule A — exact choice output wins
If an authored choice explicitly sets a durable state key, that choice is the preferred producer. A nearby event theme, route name, relationship value, or graph edge cannot replace it.

### Rule B — candidate chains are not closure
A chain such as E132 → E133 → E134 → E135 is evidence of authored progression, but it does not automatically create `pred.systemic_explanation_verified`. The final predicate needs a defined convergence rule.

### Rule C — numeric resources remain numeric
Gold, trust, security, power and reputation remain resources. `food_stable`, `border_crisis`, `guild_influence_strong`, etc. are semantic predicates/markers and must not become hidden sixth/seventh resources.

### Rule D — relationships are supporting signals
`rel.mara`, `rel.rowan`, `rel.seris`, `rel.ivo`, `rel.amara`, and `rel.toma` may gate character scenes but cannot silently qualify institutional, military, guild, civic, information, or constitutional routes.

### Rule E — route state must be durable
A route consumer must be able to determine whether the route is active/completed from explicit thread/history state. It must not infer activation from the most recent event or a relationship score.

### Rule F — no circular predicates
A predicate cannot be its own producer, directly or through an ending prerequisite chain. In particular, final constitutional prerequisites cannot require the final constitutional phase if that phase itself requires the prerequisites.

### Rule G — replay boundary
`meta.*` may transfer only through an explicit replay contract. It cannot satisfy ordinary current-run `hist.*`, `thread.*`, or `pred.*` keys by implicit coercion.

## Evidence closure contract

The systemic explanation predicate must eventually specify a distinct set of evidence IDs. Current authored investigation evidence includes:

- `history.emergency_language_compared`
- `history.redaction_reconstructed`
- `history.form_pattern_tested`
- `history.office_network_mapped`
- `history.conflicting_testimony_recorded`
- `history.payment_date_crosscheck`

The final predicate must state exactly which distinct evidence conclusions are mandatory, which are optional, and whether replay-transfer evidence can substitute for a missing current-run item. Counting arbitrary evidence fragments is insufficient.

## Coalition closure contract

`pred.coalition_cooperation` must be distinct from `pred.faction_routes_4`.

- `pred.faction_routes_4` = at least four distinct route identities satisfy their explicit route activation rules.
- `pred.coalition_cooperation` = the authored choices demonstrate actual cross-faction cooperation, negotiation or package adoption.
- `history.cross_faction_package` is a verified authored input from E148-A.

Four active routes without cooperation must not qualify coalition cooperation.

## Border closure contract

`pred.border_crisis` must not be derived solely from `resource.security <= threshold`.

The canonical border predicate must have an authored escalation source, persistence semantics, and clear/recovery rule. Border tension, low security, military readiness, and diplomatic reputation remain separate concepts unless a later authored rule explicitly combines them.

## Food stability closure contract

`pred.food_stable` must not introduce a sixth numeric resource. It should compile from explicit food-related authored history/markers and/or a documented deterministic derived rule using existing state. E192 already provides an important branch where prioritizing grain explicitly changes downstream food stability; that semantics must be preserved rather than replaced by a generic gold/trust threshold.

## Guild closure contract

The canonical commercial route is `thread.ivo_market`. Guild cooperation and strong guild influence are separate predicates:

- `pred.guild_logistics_cooperation` — cooperation in logistics/trade-risk handling;
- `pred.guild_influence_strong` — durable political/economic leverage sufficient for later constitutional/commercial choices.

Neither may be inferred from `rel.ivo` alone.

## Constitutional closure contract

The constitutional family must be compiled in dependency order:

1. authored preparation markers/routes;
2. constitutional choices and durable history;
3. emergency-power constraints/expiry;
4. final charter prerequisites;
5. final constitutional phase/convergence;
6. E265–E270 ending qualification.

No later node may become a hidden producer of its own prerequisite.

## QA gates before schema freeze

- [ ] Every durable producer has an exact source choice ID.
- [ ] Every consumer has an exact event ID or ending qualifier.
- [ ] No stale identifier survives as canonical runtime vocabulary.
- [ ] No relationship is used as a route substitute.
- [ ] No pressure is represented as a new resource.
- [ ] No predicate is circular.
- [ ] Delayed effects have stable source/consequence identity and exact-once semantics.
- [ ] Replay metadata has explicit transfer rules.
- [ ] Legacy E35–E40 concepts are mapped to canonical Act V/ending layers.
- [ ] Semantic duplicates E73/E156 and E99/E173 are reconciled.
- [ ] Reachability simulation is run against the closed catalog.
- [ ] Ending simulations are run from authored state fixtures.

## Gate

**Producer/consumer closure: in progress.**

**Production schema: BLOCKED until P0 rows are closed or explicitly authored as intentionally unresolved content gaps.**

**Engine implementation: intentionally deferred.**

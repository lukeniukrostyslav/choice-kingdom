# Choice Kingdom — Scenario QA Pass 02: Static Closure

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Expansion candidates E273–E277: **excluded**  
Status: **SCENARIO QA — STATIC CLOSURE PASS**

## Purpose

This pass advances scenario QA without starting engine, UI, Android or APK work. It reconciles the current canonical QA documents into one explicit machine-check checklist and closes only facts supported by the authoritative authored catalog and source audits.

The frozen denominator remains E01–E272. No E273–E277 producer is allowed to satisfy an E01–E272 consumer until those events are formally admitted to the production catalog.

## 1. Source-of-truth rule

Authoritative narrative sources currently cover:
- E01–E34 — `docs/EVENT_CATALOG.md`
- E35–E70 — `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`
- E71–E110 — `docs/EVENT_EXPANSION_071_110.md`
- E111–E150 — `docs/EVENT_CATALOG_EXPANSION_111_150.md`
- E151–E210 — `docs/EVENT_CATALOG_EXPANSION_151_210.md`
- E211–E270 — `docs/EVENT_CATALOG_EXPANSION_211_270.md`
- E271–E272 — `docs/EVENT_CATALOG_EXPANSION_271_280.md`

`EVENT_GRAPH.md` is a causal consistency target, not an independent producer source.

## 2. Closed source-level facts

| Fact | Producer | Status |
|---|---|---|
| `public_bridge` | E18-B | CLOSED |
| `flexible_accounts` | E09-B | CLOSED |
| `veteran_patronage` | E117-B | CLOSED |
| `estate_exception` | E118-B | CLOSED |
| `border_compensation` | E125-A | CLOSED |
| `requisition_compensation` | E156-A | CLOSED |
| `winter_rent_ceiling` | E160-A | CLOSED |
| `history.guild_logistics_cooperation` | E136-B | CLOSED |
| `history.guild_representation` | E144-A/B | CLOSED |
| `history.cross_faction_package` | E148-A | CLOSED |
| `pred.market_pressure` current cycle | E19-B | CLOSED at source level |
| clear `pred.market_pressure` current cycle | E19-A | CLOSED at source level |
| `pred.winter_severe` current cycle | E29-A/B | CLOSED at source level |
| `pred.transport_disruption` current cycle | E32 | CLOSED at source level |
| clear `pred.transport_disruption` | E136-A/B | CLOSED at source level |
| `pred.border_crisis` | E271-A | CLOSED at source level |
| clear `pred.border_crisis` | E272-A/B | CLOSED at source level |
| military constitutional evidence | E199-A | STRONG source evidence |

## 3. Reconciled transport-disruption lifecycle

An earlier audit used wording that the active producer was still open. The later source re-read supersedes that wording: E32 explicitly establishes the current `pred.transport_disruption` crisis outcome, while E136-A/B are the recovery/clear producers.

Canonical source-level contract:

`E32 -> pred.transport_disruption(active)`  
`E136-A/B -> pred.transport_disruption(clear)`

Runtime lifecycle remains OPEN: persistence through save/load, ordering against delayed effects, expiry/supersession and exact cycle identity still require formal contracts.

## 4. Delayed consequence closure

| Delayed consumer | Source identity | Result |
|---|---|---|
| E181 | E45-B infrastructure/toll concession | SOURCE CLOSED; lifecycle OPEN |
| E182 | E117-B `veteran_patronage` | CLOSED |
| E183 | E118-B `estate_exception` | CLOSED |
| E184 | secret evidence route | OPEN — no safe producer |
| E185 | E17-A `cheap_weapons` | SOURCE CLOSED; crisis lifecycle OPEN |
| E242 | E118-B prior noble exception | PARTIAL; scope explicit |
| E243 | E18-B `public_bridge` | CLOSED after vocabulary normalization |
| E244 | E09-B `flexible_accounts` | CLOSED |
| E245 | compensation route | OPEN; E125-A and E156-A cannot be silently unioned |
| E246 | E160-A `winter_rent_ceiling` | CONDITIONAL; vocabulary normalization required |

No delayed callback is runtime-ready until source choice, choice identity, target/resolution identity, exact timing/condition, exactly-once identity and cancellation/supersession semantics are defined.

## 5. Replay boundary

The run boundary is a hard invariant:
- fresh runs do not inherit run-local flags/history;
- pending delayed callbacks do not cross runs;
- active crisis predicates do not cross runs;
- ordinary `flag.*`/`history.*` cannot become `meta.*` implicitly;
- only explicitly authored `meta.*` information may cross the boundary.

E186, E247, E248 and E270 remain consumer intents without source-closed replay producers/keys. Replay isolation is contract-closed; replay producer/key coverage is not.

## 6. Derived predicate anti-shortcuts

The following remain binding QA rules:
- `rel.ivo` alone cannot satisfy `pred.guild_influence_strong`.
- E194 cannot satisfy `pred.guild_logistics_cooperation` from its own trigger.
- `thread.border` cannot be treated as `thread.border_crisis`.
- security alone cannot satisfy `pred.border_crisis`.
- E197 cannot self-create `pred.constitutional_prepared_strong`.
- E209 cannot manufacture `pred.final_charter_prerequisites`.
- `four_way_bargain` alone cannot satisfy `pred.coalition_cooperation`.
- ordinary history/flags cannot be promoted to `meta.*`.
- `price ceiling` is not a generic alias for every price-control state.
- `compensation route` is not a union of distinct compensation facts without an authored qualification rule.

## 7. Ending QA status

Frozen ending families:
1. Steward
2. Iron Crown
3. Golden Compact
4. People's Charter
5. Broken Diadem
6. Quiet Throne
7. Second Founder

The design requirement is deterministic, predicate-based and causal. Exhaustive incoming-path coverage and deterministic precedence proof are still missing. Broken Diadem and Quiet Throne remain particularly open because their failure/withdrawal producers are not fully frozen.

## 8. Remaining static gates

1. Exhaustive concrete output-token inventory for E01–E272.
2. Exhaustive trigger-token inventory for E01–E272.
3. Duplicate semantic writer detection.
4. Contradictory writer detection.
5. Undefined producer/consumer detection.
6. Predicate dependency-cycle detection.
7. Exact delayed callback identity and cancellation/supersession matrix.
8. Exhaustive ending incoming paths and deterministic precedence.
9. Exact replay `meta.*` producer/key closure.
10. Fresh-run causal reachability simulation.
11. Representative replay reachability simulation.
12. Graph-vs-catalog edge reconciliation.

## Gate result

**Scenario QA remains 65%.** This pass improves the closure record and removes an audit wording contradiction, but does not justify inflating the metric before the remaining exhaustive checks are performed.

**Engine/UI/Android/APK work remains intentionally blocked by plan.**

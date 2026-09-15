# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings and replayable paths.

## Release target
- Android-first premium one-time purchase, approximately €2.99–€4.99.
- No ads, no subscription, no mandatory backend for core gameplay.
- 20+ locales including RTL and long-string validation.
- Full authored campaign target: approximately 250–350+ meaningful nodes and 8–12 recognizable endings.

## Frozen authored scope
Production catalog is **E01–E272**. E273–E277 are expansion candidates and are excluded from production semantics, producer/consumer edges and reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.**

No mock/stub gameplay or premature production-readiness claims.

## Current phase
**Narrative/content canonicalization and QA.** Authored checkpoint E01–E272. Production schema and Decision Engine remain blocked until canonical contracts and reachability are sufficiently closed.

## Scenario QA
Dedicated Scenario QA score remains **65%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **55%**
- S07 **80%**
- S08 **78%**
- S09 **60%**
- S10 **72%**
- S11 **55%**
- S12 **35%** — S12.2 source closure, S12.3 invariant audit, S12.4 patch gate, S12.5 authoritative P0 source reconciliation, S12.6 machine P0 delta and S12.7 P0 identity normalization completed; exhaustive machine graph, exact composite formulas and reachability remain open.

## Latest QA work
- **S12.7** added `docs/SCENARIO_QA_S12_7_P0_IDENTITY_NORMALIZATION_CONTRACT_01.md`, commit `066584f94358c5584623097de2abc933c17ad4e3`. E144, E148, E136/E194 and E192 identity boundaries are normalized without inventing producers or aliases.
- **S12.6** added `docs/SCENARIO_QA_S12_6_P0_MACHINE_DELTA_01.md`. It normalized closed P0 producer/consumer edges and established machine acceptance/rejection rules.
- **S12.5** added `docs/SCENARIO_QA_S12_5_P0_AUTHORITATIVE_SOURCE_RECONCILIATION_01.md`, commit `f0c1daac7693cb60040b1e6aa270ff68ce47bbd4`. It re-read authoritative catalog evidence and verified that E136, E144, E192 and E194 source patches are actually present; E148 is authored with six named participants but still needs machine-normalized participant identities. It explicitly rejects an implicit E192 `food_logistics_stabilized` → `pred.food_stable` alias.
- **S12.4** added `docs/SCENARIO_QA_S12_4_SOURCE_PATCH_APPLICATION_GATE_01.md`, commit `17a74ef695cd0f9b94e2a20b80f3669dbda0cd74`.
- **S12.3** added `docs/SCENARIO_QA_S12_3_CANONICAL_INVARIANT_AUDIT_01.md`, commit `860444b28cd6e3e36024f9ebf9609b80532efa07`.
- **S12.2** added `docs/SCENARIO_QA_S12_2_SOURCE_CLOSURE_DELTA_AUDIT_01.md`, commit `6c8e82e825e7bcbeeb9d6f105ed7f4f9fd744559`; E32 is the explicit active transport producer and E136-A/B clear it.
- **S12.1** added the machine-oriented reachability anchor inventory in commit `a61ac9de61f4c448c511e123be38cea12b3b0f5b8`.
- Canonical budget reform source closure identifies E142-A `auditor_independence`, E154-A `crown_audited` and E198-A `legislative_budget_lock` as the three-domain source candidate set. Predicate validation remains partial.
- Canonical closure audit confirms source-level closure for guild representation, border crisis and guild logistics while keeping food stability, composite guild influence, systemic explanation, coalition cooperation, constitutional preparation and final-charter prerequisites appropriately open/partial.
- S11 ending audit established consumer-only ending qualification and rejected generic-score/consumer-as-producer shortcuts.
- S10.5 closed the semantic QA boundary for delayed lifecycle, persistence and replay isolation while executable callback contracts remain open pending exact source extraction.
- S10.4 reconciled delayed source identities for E181–E185 and E242–E246.
- S09.8 normalized the closed dependency graph and rejected self-satisfaction, alias leakage and E273–E277 contamination.

## Authoritative P0 source status
Confirmed in authored catalog text:
- E136-A/B → `transport_network_stable`; clears `transport_disruption_active`; E136-B also establishes guild logistics cooperation history.
- E144-A/B → `history.guild_representation`.
- E148-A → `history.cross_faction_package` plus named six-participant package evidence; normalized identities are now `faction.mara`, `faction.rowan`, `faction.seris`, `faction.ivo`, `faction.amara`, `faction.toma`.
- E192-A/B → `food_logistics_unstable` / `food_logistics_stabilized`; no sixth resource and no implicit `pred.food_stable` alias.
- E194-A/B → neutral-inspection vs immunity-risk branches; qualified logistics cooperation remains dependent on upstream cooperation marker and blocker absence.
- E271/E272 → canonical border declaration/resolution source chain.
- E197/E200/E207/E209/E210 → canonical contracts preserve consumer-only/convergence-only boundaries; exact formulas/evidence IDs remain open.

## Canonical producer/consumer status
Source-level closed chains include:
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E136-B → `history.guild_logistics_cooperation` → E194
- E144-A/B → `history.guild_representation`
- E271-A → active `pred.border_crisis`; E272-A/B resolve it
- E32 → active `pred.transport_disruption`; E136-A/B clear it
- E142-A/E154-A/E198-A → budget-reform source domains

Important unresolved/open areas:
- `pred.food_stable` and its relationship to `food_logistics_stabilized`
- exact machine formula for `pred.guild_influence_strong`
- exact evidence IDs and lifecycle for `pred.systemic_explanation_verified`
- `pred.coalition_cooperation` runtime qualification and invalidation
- `pred.constitutional_prepared_strong`
- `pred.final_charter_prerequisites`
- replay `meta.*` producers/keys for E247/E248/E270
- exact delayed identities/timing/cancellation for remaining open families
- complete incoming paths and deterministic precedence for endings
- exhaustive E01–E272 producer/consumer graph and fresh-run reachability
- machine graph ↔ authoritative catalog equality

## Canonical vocabulary rules
State namespaces are `resource.*`, `rel.*`, `flag.*`, `history.*`, `thread.*`, `delay.*`, `ending.*`, and explicit `meta.*` for intentionally persistent cross-run knowledge. Contextual concepts such as food pressure or winter severity must be deterministic predicates or durable markers, never silently become a sixth resource.

Delayed consequences require source choice/event, earliest turn, latest turn or resolution condition, target, exactly-once key, cancellation/supersession rule and save/load persistence. Vague prose such as “later” is not executable timing.

## Hard negative rules
- A consumer cannot manufacture its own prerequisite.
- `rel.ivo` cannot equal strong guild influence.
- E197 cannot manufacture constitutional preparedness.
- E209 cannot manufacture final-charter prerequisites.
- E210 is convergence-only.
- `four_way_bargain` does not alone prove coalition cooperation.
- security alone does not prove border crisis.
- E136 recovery cannot reactivate transport disruption.
- ordinary run state cannot automatically become `meta.*`.
- E273–E277 cannot contribute production edges.
- `food_logistics_stabilized` must not silently alias `pred.food_stable` until its complete authored predicate/lifecycle contract is explicitly closed.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **98%**
- Derived predicates / machine contracts: **86%**
- Delayed Consequences: **88%**
- Replay / Meta-state: **57%**
- Endings / precedence: **63%**
- Reachability / causal graph: **49%**
- Production data schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress is approximately **54%**. Scenario QA remains **65%** and must not be conflated with overall project completion.

## Next autonomous work
1. Extract exact E197/E200/E207/E209/E210 authored rows into the machine producer/consumer registry.
2. Compile immutable evidence IDs for systemic explanation and exact cardinality/formulas for composite predicates.
3. Continue exhaustive E01–E272 producer/consumer inventory and canonical vocabulary normalization.
4. Continue exact source extraction for E218/E225 and E251–E272 delayed/lifecycle rows.
5. Reconcile S11 ending incoming paths and deterministic precedence against the expanded graph.
6. Run fresh-run and representative replay reachability from canonical initial state.
7. Freeze production contracts only after machine checks are clean enough.
8. Then build Decision Engine → UI → localization → automated/runtime verification → Android → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes. Owner-controlled release gates must never be falsely marked complete.

## Project separation
`rulebreak8` is unrelated and must not be used as a readiness source for Choice Kingdom.

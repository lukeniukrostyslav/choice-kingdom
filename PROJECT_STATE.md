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
Dedicated Scenario QA score is now approximately **77%**. This is distinct from overall project completion and is not runtime/Android readiness.

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
- S12 **62%** — S12.21 reconciled the E242–E246 long-delay source matrix: E242–E244 source identities are closed candidates, E245 remains explicitly multi-candidate, and E246 remains open pending exact price-ceiling producer recovery. Relative timing is not falsely promoted to executable timing.

## Latest QA work
- **S12.21** added `docs/SCENARIO_QA_S12_21_LONG_DELAY_SOURCE_MATRIX_01.md`, commit `1e9ad37a6984d78ba61ef5e23e53551d7a40f232`.
- **S12.20** added `docs/SCENARIO_QA_S12_20_E272_EXACT_SOURCE_RECOVERY_01.md`, commit `92c3c3460c9621fe306c26f97079713a180eadee`.
- **S12.19** added `docs/SCENARIO_QA_S12_19_REPLAY_META_BOUNDARY_AUDIT_01.md`, commit `cc6936e6c6ffd9074e57f9ba65d62ff7ea4c2075`.
- **S12.18** added `docs/SCENARIO_QA_S12_18_COMPOSITE_PRODUCER_ORDER_AUDIT_01.md`, commit `33df93136f52883c4c897e414b0640fb6db89b56`.

## Authoritative P0 source status
Confirmed in authored catalog text:
- E136-A/B → `transport_network_stable`; clears `transport_disruption_active`; E136-B also establishes guild logistics cooperation history.
- E144-A/B → `history.guild_representation`.
- E148-A → `history.cross_faction_package` plus named six-participant package evidence; normalized identities are `faction.mara`, `faction.rowan`, `faction.seris`, `faction.ivo`, `faction.amara`, `faction.toma`.
- E192-A/B → `food_logistics_unstable` / `food_logistics_stabilized`; no sixth resource and no implicit `pred.food_stable` alias.
- E194-A/B → neutral-inspection vs immunity-risk branches; qualified logistics cooperation remains dependent on upstream cooperation marker and blocker absence.
- E271-A → formal border-crisis declaration; E271-B → non-crisis resolution.
- **E272-A/B exact source recovered:** E272-A ratifies the joint border settlement and records `history.border_crisis_resolved_diplomatically`; E272-B ends the crisis under a military security guarantee and records `history.border_crisis_resolved_by_guarantee`. Both preserve `border_crisis_declared=true`, set `border_crisis_resolved=true`, clear active `pred.border_crisis`, and require E271-A's active crisis plus an authored resolution route.
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
- E271-A → active `pred.border_crisis`; E272-A/B resolve it with exact source tokens now recovered
- E32 → active `pred.transport_disruption`; E136-A/B clear it
- E142-A/E154-A/E198-A → budget-reform source domains

### Long-delay source matrix S12.21
- E242 → E118-B `estate_exception`: source identity closed candidate; exact executable timing/lifecycle open.
- E243 → E18-B `public_bridge`: source identity closed; exact executable timing/lifecycle open.
- E244 → E09-B `flexible_accounts`: source identity closed; exact executable timing/lifecycle open.
- E245 → E125-A `border_compensation` and E156-A `requisition_compensation`: remain distinct candidates; no false merge.
- E246 → exact price-ceiling producer still open; no generic alias admitted.

Important unresolved/open areas:
- `pred.food_stable` and its relationship to `food_logistics_stabilized`
- exact machine formula and immutable evidence IDs for `pred.guild_influence_strong`
- exact evidence IDs and lifecycle for `pred.systemic_explanation_verified`
- `pred.coalition_cooperation` runtime qualification and invalidation
- `pred.constitutional_prepared_strong`
- `pred.final_charter_prerequisites`
- replay `meta.*` producers/keys for E247/E248/E270
- exact delayed identities/timing/cancellation for remaining open families
- E245 route disambiguation and E246 exact price-ceiling producer
- complete incoming paths and deterministic precedence for endings
- exhaustive E01–E272 producer/consumer graph and fresh-run reachability
- machine graph ↔ authoritative catalog equality

## Replay QA boundary
E247 is explicitly a second-run information route and E248 an explicit replay callback. Neither may be satisfied by ordinary first-run flags without a declared `meta.*` key and producer. E270's dual-witness evidence remains ordinary run evidence unless the authored source explicitly promotes it. No implicit cross-run persistence is admitted.

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
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **95%**
- Delayed Consequences: **92%**
- Replay / Meta-state: **65%**
- Endings / precedence: **69%**
- Reachability / Causal Graph: **58%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA is approximately **77%** and must not be conflated with overall project completion.

## Next autonomous work
1. Compile immutable evidence IDs and exact executable formulas for systemic explanation, guild influence, coalition cooperation, constitutional preparation, budget reform and final-charter prerequisites.
2. Recover E246 exact price-ceiling producer and resolve E245 compensation-route semantics without merging distinct sources.
3. Reconcile all remaining E01–E272 producer/consumer edges and canonical vocabulary.
4. Build the complete delayed identity/timing/cancellation matrix and verify save/load/replay isolation.
5. Reconcile S11 ending incoming paths and deterministic precedence against the expanded graph.
6. Build fresh-run graph from canonical initial state and representative replay graph with strict `meta.*` isolation.
7. Compare machine graph against authoritative catalog for equality; reject orphan/phantom edges.
8. Freeze production contracts only after machine checks are clean enough.
9. Then build Decision Engine → UI → localization → automated/runtime verification → Android → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes. Owner-controlled release gates must never be falsely marked complete.

## Project separation
`rulebreak8` is unrelated and must not be used as a readiness source for Choice Kingdom.

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
Dedicated Scenario QA score is now approximately **82%**. This is distinct from overall project completion and is not runtime/Android readiness.

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
- S12 **70%** — S12.27 created an explicit delayed-lifecycle gate matrix separating closed source identities from still-open timing/cancellation/replay semantics.

## Latest QA work
- **S12.27** added `docs/SCENARIO_QA_S12_27_DELAYED_LIFECYCLE_GATE_MATRIX_01.md`, commit `1bc4298a647dd51b56df6f0e2ce4a33e671367ac`.
- **S12.26** added `docs/SCENARIO_QA_S12_26_SYSTEMIC_EVIDENCE_IDENTITY_FREEZE_01.md`, commit `1a1dbd679a16570e4cbc766b0f711fe4a42fca67`.
- **S12.25** added `docs/SCENARIO_QA_S12_25_BUDGET_REFORM_AUTHORITATIVE_RECONCILIATION_01.md`, commit `3b56b6d4ce28d18c9352a1db403d7b04534109ec`.
- **S12.24** added `docs/SCENARIO_QA_S12_24_E245_COMPENSATION_SOURCE_RECONCILIATION_01.md`, commit `e1e90ac6422064bf6fc137a6a06c012728fa4429`.
- **S12.23** added `docs/SCENARIO_QA_S12_23_E246_PRODUCER_CLOSURE_01.md`, commit `63c911bfe91cfd1d520bc97913ceb7e5f146cf5e`.

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
- **Budget reform source set:** E142-A `auditor_independence` + E154-A `crown_audited` + E198-A `legislative_budget_lock`; negative branches E142-B/E154-B/E198-B are blockers.
- **Systemic evidence source candidates:** E232-A/E234-A/B for warehouse-financial evidence, E233-A for document/forensic evidence, E236 witness-ledger branches for witness/organizational evidence; explicit convergence producer remains OPEN.

## Canonical producer/consumer status
Source-level closed chains include:
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E160-A → `winter_rent_ceiling` → E246
- E136-B → `history.guild_logistics_cooperation` → E194
- E144-A/B → `history.guild_representation`
- E271-A → active `pred.border_crisis`; E272-A/B resolve it with exact source tokens now recovered
- E32 → active `pred.transport_disruption`; E136-A/B clear it
- E142-A/E154-A/E198-A → budget-reform source domains

### S12.22–S12.27 delayed/composite source closure
- E181 → toll concession: source-language trigger closed; exact producer choice and executable cancellation remain open.
- E182 → `veteran_patronage`: source identity closed; authored relative timing remains 4+ turns.
- E183 → `estate_exception`: source identity closed; authored relative timing remains 5+ turns.
- E184 → secret evidence route: consumer source closed; exact producer remains OPEN.
- E185 → `cheap_weapons`: source identity closed; later military-crisis resolution semantics remain OPEN.
- E242 → E118-B `estate_exception`: source identity closed candidate; executable lifecycle open.
- E243 → E18-B `public_bridge`: source identity closed; executable lifecycle open.
- E244 → E09-B `flexible_accounts`: source identity closed; executable lifecycle open.
- **E245 → compensation route:** E125-A `border_compensation` and E156-A `requisition_compensation` are confirmed compensation facts; the earlier delayed-graph audit also records E20-A `soldier_compensation`. These must be reconciled against authoritative catalog wording before any producer is selected or unioned. Generic compensation alias remains forbidden.
- E246 → **E160-A `winter_rent_ceiling` exact producer closed**; executable 5+ turn lifecycle remains open.
- **`pred.budget_reform` → source set closed:** E142-A + E154-A + E198-A. Runtime lifecycle, negative-state invalidation and reachability remain open.
- **`pred.systemic_explanation_verified` → evidence families materially frozen:** warehouse/financial candidates E232-A/E234-A/B; document/forensic candidate E233-A; witness/organizational candidate E236; explicit convergence producer remains OPEN.

## Delayed lifecycle gate
S12.27 explicitly separates source closure from executable lifecycle. Known relative timings are retained as constraints (`4+`, `5+`, `6+`, or `later`) and are not converted into guessed absolute turns. Every callback still requires sourceEventId, sourceChoiceId, consequenceId, earliestTurn, resolutionTarget, exactlyOnceKey, and cancellation/supersession semantics. Save/load persistence and replay isolation remain mandatory.

Important unresolved/open areas:
- `pred.food_stable` and its relationship to `food_logistics_stabilized`
- exact machine formula and immutable evidence IDs for `pred.guild_influence_strong`
- exact convergence producer/key and lifecycle for `pred.systemic_explanation_verified`
- `pred.coalition_cooperation` runtime qualification and invalidation
- `pred.constitutional_prepared_strong`
- `pred.final_charter_prerequisites`
- replay `meta.*` producers/keys for E247/E248/E270
- exact delayed identities/timing/cancellation for remaining open families
- E184 producer closure, E185 resolution semantics, E245 route disambiguation
- complete incoming paths and deterministic precedence for endings
- exhaustive E01–E272 producer/consumer graph and fresh-run reachability
- machine graph ↔ authoritative catalog equality

## Replay QA boundary
E247 is explicitly a second-run information route and E248 an explicit replay callback. Neither may be satisfied by ordinary first-run flags without a declared `meta.*` key and producer. E270's dual-witness evidence remains ordinary run evidence unless the authored source explicitly promotes it. No implicit cross-run persistence is admitted.

## Canonical vocabulary rules
State namespaces are `resource.*`, `rel.*`, `flag.*`, `history.*`, `thread.*`, `delay.*`, `ending.*`, and explicit `meta.*` for intentionally persistent cross-run knowledge. Contextual concepts such as food pressure or winter severity must be deterministic predicates or durable markers, never silently become a sixth resource.

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
- generic `compensation route` must not silently union distinct compensation contexts.
- E155-A `full_crown_audit_published` cannot count as a second independent budget-reform domain.
- E207 cannot manufacture systemic convergence from its own trigger.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **97%**
- Delayed Consequences: **95%**
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

Overall project progress remains approximately **60%**. Scenario QA is approximately **82%** and must not be conflated with overall project completion.

## Next autonomous work
1. Re-read authoritative source for E20-A/E125-A/E156-A and close E245 only if an exact source or explicitly authored composite is proven.
2. Close the missing explicit convergence producer/key for systemic explanation if authoritative source evidence exists; otherwise preserve OPEN.
3. Extract exact immutable evidence IDs and executable formulas for guild influence, coalition cooperation and constitutional preparation; preserve consumer-only boundaries.
4. Reconcile stale audit records against authoritative E151–E210 source text.
5. Reconcile remaining E01–E180 delayed families and canonical producer/consumer edges.
6. Extend the delayed lifecycle matrix to the remaining delayed families and define cancellation/supersession only from authored evidence.
7. Reconcile S11 ending incoming paths and deterministic precedence against the expanded graph.
8. Build fresh-run graph from canonical initial state and representative replay graph with strict `meta.*` isolation.
9. Compare machine graph against authoritative catalog for equality; reject orphan/phantom edges.
10. Freeze production contracts only after machine checks are clean enough.
11. Then build Decision Engine → UI → localization → automated/runtime verification → Android → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes. Owner-controlled release gates must never be falsely marked complete.

## Project separation
`rulebreak8` is unrelated and must not be used as a readiness source for Choice Kingdom.

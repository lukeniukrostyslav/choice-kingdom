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
- S12 **30%** — S12.2 source closure, S12.3 canonical invariant audit and S12.4 source-patch application gate completed; exhaustive reachability and authoritative patch application remain open.

## Latest QA work
- **S12.4** added `docs/SCENARIO_QA_S12_4_SOURCE_PATCH_APPLICATION_GATE_01.md`, commit `17a74ef695cd0f9b94e2a20b80f3669dbda0cd74`. It reconciles the P0 patch specification against canonical contracts and identifies a material unresolved semantic conflict: the proposed E192 patch would derive `pred.food_stable` from `food_logistics_stabilized`, while the current canonical contract still says no E01–E272 producer is verified. The patch therefore remains unapplied until authoritative source evidence explicitly resolves the contract. No premature production promotion was made.
- **S12.3** added `docs/SCENARIO_QA_S12_3_CANONICAL_INVARIANT_AUDIT_01.md`, commit `860444b28cd6e3e36024f9ebf9609b80532efa07`. It converts the latest producer/consumer registry into explicit canonical invariants and records PASS/OPEN/REJECTED states for lifecycle, alias, replay, delayed and ending rules. It does not claim exhaustive reachability.
- **S12.2** added `docs/SCENARIO_QA_S12_2_SOURCE_CLOSURE_DELTA_AUDIT_01.md`, commit `6c8e82e825e7bcbeeb9d6f105ed7f4f9fd744559`. This reconciles the latest producer inventory against stale wording and closes the source-level ambiguity for active `pred.transport_disruption`: E32 is the explicit active producer; E136-A/B are recovery/clear producers. Runtime cycle identity, ordering, persistence, expiry/supersession and delayed-effect interaction remain open.
- **S12.1** added the machine-oriented reachability anchor inventory in commit `a61ac9de61f4c448c511e123be38cea12b3b0f5b8`.
- Canonical budget reform source closure identifies E142-A `auditor_independence`, E154-A `crown_audited` and E198-A `legislative_budget_lock` as the three-domain source candidate set. Predicate validation remains partial.
- Canonical closure audit confirms source-level closure for guild representation, border crisis and guild logistics while keeping food stability, composite guild influence, systemic explanation, coalition cooperation, constitutional preparation and final-charter prerequisites appropriately open/partial.
- S12 fresh-run/replay audit defined canonical initial-state isolation and machine-check requirements.
- S11 ending audit established consumer-only ending qualification and rejected generic-score/consumer-as-producer shortcuts.
- S10.5 closed the semantic QA boundary for delayed lifecycle, persistence and replay isolation while executable callback contracts remain open pending exact source extraction.
- S10.4 reconciled delayed source identities for E181–E185 and E242–E246.
- S09.8 normalized the closed dependency graph and rejected self-satisfaction, alias leakage and E273–E277 contamination.

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
- `pred.systemic_explanation_verified`
- `pred.coalition_cooperation`
- `pred.constitutional_prepared_strong`
- `pred.final_charter_prerequisites`
- replay `meta.*` producers/keys for E247/E248/E270
- exact delayed identities/timing/cancellation for remaining open families
- complete incoming paths and deterministic precedence for endings
- exhaustive E01–E272 producer/consumer graph and fresh-run reachability
- authoritative application/re-read of P0 source patches

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
- Producer / Consumer QA: **97%**
- Derived predicates / machine contracts: **84%**
- Delayed Consequences: **88%**
- Replay / Meta-state: **57%**
- Endings / precedence: **63%**
- Reachability / causal graph: **45%**
- Production data schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+ languages: **5%**
- Android implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **53%**. Scenario QA remains **65%** and must not be conflated with overall project completion.

## Next autonomous work
1. Re-read authoritative authored catalog blocks for E136, E144, E148, E192, E194, E197, E200, E207, E209 and E210 and classify each P0 patch as present/partial/absent.
2. Resolve the E192 `pred.food_stable` versus `food_logistics_stabilized` conflict from authoritative source evidence only.
3. Generate the machine-oriented P0 producer/consumer delta.
4. Continue exhaustive E01–E272 producer/consumer inventory and canonical vocabulary normalization.
5. Continue exact source extraction for E218/E225 and E251–E272 delayed/lifecycle rows.
6. Reconcile S11 ending incoming paths and precedence against the expanded graph.
7. Run fresh-run and representative replay reachability from canonical initial state.
8. Freeze production contracts only after machine checks are clean enough.
9. Then build Decision Engine → UI → localization → automated/runtime verification → Android → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes. Owner-controlled release gates must never be falsely marked complete.

## Project separation
`rulebreak8` is unrelated and must not be used as a readiness source for Choice Kingdom.

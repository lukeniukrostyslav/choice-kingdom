# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling the kingdom of Avelune. The core appeal is meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings, and replayable paths.

## Full-release content target
This is a real full game, not a short card demo. The release target is approximately 250–350+ meaningful authored events/story nodes, with interconnected branches rather than filler repetition, plus approximately 8–12 recognizable endings and substantial replay variation.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, including RTL and long-string validation.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Non-negotiable development order
Content and canonical QA come before production contracts, engine, UI, localization, automated/runtime verification and Android release.

## Current phase
**Narrative/content canonicalization and QA.** Authored checkpoint: E01–E272. Immediate goal: reconcile authored sources and causal graph into canonical production representation and prove internal consistency/reachability.

## Authored content checkpoints
- E01–E70: authored spine/endgame
- E71–E110: authored expansion
- E111–E150: authored expansion
- E151–E210: authored expansion
- E211–E270: authored expansion
- E271: border-crisis declaration producer bridge
- E272: border-crisis active-resolution producer bridge
- E273–E277: authored producer-expansion candidates, **not yet admitted to the frozen E01–E272 production catalog**
- Total frozen authored node identifiers: **E01–E272**.

## Scenario QA reporting metric
The dedicated scenario verification metric is frozen in `docs/SCENARIO_QA_SCORECARD_01.md`.

**Scenario QA / verification progress: 65%.**

This is the fixed reporting metric for the E01–E272 authored campaign. It measures closure of scenario QA gates (canonical continuity, producer/consumer closure, derived predicates, delayed consequences, replay boundaries, endings/precedence, causal reachability and exhaustive machine checks). It is intentionally distinct from the overall project percentage.

The 65% figure does not mean the engine, runtime, Android build, UI, localization or APK are complete. It also does not mean reachability has been proven.

## Latest QA work
- S08.9 source reconciliation added as `docs/SCENARIO_QA_S08_9_SOURCE_RECONCILIATION_01.md`, commit `beb8c93e8e4e95c2fb62ab90e4cf36f0e46f7e4b`.
- S08.9 reconciled food/transport lifecycle evidence against the authoritative late-predicate audit and prevented downstream consumers from being promoted into producers. `pred.food_stable` remains OPEN; E32 is the active transport-disruption producer and E136-A/B are recovery/clear sources, while later reactivation remains unresolved.
- S08.8 source closure audit added as `docs/SCENARIO_QA_S08_8_SOURCE_CLOSURE_AUDIT_01.md`, commit `1378318513cca1f88b8ee2c310b7228b5e145a2b`.
- S08.7 domain qualification audit added as `docs/SCENARIO_QA_S08_7_DOMAIN_QUALIFICATION_AUDIT_01.md`, commit `90694d5529d3df89556d79d54fca386c5d67c99b`.
- S08.7 budget-reform closure identified the qualifying source set E142-A `auditor_independence`, E154-A `crown_audited`, E198-A `legislative_budget_lock`; ordering, reachability, negative-branch leakage and replay verification remain open.
- S08.6 closure matrix added the current closed/open producer-family matrix.
- S08.5 corrected the canonical producer registry to reject E273-A/E277 and keep `pred.food_stable` open.
- S10.3 E185 crisis-resolution/ordering contract remains source-level and blocked on exact military-crisis producer/payload lifecycle.

## Current QA checkpoint
The producer inventory is paired with `docs/MACHINE_INVENTORY_PASS_01.md`, which freezes the current source-closed fact set and explicitly separates runtime-safe normalization from unresolved producer ambiguity. This remains source-level QA, not runtime data.

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. E136-B supplies `history.guild_logistics_cooperation`; E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B establish `pred.winter_severe`; E32 establishes `pred.transport_disruption` and E136-A/B are the primary recovery/clear sources. Runtime lifecycle, persistence and ordering remain OPEN.

E243 is source-closed through explicit normalization: E18-B establishes `public_bridge`, and the delayed callback may use that exact machine vocabulary. E245 remains deliberately unresolved across distinct compensation facts; E184 has no source-closed producer; E246 remains specific to `winter_rent_ceiling` pending explicit generic-alias policy.

The canonical trigger audit has been extended through E272. It records additional source-closed facts and carries the current hard-negative rules into the machine inventory pass. Exhaustive extraction, duplicate-semantic detection, contradictory-writer detection, predicate-cycle detection and reachability simulation remain unfinished.

P0 reconciliation freezes the guild-influence domain boundary, constitutional-preparation domain boundary, systemic-evidence qualification shape, coalition positive-outcome requirements, and budget-reform institutional layers. These remain source-level contracts, not runtime implementation.

E273–E277 remain outside the frozen catalog. Their producer-expansion semantics are not silently promoted into E01–E272. The S08.4 scope-integrity correction explicitly rejects those IDs from frozen producer/consumer, predicate, delayed-source and reachability contracts.

Replay mutable-state isolation is contract-closed at the design level: a new run starts with empty pending callbacks, active-cycle predicates, unresolved crises and run-local state; only explicitly authored `meta.*` transfer data may cross the replay boundary. E247, E248 and E270 remain consumer intents without source-closed meta producers/keys.

The ending qualification design contract is established: endings must be deterministic, predicate-based and causal. Broken Diadem and Quiet Throne remain especially open because deterministic failure/withdrawal producers are not frozen.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until canonical contracts are frozen and complete catalog reconciliation passes.

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

Overall project progress remains approximately **53%**. The separate scenario QA metric is **65%** and must not be conflated with this overall project figure.

## Next highest-value work
1. Continue exhaustive E01–E272 producer/output/trigger extraction with a hard E273–E277 exclusion filter.
2. Build producer-before-consumer chronology and resolve undefined producers/consumers, duplicate semantic writers and contradictory writers without inventing semantics.
3. Finish derived predicate contracts and exact canonical vocabulary, including food stability, transport lifecycle, guild influence, constitutional preparation and coalition cooperation.
4. Close delayed E184/E245/E246 and replay/ending contracts.
5. Run fresh-run reachability and graph-vs-catalog reconciliation.
6. Freeze production contracts only after evidence is clean enough for machine validation.
7. Build the Decision Engine against frozen contracts, then UI, localization, automated/runtime verification and Android release gates.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a readiness source for Choice Kingdom.

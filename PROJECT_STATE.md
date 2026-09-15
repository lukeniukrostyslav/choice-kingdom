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

## Latest scenario QA pass
`docs/SCENARIO_QA_PASS_02_STATIC_CLOSURE.md` records the current static-closure reconciliation. It keeps the frozen denominator at E01–E272, reconciles the transport-disruption producer wording, freezes replay isolation as a contract invariant, and preserves the conservative delayed-consumer and ending gates. It does **not** inflate the scenario percentage because exhaustive inventory and reachability gates are still open.

## Current QA checkpoint
The producer inventory is paired with `docs/MACHINE_INVENTORY_PASS_01.md`, which freezes the current source-closed fact set and explicitly separates runtime-safe normalization from unresolved producer ambiguity. This remains source-level QA, not runtime data.

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. E136-B supplies `history.guild_logistics_cooperation`; E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B establish `pred.winter_severe`; E32 establishes `pred.transport_disruption` and E136-A/B are the primary recovery/clear sources. Runtime lifecycle, persistence and ordering remain OPEN.

E243 is source-closed through explicit normalization: E18-B establishes `public_bridge`, and the delayed callback may use that exact machine vocabulary. Existing EVENT_GRAPH edges remain causal candidates, not additional producers. E245 remains deliberately unresolved across distinct compensation facts; E184 has no source-closed producer; E246 remains specific to `winter_rent_ceiling` pending explicit generic-alias policy.

The canonical trigger audit has been extended through E272. It records additional source-closed facts and carries the current hard-negative rules into the machine inventory pass. Exhaustive extraction, duplicate-semantic detection, contradictory-writer detection, predicate-cycle detection and reachability simulation remain unfinished.

P0 reconciliation freezes the guild-influence domain boundary, constitutional-preparation domain boundary, systemic-evidence qualification shape, coalition positive-outcome requirements, and budget-reform institutional layers. These remain source-level contracts, not runtime implementation.

E273–E277 remain outside the frozen catalog. Their producer-expansion semantics are not silently promoted into E01–E272.

Replay mutable-state isolation is contract-closed at the design level: a new run starts with empty pending callbacks, active-cycle predicates, unresolved crises and run-local state; only explicitly authored `meta.*` transfer data may cross the replay boundary. E247, E248 and E270 remain consumer intents without source-closed meta producers/keys.

The ending qualification design contract is established: endings must be deterministic, predicate-based and causal. Broken Diadem and Quiet Throne remain especially open because deterministic failure/withdrawal producers are not frozen.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until canonical contracts are frozen and complete catalog reconciliation passes.

## Latest source-level commits
- `3d1bb4d53ee09a8f47602fda9c5b22099f0593ec` — corrected scenario QA static-closure source path after pass 02.
- `a9f515981ce38e15f3ae27b5a1917cccc65a6d00` — scenario QA static closure pass 02 added.
- `b9283504badb18c02c5d0311dbf80ce15e0b7f6c` — reconciled transport-disruption producer lifecycle in canonical producer inventory.
- `bddaaeb66ab78f673178945cac1675d3a4eccc4f` — scenario QA reporting scorecard frozen at 65%.
- `e623d9d9c0f43175906c281f6e01e5faddca4b73` — trigger audit extended through E272.
- `add6f42fdc52c2a4ebbcff4fde213657e1b0b21f` — machine inventory pass 01.
- `f77d06cf6212cffce7b8d867a71e1da022d79bb0` — corrected delayed graph audit / E243 source closure.
- `70d5eb725752516cadeef5298845e67285f0871e` — canonical producer inventory 01.
- `deba396de3cc71cc90852f50c184d83b724a6aca` — delayed producer decision matrix.
- `a5993eb86688866f053f85af883832b94f3a044c` — replay meta source closure 02.

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
1. Compile the full E01–E272 concrete output/trigger inventory from authoritative sources.
2. Detect duplicate semantic writers, contradictory writers, undefined consumers/producers and predicate cycles.
3. Complete ending prerequisite incoming-path coverage and deterministic precedence data.
4. Close exact replay `meta.*` producer/key inventory without inventing keys.
5. Freeze production contracts and only then build the static validator.
6. Implement the actual Decision Engine and runtime.
7. Proceed to UI, localization, Android QA and APK only after engine contracts are genuinely verified.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a readiness source for Choice Kingdom.

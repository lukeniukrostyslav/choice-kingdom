# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling the kingdom of Avelune. The core appeal is meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings, and replayable paths.

## Full-release content target
This is a **real full game**, not a short card demo. The release target is approximately **250–350+ meaningful authored events/story nodes**, with interconnected branches rather than filler repetition, plus approximately 8–12 recognizable endings and substantial replay variation. The first playthrough should feel like a complete multi-hour campaign; repeated playthroughs should reveal materially different information, routes, consequences, and endings. The exact final count may change during narrative QA, but quality and causal depth take priority over hitting a number mechanically.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, not English-first with later translation. Localization must cover UI, events, choices, consequences, system messages, endings, and error/fallback text. RTL languages must be tested.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Non-negotiable development order
**Content comes before engine, and APK comes last.** Do not reverse this order for convenience.

1. Fully design and QA the campaign: story, acts, characters, factions, events, branches, delayed consequences, callbacks, investigation routes, crises, pacing, replayability and endings.
2. Expand the authored network to the full-release scale and verify that events have real downstream consequences rather than filler.
3. Create the content QA matrix and close narrative dead ends, contradictions, weak branches, repetitive choices and pacing problems.
4. Only after the real campaign design is stable, finalize machine-readable data contracts against that real content.
5. Only then implement the reusable decision engine and make it execute the authored campaign faithfully.
6. Build the real UI/UX around the actual game, not placeholder content.
7. Implement localization for 20+ locales, including RTL and long-string validation.
8. Add automated tests, deterministic replay/save-load validation, full-catalog validation, balance and runtime verification.
9. Perform Android integration, performance, touch, save/reload, accessibility, audio/haptics and physical-device QA.
10. Build and verify the debug APK only after the game and systems are genuinely ready.
11. Treat the production AAB/signing/Play release as the final stage after APK and QA gates pass.

## Current phase
**Narrative/content canonicalization and QA.** The authored checkpoint is E01–E270. The immediate task is reconciling authored sources and the causal graph into a canonical production representation and proving that the content is internally consistent and reachable.

## Authored content checkpoints
- E01–E70: authored spine/endgame
- E71–E110: authored expansion
- E111–E150: authored expansion
- E151–E210: authored expansion
- E211–E270: authored expansion
- Total authored node identifiers currently planned: **E01–E270** (270 authored nodes; not all are yet canonically integrated or QA-verified).

## Narrative QA artifacts
- `docs/EVENT_CATALOG.md` contains the original E01–E34 campaign spine.
- `docs/EVENT_CATALOG_ACT_V_EXPANSION.md` extends the authored spine through E70 and the seven current ending nodes.
- `docs/EVENT_EXPANSION_071_110.md` contains E71–E110 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_111_150.md` contains E111–E150 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_151_210.md` contains E151–E210 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_211_270.md` contains E211–E270 expansion layer pending canonical graph/catalog integration.
- `docs/CONTENT_QA_MATRIX.md` defines the production content gates.
- `docs/CANONICAL_STATE_VOCABULARY.md` defines the state namespaces.
- `docs/CANONICAL_DELAY_CONTRACT.md` defines the delayed-consequence contract.
- `docs/CANONICALIZATION_BACKLOG.md` is the active execution backlog.
- `docs/PRODUCER_GAP_CLOSURE_PASS_01.md` through `docs/PRODUCER_GAP_CLOSURE_PASS_03.md` record the prior P0 closure passes.
- `docs/PRODUCER_GAP_CLOSURE_PASS_04.md` records the latest source-level producer-gap contract.
- `docs/CANONICAL_SOURCE_CORRECTIONS_01.md` freezes the explicit authored correction semantics for E192, E136, E144, E148, E194, E195, E200, E207, E209 and E210.
- `docs/AUTHORED_BRIDGE_CONTRACT_01.md`, `docs/AUTHORED_SOURCE_PATCHSET_01.md` and `docs/AUTHORED_CATALOG_PATCH_APPLICATION_01.md` document the bridge semantics and application checklist used during the latest source-edit pass.

## Current QA checkpoint
The E151–E210 authoritative catalog has now received a direct authored-source correction pass. E192 uses canonical food-logistics markers instead of a sixth numeric resource; E194 records durable guild logistics cooperation; E197/E200/E201 consume canonical qualification predicates; E207 records its distinct-evidence convergence requirement; E209 requires upstream final charter prerequisites; and E210 is explicitly convergence-only. This is **source-level progress, not runtime validation**.

P0 producer closure is still OPEN. Remaining work includes proving canonical producers for transport disruption, guild representation, coalition cooperation, border crisis, systemic evidence convergence, strong guild influence, strong constitutional preparation and final charter prerequisites across the complete E01–E270 source set. E111–E150 still contains legacy source semantics such as E136 road outcomes and E144 guild representation that must be reconciled into the canonical vocabulary before the catalog can be considered closed. E211–E270 also requires a full producer/consumer and semantic audit; authored nodes there are not runtime-verified.

Reachability remains static/pre-audit only until a real validator and production data representation exist. No engine/APK readiness claim is permitted at this stage.

## Next highest-value work
1. Apply and verify the remaining authored-source canonical corrections, beginning with E136/E144/E148 and the border-crisis producer chain.
2. Complete producer/consumer extraction and graph/catalog reconciliation for E01–E270, including E211–E270.
3. Freeze the exact combination rules for `pred.guild_influence_strong`, `pred.coalition_cooperation`, `pred.constitutional_prepared_strong`, `pred.systemic_explanation_verified` and `pred.final_charter_prerequisites` against authored source.
4. Audit undefined outputs, legacy prose triggers, duplicate semantics, missing delayed producers/consumers and mutually conflicting states.
5. Build a real static catalog validator for IDs, duplicate IDs, legacy ending collisions, graph references and missing ranges only after the canonical data contract is frozen against the authored catalog.
6. Lock deterministic derived predicates only after producer and threshold validation.
7. Normalize delayed consequences and replay metadata.
8. Perform runtime reachability, dead-end, contradiction, pacing and ending simulations once the production catalog exists.
9. Freeze production data contracts only after the above gates pass.

## Honest progress rule
Percentages represent actual state of the corresponding work. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is actually changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

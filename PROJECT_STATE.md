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
**Narrative/content canonicalization and QA.** The authored checkpoint is now E01–E272. The immediate task is reconciling authored sources and the causal graph into a canonical production representation and proving that the content is internally consistent and reachable.

## Authored content checkpoints
- E01–E70: authored spine/endgame
- E71–E110: authored expansion
- E111–E150: authored expansion
- E151–E210: authored expansion
- E211–E270: authored expansion
- E271: authored border-crisis declaration producer bridge
- E272: authored border-crisis active-resolution producer bridge
- Total authored node identifiers currently present: **E01–E272** (272 authored nodes; not all are yet canonically integrated or QA-verified).

## Narrative QA artifacts
- `docs/EVENT_CATALOG.md` contains the original E01–E34 campaign spine.
- `docs/EVENT_CATALOG_ACT_V_EXPANSION.md` extends the authored spine through E70 and the seven current ending nodes.
- `docs/EVENT_EXPANSION_071_110.md` contains E71–E110 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_111_150.md` contains E111–E150 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_151_210.md` contains E151–E210 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_211_270.md` contains E211–E270 expansion layer plus the earlier E271 bridge.
- `docs/EVENT_CATALOG_EXPANSION_271_280.md` contains E271–E272 canonical border lifecycle closure nodes.
- `docs/CONTENT_QA_MATRIX.md` defines the production content gates.
- `docs/CANONICAL_STATE_VOCABULARY.md` defines the state namespaces.
- `docs/CANONICAL_DELAY_CONTRACT.md` defines the delayed-consequence contract.
- `docs/CANONICALIZATION_BACKLOG.md` is the active execution backlog.
- `docs/CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md` is the consolidated producer/consumer source-level QA registry.
- `docs/LEGACY_SEMANTIC_AUDIT_01.md` records the E35–E40 and duplicate-semantic audit findings.

## Current QA checkpoint
The E111–E210 authoritative catalogs have received direct authored-source correction passes. E192 uses canonical food-logistics markers instead of a sixth numeric resource; E194 records durable guild logistics cooperation; E197/E200/E201 consume canonical qualification predicates; E207 records its distinct-evidence convergence requirement; E209 requires upstream final charter prerequisites; and E210 is explicitly convergence-only. E136/E144/E148 were also directly normalized for transport repair, guild representation and cross-faction package semantics.

E271 now provides an explicit authored source for border-crisis declaration, while E272 provides the corresponding authored active-crisis resolution paths. The historical declaration remains queryable after resolution; only the active crisis predicate is cleared. E195/E253/E255 remain consumers and cannot manufacture the crisis by reachability.

The border-crisis lifecycle is therefore closed at the authored-source level, but not at runtime. Remaining P0 work is exact producer enumeration for frozen combination domains, full marker/consumer inventory, trigger normalization, graph/catalog reconciliation, reachability, duplicate semantic cleanup, delayed/replay normalization and production schema freeze.

A legacy semantic audit also confirmed a P0 collision between E55 and E269 (same title but different authored choice sets) and a high-priority overlap between E36 and E226 (both Mara resignation). E73/E156 and E99/E173 remain open pending exact source comparison. These must be resolved before production schema freeze; IDs must not be silently renumbered.

Reachability remains static/pre-audit only until a real validator and production data representation exist. No engine/APK readiness claim is permitted at this stage.

## Latest source-level commits
- `f573dbe45661a9cd7a8b836dcf2efdb8e94a7fd0` — added E272 border-crisis resolution bridge.
- `7bb42f5c6c4da194004631bd4944188c1eab52b6` — refreshed canonical producer/consumer registry through E272.
- `dc97cd981bdd047084e5e07d3bc07cd8ba4e2636` — recorded legacy/duplicate semantic audit.

## Next highest-value work
1. Resolve or reframe confirmed duplicate semantic nodes without silent renumbering.
2. Enumerate exact durable producers for every domain used by the frozen combination rules.
3. Expand the registry to every concrete durable flag/history marker in E01–E272 with exact consumers.
4. Normalize remaining prose triggers and aliases.
5. Reconcile graph/catalog references and reachability.
6. Audit E73/E156 and E99/E173 using exact source text.
7. Verify delayed/replay source identities and exactly-once semantics.
8. Build a real static catalog validator only after the canonical data contract is frozen against the authored catalog.
9. Freeze production data contracts, then implement the engine.

## Honest progress rule
Percentages represent actual state of the corresponding work. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is actually changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

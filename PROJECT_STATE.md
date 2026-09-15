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
- `docs/CANONICAL_STATE_VOCABULARY.md` defines the state namespaces and is now explicitly scoped to E01–E272, including the E271/E272 border lifecycle.
- `docs/CANONICAL_DELAY_CONTRACT.md` defines the delayed-consequence contract.
- `docs/CANONICALIZATION_BACKLOG.md` is the active execution backlog.
- `docs/CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md` is the consolidated producer/consumer source-level QA registry.
- `docs/CANONICAL_CLOSURE_AUDIT_01.md` is the latest focused source-level closure audit.
- `docs/CANONICAL_TRIGGER_NORMALIZATION_03.md` records the latest safe prose-trigger normalization pass and its explicit non-normalization boundaries.
- `docs/LEGACY_SEMANTIC_AUDIT_01.md` records the E35–E40 and duplicate-semantic audit findings.
- `docs/SEMANTIC_COLLISION_RESOLUTION_01.md` records the frozen and applied semantic-resolution policy.
- `docs/LEGACY_SOURCE_COMPARISON_02.md` closes E73/E156 and E99/E173 as distinct source-level nodes.
- `docs/CANONICAL_SOURCE_CORRECTIONS_02.md` records the applied E136/E194 guild-logistics cycle correction.

## Current QA checkpoint
The E111–E210 authoritative catalogs have received direct authored-source correction passes. E136-B now establishes the immutable upstream `history.guild_logistics_cooperation` marker, and E194 now consumes that history marker rather than the qualified predicate. E194's neutral-inspector choice remains the later qualification input; immunity risk explicitly blocks qualification. This removes the identified E194 self-dependency at the authored-source level.

E192 uses canonical food-logistics markers instead of a sixth numeric resource; E197/E200/E201 consume canonical qualification predicates; E207 records its distinct-evidence convergence requirement; E209 requires upstream final charter prerequisites; and E210 is explicitly convergence-only. E144/E148 are normalized for guild representation and cross-faction package semantics: E144-A/B are now verified producers of `history.guild_representation`.

The authoritative E211–E270 catalog now distinguishes the previously overlapping Mara and Ivo nodes without renumbering: E226 is **Mara's Final Resignation Test**, explicitly a late institutional-stress consequence; E269 is **Ivo's Late Account**, explicitly a late evidence/consequence node distinct from E55. The semantic-resolution and producer/consumer registry have been synchronized with those catalog edits.

E271 now provides an explicit authored source for border-crisis declaration, while E272 provides the corresponding authored active-crisis resolution paths. The historical declaration remains queryable after resolution; only the active crisis predicate is cleared. E195/E253/E255 remain consumers and cannot manufacture the crisis by reachability.

The latest closure audit was reconciled with these authoritative sources: `history.guild_representation` and the border-crisis lifecycle are source-verified; transport disruption remains partial because E136 verifies recovery/clear but a distinct later active-disruption producer is still not identified. Production schema remains blocked.

The latest trigger-normalization pass records only safe mappings already covered by the canonical predicate matrix (resource pressure, winter/border/security/readiness families, evidence/faction cardinality families, and institutional/investigation families). Ambiguous concepts such as civic relief, guild leverage, information route, winter illness, and final-charter preparation remain explicitly open rather than being collapsed into arbitrary aliases.

The semantic-collision backlog is now synchronized: E55/E269 and E36/E226 are marked as applied/verified at the authoritative-catalog level. Their downstream graph/reachability verification remains open, as do E37/E227, E39/E229 and E40/E241.

The canonical state vocabulary scope has now been reconciled from E01–E270 to **E01–E272** so the authoritative normalization document covers the complete authored checkpoint.

Reachability remains static/pre-audit only until a real validator and production data representation exist. No engine/APK readiness claim is permitted at this stage.

## Latest source-level commits
- `b0c9410aa2bd30fcc0e49793f8ab0dffde8ac5ee` — recorded safe canonical trigger normalization pass 03.
- `86a5f2558638d252a4e3f9b36d7a8d1b4e10398b` — state sync after E01–E272 vocabulary reconciliation.
- `3c04cf8de671dbb2ead7ab91700881737d0263fd` — reconciled canonical state vocabulary scope with the complete E01–E272 authored checkpoint.
- `555e797026c7982927f34645ce60d8a3c1b45671` — synchronized canonicalization backlog after verifying the applied E55/E269 and E36/E226 catalog distinctions.
- `ca6f12a50353ee6d6e002025d300bc70d40bc29b` — synchronized producer/consumer registry after latest source-level closure reconciliation.
- `4fdcdbea31709462dd4b38e9b6c3f3189671d6ec` — reconciled closure audit with verified E144 and E271–E272 source producers.
- `d529ff3d0a44bcb4c7cce54d70103e0b78883686` — applied E136-B upstream guild-logistics history marker.
- `c08379167f311c3ce674ace63475f3be839855a8` — changed E194 to consume the upstream guild-logistics history marker and documented qualified predicate derivation.
- `33d9cd1c9c7ffe2f88358994aa043a643d4a2a33` — synchronized correction record as applied and verified.
- `249e01981cb97603aac669dc5686dab46731615d` — applied authoritative E226/E269 semantic distinctions.
- `2fa9be1c586117126c4778598ab509ebe5107389` — synchronized semantic collision resolution after authoritative catalog edits.
- `5d652e994a1a2d0521737d6bf5d39b2a8cab5933` — synchronized producer/consumer registry after source corrections.

## Next highest-value work
1. Enumerate exact durable producers for every remaining domain used by the frozen combination rules.
2. Expand the registry to every concrete durable flag/history marker in E01–E272 with exact consumers.
3. Reconcile the normalized trigger families against the complete catalog and graph, resolving safe aliases while preserving ambiguous distinctions.
4. Reconcile graph/catalog references and reachability.
5. Verify delayed/replay source identities and exactly-once semantics.
6. Verify E55/E269, E36/E226, E37/E227, E39/E229 and E40/E241 downstream roles in graph/reachability QA.
7. Build a real static catalog validator only after the canonical data contract is frozen against the authored catalog.
8. Freeze production data contracts, then implement the engine.

## Honest progress rule
Percentages represent actual state of the corresponding work. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is actually changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

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
**Narrative/content canonicalization and QA.** The authored checkpoint is E01–E270. The immediate task is no longer increasing card count; it is reconciling the authored sources and causal graph into a canonical production representation and proving that the content is internally consistent and reachable.

## Authored content checkpoints
- E01–E70: authored spine/endgame
- E71–E110: authored expansion
- E111–E150: authored expansion
- E151–E210: authored expansion
- E211–E270: authored expansion
- Total authored node identifiers currently planned: **E01–E270** (270 authored nodes; not all are yet canonically integrated or QA-verified).

## Content quality rules
- Do not inflate length with repeated or cosmetic cards.
- Important choices must alter future state, information, relationships, access, risks or endings.
- Delayed consequences must actually arrive and remember earlier decisions.
- Replayability must come from different information and causal paths, not merely shuffled text.
- Critical endings should have multiple independent ways to qualify where appropriate.
- Every major character needs meaningful positive and negative arcs.
- Factions must sometimes be substantively correct rather than cartoonishly right/wrong.
- A first playthrough should be a complete game experience, not a teaser or vertical-slice-only product.

## Narrative QA artifacts
- `docs/EVENT_CATALOG.md` contains the original E01–E34 campaign spine.
- `docs/EVENT_CATALOG_ACT_V_EXPANSION.md` extends the authored spine through E70 and the seven current ending nodes.
- `docs/EVENT_EXPANSION_071_110.md` contains E71–E110 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_111_150.md` contains E111–E150 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_151_210.md` contains E151–E210 expansion layer pending canonical graph/catalog integration.
- `docs/EVENT_CATALOG_EXPANSION_211_270.md` contains E211–E270 expansion layer pending canonical graph/catalog integration.
- `docs/CONTENT_QA_MATRIX.md` defines the production content gates.
- `docs/CANONICAL_EVENT_AUDIT_01.md` records the first reconciliation findings.
- `docs/CANONICAL_EVENT_AUDIT_02.md` records additional repeated-event and derived-condition findings.
- `docs/CANONICAL_TRIGGER_AUDIT_01.md` records the initial producer/consumer and derived-trigger inventory.
- `docs/CANONICAL_STATE_VOCABULARY.md` defines the state namespaces.
- `docs/CANONICAL_DELAY_CONTRACT.md` defines the delayed-consequence contract.
- `docs/CANONICALIZATION_BACKLOG.md` is the active execution backlog.

## Current QA checkpoint
Audit work has now confirmed additional repeated character-scene titles/near-titles (including Mara/Rowan callbacks) and a wider class of free-form derived trigger phrases. These are tracked as canonicalization work, not treated as resolved. E01–E270 remain authored rather than production-verified content.

## Next highest-value work
1. Complete producer/consumer extraction for the full E01–E270 catalog.
2. Define deterministic derived predicates for contextual triggers.
3. Reconcile graph edges against actual catalog triggers/effects.
4. Normalize delayed consequences and replay metadata.
5. Perform reachability, dead-end, contradiction, pacing and ending simulations.
6. Freeze production data contracts only after the above gates pass.

## Honest progress rule
Percentages represent actual state of the corresponding work. Documentation alone does not make implementation complete. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

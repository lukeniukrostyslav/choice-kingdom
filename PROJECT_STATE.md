# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling the kingdom of Avelune. The core appeal is meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings, and replayable paths.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Full-release content target
This is a **full game**, not a short card demo. The first commercial release must contain a substantial authored campaign and replayable branching structure.

Target scale:
- approximately **250–350+ meaningful authored events/content nodes** across the complete campaign;
- approximately **8–12 meaningful endings**;
- multiple character arcs, faction conflicts, investigation routes, systemic crises and callbacks;
- first playthrough target roughly **3–5 hours**;
- multiple-playthrough target roughly **10–20+ hours**;
- deep branch/completion exploration target roughly **20–30+ hours**;
- repetition must reveal different information, consequences and routes rather than merely replay identical cards.

The numbers are quality targets, not permission to pad the game. Every added event must have a purpose, downstream consequence or meaningful variation.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, not English-first with later translation. Localization must cover UI, events, choices, consequences, system messages, endings, and error/fallback text. RTL languages must be tested.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Absolute development-order rule
**Content comes before engine. Engine comes before final Android build. APK is the final technical step.**

The project must be developed in this order:
1. Fully develop and review the story/world/characters/factions.
2. Build the complete event network, branches, delayed consequences, callbacks, investigations, crises, replay paths and endings.
3. Perform narrative/coherence/balance/content QA and close dead ends before implementation.
4. Freeze the authored gameplay contracts and derive the data model from the real content.
5. Only then implement the reusable decision engine.
6. Build the real playable game/UI around authored content; never use placeholders as a substitute for missing content.
7. Implement localization, automated tests, deterministic replay, save/load and runtime validation.
8. Polish and balance the full campaign.
9. Perform Android integration and device QA.
10. **Build the APK only at the end, after the game itself is genuinely complete and verified.**
11. Then prepare the production AAB/store/release process.

Do not move an implementation phase forward merely because a document, prototype or stub exists. A later phase must not be used to hide unfinished earlier content.

## Current phase
**Narrative/content architecture first.** The current priority is to make the full campaign genuinely interesting and sufficiently large before engine implementation.

## Current priority
Do not rush into UI, engine or APK work. Continue expanding the authored campaign, story logic, event graph, character/faction arcs, delayed consequences, investigation, replayability and endings until the content gate is genuinely satisfied. Then derive and implement the engine from that real design.

## Honesty / progress reporting
Progress percentages must reflect actual completed work, not documentation volume or intentions. Never claim “ready” until the relevant implementation and verification gates pass. Engine, Android and APK percentages remain low/zero while those components are not actually implemented and tested.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

## Continuation rule for any GPT/agent
A new GPT/agent must read this file plus `PLAN.md`, `STORY_BIBLE.md`, `EVENT_CATALOG.md`, `NARRATIVE_REVIEW.md`, and `EVENT_GRAPH.md` before continuing. The content-first order above is authoritative. Continue from the repository state; do not invent missing progress and do not restart already completed work without evidence of a defect.

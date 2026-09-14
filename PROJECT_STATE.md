# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling the kingdom of Avelune. The core appeal is meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings, and replayable paths.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, not English-first with later translation. Localization must cover UI, events, choices, consequences, system messages, endings, and error/fallback text. RTL languages must be tested.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Current phase
**Narrative/content architecture first.** Before building the engine, the first campaign's story logic, characters, event network, delayed consequences, replay paths, and ending rules are being designed so the engine is built around real gameplay rather than placeholder events.

## Completed content-design work
- `docs/STORY_BIBLE.md` defines the original setting, tone, six recurring characters, five-act campaign, themes, replay philosophy, ending philosophy, and first-release content target.
- `docs/EVENT_CATALOG.md` defines the first 40-event campaign skeleton, meaningful alternatives, immediate effects, delayed consequences, relationship arcs, hidden-ledger mystery, crisis escalation, and ending resolution logic.

## Required development order
1. Audit repository and preserve source-of-truth documentation.
2. Design and review the complete narrative/event network before implementation.
3. Define data contracts for state, events, choices, conditions, consequences, characters, history, endings and saves against the real catalog.
4. Implement reusable decision engine.
5. Implement real playable vertical slice using authored content.
6. Add automated unit/contract/deterministic replay/save-load/runtime tests.
7. Implement localization architecture for 20+ locales from the beginning.
8. Expand and balance the authored content network to the full release target.
9. Android UI/UX, audio/haptics, offline validation.
10. Debug APK and physical Android QA.
11. Release AAB, production signing, Play Console preparation.

## Current priority
Do not rush into UI or engine code with placeholder content. First make the campaign interesting, internally consistent, replayable, and consequence-driven. Then make the engine faithfully execute that design. Documentation percentages only increase when the underlying work is actually complete and verified.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

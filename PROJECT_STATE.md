# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling a kingdom. Two meaningful choices per event, immediate and delayed consequences, persistent decision history, characters, resources, event chains, multiple endings, replayable paths.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, not English-first with later translation. Localization is a release requirement and must cover UI, events, choices, consequences, system messages, endings, and error/fallback text. RTL languages must be tested.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Current phase
Foundation/specification. The repository currently contains product and continuation documentation; implementation has not yet been represented as a completed playable game.

## Required development order
1. Audit repository and preserve source-of-truth documentation.
2. Define data model for state, events, choices, conditions, consequences, characters, history, endings and saves.
3. Implement reusable decision engine.
4. Implement real playable vertical slice.
5. Add automated unit/contract/runtime tests.
6. Add localization architecture for 20+ locales from the beginning.
7. Expand content and systemic event network.
8. Android UI/UX, audio/haptics, offline validation.
9. Debug APK and physical Android QA.
10. Release AAB, production signing, Play Console preparation.

## Current priority
Build the real engine and vertical slice before mass content production. Do not inflate percentages merely because documentation exists.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

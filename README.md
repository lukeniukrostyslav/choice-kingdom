# Choice Kingdom

Original premium decision-and-consequence mobile game set in the kingdom of Avelune.

## Product direction

Choice Kingdom takes inspiration only from the **high-level structure** of decision-driven games such as Reigns: short situations, meaningful opposing choices, persistent consequences, characters, resources, event chains, multiple endings and replay variation.

This project is **not a clone**. Worldbuilding, characters, writing, events, artwork, mechanics, UI and code must be original.

## Full-game target

This is a **real full game**, not a short card demo or 20–40 card vertical slice.

Current authored checkpoint: **E01–E270 (270 meaningful candidate events)**. The release target remains approximately **250–350+ meaningful authored events/story nodes**, with approximately **8–12 recognizable endings**, interconnected branches, delayed consequences, investigation routes, replay divergence and a multi-hour first campaign. The final count may change after QA; causal quality matters more than hitting a number mechanically.

## Target product

- Android-first premium game
- Offline-first; no mandatory online service
- No advertising
- No subscriptions
- No required backend for core gameplay
- Target price approximately €2.99–€4.99
- Substantial first playthrough and materially different replays
- 20+ release locales, including RTL languages

## Core loop

1. Present a situation.
2. Offer meaningful opposing choices.
3. Apply immediate state changes.
4. Record decision/history state.
5. Schedule real delayed consequences where authored.
6. Unlock future events through canonical state/history/thread conditions.
7. Continue through crises and constitutional/endgame routes.
8. Resolve a causal ending.
9. Allow replay with intentionally different information and routes.

## Current campaign

The campaign is authored around Avelune's ruler and the five pressure centers of Crown, Commons, Houses, Guilds and Border. Core state uses gold, trust, security, power and reputation, plus character relationships, history, flags, threads, delayed consequences and replay metadata.

The narrative is currently in **canonicalization and QA**. E01–E270 are authored but are not yet engine-integrated or reachability-verified.

## Development order — non-negotiable

**Content comes before engine, and APK comes last.**

1. Finish/QA the full campaign and causal network.
2. Reconcile E01–E270 into one canonical production catalog.
3. Close dead ends, contradictions, duplicate semantics, pacing and ending-reachability defects.
4. Freeze machine-readable contracts against the real authored catalog.
5. Implement the reusable decision engine.
6. Build the real UI/UX around the production content.
7. Implement and validate 20+ localization, including RTL and long strings.
8. Add automated content/state/replay/save-load/balance tests.
9. Perform Android integration and physical-device QA.
10. Build the debug APK only after the above gates genuinely pass.
11. Produce the production AAB/signing/store release only at the final gate.

## Current canonicalization artifacts

- `docs/CONTENT_QA_MATRIX.md`
- `docs/CANONICAL_EVENT_AUDIT_01.md`
- `docs/CANONICAL_EVENT_AUDIT_02.md`
- `docs/CANONICAL_STATE_VOCABULARY.md`
- `docs/CANONICAL_DELAY_CONTRACT.md`
- `docs/CANONICAL_TRIGGER_AUDIT_01.md`
- `docs/CANONICALIZATION_BACKLOG.md`
- `docs/EVENT_GRAPH.md`

These documents are QA/design contracts, not claims of runtime implementation.

## Project separation

`rulebreak8` is a separate project and must not be modified or used as a readiness source for Choice Kingdom.

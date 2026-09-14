# AGENTS.md — Choice Kingdom

## Mission

Build an original premium mobile decision game whose core appeal comes from meaningful choices and delayed consequences. The reference category is decision-driven games such as Reigns, but the implementation, world, narrative, characters, art, UI, and content must be original.

## Non-negotiable product rules

1. Do not clone Reigns or copy its protected creative expression.
2. Do not introduce ads, subscriptions, or mandatory online dependencies into the MVP.
3. Core gameplay must work offline.
4. No mock/stub gameplay may be presented as production-ready.
5. Every choice must have a deterministic, testable state effect or a documented controlled-random effect.
6. Delayed consequences must be represented as real state/history rules, not scripted fake callbacks.
7. Save/load must preserve the complete gameplay state needed to reproduce a run.
8. Content must be data-driven so new events can be added without rewriting the engine.
9. Localization must be designed into the content model from the beginning.
10. Android is the first release target.

## Preferred architecture

Separate the project into:

- **Decision Engine** — state transitions, choice resolution, conditions, effects, history, deterministic randomness.
- **Event Catalog** — data-driven situations, choices, prerequisites, effects, follow-ups, tags.
- **Character System** — relationships, character state, availability, personal event chains.
- **Resource System** — economy, trust, security, power, reputation and future extensibility.
- **Consequence Scheduler** — delayed effects and event triggers derived from recorded history.
- **Run / Ending System** — victory, defeat, narrative endings, replay state.
- **Presentation Layer** — card/event UI, animations, input, feedback and accessibility.
- **Persistence** — versioned local save data with validation and recovery.
- **Localization** — locale-aware data lookup with safe fallback.
- **Verification** — unit, contract, integration, deterministic replay and headless gameplay tests.

## Engineering workflow

Work in large coherent blocks. Finish and verify one block before moving to the next. Prefer small, reviewable commits with clear evidence.

Before declaring a block complete:

- inspect the current repository state;
- implement the smallest correct change;
- run applicable automated checks;
- inspect failures rather than masking them;
- update project state/documentation;
- only then increase the completion estimate.

## Release gates

The project is not considered production-ready until:

- the complete core loop is playable;
- event/state persistence is verified;
- content contracts pass for the full catalog;
- deterministic replay/invariant tests pass;
- Android build succeeds;
- physical Android QA is completed;
- production signing is configured by the owner;
- store assets and metadata are validated.

Owner-controlled gates must never be falsely marked complete by automation.

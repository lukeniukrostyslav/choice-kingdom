# CONTINUATION — Choice Kingdom

## Purpose

Fast handoff for any future ChatGPT session or developer. Read this file first, then `AGENTS.md`, `PROJECT_STATE.md`, `PLAN.md`, `DECISION_LOG.md`, and `README.md`.

## Repository

- GitHub: `lukeniukrostyslav/choice-kingdom`
- Project: **Choice Kingdom**
- Current status: **authored full-game checkpoint + canonicalization/QA phase**
- Separate from `rulebreak8`.

## What we are building

An original premium Android-first decision-and-consequence game set in Avelune. The player receives meaningful situations, makes opposing choices, changes resources/relationships/history, encounters delayed consequences, and reaches different endings through causal routes. Replay reveals different information and possibilities.

This is a **real full game**, not a short card demo. The frozen authored production scope currently reaches **E01–E272**, with E273–E277 remaining expansion candidates outside the frozen catalog. Release target remains approximately 250–350+ meaningful nodes and approximately 8–12 recognizable endings.

## Reference boundary

The broad decision-game formula may be inspired by Reigns, but **do not copy** its world, characters, text, artwork, UI, event wording, distinctive presentation, or protected creative expression. The project must have its own identity.

## Product target

- Android first
- Premium one-time purchase ~€2.99–€4.99
- Offline core gameplay
- No ads
- No subscription
- No mandatory backend
- 20+ release locales including RTL languages
- Multi-hour first campaign with materially different replays

## Canonical current state

Authored sources:

- E01–E70: core spine/endgame
- E71–E110: expansion
- E111–E150: expansion
- E151–E210: expansion
- E211–E270: expansion
- E271–E272: border-crisis producer/resolution bridge

Canonical QA artifacts include the event/trigger/state vocabulary, producer-consumer registry, delayed-consequence contracts, predicate dependency audits, event graph and scenario QA worklog.

The campaign is **not yet production-integrated**. Exhaustive producer/consumer closure, unresolved derived conditions, delayed runtime semantics, replay meta-state, ending-path coverage and fresh-run reachability remain open.

## Non-negotiable development order

**Content → canonical QA → machine-readable contracts → engine → UI → localization/tests → Android QA → APK → production release.**

Do not reverse this order for convenience.

## Core loop that must become real

`event → two choices → canonical state transition → history → delayed consequence → future trigger → persistence → ending/replay`

## Working rule

Operate autonomously when the user says to continue. Work in large coherent blocks, verify actual results, update persistent documentation, and continue to the next highest-value safe block. Do not stop after one trivial task.

Never report a percentage from planned work alone. Distinguish implementation, tests, integration, runtime verification and owner-required gates.

## Latest durable QA checkpoint

- S10.3 E185 crisis-resolution / ordering contract: `d9c5853ec0fa92c9b9d0b96da0c246904516de81`
- S10.2 delayed identity/lifecycle matrix: `107c2c40f0c1e454e92bf86904287b691694f4ef`
- S09 predicate graph checkpoint: `ca4c5b848a08dc577a5ec61430ea533bda5496ac`
- S08 producer/consumer correction checkpoint: `b2f562705553ad4927e8987f37e1782a5abaf193`
- S07 border lifecycle artifact: `ad08b00cd5465c03aca0aeb2aac8e4b8a74b8dd7`
- S07 event-graph reconciliation: `67539450464ae167552534dca8375a25daa8f138`

## Next highest-value work

1. Return to exhaustive S08 producer/consumer closure across the frozen E01–E272 catalog.
2. Resolve undefined producers/consumers, duplicate semantic writers and contradictory writers without inventing semantics.
3. Reconcile remaining derived predicates and exact canonical vocabulary.
4. Close remaining delayed/replay/ending contracts.
5. Run fresh-run reachability and graph-vs-catalog reconciliation.
6. Freeze production contracts only after the above evidence is clean enough for machine validation.
7. Then build the Decision Engine against the frozen contracts, followed by UI, localization, automated/runtime verification and Android release gates.

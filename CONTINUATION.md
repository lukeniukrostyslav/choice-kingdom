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

This is a **real full game**, not a short card demo. Authored content currently reaches E01–E270, with a release target of approximately 250–350+ meaningful nodes and approximately 8–12 recognizable endings.

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

Canonical QA artifacts now include:

- `docs/CANONICAL_EVENT_AUDIT_01.md`
- `docs/CANONICAL_EVENT_AUDIT_02.md`
- `docs/CANONICAL_TRIGGER_AUDIT_01.md`
- `docs/CANONICAL_STATE_VOCABULARY.md`
- `docs/CANONICAL_DELAY_CONTRACT.md`
- `docs/CANONICALIZATION_BACKLOG.md`
- `docs/CONTENT_QA_MATRIX.md`
- `docs/EVENT_GRAPH.md`

The campaign is **not yet production-integrated**. Trigger producer/consumer extraction, derived-condition definitions, delayed normalization, replay meta-state, reachability, contradiction, pacing and ending simulations remain open.

## Non-negotiable development order

**Content → canonical QA → machine-readable contracts → engine → UI → localization/tests → Android QA → APK → production release.**

Do not reverse this order for convenience.

## Core loop that must become real

`event → two choices → canonical state transition → history → delayed consequence → future trigger → persistence → ending/replay`

## Working rule

Operate autonomously when the user says to continue. Work in large coherent blocks, verify actual results, update persistent documentation, and continue to the next highest-value safe block. Do not stop after one trivial task.

Never report a percentage from planned work alone. Distinguish implementation, tests, integration, runtime verification and owner-required gates.

## Next highest-value work

1. Continue producer/consumer and derived-trigger extraction across E01–E270.
2. Reconcile catalog and graph into one canonical registry.
3. Audit delayed consequences and replay metadata.
4. Run reachability/dead-end/ending analysis.
5. Only after content is stable, freeze production data contracts and begin engine implementation.

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

The campaign is **not yet production-integrated**. Exhaustive producer/consumer closure, machine dependency extraction, delayed runtime semantics, replay meta-state, deterministic ending precedence and fresh-run reachability remain open.

## Non-negotiable development order

**Content → canonical QA → machine-readable contracts → engine → UI → localization/tests → Android QA → APK → production release.**

Do not reverse this order for convenience.

## Core loop that must become real

`event → two choices → canonical state transition → history → delayed consequence → future trigger → persistence → ending/replay`

## Working rule

Operate autonomously when the user says to continue. Work in large coherent blocks, verify actual results, update persistent documentation, and continue to the next highest-value safe block. Do not stop after one trivial task.

Never report a percentage from planned work alone. Distinguish implementation, tests, integration, runtime verification and owner-required gates.

## Latest durable QA checkpoint

- S13 composite source closures: current derived-predicate contract confirms guild influence, systemic explanation, coalition cooperation, constitutional preparation and budget reform source boundaries.
- Replay provenance correction: `989e78afbe8829e631911637cb0861074b428f2a` updated the reproducible scenario scorecard after correcting E131/E186 provenance handling.
- S10.4 delayed source-boundary verification: `5d798fb547eb7b0d7a4f8325a39c1709441e9e63`
- S11.1 E33/E34 ending-boundary source closure: source/graph CLOSED; deterministic runtime ending order remains OPEN.
- S08.11 budget reform / coalition source closure: source closure PASS; executable qualification/reachability remains open.

## Scenario score

The reproducible scenario QA scorecard is `docs/SCENARIO_QA_SCORECARD_01.md`.

Current block scores:

- S01 80%
- S02 70%
- S03 70%
- S04 70%
- S05 60%
- S06 60%
- S07 80%
- S08 84%
- S09 82%
- S10 80%
- S11 72%
- S12 95%
- **Aggregate: 75%**

The aggregate is the arithmetic mean of the twelve block scores. It is not runtime readiness.

## Next highest-value work

1. Exhaustive producer/consumer inventory over the frozen E01–E272 catalog.
2. Undefined producer/consumer, duplicate semantic writer and contradictory writer detection.
3. Machine token extraction and dependency-cycle validation.
4. Close remaining delayed lifecycle/save-load/exactly-once and replay producer/key contracts.
5. Resolve exact ending prerequisite/blocker sets and deterministic precedence.
6. Run fresh-run and replay causal reachability and graph/catalog parity.
7. Freeze production contracts only after all evidence is clean enough for machine validation.
8. Only then build the Decision Engine, followed by UI, localization, automated/runtime verification and Android release gates.

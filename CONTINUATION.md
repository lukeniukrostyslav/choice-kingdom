# CONTINUATION — Choice Kingdom

## Purpose

Fast handoff for any future ChatGPT session or developer. Read this file first, then `AGENTS.md`, `PROJECT_STATE.md`, `PLAN.md`, `DECISION_LOG.md`, and `README.md`.

## Repository

- GitHub: `lukeniukrostyslav/choice-kingdom`
- Project: **Choice Kingdom**
- Current status: **full authored game checkpoint + runtime integration + application session boundary**
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

Blocks 1–6 have implementation/verification closure at their defined boundaries. The runtime now includes state, authored choice execution, deterministic routing, delayed lifecycle, replay/meta transfer, ending/precedence resolution, integrity-checked persistence/recovery, and the presentation-neutral `GameSession` application boundary.

The frozen authored catalog remains **E01–E272**. The remaining production work is to expand the application runtime into exhaustive full-campaign scenario execution, then build the Android presentation, localization, device QA and release gates.

## Non-negotiable development order

**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → production release.**

Do not reverse this order for convenience.

## Core loop that must become real

`event → two choices → canonical state transition → history → delayed consequence → future trigger → persistence → ending/replay`

## Working rule

Operate autonomously when the user says to continue. Work in large coherent blocks, verify actual results, update persistent documentation, and continue to the next highest-value safe block. Do not stop after one trivial task.

Never report a percentage from planned work alone. Distinguish implementation, tests, integration, runtime verification and owner-required gates.

## Latest runtime closure

- Block 5 ending/precedence executable boundary is closed and verified.
- Block 6 save/load/determinism is closed and verified.
- `runtime/session.py` adds `GameSession` and `SessionView` as the application-facing runtime seam.
- `tests/test_game_session.py` covers session presentation focus, choice delegation, persistence, backup recovery and atomic ending qualification failure.
- `.github/workflows/runtime-session-boundary.yml` verifies the session boundary in CI.
- `docs/RUNTIME_SESSION_BOUNDARY_CLOSURE_01.md` records the closure.
- Local verification: `PYTHONPATH=. pytest -q` → **178 passed**; dedicated session-boundary validation → **PASS** over E01–E272.
- This closure does not claim Android UI, physical-device QA, APK/AAB or store readiness.

## Current major-block status

- Foundation / Rules: **100%**
- Authored Content: **90%**
- Canonical IDs / Continuity: **100%**
- Producer / Consumer QA: **100% source-level**
- Derived Predicates / Machine Contracts: **100% source-level**
- Delayed Consequences: **100% runtime-verified**
- Replay / Meta-state: **100% runtime-verified**
- Endings / precedence: **100% runtime-verified at executable boundary**
- Reachability / Causal Graph: **100% source-level; exhaustive gameplay reachability remains open**
- Production Data Schema: **36%**
- Runtime State / Persistence Foundation: **100% current foundation**
- Decision Engine / Application Runtime: **30%**
- UI / UX: **0%**
- Localization 20+ / RTL: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **15%**
- APK / AAB: **0%**
- Release / Store: **0%**

## Next highest-value work

1. Expand `GameSession` into exhaustive full-campaign scenario execution without inventing authored semantics.
2. Add deterministic full-catalog scenario/reachability simulation and classify every unreachable/sink case.
3. Close the remaining production data-schema extraction needed by the application layer.
4. Build the real Android presentation layer against `GameSession`.
5. Implement 20+ localization and RTL/long-string validation.
6. Run automated balance, replay, persistence and full-catalog regression gates.
7. Build and verify Android, then perform physical-device QA.
8. Produce the final APK/AAB and owner-controlled release materials.

## Owner-required gates

Physical Android QA, production signing credentials and store publication remain owner-controlled gates and must never be marked complete by local automation alone.

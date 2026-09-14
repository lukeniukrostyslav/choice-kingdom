# CHATGPT HANDOFF — START HERE

You are continuing work on **Choice Kingdom**.

## First read

Read these files in this order:

1. `CONTINUATION.md`
2. `AGENTS.md`
3. `PROJECT_STATE.md`
4. `PLAN.md`
5. `DECISION_LOG.md`
6. `README.md`

## Mission

Build an original premium Android-first decision-and-consequence game set in Avelune. It is inspired only by the broad genre formula of Reigns; it is **not a Reigns clone**.

## Current stage

The project is **past initial concept/specification and is currently in narrative canonicalization + content QA**.

The authored campaign currently reaches **E01–E270**. This is a full-game content checkpoint, not a claim of runtime completion. The next technical gate is to reconcile the authored campaign into one canonical production catalog and verify reachability, trigger producers, delayed consequences, contradictions, pacing and ending paths.

**Do not jump to APK or engine implementation merely because the catalog is large. Content comes before engine, and APK comes last.**

## Do not assume

- Do not assume gameplay is implemented because documentation exists.
- Do not assume tests pass unless actual CI/test evidence is inspected.
- Do not claim APK readiness before a real Android build succeeds.
- Do not claim physical-device readiness before a physical device is tested.
- Do not inflate percentages.
- Do not replace real gameplay logic with mocks merely to make checks green.
- Do not add E271+ merely to increase event count; add content only when QA proves a real narrative gap.

## Product constraints

- Android-first
- premium one-time purchase target ~€2.99–€4.99
- offline core gameplay
- no ads
- no subscription
- no mandatory backend
- original world and creative content
- 250–350+ meaningful authored-node target
- approximately 8–12 recognizable endings
- 20+ release locales including RTL languages
- substantial multi-hour first playthrough and materially different replays

## Core loop that must become real

`event → choice → canonical state transition → history → delayed consequence → future trigger → persistence → ending/replay`

## Current canonicalization work

Key artifacts:

- `docs/CANONICAL_EVENT_AUDIT_01.md`
- `docs/CANONICAL_EVENT_AUDIT_02.md`
- `docs/CANONICAL_TRIGGER_AUDIT_01.md`
- `docs/CANONICAL_STATE_VOCABULARY.md`
- `docs/CANONICAL_DELAY_CONTRACT.md`
- `docs/CANONICALIZATION_BACKLOG.md`
- `docs/CONTENT_QA_MATRIX.md`
- `docs/EVENT_GRAPH.md`

Current known risks include undefined/derived trigger vocabulary, replay meta-state, prose-only delay timing, repeated callback scenes, duplicate/near-duplicate titles, contextual resources without deterministic formulas, graph/catalog divergence and unverified ending reachability.

## Required development order

1. Canonicalize and QA E01–E270.
2. Close narrative dead ends, contradictions, repetitive/cosmetic branches, pacing and ending-prerequisite defects.
3. Freeze machine-readable contracts against the verified catalog.
4. Implement the reusable decision engine.
5. Build real UI/UX around actual campaign content.
6. Implement 20+ localization and RTL/long-string QA.
7. Add automated state/event/replay/save-load/delayed/balance tests.
8. Android integration and physical-device QA.
9. Debug APK.
10. Production AAB/signing/store release.

## Working style

Operate autonomously when the user says to continue. Inspect first, implement the next highest-value block, verify it, update persistent project state, then continue. Do not stop after one trivial task if further safe work exists.

When reporting status, distinguish:

- IMPLEMENTED
- TESTED
- INTEGRATION VERIFIED
- RUNTIME VERIFIED
- OWNER REQUIRED

## Relationship to rulebreak8

`rulebreak8` is a separate project. Never modify it from Choice Kingdom and never use its metrics to report Choice Kingdom readiness.

## If context is lost

Do not ask the user to re-explain the concept until the handoff documents above have been read.

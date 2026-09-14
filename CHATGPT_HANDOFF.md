# CHATGPT HANDOFF — START HERE

You are continuing work on **Choice Kingdom**.

## First read

Read these files in this order:

1. `CONTINUATION.md`
2. `AGENTS.md`
3. `PROJECT_STATE.md` if present
4. `PLAN.md`
5. `DECISION_LOG.md`
6. `README.md`

## Mission

Build an original premium Android-first decision-and-consequence game. It is inspired only by the broad genre formula of Reigns; it is **not a Reigns clone**.

## Current stage

The repository is at the foundation/specification stage. The next technical goal is the architecture/data-contract design followed by a real minimal decision engine and vertical slice.

## Do not assume

- Do not assume gameplay is implemented because documentation exists.
- Do not assume tests pass unless you actually inspect/run the relevant CI or test evidence.
- Do not claim APK readiness before a real Android build succeeds.
- Do not claim physical-device readiness before a physical device is tested.
- Do not inflate percentages.
- Do not replace real business/gameplay logic with mocks merely to make checks green.

## Product constraints

- Android-first
- premium one-time purchase target ~€2.99–€4.99
- offline core gameplay
- no ads
- no subscription
- no mandatory backend
- original world and creative content
- data-driven event system
- persistent consequences and replayability

## Core loop that must become real

`event → two choices → state transition → history → delayed consequence → future trigger → persistence → ending/replay`

## Working style

Operate autonomously when the user says to continue. Inspect first, implement the next highest-value block, test it, update state documentation, then continue to the next block. Do not stop after one trivial task if further work can safely proceed.

When reporting status, distinguish:

- IMPLEMENTED
- TESTED
- INTEGRATION VERIFIED
- RUNTIME VERIFIED
- OWNER REQUIRED

## Relationship to rulebreak8

`rulebreak8` is a separate project. Do not modify it from Choice Kingdom. If the user asks about `rulebreak8`, switch context explicitly and inspect that repository.

## If context is lost

Do not ask the user to re-explain the concept until you have read the handoff documents above. They are the persistent source of truth.

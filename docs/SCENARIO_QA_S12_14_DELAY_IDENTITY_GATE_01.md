# Choice Kingdom — S12.14 Delayed Identity Gate 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA
Frozen production scope: E01–E272.

## Purpose
Normalize identity requirements for long-delay callbacks E242–E246 without guessing authored turn values or cancellation semantics.

## Canonical identity contract
Every delayed callback must resolve to:
`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellation/supersessionRule`

This is an extraction gate, not runtime implementation.

## E242 — Renewed Exception
- Trigger: prior noble exception + 6+ turns.
- Canonical upstream source: `E118-B → estate_exception → E242`.
- Source choice identity: E118-B.
- `earliestTurn`: OPEN; exact authored relative-turn semantics required.
- `resolutionTarget`: OPEN.
- `exactlyOnceKey`: OPEN.
- `cancellation/supersessionRule`: OPEN.

## E243 — Old Bridge
- Trigger: public bridge investment + 5+ turns.
- Canonical upstream source: `E18-B → public_bridge → E243`.
- Source choice identity: E18-B.
- `earliestTurn`: OPEN.
- `resolutionTarget`: OPEN.
- `exactlyOnceKey`: OPEN.
- `cancellation/supersessionRule`: OPEN.

## E244 — Audit Comes Due
- Trigger: flexible accounts + 5+ turns.
- Canonical upstream source: `E09-B → flexible_accounts → E244`.
- Source choice identity: E09-B.
- `earliestTurn`: OPEN.
- `resolutionTarget`: OPEN.
- `exactlyOnceKey`: OPEN.
- `cancellation/supersessionRule`: OPEN.

## E245 — Soldier's Son Returns
- Trigger: compensation route + 6+ turns.
- Canonical source candidates: E125-A and E156-A compensation routes.
- Source choice identity: OPEN until authoritative text distinguishes accepted route(s).
- `earliestTurn`: OPEN.
- `resolutionTarget`: OPEN.
- `exactlyOnceKey`: OPEN.
- `cancellation/supersessionRule`: OPEN.
- Do not collapse E125-A/E156-A into a generic producer without authored evidence.

## E246 — Price Ceiling Memory
- Trigger: price ceiling + 5+ turns.
- Source event/choice identity: OPEN; authoritative producer row must be extracted.
- `earliestTurn`: OPEN.
- `resolutionTarget`: OPEN.
- `exactlyOnceKey`: OPEN.
- `cancellation/supersessionRule`: OPEN.
- Do not silently conflate `winter_rent_ceiling` with generic price-control state.

## Acceptance rules
1. Natural-language timing is not executable timing.
2. E242/E243/E244 retain exact closed producer identities.
3. E245 remains multi-candidate until source disambiguation is proven.
4. E246 remains source-open until its producer is extracted.
5. Exactly-once keys must include source choice identity.
6. Cancellation/supersession must be explicit and observable.
7. Save/load and replay isolation remain mandatory downstream checks.
8. E273–E277 cannot satisfy callback source requirements.

## Gate
S12.14 PASS for identity normalization and source-closure classification. No delayed callback is runtime-ready. Exact relative-turn semantics, targets and cancellation rules remain extraction blockers.

# Choice Kingdom — E33/E34 Source Recovery 01

Date: 2026-09-15
Status: **SOURCE RECOVERED — RECONCILIATION REQUIRED**

## Finding

The full authored text for E33 and E34 was recovered from the GitHub branch:

`qa/e35-e55-producer-audit`

Source file:
`docs/EVENT_CATALOG.md`

Recovered blob:
`61de059299400f4621b8e9c74e9c7c654c8fad5c`

This is not a reconstruction. The following text is the recovered authored source.

## E33 — The Emergency Crown

**Trigger:** `emergency_decree_used` or severe crisis.

Council offers unlimited emergency authority for thirty days.

**A — Accept**
- Immediate: +8 power, +5 security.
- Flag: `emergency_power`.
- Delayed: unless voluntarily surrendered, unlocks Iron Crown path.

**B — Refuse**
- Immediate: -4 power, +6 trust.
- Flag: `constitutional_limit`.
- If cross-faction relationships are strong, unlocks Second Founder path.

## E34 — The People's Queue

**Trigger:** trust >= 65 or welfare branch.

Thousands wait outside the palace with petitions during the winter crisis.

**A — Meet them**
- Immediate: +7 trust, -3 power.
- Flag: `people_heard`.

**B — Send written relief orders**
- Immediate: +3 trust, +2 power.
- If bureaucracy is weak, relief arrives late.

## Provenance assessment

- Exact event IDs: recovered.
- Exact headings: recovered.
- Exact trigger text: recovered.
- Exact narrative text: recovered.
- Exact choice text: recovered.
- Exact immediate effects: recovered.
- Exact authored flags: recovered.
- Exact delayed notes: recovered.

Therefore E33/E34 must no longer be classified as "original source unrecoverable".

## Canonical reconciliation requirement

The recovered source comes from a branch whose surrounding catalog differs from the current canonical main catalog. In particular, the recovered branch contains an earlier E32 authored formulation, while current main has the later canonical E32 transport-disruption formulation.

Therefore this recovery is **not** an instruction to blindly copy the entire historical branch back into `EVENT_CATALOG.md`.

The correct next step is surgical reconciliation:

1. Preserve the recovered E33/E34 text as source evidence.
2. Compare E33's `emergency_decree_used` producer against current canonical E01-E32 state vocabulary.
3. Compare E33's `severe crisis` trigger against current canonical crisis predicates.
4. Compare E33's `constitutional_limit` downstream consumers and ending contracts.
5. Compare E34's `people_heard` producer against all current consumers, especially E50 and ending prerequisites.
6. Determine whether current E32 should feed E33 directly or only satisfy the generic severe-crisis route.
7. Reconcile any stale branch-only event IDs before admitting the recovered nodes into production contracts.
8. Only after that reconciliation, update the canonical E01-E34 catalog and machine QA artifacts.

## Important rule

The recovered branch is historical source evidence, not automatically the current canonical version. No unrelated historical branch content should be reintroduced merely because E33/E34 were recovered there.

## Verdict

**E33/E34 SOURCE RECOVERY: CLOSED.**

**E33/E34 CANONICAL INTEGRATION: OPEN.**

**E33/E34 RUNTIME IMPLEMENTATION: NOT STARTED.**

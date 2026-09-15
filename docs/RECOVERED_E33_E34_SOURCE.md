# Choice Kingdom — Recovered E33/E34 Source

Date: 2026-09-15
Status: **RECOVERED FROM TRUSTED AUTHORED HISTORY**

The following exact authored source was recovered from commit `7e6c7d25f04a53402e5ee7b5051af793413bfacf` and restored locally into `docs/EVENT_CATALOG.md`.

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

## Canonical implication

E35 in the Act V continuation uses `E33 resolved` as its authored trigger. Therefore E33/E34 must remain canonical source IDs rather than being treated as legacy ending material.

This recovery does not close runtime reachability or trigger semantics; those remain in the canonical QA phase.

# Choice Kingdom — Canonical E33–E34 Event Source

This file is an authoritative catalog source for E33–E34. It restores the exact authored source recovered from the historical producer-audit branch without reconstructing or rewriting the event semantics.

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

## Source provenance

- Historical source branch: `qa/e35-e55-producer-audit`
- Historical source blob: `61de059299400f4621b8e9c74e9c7c654c8fad5c`
- Reconstruction: **false**
- This source is now included in the frozen catalog-source manifest. Machine trigger bindings remain separately governed by `docs/MACHINE_E33_E34_CANONICAL_CONTRACT_01.json`.

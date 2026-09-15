# Choice Kingdom — E33/E34 Canonical Integration Record

Status: INTEGRATION OPEN — source recovered exactly; canonical catalog insertion and executable consumer closure remain separate gates.

## Canonical recovered source

The exact authored source was recovered from the repository's historical `qa/e35-e55-producer-audit` branch, blob `61de059299400f4621b8e9c74e9c7c654c8fad5c`. It is recorded verbatim below so no narrative reconstruction is required.

### E33 — The Emergency Crown
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

### E34 — The People's Queue
**Trigger:** trust >= 65 or welfare branch.

Thousands wait outside the palace with petitions during the winter crisis.

**A — Meet them**
- Immediate: +7 trust, -3 power.
- Flag: `people_heard`.

**B — Send written relief orders**
- Immediate: +3 trust, +2 power.
- If bureaucracy is weak, relief arrives late.

## Reconciliation against current main

1. Current canonical `docs/EVENT_CATALOG.md` ends its foundational source at E32. E32 must remain the current main formulation; historical source material must not replace it.
2. E33's `emergency_decree_used` producer is already present in current E02-A.
3. The phrase `severe crisis` is not promoted here into an invented predicate. Before engine implementation, the exact crisis predicate/binding must be explicitly authored and machine-contractualized.
4. `emergency_power` and `constitutional_limit` are new canonical outcome flags. Their downstream consumers must be inventoried before any ending/engine predicate is inferred from them.
5. E34's `people_heard` is an explicit evidence flag. It must not silently become a final ending predicate. Existing consumers (including E50 and ending support/qualification logic) require semantic reconciliation.
6. E35+ expansion catalogs already depend on E33 being resolved; this record therefore treats E33 as a real authored production event, not a placeholder.
7. The historical branch is evidence for exact authorship, not an automatic authority override over current main. Canonical integration is complete only when the main source boundary, machine ID inventory, producer/consumer contracts, and CI validators all agree.

## Closure matrix

| Gate | Status | Rule |
|---|---|---|
| Exact authored E33 source | CLOSED | Recovered verbatim from historical authored branch |
| Exact authored E34 source | CLOSED | Recovered verbatim from historical authored branch |
| E02-A -> `emergency_decree_used` | CLOSED | Existing current-main producer |
| E33 severe-crisis executable predicate | OPEN | No invented alias permitted |
| `emergency_power` downstream inventory | OPEN | Must reconcile endings/consumers |
| `constitutional_limit` downstream inventory | OPEN | Must reconcile Second Founder / constitutional predicates |
| `people_heard` downstream inventory | OPEN | Must reconcile E50 and ending support semantics |
| Main EVENT_CATALOG insertion | OPEN | Requires surgical source update |
| Machine event-ID/contract update | OPEN | Must follow source insertion |
| CI canonical verification | OPEN | Must run after all source/contract edits |

## Non-goals

- Do not reconstruct E33/E34 from E35+ hints.
- Do not restore or overwrite current E32 with historical text merely because the historical branch contains an E32.
- Do not infer ending eligibility from support evidence.
- Do not mark the Decision Engine, runtime, APK, or release ready from this documentation alone.

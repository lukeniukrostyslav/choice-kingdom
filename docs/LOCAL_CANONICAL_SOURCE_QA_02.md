# Choice Kingdom — Local Canonical Source QA Report 02

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — GENERATED FROM THE UPLOADED ZIP; NOT ENGINE VALIDATION**

## Scope

The uploaded repository was unpacked and audited locally. This pass does not create production schema or runtime code. It reconciles the authoritative event-source boundary and records concrete source defects before the next canonicalization gate.

## Authoritative source boundary

- **E01–E32** → `docs/EVENT_CATALOG.md`
- **E33–E34** → **NO AUTHORITATIVE EVENT SOURCE PRESENT** (blocking gap)
- **E35–E70** → `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`
- **E71–E110** → `docs/EVENT_EXPANSION_071_110.md`
- **E111–E150** → `docs/EVENT_CATALOG_EXPANSION_111_150.md`
- **E151–E210** → `docs/EVENT_CATALOG_EXPANSION_151_210.md`
- **E211–E270** → `docs/EVENT_CATALOG_EXPANSION_211_270.md`
- **E271–E272** → `docs/EVENT_CATALOG_EXPANSION_271_280.md`

Non-canonical/legacy authoring sources retained for audit:
- `docs/EVENT_CATALOG_EXPANSION_02.md` — older E71–E110 draft/parallel source; must not be imported alongside the authoritative E71–E110 catalog.
- `docs/EVENT_CATALOG_EXPANSION_273_277.md` — authored P0 producer candidates; not part of the frozen E01–E272 production scope yet.

## Local inventory result

- Canonical event IDs discovered: **270 / 272**
- Missing IDs in E01–E272 boundary: **2** (`E33`, `E34`)
- Extra IDs in canonical boundary: **0**
- Duplicate titles in canonical boundary: **3** title pairs/groups
- Legacy/parallel source IDs overlapping canonical IDs: **40** (expected and retained outside canonical boundary)

The authoritative sources currently cover **E01–E32 and E35–E272**. E33/E34 are absent from the actual canonical source files even though multiple QA documents still describe them. This is a source-of-truth gap, not something to solve by inventing replacement events inside the engine.

## Source corrections applied locally

### 1. Removed duplicate E271 from the E211–E270 catalog
`docs/EVENT_CATALOG_EXPANSION_211_270.md` contained a second E271 bridge after E270. The authoritative E271/E272 source is `docs/EVENT_CATALOG_EXPANSION_271_280.md`; the duplicate would create two source definitions for the same stable ID. The duplicate block was removed locally without deleting the authoritative E271/E272 source.

### 2. Corrected E212 output token spelling
E212 now uses `clerk_disciplined` instead of the source typo `clerk_discipled`. The change is semantic-preserving normalization and matches the existing QA finding that the misspelling must not enter production schema.

## Remaining canonical source issues discovered

### A. E33/E34 are missing from the authoritative catalog
The actual authoritative `docs/EVENT_CATALOG.md` ends at E32. No `### E33` or `### E34` source exists anywhere in the uploaded repository. Older QA artifacts describe E33 as producing `emergency_power` / `constitutional_limit` and E34 as producing `people_heard` / a relief-orders branch, but those descriptions are not sufficient to reconstruct the authored event text without invention. E35 then explicitly uses `E33 resolved` as its trigger, so the missing pair currently creates a broken upstream dependency. **Required action: recover the original authored E33/E34 source from a trusted historical artifact or deliberately author replacements before canonical schema freeze. Do not manufacture them in runtime code.**

### B. E271 has an undefined legacy trigger token
Both copies of the E271 source use `thread.border` in the trigger. `thread.border` is not present in the canonical thread vocabulary; the canonical family is `thread.border_crisis`, but E271 cannot consume its own newly produced active crisis state. Therefore this must **not** be fixed by a blind alias to `thread.border_crisis`. The upstream trigger must be reconciled against the existing `pred.border_tension` / corroborated warning semantics before schema freeze.

### C. E144 still consumes legacy source vocabulary intentionally
E144 is triggered by `guild_political_representation` and produces canonical `history.guild_representation`. Existing QA defines the former as a source-language alias, not a second runtime fact. This mapping must be made explicit in the future trigger-normalization layer; it should not create a duplicate state key.

### D. E273–E277 are authored but remain outside the E01–E272 freeze
These nodes are useful P0 producer bridges for food stability, market pressure, guild labor tension, information pressure and transport recovery. They should be reconciled into the canonical campaign only after their triggers, downstream consumers, reachability and interaction with existing E01–E272 state are proven. They must not silently become production events merely because they exist in the repository.

## Duplicate-title review

- `Rowan's Oath` → E37, E96
- `The Baker's Ledger` → E71, E112
- `Toma's Price` → E82, E121

These are title collisions, not ID collisions. Preserve stable IDs and compare downstream semantics before any rename/merge decision.

## Canonicalization gate after this local pass

| Area | Result |
|---|---|
| E01–E272 source ID boundary | **BLOCKED — E33/E34 MISSING** |
| E271 duplicate source | **CORRECTED LOCALLY** |
| E212 spelling typo | **CORRECTED LOCALLY** |
| E35–E40 legacy collision | **DESIGN RESOLVED / RUNTIME MIGRATION OPEN** |
| E73/E156 semantic comparison | **OPEN** |
| E99/E173 semantic comparison | **OPEN** |
| E271 upstream trigger | **OPEN** |
| Producer/consumer ordering | **OPEN** |
| Delayed consequence identity/timing/cancellation | **OPEN** |
| Replay meta-state | **OPEN** |
| Ending reachability/precedence | **OPEN** |
| Production schema | **BLOCKED** |
| Decision Engine | **NOT STARTED BY DESIGN** |

## Next high-value source pass

1. Recover or deliberately re-author E33/E34 from a trusted source; do not invent runtime substitutes.
2. Resolve the E271 upstream trigger without introducing a circular alias.
3. Reconcile all canonical trigger tokens to exact producer choices or explicitly defined derived predicates.
4. Complete the exact producer set for guild influence, coalition cooperation, constitutional preparation and final charter prerequisites.
5. Reconcile delayed consequence source IDs, windows, exactly-once identity and cancellation/supersession.
6. Reconcile replay-only references into an explicit `meta.*` transfer contract.
7. Re-run graph/catalog reconciliation and reachability/ending analysis.
8. Only after those gates pass, freeze machine-readable production contracts.

## Integrity note

This report is a source-QA artifact. It does not claim runtime reachability, engine readiness, Android readiness or APK readiness.

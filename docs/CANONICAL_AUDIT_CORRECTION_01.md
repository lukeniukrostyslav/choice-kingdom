# Choice Kingdom — Canonical Audit Correction 01

Date: 2026-09-14

## Purpose

This correction supersedes inaccurate title examples previously recorded in `CANONICAL_EVENT_AUDIT_02.md`. The source catalogs were re-read directly before recording these corrections.

## Corrections

The following earlier examples were **incorrect** and must not be used for QA:

- E36 is **The Ledger Opens**, not Mara's Resignation.
- E95 is **The Noble Soup Kitchen**, not Mara's Resignation Letter.
- E96 is **The Guild Stores**, not Rowan's Oath.
- E37 is **The Choice of Heir**, not Rowan's Oath.

E226 is genuinely **Mara's Resignation**.

Therefore the previous claim that E36/E95/E226 and E37/E96 were repeated character-event titles is withdrawn.

## Confirmed repetition / near-repetition candidates from inspected sources

These are genuine QA candidates observed in the actual catalogs:

- E73 **The Widow's Petition** and E156 **The Widow's Petition** — same title; must be checked for materially different prerequisites, consequences and narrative purpose.
- E99 **The Empty Barracks** and E173 **The Empty Barracks** — same title; must be checked as distinct state-reactive callbacks rather than duplicate scenes.
- E226 **Mara's Resignation** is thematically related to earlier institutional-loyalty material, but no duplicate title claim is made without further source verification.

## Confirmed concrete normalization defects

### E118 — non-selective relationship gate

E118 uses `Seris >= 0`. Because the relationship model is -3..+3, this includes neutral and positive states and is potentially much broader than a meaningful relationship gate. It should be retained only if neutrality is intentionally sufficient; otherwise replace it with an explicit threshold or canonical route condition.

### E192 — non-canonical resource

E192 uses `+4 food stability` as an effect. The canonical state vocabulary defines five primary numeric resources only: gold, trust, security, power and reputation. Food stability must therefore become either a deterministic derived condition or an explicitly approved durable state fact; it must not silently become a sixth numeric resource.

### E112/E123/E138/E218/E225 — food-pressure vocabulary

These events use variants such as `food-price pressure`, `food shortage`, `food pressure` and `severe food pressure`. They require one deterministic canonical definition or explicitly separated predicates.

### E136/E139/E172/E240/E253 — border vocabulary

The catalog uses `winter severity`, `border tension`, `border pressure`, `border crisis`, and related route shorthand. These need canonical derived predicates rather than free-form trigger prose.

### E131 — replay state wording

E131 explicitly references previous-run information and simultaneously says that the informational callback flag is unavailable to the current save. This must be represented using versioned `meta.*` state, never an ordinary current-run flag.

## Current audit rule

Source files are authoritative evidence for audit findings. Any audit entry that conflicts with the actual catalog must be corrected before it can influence implementation.

No content-readiness percentage is increased merely because a defect was documented.

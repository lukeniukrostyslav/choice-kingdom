# Choice Kingdom — Premium Design P3 People Codex QA v1

Status: **P3 VISUAL IMPLEMENTATION PROOF — 15%**

Date: 2026-09-17

## Scope

This checkpoint verifies the first real P3 implementation surface: a portrait-led People / Character Codex designed for premium mobile presentation. It is intentionally separated from canonical character binding so visual work can proceed without inventing game data.

## Implemented surface

- `web-preview/design-people-codex-p3.html`
- Launcher entry added in `web-preview/index.html`
- Portrait-led character cards with identity, role, visual tier and canonical-binding status.
- Detail rhythm for narrative context, relationship/consequence tags and production-gate visibility.
- Responsive mobile composition for compact portrait widths.
- Light/dark theme behavior.
- LTR/RTL direction toggle and mirrored card layout.
- Explicit noncanonical labeling for existing candidate artwork.

## QA matrix

| Check | Result |
|---|---|
| Portrait-first hierarchy | PASS |
| Human identity before metadata | PASS |
| Candidate artwork clearly noncanonical | PASS |
| No invented character IDs | PASS |
| No invented faction binding | PASS |
| No good/evil faction color coding | PASS |
| Mobile two-column → one-column adaptation | PASS |
| Compact 360–430px composition rules | PASS |
| Light/dark presentation | PASS |
| RTL layout direction | PASS |
| Long text tolerance | PASS |
| Touch-sized theme/direction controls | PASS |
| Canonical People binding | OPEN |
| Final authored production portraits | OPEN |
| Provenance/licensing | OPEN |
| Rendered Vercel/mobile inspection | DEFERRED by production workflow |

## Percentage decision

P3 advances from 0% to **15%** because a real, inspectable People Codex surface is now implemented and exposed from the design launcher. This percentage does **not** claim canonical data integration, final artwork, provenance, or rendered Vercel validation.

## Next gate

Continue P3 only after the canonical People source is identified and bound without fabrication. Then add real character entries, relationship states and production artwork while preserving the current portrait-led visual hierarchy.

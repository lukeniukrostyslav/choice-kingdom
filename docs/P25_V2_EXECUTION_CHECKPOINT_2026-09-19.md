# P25 Premium Design — V2 Execution Checkpoint

Date: 2026-09-19
Branch: main
Status: OPEN
P25: 92%
Premium Design P1–P25 aggregate: 99.68%

## What changed in V2

- Added `web-preview/game-premium.html` as the stronger cinematic game presentation surface.
- Moved repository root and `web-preview/index.html` to the premium game entry.
- Preserved canonical E01, E02 and E05 gameplay vocabulary.
- Preserved canonical People: Mara, Rowan, Seris, Ivo, Amara, Toma.
- Preserved canonical institutional vocabulary: Crown, Commons, Noble, Guild, Border / Security, Civic / Medical.
- Removed reliance on the old review/landing page as the intended game entry.
- Kept responsive, safe-area, RTL, large-text, reduced-motion and local persistence behavior in the premium surface.
- Updated the P25 interactive gate to exercise the premium surface.

## P25 sub-blocks

| Sub-block | % | Current evidence / remaining |
|---|---:|---|
| 25.1 Visual game shell / cinematic composition | 96% | Full-screen atmospheric shell and framed game scenes implemented; final reference comparison remains. |
| 25.2 Main menu / first impression | 95% | Cinematic launcher with realm backdrop and direct start/continue actions; deployment proof remains. |
| 25.3 Event / situation scene | 96% | E01/E02/E05 presented as framed narrative scenes with illustrated chamber treatment. |
| 25.4 Choice chamber / decision interaction | 95% | Canonical choices, effects, touch-sized controls and state transitions implemented. |
| 25.5 Consequence / memory reveal | 95% | Dedicated consequence scene, effect readout and recorded flag implemented. |
| 25.6 Kingdom / realm presentation | 94% | Full map-style realm surface with nodes and realm vocabulary implemented. |
| 25.7 People / character presentation | 92% | Six canonical People with stronger illustrated presentation; final production-art provenance remains open. |
| 25.8 Factions / institutional presentation | 92% | Six canonical institutional positions with banner/sigil presentation; final production-art provenance remains open. |
| 25.9 Investigation / evidence board | 94% | Four verified routes and physical evidence-board composition implemented. |
| 25.10 History / decision chronicle | 95% | Decision timeline is interactive and records the current run. |
| 25.11 Endings / resolution landing | 93% | Resolution surface is present without inventing a current ending outcome. |
| 25.12 Settings / accessibility presentation | 95% | Large text, RTL, reduced motion, presentation toggle and reset are implemented. |
| 25.13 Navigation / information architecture | 95% | Persistent game navigation across all major surfaces is implemented. |
| 25.14 Responsive / safe-area composition | 94% | Mobile/tablet/desktop CSS reflow and safe-area padding are implemented; live device proof remains. |
| 25.15 Visual regression / final acceptance | 72% | Previous gate was green, but V2 requires a fresh green run and frozen-reference visual comparison. |

## Honest closure rule

P25 is not 100% yet. The percentages above reflect implementation progress after V2 and do not replace the final visual regression gate. A green automated test is necessary but is not by itself proof that the deployed game visually matches the approved references.

## Final V2 correction

The institutional/faction presentation was rechecked against the canonical vocabulary and the descriptive copy was reduced to the neutral label **Verified institutional position**. No generated faction lore, motto, territory, relationship state or invented kingdom name is used by the V2 presentation.

Latest implementation commit: `26bd12f43d4a337591aca9d7c3cb7683d6e85813`.

## Save rule

This checkpoint is committed to GitHub on `main` so the V2 state and percentages are recoverable.

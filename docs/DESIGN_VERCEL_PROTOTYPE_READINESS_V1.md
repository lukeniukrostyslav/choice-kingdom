# Choice Kingdom — Design → Vercel Prototype Readiness V1

Status: ACTIVE — autonomous visual prototype production.

The D1–D22 production design contract is closed at 100%. This tracker measures conversion of that closed design contract into a reviewable static Vercel surface.

## Prototype blocks

| Block | Scope | Status |
|---|---|---:|
| V1 | Visual asset inventory and existing preview audit | 100% |
| V2 | Missing authored artwork production | 0% |
| V3 | Design tokens → web presentation layer | 100% |
| V4 | Prototype entry/launcher and navigation surface | 100% |
| V5 | Event/choice visual slice | 100% |
| V6 | Character/faction visual surface | 100% |
| V7 | Realm/dashboard visual surface | 100% |
| V8 | History/chronicle visual surface | 100% |
| V9 | Investigation/evidence visual surface | 100% |
| V10 | Ending/outcome visual surface | 100% |
| V11 | Settings/accessibility visual surface | 100% |
| V12 | Theme, responsive, large-text and RTL review | 100% |
| V13 | Motion/feedback presentation | 95% |
| V14 | Cross-screen visual integration | 97% |
| V15 | Mobile visual QA on the static preview | 90% |
| V16 | Vercel production build configuration | 100% |
| V17 | Published Vercel deployment | 0% — deployment action not yet verified |
| V18 | Published-prototype final visual QA | 0% |

**Prototype tracker average: 82.50%.** This average includes V2, V17 and V18 as real remaining gates; it is intentionally not presented as the D1–D22 design percentage.

## Current executable surface

`web-preview/game-flow.html` provides a clickable Event → Choice → Consequence → Investigation/Evidence → Ending flow plus Realm, Characters, History and Settings. Theme, large-text and RTL controls are interactive. Evidence confidence/source presentation and ending-state navigation are part of the same reviewable surface.

## Latest local QA pass

The local design smoke check validates the eight primary screens, five authored SVG assets, local artwork references, state-continuity markers, accessible skip navigation, navigation labelling, duplicate HTML IDs, reduced-motion support, and explicit interactive target sizing for navigation (48px) and choice controls (56px). The local pass is green. Browser-based visual regression is still a separate gate because the local Playwright/Chromium run has not produced a complete screenshot evidence set yet.

## Rules

1. D1–D22 percentages are not changed by this tracker and remain closed at 100%.
2. A preview file is not counted as final authored artwork.
3. V17 is not marked complete until an actual Vercel deployment is verified.
4. V18 requires checking the published deployment, not only repository files.
5. Android runtime, physical device QA, signing and store release remain separate engineering gates.
6. Work proceeds autonomously in dependency order and each meaningful change is committed to GitHub.
7. Percentages increase only after executable or auditable evidence exists.

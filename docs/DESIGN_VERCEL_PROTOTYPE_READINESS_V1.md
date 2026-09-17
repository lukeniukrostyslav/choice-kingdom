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
| V13 | Motion/feedback presentation | 100% |
| V14 | Cross-screen visual integration | 100% |
| V15 | Mobile visual QA on the static preview | 90% |
| V16 | Vercel production build configuration | 100% |
| V17 | Published Vercel deployment | 0% — deployment action not yet verified |
| V18 | Published-prototype final visual QA | 0% |

**Prototype tracker average: 82.78%.** This average includes V2, V15, V17 and V18 as real remaining gates; it is intentionally not presented as the D1–D22 design percentage.

## V13 / V14 closure

V13 and V14 were closed at 100% in `docs/V13_V14_CLOSURE_AUDIT_01.md`. The integrated `web-preview/game-flow.html` now has explicit entrance motion, choice confirmation feedback, reduced-motion handling, live announcements, active-tab synchronization with `aria-current`, persistent choice state, and state propagation across Consequence, Investigation, History, Ending, Realm and Character surfaces.

## Current executable surface

`web-preview/game-flow.html` provides a clickable Event → Choice → Consequence → Investigation/Evidence → Ending flow plus Realm, Characters, History and Settings. Theme, large-text and RTL controls are interactive. Evidence confidence/source presentation and ending-state navigation are part of the same reviewable surface.

## QA boundary

The repository-level smoke contract covers primary screens, authored assets, local references, state continuity, accessibility markers and interaction target sizing. Browser-based visual regression remains a separate gate: V15 is not promoted to 100% until the screenshot/viewport evidence set is actually produced. V17/V18 likewise remain closed until publication and published-surface QA are verified.

## Rules

1. D1–D22 percentages are not changed by this tracker and remain closed at 100%.
2. A preview file is not counted as final authored artwork.
3. V17 is not marked complete until an actual Vercel deployment is verified.
4. V18 requires checking the published deployment, not only repository files.
5. Android runtime, physical device QA, signing and store release remain separate engineering gates.
6. Work proceeds autonomously in dependency order and each meaningful change is committed to GitHub.
7. Percentages increase only after executable or auditable evidence exists.

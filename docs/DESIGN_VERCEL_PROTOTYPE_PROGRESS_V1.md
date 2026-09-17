# Choice Kingdom — Design Vercel Prototype Progress V1

Updated after autonomous runtime QA hardening on 2026-09-17.

## D1–D22 design contract

**Overall: 100%.** The production design contract is closed; executable prototype work is tracked separately below.

## Executable prototype blocks

| Block | Status | Evidence / meaning |
|---|---:|---|
| V1 Asset inventory | 100% | audited preview asset families |
| V2 Final authored artwork | 0% | five authored SVGs are produced and integrated into `game-flow.html`; gate remains closed until the corrected automated visual regression run passes |
| V3 Web presentation layer | 100% | executable static web surface |
| V4 Launcher / navigation | 100% | launcher + seven-tab flow |
| V5 Event / Choice | 100% | event screen, three choice states and persisted selection |
| V6 Characters / Factions | 100% | authored portraits + faction mark integrated in People |
| V7 Realm / Dashboard | 100% | realm metrics and state-aware presentation |
| V8 History / Chronicle | 100% | chronology presentation with recorded decision continuity |
| V9 Investigation / Evidence | 100% | evidence source + confidence surface |
| V10 Ending / Outcome | 100% | ending surface + authored atmosphere + recorded decision outcome + return paths |
| V11 Settings / Accessibility | 100% | theme, large text, RTL controls |
| V12 Responsive / RTL / Large text | 100% | mobile-first CSS and state controls |
| V13 Motion / Feedback | 100% | screen entrance, hover/selection, focus-visible, reduced-motion handling |
| V14 Cross-screen Integration | 100% | event → consequence → evidence → ending carries the selected decision into Realm, People, History and Ending; state persists locally |
| V15 Mobile Visual QA | 85% | four required viewport sizes are registered; executable regression is still awaiting a verified GREEN run |
| V16 Vercel Build Configuration | 100% | static prototype structure plus explicit `vercel.json` asset delivery policy |
| V17 Actual Vercel Deployment | 0% | no verified published deployment yet |
| V18 Published Prototype QA | 0% | blocked until V17 is verified |

**Executable prototype tracker: ~82.8% by the current block-weighted arithmetic average.** V2 and V15 are intentionally not inflated until executable regression evidence exists.

## Latest autonomous implementation

### Authored artwork integrated

Five project-authored SVG assets are wired into the executable main flow and have a dedicated review surface:

- `web-preview/artwork/event-empty-granary.svg` — Event hero
- `web-preview/artwork/queen-elira.svg` — Queen Elira portrait
- `web-preview/artwork/lord-cael.svg` — Lord Cael portrait
- `web-preview/artwork/river-compact.svg` — River Compact faction mark
- `web-preview/artwork/ending-chronicle.svg` — Ending atmosphere

### Regression gate hardening

The visual regression workflow tests only repository-existing preview surfaces, four required viewport sizes, and all five authored SVG assets. It now also waits for the preview HTTP server to become reachable before starting Playwright. 

The runtime gate additionally records and fails on uncaught page errors, browser `console.error` events, failed network requests, and broken images. Screenshots and a machine-readable `manifest.json` remain workflow artifacts.

### Runtime QA contract

`docs/DESIGN_RUNTIME_QA_CONTRACT_V1.md` now defines the auditable rules for document integrity, browser runtime integrity, authored artwork integrity, responsive evidence, accessibility presentation, and state continuity. This prevents visual completeness from being counted while browser runtime defects remain.

### Vercel delivery preparation

`vercel.json` provides clean URLs, security response headers and immutable caching for authored SVG artwork. This is deployment preparation, not evidence of a live deployment.

## Completion rules

- Never increase a percentage without executable or auditable evidence.
- D1–D22 remain exactly 100%; prototype progress does not inflate the design-contract percentage.
- V2 can move above 0% only after authored artwork is integrated **and** the corrected visual regression gate passes.
- V15 requires an executed mobile/browser regression pass, not merely responsive CSS.
- V17 requires a real Vercel deployment URL or equivalent verified deployment evidence.
- V18 requires QA against the published deployment.

## Next autonomous sequence

1. Inspect the latest visual regression execution/status.
2. If RED, fix the concrete browser/design defect and commit a new checkpoint.
3. If GREEN, close V2 and V15 using the recorded evidence and recalculate the tracker.
4. Continue visual polish and deployment readiness checks.
5. Verify actual Vercel deployment when a deployment mechanism produces a real URL.
6. Run published-deployment QA and close V18 only with evidence.

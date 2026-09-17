# Choice Kingdom — Design Vercel Prototype Progress V1

Updated after autonomous authored-art integration and deployment-preparation pass on 2026-09-17.

## D1–D22 design contract

**Overall: 100%.** The production design contract is closed; executable prototype work is tracked separately below.

## Executable prototype blocks

| Block | Status | Evidence / meaning |
|---|---:|---|
| V1 Asset inventory | 100% | audited preview asset families |
| V2 Final authored artwork | 0% | five authored SVGs are produced and integrated into `game-flow.html`; gate remains closed until the automated visual regression run passes |
| V3 Web presentation layer | 100% | executable static web surface |
| V4 Launcher / navigation | 100% | launcher + seven-tab flow |
| V5 Event / Choice | 100% | event screen, three choice states and persisted selection |
| V6 Characters / Factions | 100% | authored portraits + faction mark now integrated in People |
| V7 Realm / Dashboard | 100% | realm metrics and state-aware presentation |
| V8 History / Chronicle | 100% | chronology presentation with recorded decision continuity |
| V9 Investigation / Evidence | 100% | evidence source + confidence surface |
| V10 Ending / Outcome | 100% | ending surface + authored atmosphere + recorded decision outcome + return paths |
| V11 Settings / Accessibility | 100% | theme, large text, RTL controls |
| V12 Responsive / RTL / Large text | 100% | mobile-first CSS and state controls |
| V13 Motion / Feedback | 100% | screen entrance, hover/selection, focus-visible, reduced-motion handling |
| V14 Cross-screen Integration | 100% | event → consequence → evidence → ending carries the selected decision into Realm, People, History and Ending; state persists locally |
| V15 Mobile Visual QA | 85% | automated regression matrix now covers 360x800, 412x915, 412x1000 and 1440x900; latest run is still executing |
| V16 Vercel Build Configuration | 100% | static prototype structure plus explicit `vercel.json` asset delivery policy |
| V17 Actual Vercel Deployment | 0% | no verified published deployment yet |
| V18 Published Prototype QA | 0% | blocked until V17 is verified |

**Executable prototype tracker: ~82.8% by the current block-weighted arithmetic average.** V2 is intentionally not inflated until the regression gate passes.

## Latest autonomous implementation

### Authored artwork integrated

The five project-authored SVG assets are now wired into the executable main flow:

- `web-preview/artwork/event-empty-granary.svg` — Event hero
- `web-preview/artwork/queen-elira.svg` — Queen Elira portrait
- `web-preview/artwork/lord-cael.svg` — Lord Cael portrait
- `web-preview/artwork/river-compact.svg` — River Compact faction mark
- `web-preview/artwork/ending-chronicle.svg` — Ending atmosphere

`web-preview/artwork-preview.html` provides a dedicated review surface, and `docs/DESIGN_ARTWORK_CATALOG_V1.md` records stable IDs, crop intent and provenance.

### Regression gate upgraded

`.github/workflows/design-visual-regression.yml` now tests the main `game-flow.html`, the artwork review surface and the existing design surfaces at mobile and desktop viewports. It also verifies that all five authored SVG assets return successfully and records screenshot/manifest evidence as a workflow artifact.

The latest regression run for commit `90b63289125ff546ef0d989a36f25cbd9e536c87` is currently **in progress**, so no pass is claimed yet. fileciteturn58file0L2-L2

### Vercel delivery preparation

`vercel.json` was added with clean URLs, security response headers and immutable caching for authored SVG artwork. This prepares static asset delivery but does not count as an actual deployment.

## Completion rules

- Never increase a percentage without executable or auditable evidence.
- D1–D22 remain exactly 100%; prototype progress does not inflate the design-contract percentage.
- V2 can move above 0% only after authored artwork is integrated **and** the visual regression gate passes.
- V15 requires an executed mobile/browser regression pass, not merely responsive CSS.
- V17 requires a real Vercel deployment URL or equivalent verified deployment evidence.
- V18 requires QA against the published deployment.

## Next autonomous sequence

1. Monitor/verify the current visual regression gate.
2. If it fails, diagnose and fix the concrete visual/asset issue and re-run through the next push.
3. If it passes, close V2 with auditable evidence and recalculate the tracker.
4. Continue hardening the Vercel-ready surface.
5. Proceed to actual Vercel deployment verification when a deployment mechanism is available; do not mark V17 complete without a real URL.
6. Run published-deployment QA and close V18 only after evidence is captured.

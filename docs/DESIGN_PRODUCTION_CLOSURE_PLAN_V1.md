# Choice Kingdom — Design Production Closure Plan v1

Status: ACTIVE — autonomous design closure

This document tracks the 22 working design blocks as production-work estimates. It does not convert design specification into runtime/device completion.

## 22-block current status

| Block | Current | Closure target | Evidence |
|---|---:|---:|---|
| D1 Design Specification / Contract | 100% | 100% | contract + screen matrix |
| D2 Design Tokens / Theme | 100% | 100% | semantic token contract v1.1 with light/dark mappings, typography, component tokens, states, motion and accessibility rules |
| D3 Event Screen | 100% | 100% | event/edge-case/state closure contract |
| D4 Choice System / States | 100% | 100% | complete interaction-state closure contract |
| D5 Consequence Feedback | 100% | 100% | consequence-state and hidden-future contract |
| D6 Realm / Kingdom Dashboard | 100% | 100% | sparse/full/state and responsive contract |
| D7 History / Chronicle | 100% | 100% | empty/long/RTL/state contract |
| D8 Character System | 100% | 100% | portrait/relationship/availability contract |
| D9 Faction System | 100% | 100% | complete stance-state contract |
| D10 Investigation / Evidence | 100% | 100% | uncertainty/branching evidence closure contract |
| D11 Ending / Outcome | 100% | 100% | ending-family visual closure contract |
| D12 Navigation / Transitions | 100% | 100% | transition/focus/reduced-motion closure contract |
| D13 Settings / Accessibility Controls | 100% | 100% | control/state closure contract |
| D14 RTL / Localization-ready UI | 100% | 100% | RTL/CJK/long-string closure contract |
| D15 Large Text / Responsive Layout | 100% | 100% | 360/412/tall/safe-area closure contract |
| D16 Accessibility / Semantics | 100% | 100% | semantics/focus/state closure contract |
| D17 Visual Language / Art Direction | 100% | 100% | visual language/art-direction closure contract |
| D18 Asset / Illustration System | 100% | 100% | asset-family/crop/fallback/art-direction closure contract; final artwork production remains separate |
| D19 Motion / Micro-interactions | 100% | 100% | state-motion/reduced-motion closure contract |
| D20 Visual QA / Regression | 98% | 100% | executable Playwright regression gate committed; actual Actions execution evidence still required for final 2% |
| D21 Cross-screen Design Integration | 100% | 100% | cross-screen invariant and shared-language closure contract |
| D22 Production Mobile Design Handoff | 100% | 100% | implementation-ready design handoff contract |

**Current design-production average: 99.91%** (21 blocks at 100%, D20 at 98%).

## Rules

1. A percentage increases only after a concrete artifact, audit, implementation evidence, or verification supports the increase.
2. A checklist file by itself is not execution evidence.
3. The asset manifest is a contract; it does not prove that every final artwork exists.
4. Runtime UI, Android implementation, physical device QA, signing and store release remain separate engineering gates.
5. Work proceeds in dependency order and every completed design artifact is committed to GitHub.
6. D20 cannot be raised from 98% to 100% until actual visual regression evidence exists; this is intentionally not fabricated from documentation.

## Latest autonomous closure pass

- Added `.github/workflows/design-visual-regression.yml`.
- The gate serves `web-preview`, launches Chromium through Playwright, captures 9 critical design screens at 360x800, 412x915 and 412x1000, records overflow/text metrics, and uploads the visual evidence artifact.
- This converts D20 from a documentation-only checkpoint into an executable verification gate.
- The workflow is intentionally not treated as executed evidence until GitHub Actions produces a completed run and artifact.

## Remaining design work

D20 Visual QA / Regression remains at 98% pending the first successful executed visual regression run. Once the run produces a valid artifact with all required matrix entries passing, D20 can move to 100% and the design-production average becomes 100%.

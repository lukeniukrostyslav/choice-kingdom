# Choice Kingdom — V16 Design QA Progress

## Scope

V16 is the visual-QA hardening pass for the completed V2 design preview. It does not claim Android runtime completion; it verifies the static Vercel-ready presentation surface against the existing design QA contract.

## Closure matrix

| V16 block | Progress | Evidence |
|---|---:|---|
| 1. Preview serving contract | 100% | Dedicated GitHub Actions workflow serves `design-preview` and verifies HTTP response. |
| 2. 360dp portrait | 100% | Automated Playwright viewport case in the V16 matrix. |
| 3. 412dp portrait | 100% | Automated Playwright viewport case in the V16 matrix. |
| 4. Tall phone / 412x1000 | 100% | Automated Playwright viewport case in the V16 matrix. |
| 5. Desktop / 1440x900 | 100% | Automated Playwright viewport case in the V16 matrix. |
| 6. Overflow / clipping guard | 100% implementation | Matrix fails on horizontal overflow and broken images. CI execution is still required to mark the gate GREEN. |
| 7. Interactive target guard | 100% implementation | Matrix rejects visible controls below 48px in either dimension. CI execution is still required to mark the gate GREEN. |
| 8. Accessibility presentation guard | 100% implementation | Matrix checks focus-visible, reduced-motion CSS, RTL CSS, viewport-fit meta, runtime console/page/request errors. CI execution is still required to mark the gate GREEN. |
| 9. Cross-screen navigation | 100% implementation | Matrix programmatically visits Event, Realm, History, People, Investigation, Ending and Settings and asserts the selected view is active. CI execution is still required to mark the gate GREEN. |
| 10. Evidence artifact | 100% implementation | Workflow uploads `v16-evidence.json` for every run. |

**V16 implementation: 100%.**

**V16 verification state: PENDING CI RUN.** The repository connector can create the workflow but cannot truthfully claim a GitHub Actions execution result until GitHub runs it.

## Relation to V2

V2 remains closed as the visual implementation layer. V16 adds an executable regression gate around that preview so subsequent V17/V18 work cannot silently regress the responsive/accessibility presentation surface.

# Choice Kingdom — V2 Design Progress

This document tracks **real V2 visual implementation**, not the already-closed design specification.

## Current V2 progress

| V2 block | Progress | Evidence |
|---|---:|---|
| 1. Visual foundation / tokens | 100% | Responsive visual shell, surfaces, typography, semantic state styling in `design-preview/index.html`. |
| 2. Event screen | 100% | Art area, event eyebrow/title/narrative and responsive composition implemented. |
| 3. Choice cards / interaction states | 100% | Two opposing choices, focus-visible styling, minimum-height controls and resolving/disabled behavior implemented. |
| 4. Resource/status strip | 100% | Five resource indicators implemented in the event preview. |
| 5. Character / faction presentation | 0% | Dedicated runtime preview components not yet implemented in V2 slice. |
| 6. History / consequence presentation | 35% | Immediate consequence feedback exists; dedicated History screen is still open. |
| 7. Secondary navigation | 100% | Realm / History / People navigation surface is present in the preview. |
| 8. Responsive/mobile layout | 100% | Mobile-first layout plus larger viewport treatment implemented; no fixed-width desktop dependency. |
| 9. Accessibility / RTL / presentation states | 55% | Semantic labels, keyboard focus, status role and non-color feedback are present; RTL and full large-text/locale validation remain open. |
| 10. Final V2 visual QA | 20% | Preview exists; complete cross-screen visual regression remains open. |

**V2 overall: 66%** (weighted implementation checkpoint; this is not a claim of final V2 closure).

## V2 closure gate

V2 may be marked 100% only after the remaining character/faction, history/consequence, RTL/large-text, and cross-screen visual-QA work is implemented and verified.

## Preview

`design-preview/index.html` is a self-contained static V2 visual slice intended to be deployable as the Vercel project root.

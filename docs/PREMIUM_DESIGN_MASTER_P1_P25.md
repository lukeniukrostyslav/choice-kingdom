# Choice Kingdom — Premium Design Master P1–P25

Status: ACTIVE — premium-design execution track

This document is the canonical working checklist for the 25-block premium visual design track. Percentages are engineering/design completion estimates, not claims of commercial quality or store readiness. A block reaches 100% only when its visual contract, representative implementation/proof, responsive behavior, accessibility requirements, and regression evidence are present.

## Premium Design P1–P25

| Block | Scope | Current | Exit gate |
|---|---|---:|---|
| P1 | Premium vision / art direction | 15% | Signed visual north star + representative screens |
| P2 | Core visual identity / design language | 0% | Tokenized identity applied across representative surfaces |
| P3 | Typography / type hierarchy | 0% | Complete type scale, wrapping, accessibility and locale rules |
| P4 | Color / materials / surfaces | 0% | Semantic color/material tokens + contrast proof |
| P5 | Layout / grid / spacing / responsive system | 0% | Responsive contracts across target window classes + safe-content bounds |
| P6 | Choice experience / choice cards / choice chamber | 0% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 0% | Full event surface and state variants |
| P8 | Character presentation | 0% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 0% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 0% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 0% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 0% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 0% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 0% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 0% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 0% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 0% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 0% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 0% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 0% | Purposeful semantic motion + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 0% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 0% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 0% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 0% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 0% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 0.60% (V2 baseline; simple arithmetic mean).**

## Visual Design Reset v2

- The legacy visual percentages are retired for the new V2 implementation track.
- The canonical V2 reset contract is `docs/VISUAL_DESIGN_RESET_V2.md`.
- Fresh V2 P1 visual anchor: `web-preview/design-v2/p1-visual-anchor.html`, commit `bed0154c738bb083ff0fb1c1a3a44a992311619d`.
- P1 is intentionally 15%: the new visual anchor exists, but the shared design system, representative screen set, responsive/accessibility proof and regression closure are not complete.
- P2–P25 are intentionally 0% until rebuilt on the V2 foundation. Existing legacy implementations remain preserved in Git history and are not counted as V2 completion.

## Current evidence

- androidApp/ is the first real Android Compose application module, with launcher Activity, adaptive Compact/Medium/Expanded presentation, safe-drawing insets and semantic interaction states.
- The Android event surface now consumes an immutable AndroidPresentationPort projection through a narrow presentation-only adapter; the current launcher uses an explicitly named sample projection until the production runtime bridge is available.
- Event title, event id, turn and authored choice id/label/text are rendered from the projection rather than from a parallel Android gameplay model. Choice interaction is UI-local and does not mutate canonical gameplay.
- Android instrumentation coverage now includes projection rendering and accessible selected-state interaction; the workflow runs build, JVM tests and emulator instrumentation tests.
- .github/workflows/android-presentation.yml uses Java 17, Android SDK setup and pinned Gradle 8.7.3.
- The Android layer is presentation-only; canonical gameplay remains owned by the existing runtime seam.
- runtime/premium_screen_states.py, runtime/premium_surface_projection.py and runtime/premium_regression_matrix.py remain the canonical platform-neutral presentation contracts.
- Existing rendered preview evidence covers responsive density, RTL, large text, reduced motion, safe area and focus-visible behavior.
- Physical Android/device proof is not claimed yet; emulator CI is verification infrastructure, not a substitute for final target-device evidence.
- The canonical visual north star is recorded in design-reference/FINAL_DESIGN_VISION_V1.md; it defines the premium cinematic medieval-fantasy direction used to evaluate subsequent P1–P25 work.
- Latest P1 implementation commit `d875add3aea74893c42f7af0283f2a74c503477c` adds explicit Large Text and RTL review controls, semantic pressed-state exposure, 48px interaction targets and reduced-motion handling on the representative art-direction surface. Inspection evidence was synchronized in `9735a50637f9e8a8d392bc52bf1ca99e02a92ee6`. These strengthen reproducible review coverage; P1 remains 72% because the locked exit gate still requires actual rendered Android/runtime evidence and final asset provenance/licensing.
- P21 accessibility review surface now has executable Large Text, RTL and Reduced Motion controls, with V15 closure checks added in commit `15647fd1f802283735cc958427b879b4eb7aba34`. The implementation is strengthened, but P21 remains 84% until the updated gate has confirmed CI evidence and Android accessibility-service/device proof.
- P1 art-direction review surface has been strengthened with layered card depth, focus-within treatment, long-label resilience and reduced-motion-safe presentation; latest implementation commits `583b26f782066b064821fec4fc76fb3c522d04fe` and `a4b7598fc807e6499cbacc12e6c5c45857cf0e7a`. P1 remains 72% pending its full exit gate.
- P2 representative People & Factions surface now uses explicit shared canvas/surface/elevation/accent/radius/spacing tokens, plus resilient heading wrapping; implementation commit `fcff1be22b2170affc1bd0d9aa459f906e4fbde9`. P2 remains 74% pending cross-surface token application and regression proof.
- P13 relationship presentation has a committed premium visual surface and green V15 cross-viewport closure: run #647 / ID 35335301852.
- P14 investigation presentation has a committed premium visual surface and green V15 cross-viewport closure: run #651 / ID 35335654075, head 873efe4b1438616b2690fe53853b8765e3fb1adb, completed 2026-09-18.
- P15 crisis presentation: green V15 cross-viewport closure, run #654 / ID 35335872569, completed 2026-09-18.
- P16 ending presentation: green V15 cross-viewport closure, run #658 / ID 35336044736, completed successfully.
- P17 replay presentation: green V15 cross-viewport closure, run #664 / ID 35336289832, head f1112a80da7f829404fcff49d8eeab7194c5364e, completed successfully.
- P18 launcher: committed premium first-impression surface in web-preview/index.html, with green V15 cross-viewport closure run #665 / ID 35336465517, head f2f38a0b6f01b8a9ea027593b2f420dd4164d53a; launcher theme and viewport-fit checks passed.

## Quality rules

- Do not copy competitor art, branding or proprietary UI.
- Use competitors and award-winning games for interaction principles, not imitation.
- Never mark a block 100% because a document exists.
- Every important state needs an explicit visual state where applicable.
- Reduced motion, large text, RTL and long-string behavior are part of the design.
- Android/device proof is required before claiming production UI completion.

## Next bottleneck

Continue the premium-design track with P19 — Navigation / Information Architecture. Strengthen contextual hierarchy, current-journey continuity, responsive behavior, accessibility and low-cognitive-load navigation without turning the experience into a generic dashboard.

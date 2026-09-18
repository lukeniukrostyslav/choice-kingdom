# Choice Kingdom — Premium Design Master P1–P25

Status: ACTIVE — premium-design execution track

This document is the canonical working checklist for the 25-block premium visual design track. Percentages are engineering/design completion estimates, not claims of commercial quality or store readiness. A block reaches 100% only when its visual contract, representative implementation/proof, responsive behavior, accessibility requirements, and regression evidence are present.

## Premium Design P1–P25

| Block | Scope | Current | Exit gate |
|---|---|---:|---|
| P1 | Premium vision / art direction | 72% | Signed visual north star + representative screens |
| P2 | Core visual identity / design language | 74% | Tokenized identity applied across representative surfaces |
| P3 | Typography / type hierarchy | 66% | Complete type scale, wrapping, accessibility and locale rules |
| P4 | Color / materials / surfaces | 70% | Semantic color/material tokens + contrast proof |
| P5 | Layout / grid / spacing / responsive system | 78% | Responsive contracts across target window classes + safe-content bounds |
| P6 | Choice experience / choice cards / choice chamber | 75% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 70% | Full event surface and state variants |
| P8 | Character presentation | 57% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 59% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 56% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 72% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 60% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 100% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 100% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 100% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 100% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 100% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 100% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 78% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 74% | Purposeful semantic motion + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 84% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 53% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 30% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 38% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 58% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 72.96% (simple arithmetic mean of block estimates).**

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

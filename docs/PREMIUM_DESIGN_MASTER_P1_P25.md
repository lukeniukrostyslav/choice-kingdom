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
| P13 | Relationships / character state | 56% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 56% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 46% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 56% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 47% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 73% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 78% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 74% | Purposeful semantic motion + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 84% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 53% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 30% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 38% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 58% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 62.24% (simple arithmetic mean of block estimates).**

## Current evidence

- `androidApp/` is the first real Android Compose application module, with launcher Activity, adaptive Compact/Medium/Expanded presentation, safe-drawing insets and semantic interaction states.
- `.github/workflows/android-presentation.yml` adds an Android build gate using Java 17, Android SDK setup and Gradle 8.7.3.
- The Android layer is presentation-only; canonical gameplay remains owned by the existing runtime seam.
- `runtime/premium_screen_states.py`, `runtime/premium_surface_projection.py` and `runtime/premium_regression_matrix.py` remain the canonical platform-neutral presentation contracts.
- Existing rendered preview evidence covers responsive density, RTL, large text, reduced motion, safe area and focus-visible behavior.
- Physical Android/device proof is not claimed yet.

## Quality rules

- Do not copy competitor art, branding or proprietary UI.
- Use competitors and award-winning games for interaction principles, not imitation.
- Never mark a block 100% because a document exists.
- Every important state needs an explicit visual state where applicable.
- Reduced motion, large text, RTL and long-string behavior are part of the design.
- Android/device proof is required before claiming production UI completion.

## Next bottleneck

Make the Android surface consume the canonical runtime presentation projection through a narrow adapter, then add emulator/device interaction evidence and cross-screen visual regression. No physical Android proof is claimed until it exists.

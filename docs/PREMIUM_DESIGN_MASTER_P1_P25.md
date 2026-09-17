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

**Aggregate P1–P25 estimate: 62.12% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `androidApp/` is now a real Android application module using Jetpack Compose and Material 3, with a launcher Activity, adaptive Compact/Medium/Expanded presentation, safe-drawing insets and semantic state controls.
- The Android surface preserves the canonical premium state vocabulary across Event, Realm, History, People, Investigation, Ending and Settings; it is presentation-only and does not mutate gameplay.
- `.github/workflows/android-presentation.yml` adds an Android build gate using Java 17, Android SDK setup and Gradle 8.7.3.
- `runtime/premium_screen_states.py` remains the canonical cross-screen state vocabulary for the platform-neutral presentation contract.
- `runtime/premium_surface_projection.py` remains the canonical platform-neutral width/density projection; Android implementation mirrors its boundaries rather than replacing it.
- Existing rendered preview and cross-screen regression evidence remains required; Android source implementation does not by itself constitute physical device proof.
- `tests/test_design_preview_contract.py` validates the rendered preview contract for all seven screens, shared interaction states, safe-area handling, RTL, large-text and reduced-motion controls.
- `design-preview/premium-screen-state-matrix-v1.html` provides interactive rendered proof for seven key screens across Compact/Medium/Expanded density, RTL, large text, reduced motion, safe-area and focus-visible behavior.
- `design-preview/premium-consequence-lab-v1.html` provides dedicated rendered consequence proof for resolved/pending states with compact layout, RTL, large-text, focus-visible, safe-area and reduced-motion behavior.
- No physical Android/device screenshot or interaction session is claimed yet. P24 remains below completion until that evidence exists.

## Production-facing integration evidence

The runtime exposes a presentation-neutral `GameSession` snapshot and a `SessionPresenter` that owns transient interaction state while routing gameplay mutation back through `GameSession`. Visual adaptation, accessibility semantics, locale policy, premium feedback and screen-state vocabulary remain presentation-only and do not calculate gameplay outcomes.

## Execution order

1. P1–P5: visual foundation and adaptive layout/safe-area contract.
2. P6–P7: authored choice/event state language in production-facing surfaces.
3. P8–P20: Realm, History, People, Investigation, Ending, Replay, Main Menu and navigation.
4. P21–P24: accessibility, localization, Android adaptation, audio/haptics and device proof.
5. P25: final cross-screen polish and regression gate.

## Quality rules

- Do not copy competitor art, branding or proprietary UI.
- Use competitors and award-winning games for interaction principles, not imitation.
- Never mark a block 100% because a document exists.
- Never invent gameplay semantics to make a visual demo look complete.
- Every important state needs an explicit visual state: default, focus, pressed, disabled/blocked, selected, success, failure, pending and error where applicable.
- Mobile readability and touch ergonomics are first-class premium requirements.
- Reduced motion, large text, RTL and long-string behavior are part of the design, not post-release fixes.
- Generated machine data remains derived; authored gameplay remains the source of truth.
- Android/device proof is required before claiming production UI completion.

## Execution note

The current increment establishes the first real Android presentation module and a CI build gate while preserving the platform-neutral presentation/gameplay boundary. Percentages were raised only where the new Android implementation and its adaptive/accessibility structure provide additional evidence. P24 is still explicitly below completion because no physical Android/device proof exists. Next bottleneck: make the Android surface consume the canonical runtime presentation projection through a narrow adapter, then add device/emulator interaction evidence and cross-screen visual regression.

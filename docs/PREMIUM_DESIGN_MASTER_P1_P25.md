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
| P5 | Layout / grid / spacing / responsive system | 71% | Responsive contracts across target window classes + safe-content bounds |
| P6 | Choice experience / choice cards / choice chamber | 71% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 62% | Full event surface and state variants |
| P8 | Character presentation | 56% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 58% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 55% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 60% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 58% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 54% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 54% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 45% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 54% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 47% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 69% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 75% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 67% | Purposeful semantic motion + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 75% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 42% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 16% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 27% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 35% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 57.24% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `runtime/android_adaptive_contract.py` adds an Android-facing presentation contract: Compact → single pane/bottom navigation, Medium → supporting pane/navigation rail, Expanded → two-pane presentation.
- `runtime/adaptive_navigation.py` remains the single window-width policy source; device identity is not used for layout decisions.
- `runtime/safe_area.py` is consumed by the Android-facing contract so system bars/cutouts/gesture insets reduce usable content bounds rather than clipping interactive content.
- `runtime/accessibility_semantics.py` adds explicit action role, accessible label, hint, state, enabled state and 48dp minimum touch-target semantics.
- `tests/test_android_adaptive_contract.py` verifies compact/medium/expanded contracts, safe-content dimensions and invalid dimensions.
- `tests/test_accessibility_semantics.py` verifies button semantics, disabled-state behavior and non-empty accessible labels.
- `runtime/locale_layout.py` and `design-preview/premium-locale-lab-v1.html` continue to provide LTR/RTL, long-string and large-text evidence.
- Current Android guidance recommends window-size-class-driven adaptation, state continuity during resize/fold/unfold/multi-window, responsive layouts, and Material 3 Adaptive primitives. citeturn0search0turn0search2turn0search4turn0search9
- The current Material 3 Adaptive release line also supports adaptive pane/navigation primitives and state-preserving adaptive behavior. citeturn0search0turn0search11
- No CI-green claim is made for the newest test commits until GitHub Actions reports an actual run.

## Production-facing integration evidence

The runtime exposes a presentation-neutral `GameSession` snapshot and a `SessionPresenter` that owns transient interaction state while routing gameplay mutation back through `GameSession`. Visual adaptation, accessibility semantics and locale policy remain presentation-only and do not calculate gameplay outcomes.

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

The current increment advances Android-facing adaptive contracts and accessibility semantics without introducing a gameplay/UI ownership leak. Next: connect these contracts to the visual preview and production-facing screen hosts, then build audio/haptic semantic feedback and cross-screen regression evidence. Documentation alone will not close P21–P25.

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
| P6 | Choice experience / choice cards / choice chamber | 73% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 62% | Full event surface and state variants |
| P8 | Character presentation | 56% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 58% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 55% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 62% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 58% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 54% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 54% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 45% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 54% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 47% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 69% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 75% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 70% | Purposeful semantic motion + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 77% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 46% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 30% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 27% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 38% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 58.52% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `runtime/premium_feedback.py` composes semantic motion with audio/haptic feedback into one presentation-only projection without gameplay mutation.
- `tests/test_premium_feedback.py` verifies complete semantic coverage, reduced-motion behavior and independent audio/haptic settings.
- `docs/PREMIUM_FEEDBACK_INTEGRATION_V1.md` records the player-feedback state matrix and accessibility behavior.
- `design-preview/premium-locale-lab-v1.html` now provides representative consequence-state, semantic pressed-state, keyboard-focus, reduced-motion, long-string, RTL and large-text proof.
- `runtime/audio_haptics.py` provides the stable cross-platform sound/haptic vocabulary.
- `runtime/motion.py` provides semantic enter/focus/confirm/resolve/pending/error motion with reduced-motion support.
- `runtime/accessibility_semantics.py` provides explicit role/label/hint/state/enabled semantics and 48dp minimum touch-target semantics.
- `runtime/locale_layout.py` continues to provide presentation-only LTR/RTL direction, navigation mirroring, wrapping and large-text reflow policy.
- Android adaptive design remains window-size-class driven rather than device-specific; Android guidance recommends responsive/adaptive layouts, state continuity across resize/fold/unfold, and adaptive navigation/pane primitives. citeturn0search0turn0search1turn0search5turn0search7
- The current Material 3 Adaptive release line provides adaptive navigation/pane primitives and recent state-synchronization fixes. citeturn0search5
- No CI-green claim is made for the newest commits until GitHub Actions reports an actual run.

## Production-facing integration evidence

The runtime exposes a presentation-neutral `GameSession` snapshot and a `SessionPresenter` that owns transient interaction state while routing gameplay mutation back through `GameSession`. Visual adaptation, accessibility semantics, locale policy and premium feedback remain presentation-only and do not calculate gameplay outcomes.

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

The current increment closes the composition seam between semantic motion and audio/haptic feedback and expands representative visual proof for choice/consequence states, accessibility, RTL and reduced motion. Next: bind the same contracts across the remaining screen family and build cross-screen visual regression evidence. Documentation alone will not close P20–P25.

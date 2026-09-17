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
| P5 | Layout / grid / spacing / responsive system | 69% | Responsive contracts across target window classes + safe-content bounds |
| P6 | Choice experience / choice cards / choice chamber | 70% | All choice states + proof + accessibility + visual regression |
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
| P21 | Accessibility / touch / keyboard / focus | 72% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 42% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 16% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 23% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 35% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 56.92% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `runtime/premium_journey.py` composes Event/Choice, Consequence and the journey screen family behind one navigation-neutral premium journey host.
- `runtime/adaptive_navigation.py` adds a pure presentation contract based on available window width: Compact → bottom navigation, Medium → navigation rail, Expanded → two-pane presentation.
- `runtime/main_menu.py` adds the production-facing premium launcher contract: Continue, New Run, History and Settings.
- `runtime/launcher_journey.py` connects launcher destinations to the composed journey boundary without adding gameplay rules.
- `runtime/motion.py` adds semantic motion vocabulary for enter, focus, confirm, resolve, pending and error states; reduced-motion mode preserves semantic feedback while removing decorative motion.
- `runtime/safe_area.py` adds a platform-neutral safe-content bounds contract for system bars, cutouts and gesture zones.
- `runtime/locale_layout.py` adds a presentation-only locale policy for LTR/RTL direction, navigation mirroring, long-string wrapping and large-text reflow.
- `tests/test_locale_layout.py` verifies RTL mirroring policy and large-text expansion without disabling wrapping.
- `design-preview/premium-locale-lab-v1.html` provides representative visual proof for LTR, RTL, large text and long strings.
- `docs/LOCALE_LAYOUT_CONTRACT_V1.md` defines locale/RTL rules and explicitly keeps localization outside gameplay semantics.
- Current Android guidance confirms window-size-class-driven adaptation, state continuity across resize/fold/unfold/multi-window, and safe handling of system UI insets. citeturn0search0turn0search1turn0search2turn0search4
- Compose Material 3 Adaptive provides adaptive navigation/pane primitives; production Android binding remains open until the actual Android module and device proof exist. citeturn0search3turn0search8
- No CI-green claim is made for the newest test commits until GitHub Actions reports an actual run.

## Production-facing integration evidence

The runtime exposes a presentation-neutral `GameSession` snapshot and a `SessionPresenter` that owns transient interaction state while routing gameplay mutation back through `GameSession`. The design track treats that seam as the authoritative bridge: visual state may describe interaction, but it must not calculate gameplay outcomes or duplicate routing rules.

The production integration contract covers Event/Choice, Consequence, Realm, History, People/Factions, Investigation, Ending, Settings, navigation, Main Menu/launcher and the launcher-to-journey boundary. Motion and locale behavior are presentation policies and remain independent of gameplay mutation.

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

The current increment adds representative locale/RTL visual proof and a machine-readable locale presentation policy. The next implementation series moves into Android-facing adaptive binding, accessibility semantics, then audio/haptics and cross-screen visual regression. Documentation alone will not close P18–P25.

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
| P5 | Layout / grid / spacing / responsive system | 68% | Responsive contracts across target window classes |
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
| P18 | Main menu / launcher | 60% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 70% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 62% | Purposeful motion system + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 70% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 34% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 16% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 18% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 33% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 55.64% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `runtime/premium_journey.py` composes Event/Choice, Consequence and the journey screen family behind one navigation-neutral premium journey host.
- `runtime/adaptive_navigation.py` adds a pure presentation contract based on available window width: Compact → bottom navigation, Medium → navigation rail, Expanded → two-pane presentation.
- `tests/test_adaptive_navigation.py` verifies the width-class boundaries and presentation-only navigation behavior.
- Adaptive decisions use available app-window space rather than physical device identity. This matches current Android guidance for phones, foldables, tablets and resizable windows.
- Safe insets remain an explicit requirement; adaptive navigation must not place interactive controls under gesture/system-bar insets.
- The journey screen contracts deliberately do not calculate gameplay effects, route events, invent relationship values, fabricate evidence, or mutate `GameSession`.
- No new CI-green claim is made for the latest test commit until GitHub Actions reports an actual run.

## Production-facing integration evidence

The runtime exposes a presentation-neutral `GameSession` snapshot and a `SessionPresenter` that owns transient interaction state while routing gameplay mutation back through `GameSession`. The design track treats that seam as the authoritative bridge: visual state may describe interaction, but it must not calculate gameplay outcomes or duplicate routing rules.

The production integration contract covers Event/Choice, Consequence, Realm, History, People/Factions, Investigation, Ending, Settings and navigation. Crisis, Replay and Motion remain semantic presentation layers and must not duplicate gameplay semantics.

## Execution order

1. P1–P5: strengthen the visual foundation and adaptive layout contract.
2. P6–P7: integrate the authored choice/event state language into production-facing surfaces.
3. P8–P20: extend the same visual language through Realm, History, People, Investigation, Ending, Replay and Main Menu/navigation.
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

The current increment moves the project from composed journey navigation into an explicit adaptive-navigation contract. The next implementation work remains the actual platform UI host and representative visual proof; documentation alone will not close P18–P25.

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
| P5 | Layout / grid / spacing / responsive system | 76% | Responsive contracts across target window classes + safe-content bounds |
| P6 | Choice experience / choice cards / choice chamber | 75% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 67% | Full event surface and state variants |
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
| P18 | Main menu / launcher | 71% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 77% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 74% | Purposeful semantic motion + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 82% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 53% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 30% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 31% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 56% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate: 61.48% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `runtime/premium_screen_states.py` defines the canonical cross-screen state vocabulary for Event, Realm, History, People, Investigation, Ending and Settings.
- `runtime/premium_surface_projection.py` maps actual available app-window width to compact/comfortable/expanded premium surface density without changing gameplay semantics.
- `runtime/premium_regression_matrix.py` generates a machine-readable cross-screen regression matrix spanning all seven premium screens, required states and Compact/Medium/Expanded/RTL/large-text/reduced-motion dimensions.
- `runtime/premium_surface_host.py` binds the adaptive presentation projection to Event/Choice plus Realm/History/People/Investigation/Ending/Settings screen hosts without changing gameplay semantics.
- `runtime/premium_consequence_surface.py` binds the transient consequence/result surface to the same adaptive presentation contract while delegating consequence mutation to the canonical `ConsequenceHost`.
- `tests/test_premium_screen_states.py`, `tests/test_premium_surface_projection.py`, `tests/test_premium_regression_matrix.py`, `tests/test_premium_surface_host.py`, `tests/test_premium_consequence_surface.py` and `tests/test_premium_consequence_accessibility.py` cover shared interaction states, adaptive projection, cross-screen invariants and a real authored consequence flow across required widths.
- `tests/test_design_preview_contract.py` validates the rendered preview contract for all seven screens, shared interaction states, safe-area handling, RTL, large-text and reduced-motion controls.
- `tests/test_consequence_screen_runtime.py` remains the canonical runtime-level evidence that E01-A resolves to E02 and that dismissing the consequence is presentation-only.
- `docs/PREMIUM_SCREEN_STATE_CONTRACT_V1.md`, `docs/PREMIUM_ADAPTIVE_SURFACE_CONTRACT_V1.md` and `docs/PREMIUM_CROSS_SCREEN_REGRESSION_V1.md` define the cross-screen rendering, accessibility, RTL, reduced-motion, responsive and regression rules.
- `design-preview/premium-screen-state-matrix-v1.html` now provides interactive rendered proof for seven key screens across Compact/Medium/Expanded density, RTL, large text, reduced motion, safe-area and focus-visible behavior. It remains explicit that this is not physical Android/device proof.
- `design-preview/premium-consequence-lab-v1.html` provides dedicated rendered consequence proof for resolved/pending states with compact layout, RTL, large-text, focus-visible, safe-area and reduced-motion behavior. It explicitly remains visual evidence rather than physical Android/device proof.
- `runtime/premium_feedback.py` continues to compose semantic motion with audio/haptic feedback into one presentation-only projection.
- `design-preview/premium-locale-lab-v1.html` continues to provide choice/consequence, long-string, RTL, large-text, focus and reduced-motion proof.
- Android adaptive design remains window-size-class driven rather than device-specific. Current Android guidance recommends responsive/adaptive layouts, continuity across resize/fold/unfold, adaptive navigation and pane primitives, and testing across device types.
- The authored-choice workflow for commit `8e099d2` completed successfully. The latest rendered-evidence changes have also passed the latest canonical graph workflow; the complete preview-specific regression run must still finish before claiming the full suite green.

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

The current increment expands the rendered cross-screen evidence from simple RTL/large-text toggles into explicit Compact/Medium/Expanded density controls plus reduced-motion and safe-area behavior, and adds a contract test for the preview evidence. P5/P20/P21/P22/P25 estimates were adjusted only for this newly evidenced presentation behavior. P24 remains unchanged because there is still no physical Android/device proof. Next bottleneck: complete the preview-specific regression run, then establish the first real Android presentation layer and device-proof path.

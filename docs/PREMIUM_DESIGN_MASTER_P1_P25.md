# Choice Kingdom — Premium Design Master P1–P25

Status: ACTIVE — premium-design execution track

This document is the canonical working checklist for the 25-block premium visual design track. Percentages are engineering/design completion estimates, not claims of commercial quality or store readiness. A block reaches 100% only when its visual contract, representative implementation/proof, responsive behavior, accessibility requirements, and regression evidence are present.

## Benchmark principles

The premium bar is informed by current high-quality mobile game design references and award-recognized interaction patterns. The target is not to copy another game: Choice Kingdom must have its own Avelune identity.

Current platform guidance reinforces cohesive visual language, clear hierarchy, narrative embedded into interaction, responsive/touch-first presentation, accessible controls and physical-device validation. Android guidance specifically reinforces adaptive layouts, safe insets, state preservation across configuration changes, readable line lengths, 48dp touch targets and contrast verification. These references are used as principles only; no competitor art, branding, characters, layouts or proprietary assets are copied.

## Premium Design P1–P25

| Block | Scope | Current | Exit gate |
|---|---|---:|---|
| P1 | Premium vision / art direction | 72% | Signed visual north star + representative screens |
| P2 | Core visual identity / design language | 74% | Tokenized identity applied across representative surfaces |
| P3 | Typography / type hierarchy | 66% | Complete type scale, wrapping, accessibility and locale rules |
| P4 | Color / materials / surfaces | 70% | Semantic color/material tokens + contrast proof |
| P5 | Layout / grid / spacing / responsive system | 67% | Responsive contracts across target phone widths |
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
| P19 | Navigation / information architecture | 68% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 62% | Purposeful motion system + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 70% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 34% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 16% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 16% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 33% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate after this increment: 55.24% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `web-preview/premium-game-slice-v1.html` is a committed five-stage playable premium design slice: Event → Choice → Consequence → Realm → History.
- `runtime/journey_screens.py` provides production-facing, presentation-only screen contracts for Realm, History, People/Factions, Investigation, Ending and Settings, all derived from the same canonical `SessionPresenter` snapshot.
- `runtime/premium_journey.py` now composes Event/Choice, Consequence and the journey screen family behind one navigation-neutral premium journey host. Navigation changes only the visible projection; gameplay mutation remains behind `SessionPresenter`.
- `tests/test_journey_screens.py` locks the screen-family projections to canonical session data and verifies Settings flags remain presentation-only.
- `tests/test_premium_journey.py` verifies navigation projection, surface switching and presentation-only Settings behavior without inventing gameplay state.
- The journey screen contracts deliberately do not calculate gameplay effects, route events, invent relationship values, fabricate evidence, or mutate `GameSession`.
- The slice and runtime contracts use responsive phone-first composition, safe-area padding, 48dp-class primary controls, keyboard focus visibility, semantic choice selection, reduced-motion behavior and RTL-safe directional styling.
- The slice demonstrates the intended premium hierarchy: focal art zone → authored situation → resource snapshot → opposing choices → immediate consequence → delayed consequence → realm pulse → decision memory.
- Android guidance is treated as a design constraint: adaptive layouts, safe insets, state preservation across resizing/configuration changes, readable line lengths, accessible touch targets and contrast remain required before P24/P25 closure.

## Production-facing integration evidence

The runtime exposes a presentation-neutral `GameSession` snapshot and a `SessionPresenter` that owns transient interaction state while routing gameplay mutation back through `GameSession`. The design track treats that seam as the authoritative bridge: visual state may describe interaction, but it must not calculate gameplay outcomes or duplicate routing rules.

The production integration contract covers:

- Event/Choice: idle, focused, selected, pressed, resolving, resolved, disabled, blocked and error states.
- Realm: resource presentation and pressure indicators derived from the session snapshot.
- History: canonical decision-memory identifiers projected from runtime history.
- People/Factions: relationship values projected from canonical runtime relationships.
- Investigation: canonical thread identifiers and ending-evidence families projected without inventing gameplay facts.
- Consequences: pending delayed-consequence identity, target, status, schedule and source event are projected from runtime delay records.
- Ending: terminal/ending identity and source-closed evidence presentation derived from the session boundary.
- Settings: large text, reduced motion and RTL presentation modes.
- Crisis: urgency, escalation and consequence-preview states are presentation-only and remain separate from gameplay mutation.
- Replay: prior-run memory and new-run presentation are explicitly separated so replay cannot silently reuse gameplay state.
- Motion: enter, confirm and pending feedback are semantic states; reduced-motion mode removes decoration without removing information.
- Navigation: `PremiumJourneyHost` provides a single surface-selection boundary while preserving the canonical session snapshot across surface changes.

The verifier is intentionally static and deterministic. It is a regression guard, not a substitute for real-device visual QA. No GitHub Actions run was reported for the latest test commit yet, so the new tests are committed evidence but are not claimed as CI-green.

## Execution order

1. P1–P5: strengthen the visual foundation before adding more screens.
2. P6–P7: integrate the authored choice/event state language into production-facing surfaces.
3. P8–P20: extend the same visual language through Realm, History, People, Investigation, Ending, Replay and Main Menu, with production-facing integration rather than preview-only duplication.
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

The first premium vertical slice is intentionally being built before mechanically pushing every block toward 100%. The latest increment crosses from separate production-facing screen contracts into a composed journey/navigation boundary. The same visual contracts will continue into the actual platform UI host, followed by localization, Android/device proof, authored audio/haptics and final cross-screen QA.

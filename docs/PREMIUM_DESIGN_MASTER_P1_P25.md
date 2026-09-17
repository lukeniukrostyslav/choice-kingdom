# Choice Kingdom — Premium Design Master P1–P25

Status: ACTIVE — premium-design execution track

This document is the canonical working checklist for the 25-block premium visual design track. Percentages are engineering/design completion estimates, not claims of commercial quality or store readiness. A block reaches 100% only when its visual contract, representative implementation/proof, responsive behavior, accessibility requirements, and regression evidence are present.

## Benchmark principles

The premium bar is informed by current high-quality mobile game design references and award-recognized interaction patterns. The target is not to copy another game: Choice Kingdom must have its own Avelune identity.

Current platform guidance reinforces cohesive visual language, clear hierarchy, narrative embedded into interaction, responsive/touch-first presentation, accessible controls and physical-device validation. Apple guidance emphasizes legibility across screen sizes, adaptable layouts, appropriately sized controls, multiple interaction methods, accessibility support and testing on supported devices. Android guidance similarly recommends window-size-class-based adaptive layouts, reflow/reveal/presentation changes, safe-area-aware interfaces and testing across device types. These references are used as principles only; no competitor art, branding, characters, layouts or proprietary assets are copied.

## Premium Design P1–P25

| Block | Scope | Current | Exit gate |
|---|---|---:|---|
| P1 | Premium vision / art direction | 70% | Signed visual north star + representative screens |
| P2 | Core visual identity / design language | 72% | Tokenized identity applied across representative surfaces |
| P3 | Typography / type hierarchy | 66% | Complete type scale, wrapping, accessibility and locale rules |
| P4 | Color / materials / surfaces | 70% | Semantic color/material tokens + contrast proof |
| P5 | Layout / grid / spacing / responsive system | 64% | Responsive contracts across target phone widths |
| P6 | Choice experience / choice cards / choice chamber | 68% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 55% | Full event surface and state variants |
| P8 | Character presentation | 49% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 51% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 49% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 54% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 50% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 46% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 45% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 28% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 46% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 28% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 48% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 51% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 36% | Purposeful motion system + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 64% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 22% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 16% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 16% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 27% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate after this increment: 47.64% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `runtime/session.py` now exposes canonical presentation-neutral projections for history, investigation threads, pending delayed consequences and ending evidence families directly from `GameState`.
- `runtime/presentation.py` now converts those canonical fields into typed UI-facing `SessionPresentation` models without duplicating gameplay rules.
- `tools/verify_premium_production_integration.py` now gates the four narrative projections in addition to the nine interaction states, seven representative screens, adaptive/accessibility modes and `GameSession` mutation boundary.
- `tests/test_premium_presentation_projection.py` adds regression coverage for the new narrative projections and confirms transient choice states do not mutate gameplay turn state.
- `design-preview/premium-design-system-v2.html` continues to unify the reusable visual system across Event, Realm, History, People/Factions, Investigation, Ending, Settings and the full decision-state matrix.
- `docs/DESIGN_TOKENS_V2.json` freezes semantic colors, typography, spacing, touch targets, safe-area rules, adaptive window classes and state vocabulary in a machine-readable design contract.
- `.github/workflows/premium-design-system-gate.yml` provides a Playwright matrix for compact/medium/expanded widths plus RTL, large-text, reduced-motion and light-theme execution.
- The new evidence raises P10–P14 and P16 conservatively because those runtime narrative domains now have an explicit typed presentation bridge; this does not close Android runtime, final-art provenance or physical-device gates.

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

The verifier is intentionally static and deterministic. It is a regression guard, not a substitute for real-device visual QA.

## Execution order

1. P1–P5: strengthen the visual foundation before adding more screens.
2. P6: integrate the authored choice state language into production-facing choice surfaces.
3. P7–P20: extend the same visual language through the full player journey, with production-facing integration rather than preview-only duplication.
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

## Immediate next execution target

Continue production-facing integration from the new narrative projection bridge into actual Event, Realm, History, People, Investigation and Ending surfaces; then harden P20–P25 with motion semantics, localization/RTL stress, Android adaptation and cross-screen regression. Use fresh internet research only when a concrete design decision needs a new benchmark; do not add repetitive benchmark documents when existing evidence is sufficient.

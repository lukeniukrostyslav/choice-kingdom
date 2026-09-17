# Choice Kingdom — Premium Design Master P1–P25

Status: ACTIVE — premium-design execution track

This document is the canonical working checklist for the 25-block premium visual design track. Percentages are engineering/design completion estimates, not claims of commercial quality or store readiness. A block reaches 100% only when its visual contract, representative implementation/proof, responsive behavior, accessibility requirements, and regression evidence are present.

## Benchmark principles

The premium bar is informed by current high-quality mobile game design references and award-recognized interaction patterns. The target is not to copy another game: Choice Kingdom must have its own Avelune identity.

Recent 2026 guidance reinforces durable requirements: cohesive visual language, clear hierarchy, narrative embedded into interaction, responsive/touch-first presentation, accessible controls and physical-device validation. Apple’s current game-interface guidance emphasizes legibility across screen sizes, adaptable layouts, appropriately sized controls, multiple interaction methods, accessibility support and testing on supported devices. These references are used as principles only; no competitor art, branding, characters, layouts or proprietary assets are copied.

## Premium Design P1–P25

| Block | Scope | Current | Exit gate |
|---|---|---:|---|
| P1 | Premium vision / art direction | 70% | Signed visual north star + representative screens |
| P2 | Core visual identity / design language | 72% | Tokenized identity applied across representative surfaces |
| P3 | Typography / type hierarchy | 66% | Complete type scale, wrapping, accessibility and locale rules |
| P4 | Color / materials / surfaces | 70% | Semantic color/material tokens + contrast proof |
| P5 | Layout / grid / spacing / responsive system | 64% | Responsive contracts across target phone widths |
| P6 | Choice experience / choice cards / choice chamber | 65% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 52% | Full event surface and state variants |
| P8 | Character presentation | 46% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 48% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 43% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 48% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 43% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 40% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 38% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 28% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 40% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 28% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 48% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 48% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 36% | Purposeful motion system + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 62% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 22% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 16% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 16% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 25% | Full visual regression and no unresolved P1–P24 blockers |

**Aggregate P1–P25 estimate after this increment: 45.4% (simple arithmetic mean of block estimates).** This is an engineering/design evidence estimate, not a commercial-readiness score.

## Evidence added in the current design increment

- `design-preview/premium-design-system-v2.html` unifies the reusable visual system across Event, Realm, History, People/Factions, Investigation, Ending, Settings and the full decision-state matrix.
- `docs/DESIGN_TOKENS_V2.json` freezes semantic colors, typography, spacing, touch targets, safe-area rules, adaptive window classes and state vocabulary in a machine-readable design contract.
- `.github/workflows/premium-design-system-gate.yml` adds a Playwright matrix for compact/medium/expanded widths plus RTL, large-text, reduced-motion and light-theme execution.
- `tools/verify_premium_design_system.py` provides a local static contract check for the same design-system invariants.
- The new evidence increases the P1–P25 estimates conservatively, but does not close Android runtime, final-art provenance or physical-device gates.

- `design-preview/premium-choice-lab.html` provides a dedicated authored choice-state gallery covering default, focus, selected, blocked, pending, resolved and high-risk states.
- `design-preview/premium-foundation-lab.html` turns the Avelune direction into reusable P1–P5 visual primitives: semantic surfaces, restrained accent usage, editorial type hierarchy, spacing tokens, touch-safe controls, and explicit decision-state language.
- `design-preview/premium-journey-lab.html` now integrates that state vocabulary across Event, Realm, History, People/Factions, Investigation and Ending in one responsive journey proof. It deliberately keeps gameplay authority outside the presentation layer.
- The journey lab adds representative selected/blocked/pending/risk/resolved states, causal history, resource pressure, relationship/faction presentation, evidence progression and an ending landing surface.
- The choice percentage is raised only for the new cross-screen evidence; production gameplay integration and Android/device regression are still open gates.
- P1–P5 remain deliberately unchanged: the new lab strengthens evidence but does not by itself prove production implementation or device regression.

## Execution order

1. P1–P5: strengthen the visual foundation before adding more screens.
2. P6: continue the active choice-experience track; integrate the authored state language into production-facing choice surfaces.
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

Move from journey proof into production-facing integration: first unify the Event/Choice surface with the reusable foundation, then apply the same contracts to Realm, History, People, Investigation and Ending. Use fresh internet research only when a concrete design decision needs a new benchmark; do not add repetitive benchmark documents when existing evidence is sufficient.

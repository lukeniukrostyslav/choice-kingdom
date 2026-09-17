# Choice Kingdom — Premium Design Master P1–P25

Status: ACTIVE — premium-design execution track

This document is the canonical working checklist for the 25-block premium visual design track. Percentages are engineering/design completion estimates, not claims of commercial quality or store readiness. A block reaches 100% only when its visual contract, representative implementation/proof, responsive behavior, accessibility requirements, and regression evidence are present.

## Benchmark principles

The premium bar is informed by current high-quality mobile game design references and award-recognized interaction patterns. The target is not to copy another game: Choice Kingdom must have its own Avelune identity.

Recent 2026 design references reinforce durable requirements: distinctive cohesive visual language, platform-native interaction, narrative embedded into interaction, authored environmental detail, clearly exposed accessibility controls, and responsive/touch-first presentation. Apple’s 2026 design coverage highlights games such as Is This Seat Taken? and Pine Hearts for distinctive presentation, interaction, surrounding detail, and accessibility options. Apple’s current game-interface guidance also emphasizes legibility on smaller screens, appropriately sized controls, multiple interaction methods, accessibility support, and physical-device testing. These references are used as principles only; no competitor art, branding, characters, layouts, or proprietary assets are copied.

## Premium Design P1–P25

| Block | Scope | Current | Exit gate |
|---|---|---:|---|
| P1 | Premium vision / art direction | 65% | Signed visual north star + representative screens |
| P2 | Core visual identity / design language | 65% | Tokenized identity applied across representative surfaces |
| P3 | Typography / type hierarchy | 58% | Complete type scale, wrapping, accessibility and locale rules |
| P4 | Color / materials / surfaces | 62% | Semantic color/material tokens + contrast proof |
| P5 | Layout / grid / spacing / responsive system | 56% | Responsive contracts across target phone widths |
| P6 | Choice experience / choice cards / choice chamber | 50% | All choice states + proof + accessibility + visual regression |
| P7 | Event / situation presentation | 35% | Full event surface and state variants |
| P8 | Character presentation | 30% | Character identity, state, relationship and fallback visuals |
| P9 | Kingdom / world presentation | 30% | Avelune world surfaces and visual continuity |
| P10 | Resources / stats / pressure visualization | 28% | Scannable resource language and state transitions |
| P11 | Consequences / delayed consequences | 32% | Immediate, pending, triggered and cancelled visual states |
| P12 | History / decision memory | 25% | Timeline/history hierarchy and causal readability |
| P13 | Relationships / character state | 25% | Relationship states and progression presentation |
| P14 | Investigation / threads / evidence | 20% | Evidence hierarchy, discovery and unresolved states |
| P15 | Crisis / high-stakes presentation | 20% | Escalation, urgency and consequence preview without clutter |
| P16 | Endings / resolution experience | 25% | Ending identity, summary and emotional landing |
| P17 | Replay / new-run experience | 20% | Replay motivation, continuity and clean reset semantics |
| P18 | Main menu / launcher | 40% | Premium first impression + navigation + responsive proof |
| P19 | Navigation / information architecture | 35% | Consistent hierarchy and low-cognitive-load navigation |
| P20 | Motion / micro-interactions / feedback | 20% | Purposeful motion system + reduced-motion behavior |
| P21 | Accessibility / touch / keyboard / focus | 46% | Semantic, focus, contrast, touch-target and reduced-motion proof |
| P22 | Localization / long strings / RTL | 5% | Locale-safe layout and RTL proof across key screens |
| P23 | Audio / haptics / premium feedback | 10% | Audio/haptic vocabulary mapped to meaningful player actions |
| P24 | Android devices / safe areas / resolution adaptation | 10% | Real Android presentation proof on target device classes |
| P25 | Final premium polish / cross-screen QA | 15% | Full visual regression and no unresolved P1–P24 blockers |

## Evidence added in the current design increment

- `design-preview/premium-choice-lab.html` provides a dedicated authored choice-state gallery covering default, focus, selected, blocked, pending, resolved and high-risk states.
- `design-preview/premium-foundation-lab.html` now turns the Avelune direction into reusable P1–P5 visual primitives: semantic surfaces, restrained accent usage, editorial type hierarchy, spacing tokens, touch-safe controls, and explicit default/selected/blocked/pending/resolved/risk state language.
- The choice lab preserves touch-sized controls, keyboard focus, explicit disabled semantics, responsive mobile geometry and reduced-motion behavior.
- The P6 percentage remains deliberately conservative at 50% because these labs are representative design proof, not yet full cross-screen gameplay integration or Android/device regression evidence.
- P2/P3/P4/P5 remain at their current levels until the same foundation is applied to representative production-facing surfaces; the lab alone does not justify another percentage increase.

## Execution order

1. P1–P5: strengthen the visual foundation before adding more screens.
2. P6: continue the active choice-experience track; do not declare completion from documentation alone.
3. P7–P20: extend the same visual language through the full player journey.
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

Continue P6 with cross-screen integration of the authored choice language, while applying the P1–P5 foundation to representative event, realm, history, people, investigation and ending surfaces. Fresh internet research should be used selectively when a concrete design decision needs a new benchmark; the repository should not accumulate repetitive benchmark documents when existing evidence is sufficient.

# Choice Kingdom — Premium Design System v2 Closure

Status: **ACTIVE / implementation-ready design system**

Date: 2026-09-17

## Purpose

This artifact closes the reusable visual-system work needed to carry the Premium Design P1–P25 track consistently across the player journey. It does **not** claim that Android runtime, final artwork licensing, or physical-device QA has happened.

The companion implementation proof is:

- `design-preview/premium-design-system-v2.html`
- `docs/DESIGN_TOKENS_V2.json`
- `.github/workflows/premium-design-system-gate.yml`

## Current design contract

### Adaptive composition

The design is based on available window width rather than device model:

- **Compact `<600dp`** — one primary pane; secondary information stacks below or opens as a focused destination.
- **Medium `600–839dp`** — primary content remains dominant; supporting context may become a second pane when it improves comprehension.
- **Expanded `>=840dp`** — two-pane composition is allowed; the decision/event surface remains visually dominant.

This follows current Android adaptive guidance to make layout decisions from window size classes and to use reflow, reveal and presentation changes instead of device-specific layouts.

### Core visual language

- Avelune uses a restrained chronicle/editorial identity rather than F2P-like dashboard styling.
- Gold is reserved for authored emphasis and important chronology.
- Authority, warning, stability and negative states use semantic roles.
- State meaning never depends on color alone.
- Narrative containers are intrinsically sized and may reflow under large text or localization expansion.
- The decision surface remains the visual center of gravity.

### Interaction state vocabulary

Every applicable interactive surface has explicit:

`default → focus → pressed → selected → blocked → pending → resolved → error/high-risk`

The UI never fabricates gameplay consequences. It presents canonical state supplied by the game/session layer.

### Accessibility

The v2 contract requires:

- 48dp minimum interactive targets.
- 56dp preferred choice target.
- visible keyboard/focus treatment.
- screen-reader names/roles for interactive controls.
- large-text reflow rather than clipping.
- RTL mirroring.
- long-string and CJK expansion tolerance.
- reduced-motion behavior that removes non-essential animation while preserving state feedback.
- state communication through text/icons/borders in addition to color.

### Screen-family coverage

The v2 lab provides a common composition vocabulary for:

1. Event
2. Realm
3. History
4. People / factions
5. Investigation
6. Ending
7. Settings
8. Choice-state matrix

## P1–P25 evidence impact

| Block | Design-system contribution | Remaining production gate |
|---|---|---|
| P1 | Avelune north-star language is encoded in shared tokens and representative surfaces | Final authored art direction sign-off |
| P2 | Shared semantic identity and reusable states | Full production integration |
| P3 | Complete scalable type roles and reflow rules | Runtime font/locale/device verification |
| P4 | Semantic light/dark materials and state roles | Contrast verification on final Android theme |
| P5 | Compact/medium/expanded layout contract | Android runtime adaptation proof |
| P6 | Choice state vocabulary and 56dp target | Canonical runtime event integration |
| P7 | Event composition uses same art/narrative/decision hierarchy | Full authored-event runtime coverage |
| P8 | People/faction card language and portrait-safe zones | Complete canonical character asset coverage |
| P9 | Realm resource/context composition | Runtime integration |
| P10 | Resource strip and pressure meter language | Runtime state verification |
| P11 | Pending/resolved/blocked state vocabulary | Real delayed-consequence runtime proof |
| P12 | Chronological causal history presentation | Runtime history binding |
| P13 | Relationship presentation language | Full relationship-state binding |
| P14 | Evidence chain hierarchy | Investigation runtime binding |
| P15 | High-risk/warning state language | Crisis runtime coverage |
| P16 | Ending landing composition | Ending runtime + final artwork |
| P17 | Replay entry language | Replay runtime integration |
| P18 | Launcher/navigation visual grammar | Final launcher runtime |
| P19 | Adaptive navigation contract | Runtime navigation across window classes |
| P20 | Reduced-motion and state-feedback vocabulary | Runtime animation/haptic implementation |
| P21 | Accessibility contract encoded in components | Android accessibility/device verification |
| P22 | RTL/large-text/long-string behavior is represented | Full locale matrix in runtime |
| P23 | Semantic state hooks are ready for audio/haptic mapping | Actual audio/haptic assets and device proof |
| P24 | Window-class and safe-area contract | Physical Android devices |
| P25 | Shared system reduces cross-screen visual drift | Full production visual regression + device gate |

## Verification standard

The companion CI gate must verify:

- HTTP success and non-empty document.
- No horizontal overflow at registered widths.
- No uncaught page errors.
- No console errors.
- No failed requests.
- No broken images.
- Interactive controls meet the 48dp minimum.
- Choice controls meet the 56dp minimum.
- All eight screen/state views can be activated.
- RTL, large-text and reduced-motion modes are executable.
- Compact, medium and expanded modes are executable.

## Explicit non-claims

This document does not turn a browser preview into Android runtime evidence. Current Android guidance recommends testing across device types and adapting to actual window configuration; physical-device validation remains a separate gate.

Final production artwork also remains subject to the project's asset provenance/licensing rules.

## Benchmark basis

The system was checked against current platform guidance and the 2026 Apple Design Award ecosystem as inspiration for clarity, craft, accessibility and responsive presentation. Competitor art, branding, characters and proprietary layouts are not copied.

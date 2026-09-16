# Choice Kingdom — UI Design System v1

## Purpose

Define the visual and interaction language for the production Android presentation layer before UI implementation begins. This document is a design contract, not a mock implementation and does not change runtime gameplay semantics.

## Product feeling

Choice Kingdom should feel like a premium illustrated political chronicle rather than a generic mobile game UI.

The visual hierarchy is:

1. **The situation** — what is happening now.
2. **The human stakes** — who is involved and why it matters.
3. **The decision** — two or three clearly opposed actions.
4. **The consequences** — immediate state feedback without exposing hidden future outcomes.
5. **The realm** — a compact persistent view of the kingdom's condition.

The interface must support tension, reading, and deliberate choices. It must never feel like a spreadsheet, social feed, or ad-driven F2P interface.

## Visual direction

### Palette roles

Use warm parchment neutrals as the primary surface family, near-black ink for body text, restrained muted burgundy for danger/authority, deep forest for stability/positive civic outcomes, and antique brass for selected/high-importance accents.

These are semantic roles, not hard-coded colors. Theme tokens must permit future accessibility and dark-mode adjustments without changing content data.

Suggested token families:

- `surface.canvas`
- `surface.card`
- `surface.elevated`
- `ink.primary`
- `ink.secondary`
- `accent.authority`
- `accent.warning`
- `accent.stability`
- `accent.gold`
- `state.positive`
- `state.negative`
- `state.neutral`
- `focus.visible`

### Typography

Use a readable display face for titles/headings and a highly legible sans/serif-compatible text face for body copy. Font selection must be license-safe for commercial Android distribution and support all release locales through explicit fallback chains.

Hierarchy:

- Display title: event/ending title, high contrast.
- Section title: location, character, chapter.
- Body: narrative text.
- Choice label: short, decisive, visually dominant.
- State label: compact and scannable.
- Supporting metadata: smallest text, never required to understand a choice.

Never communicate meaning through font weight alone.

## Core screen: Event

Portrait-first layout, optimized for one-handed use.

```text
┌──────────────────────────────┐
│  AVELUNE          TURN 014   │
│  ──────────────────────────  │
│  GOLD  ●●●   TRUST ●●○       │
│  SECURITY ●○○  POWER ●●●     │
│                              │
│       [ EVENT ART ]          │
│                              │
│  THE WINTER LEDGER           │
│  --------------------------  │
│  Narrative text in short      │
│  readable paragraphs.        │
│                              │
│  Mara waits for your answer. │
│                              │
│  ┌────────────────────────┐  │
│  │ OPEN THE LEDGER        │  │
│  │ Trust the evidence.    │  │
│  └────────────────────────┘  │
│                              │
│  ┌────────────────────────┐  │
│  │ BURN THE LEDGER        │  │
│  │ Protect the Crown.     │  │
│  └────────────────────────┘  │
│                              │
│       History   Realm   ☰   │
└──────────────────────────────┘
```

### Event screen rules

- Artwork supports the scene but never hides the decision.
- Narrative width should remain narrow enough for comfortable mobile reading.
- Choices are large touch targets with a clear primary label and optional one-line consequence framing that describes intent, not hidden results.
- Do not show raw stat deltas before selection unless the authored event explicitly calls for transparent accounting.
- Disable double-submission while a choice resolves.
- After resolution, animate only the changed state indicators; do not use excessive motion.

## Realm/status panel

The player needs a fast answer to: “How is my kingdom doing?”

Primary state indicators:

- Gold
- Trust
- Security
- Power
- Reputation

Secondary layer:

- character relationships
- active delayed consequences
- major factions
- investigation knowledge

The five primary resources must not dominate the screen. The game is about decisions and consequences, not resource optimization alone.

## Choice interaction

Every choice should communicate an intentional tradeoff.

States:

- idle
- focused
- pressed
- resolving
- disabled
- resolved

Requirements:

- minimum touch target suitable for Android accessibility guidelines;
- visible keyboard/focus equivalent where applicable;
- no color-only distinction;
- deterministic transition into the runtime `GameSession` boundary;
- accessible content descriptions generated from localized content;
- haptic/audio feedback optional and presentation-only.

## Consequence feedback

Immediately after a choice, show a restrained “consequence pulse”:

- changed resource indicator;
- relationship movement when authored;
- new history marker when relevant;
- delayed consequence notification only when it becomes active/visible by authored rules.

Never reveal future consequences merely because the UI knows them internally.

## Character presentation

Characters should feel like people, not menu icons.

Each character surface can contain:

- portrait/art;
- name and role;
- relationship direction and intensity;
- one short contextual line;
- relevant history entries;
- current availability.

The UI must avoid reducing relationships to a single heart meter. Numeric/internal values can exist in runtime, but the presentation should emphasize narrative meaning.

## Faction presentation

Crown, Commons, Houses, Guilds, Border/security and civic/medical voices should be represented as distinct political constituencies without visually declaring any faction inherently good or evil.

Faction cards should show:

- current stance/context;
- recent relevant decision;
- pressure on the Crown;
- unresolved issue.

## History

The history screen is a first-class feature, not an afterthought.

Show:

- decision/event title;
- turn/date;
- people/factions involved;
- short authored summary;
- important state markers only when useful.

Avoid exposing implementation IDs such as `E199` to players.

## Investigation UI

Investigation routes should present evidence as a connected chain rather than a checklist.

Evidence nodes can originate from Mara, Toma, Seris, direct decree/account comparison, or expansion evidence. The UI must preserve uncertainty when the authored narrative preserves uncertainty.

Do not visually imply a single mastermind when the canonical narrative intentionally supports a systemic explanation.

## Ending presentation

An ending should feel like the final page of a political chronicle.

Sequence:

1. decisive final event;
2. short pause/transition;
3. ending title;
4. authored ending narrative;
5. key causes remembered from the run;
6. optional “what changed” replay information;
7. continue/replay action.

Do not display a gamified score as the primary ending verdict.

## Navigation

Primary navigation should remain shallow:

- Current event
- Realm
- History
- Characters / factions where context requires it
- Settings / accessibility

Avoid persistent bottom navigation if it competes with the decision surface. A compact secondary navigation treatment is preferred during event play.

## Accessibility

Required from first implementation pass:

- scalable text;
- screen-reader labels;
- sufficient contrast;
- non-color state communication;
- large touch targets;
- reduced-motion support;
- RTL layout mirroring;
- long-string resilience;
- locale-aware number/date formatting;
- safe font fallback.

## Responsive rules

Android portrait is the reference composition. Landscape is not a launch requirement unless later device testing demonstrates a strong need.

The design must survive:

- small Android phones;
- modern tall phones;
- large-font accessibility settings;
- translated strings substantially longer than English;
- RTL scripts;
- safe areas and gesture navigation.

## Implementation boundary

The UI layer must consume the existing presentation-neutral `GameSession` seam. It must not duplicate decision rules, trigger predicates, ending qualification, delayed scheduling, or persistence logic.

The presentation layer may:

- render a session snapshot;
- dispatch an authored choice;
- render state/history/relationship information;
- request save/load through the application boundary;
- provide presentation feedback.

The presentation layer must not invent gameplay semantics.

## First implementation slice

Implement in this order:

1. design tokens/theme;
2. event screen;
3. choice interaction states;
4. realm/status panel;
5. history screen;
6. character/faction surfaces;
7. consequence feedback;
8. ending presentation;
9. accessibility and RTL pass;
10. physical Android QA and visual regression checks.

The first vertical UI slice should render a real authored event through `GameSession`, not a fake/demo event.

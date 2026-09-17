# Choice Kingdom — UI Visual Specification V3

## Status

Implementation-oriented visual contract for the premium illustrated political chronicle presentation layer. This document is presentation-only: gameplay truth remains in `GameSession` and authored content.

## Visual identity

- Premium illustrated political chronicle; never generic F2P dashboard styling.
- Warm parchment surfaces, near-black ink, restrained burgundy authority/warning, deep forest stability, antique brass emphasis.
- Editorial composition: generous margins, short reading measure, quiet dividers, restrained depth, tactile but calm controls.
- Avoid gradients that look glossy, excessive shadows, neon colors, gamified badges, progress bars that imply a score, or decorative UI that competes with the decision.

## Global hierarchy

1. Current situation / scene
2. Event title and narrative
3. Human stakes
4. Decision heading
5. Choice surfaces
6. Consequence feedback
7. Secondary navigation
8. Supporting panels

The five realm resources remain compact context rather than the primary visual focus.

## Event Screen gold standard

- Portrait-first, one-handed composition.
- Scene art may occupy a strong visual band, but text and decisions remain readable without it.
- Event title uses a display hierarchy and a controlled reading width.
- Narrative uses a comfortable mobile measure and must never be compressed to preserve decorative layout.
- Human-stakes context gets a subtle editorial rule/accent and remains visually separate from narrative.
- Decision heading creates a clear transition from reading to action.
- Choices are visually dominant, evenly spaced, and never visually ranked by position, color, or decoration.

## Choice system

### A/B

- Equal width and equal visual weight.
- Same internal hierarchy: kicker → decisive title → optional supporting line → state.
- No preselection of the first option through stronger color or size.

### A/B/C

- All three choices have equal visual hierarchy.
- Narrow portrait: stacked vertically.
- Wider layouts: balanced columns with equal minimum height.
- Long labels and supporting text wrap naturally; no clipping or horizontal scrolling.
- Choice order comes from authored order.

### Interaction states

Every choice must have visually distinguishable:

- idle
- focus
- pressed
- resolving
- disabled
- resolved/selected

State communication must not depend on color alone. Focus uses a visible outline, pressed uses tactile depth/position, resolving/disabled use opacity/state text, and resolved uses an explicit state cue.

Double submission is blocked at the presentation boundary while the transition is resolving.

## Responsive rules

Reference widths:

- <=380px: compact single-column layout, reduced decorative spacing, no critical fixed-width elements.
- 381–559px: portrait single-column decision layout, including A/B/C.
- >=560px: A/B/C may use three balanced columns.
- >=720px: controlled reading shell up to 760px with larger side margins.

All critical dimensions must remain fluid enough for Android portrait devices.

## Large text

Large accessibility text increases narrative, choice-title and support sizes and choice minimum height. Layout must reflow rather than shrink text or clip content.

## RTL

Use logical properties (`margin-inline`, `padding-inline`, `inset-inline-*`, etc.). Choice accent rails, state labels and alignment mirror naturally. Do not reverse authored choice order merely because the locale is RTL.

## Accessibility

- Semantic headings and grouped decisions.
- `aria-label`/accessible names describe the complete choice without exposing hidden gameplay outcomes.
- Focus is visible.
- Touch targets remain comfortably usable.
- Forced-colors mode preserves state distinctions.
- Reduced-motion removes decorative movement and transitions.
- State changes are announced through a restrained live status region.

## Artwork / no-artwork

Artwork should communicate place, atmosphere and human context, not game mechanics. When artwork is unavailable, use an intentional editorial archive treatment rather than an empty or broken media box.

## Secondary surfaces

### Realm

Show the kingdom's condition as contextual information. Keep resource numbers compact; provide narrative pressure/context beneath them.

### History

Present decisions as a royal record: turn/date, event title, involved people/factions, authored summary and only useful state markers. Never expose internal event IDs.

### People

Portrait-first character surfaces with name, role, contextual relationship language and relevant history. Do not reduce relationships to a single heart meter.

### Factions

Present constituencies through interests, current stance/context, pressure and unresolved issues. Do not visually encode a faction as inherently good or evil.

### Investigation

Use connected evidence chains. Preserve authored uncertainty and avoid implying a single culprit where the narrative supports a systemic explanation.

### Consequences

Use restrained confirmation/pulse presentation. Show authored-visible immediate changes without leaking hidden future consequences.

### Ending

Ending presentation is a chronicle page: decisive event → pause → ending title → authored narrative → remembered causes → optional replay context → continue/replay.

## Visual QA contract

A design block reaches 100% only after:

1. implementation exists;
2. all interaction states are reviewed;
3. responsive widths are reviewed;
4. large text and long strings are reviewed;
5. RTL is reviewed where applicable;
6. accessibility semantics are reviewed;
7. screenshot/visual regression evidence exists where applicable;
8. physical Android QA is complete for device-dependent claims.

Repository implementation alone must never be represented as physical-device verification.

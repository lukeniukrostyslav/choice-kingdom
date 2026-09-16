# Choice Kingdom — Production Screen Specifications

This document converts the visual direction into screen-level production contracts. It intentionally does not implement gameplay semantics.

## Screen 01 — Event / Decision

### Player question
**What is happening, and what am I going to do about it?**

### Composition

1. Quiet header: Avelune + turn + compact realm state.
2. Optional scene illustration.
3. Event title.
4. Narrative body.
5. Human reaction/context line when authored.
6. Two or three choice surfaces.
7. Compact secondary navigation.

### Dominance

The choice surface is the strongest interactive element. Statistics remain subordinate.

### Empty/edge states

- No artwork: typography and spacing must still look intentional.
- One choice: use the same component but never invent a second choice.
- Long narrative: scroll naturally; choices remain reachable without clipping.
- Very large text: collapse secondary metadata before reducing readable narrative size.

### Interaction

Choice selection must dispatch exactly once through `GameSession`. The UI must not calculate gameplay effects.

## Screen 02 — Realm

### Player question
**What condition is the kingdom in?**

### Composition

- Realm headline / current situation.
- Five primary resources as a coherent state group.
- Faction pressure section.
- Relationship section.
- Active delayed consequences.
- Investigation knowledge.

### Rule

Never turn the five resources into five large percentage bars dominating the page.

## Screen 03 — History

### Player question
**What have my decisions already changed?**

### Composition

Chronological authored entries with generous whitespace.

Each entry:

- title;
- turn/date;
- people/factions;
- authored summary;
- important marker where useful.

Internal IDs are hidden.

## Screen 04 — Characters

### Player question
**Who are the people around the Crown, and what has happened between us?**

### Composition

Portrait-led character list → character detail.

Detail view:

- portrait;
- role;
- current relationship description;
- recent history;
- relevant current context.

Avoid heart-meter presentation as the primary visual.

## Screen 05 — Factions

### Player question
**Which constituencies are exerting pressure, and why?**

Show faction context rather than alignment scores alone.

## Screen 06 — Investigation

### Player question
**What do I actually know, and how did I learn it?**

Use a connected evidence graph.

Evidence is authored information, not a free-form detective minigame. The visual layer must not invent connections or conclusions.

## Screen 07 — Consequence Overlay

### Player question
**What changed because of my decision?**

Use a compact transient layer, not a separate reward screen.

Possible rows:

- Gold changed.
- Trust changed.
- Security changed.
- Power changed.
- Reputation changed.
- Relationship changed.
- History recorded.
- Delayed consequence activated/created when the runtime exposes it.

Only render values actually returned by the runtime snapshot/result.

## Screen 08 — Ending

### Player question
**What kind of political legacy did this reign create?**

The ending should read like the last page of the player's chronicle.

Sequence:

1. final event resolves;
2. restrained transition;
3. ending title;
4. ending narrative;
5. remembered causes;
6. relevant people/factions;
7. replay/continue.

No primary score or leaderboard treatment.

## Shared component rules

### Buttons

Primary actions are calm, tactile, and readable. Avoid neon/high-gloss treatment.

### Cards

Use cards only when grouping information genuinely helps. The event decision surface may use cards/rows; narrative copy should not be trapped in many nested cards.

### Icons

Icons are supportive. Never make an icon the only representation of a critical state.

### Dividers

Prefer whitespace and typography over heavy borders.

### Images

Images must have explicit content descriptions where semantically meaningful. Decorative images must be marked decorative.

## Design review checklist

Before implementation of each screen:

- [ ] One clear player question.
- [ ] One clear visual focal point.
- [ ] Decision or information hierarchy is obvious.
- [ ] No F2P/ad-dashboard visual language.
- [ ] No unnecessary ornament.
- [ ] Long text tested conceptually.
- [ ] RTL considered.
- [ ] Large text considered.
- [ ] Reduced motion considered.
- [ ] Runtime boundary identified.
- [ ] No gameplay semantics duplicated in presentation.

# Choice Kingdom — Premium Visual Specification v2

## 1. Design target

Choice Kingdom is presented as a **premium illustrated political chronicle**. The interface should feel authored, quiet, tactile, and consequential. It must not resemble a dashboard, card-heavy F2P game, fantasy RPG inventory, or generic visual-novel shell.

The player should feel that they are sitting with a royal chronicle and making decisions that will remain visible in history.

### Core design principles

1. **Story before statistics.** Numbers support decisions; they do not become the game surface.
2. **Hierarchy before decoration.** Every screen has one dominant question.
3. **Human stakes before systems.** Characters and consequences are more important than meters.
4. **Tension through restraint.** Use spacing, typography, composition, and subtle motion rather than constant effects.
5. **No fake luxury.** Avoid excessive gold, ornamental frames, glowing buttons, particle effects, or pseudo-medieval UI chrome.
6. **Every visual treatment must survive localization and accessibility.**

## 2. Art direction

### World language

Avelune should visually read as a believable late-medieval political realm without locking itself to a specific historical country.

Art direction:

- painterly, grounded, slightly desaturated environments;
- natural faces and believable clothing;
- weather and season used as narrative atmosphere;
- architecture and objects that communicate class and institution;
- restrained texture, never noisy parchment everywhere;
- character portraits with expression and posture carrying meaning.

Avoid:

- cartoon proportions;
- glossy mobile-game fantasy armor;
- excessive magical effects;
- generic castle stock imagery;
- visual shorthand that makes one faction automatically heroic or villainous.

### Illustration composition

Event art should normally reserve a calm area for readable text. The focal subject should sit away from critical UI overlays. Important faces should not be hidden by resource/status chrome.

Use a consistent cinematic crop family so event-to-event transitions feel like one illustrated book rather than unrelated images.

## 3. Color system

Use semantic tokens rather than event-specific colors.

### Base roles

- `canvas`: warm paper/stone neutral.
- `surface`: slightly lifted parchment/card surface.
- `surface-elevated`: stronger separation for modal/context surfaces.
- `ink-primary`: near-black readable text.
- `ink-secondary`: muted explanatory text.
- `authority`: restrained burgundy.
- `stability`: deep forest.
- `gold-accent`: antique brass used sparingly for focus/importance.
- `warning`: warm amber/brown warning role.
- `danger`: muted red role.
- `focus`: high-contrast accessibility focus treatment.

Color must never be the only carrier of meaning. Every positive/negative/changed state also gets text, iconography, shape, motion, or positioning support.

## 4. Typography system

Typography should create the feeling of a printed chronicle while remaining extremely readable on small Android screens.

### Roles

- `display-xl`: ending/title moments.
- `display-lg`: event title.
- `section`: Realm, History, Characters, Investigation headings.
- `body`: narrative copy.
- `body-emphasis`: character names and important phrases.
- `choice-title`: decisive action label.
- `choice-support`: optional intent/context line.
- `state-label`: compact resource/faction labels.
- `meta`: turn/date/supporting information.

Rules:

- Never use all-caps for long narrative text.
- Never rely on weight alone to communicate state.
- Preserve generous line height for narrative copy.
- Keep narrative measure narrow enough to avoid tiring long lines.
- Test the entire hierarchy at enlarged accessibility text sizes.

## 5. Spacing and geometry

Use a small spacing scale and repeat it consistently. Avoid arbitrary per-screen spacing.

Recommended conceptual scale:

`xs → sm → md → lg → xl → 2xl → 3xl`

The event screen should have noticeably more breathing room around the narrative and decision surface than around metadata.

Cards should use restrained corner radii. The product should feel like a book/tabletop object, not a rounded social app.

## 6. Event screen — production composition

The event screen is the visual identity of the entire game.

### Priority order

1. event title / immediate situation;
2. illustration;
3. narrative;
4. choices;
5. compact realm state;
6. navigation.

### Header

Show:

- Avelune mark/name;
- turn indicator;
- compact state summary.

The header must remain quiet. It should never compete with the current decision.

### Event body

Recommended flow:

`context → art → title → narrative → human reaction → choices`

The exact ordering may vary when art is unavailable, but the decision surface must remain dominant.

### Choice surface

Each choice is a substantial tactile row/card:

- action label;
- optional one-line intent framing;
- generous vertical padding;
- visible focus/pressed state;
- clear disabled/resolving state.

Do not expose hidden future outcomes or raw resource deltas by default.

## 7. Realm screen

The Realm screen answers one question:

> **What condition is my kingdom in right now?**

Primary resources are presented as a visual state composition, not five competing progress bars.

Recommended structure:

- current realm summary;
- five primary resources;
- faction pressure;
- important relationships;
- active delayed consequences;
- investigation knowledge.

The player should understand the situation in a few seconds without feeling that they are optimizing a spreadsheet.

## 8. History screen

History should resemble pages in a royal record.

Each entry contains:

- event title;
- turn/date;
- people/factions involved;
- short authored consequence summary;
- optional important marker.

Use chronology and whitespace as the organizing principle. Avoid dense table layouts.

Never expose internal event IDs such as `E199` in normal player-facing UI.

## 9. Character screen

Character presentation must communicate **relationship + personhood + history**.

Portraits should have enough visual space to carry expression. Relationship state should be represented through language and contextual cues, with numeric values remaining secondary.

A character page should answer:

- Who is this person?
- What do they want?
- What has happened between us?
- What is their current relationship to the Crown?

## 10. Faction screen

Factions are political constituencies, not morality meters.

Show:

- current position;
- pressure/concern;
- recent relevant decision;
- unresolved issue;
- important associated characters.

Avoid faction colors that permanently encode good/evil.

## 11. Investigation screen

Investigation is presented as an evidence wall / connected chain rather than a quest checklist.

Evidence nodes should have:

- source;
- short fact;
- confidence/uncertainty when authored;
- links to related evidence;
- relevant people/factions.

The visual language must permit several independent routes to the same systemic understanding.

## 12. Consequence feedback

After a decision, the interface should briefly acknowledge what changed.

Preferred sequence:

1. choice settles;
2. selected choice receives a subtle completion state;
3. changed state markers move/pulse once;
4. relationship/history markers appear when relevant;
5. next event enters.

Avoid full-screen reward effects. Political consequences should feel weighty, not like points being collected.

## 13. Ending screen

The ending is the final page of the chronicle.

Composition:

- quiet transition;
- ending title;
- authored narrative;
- remembered causes;
- meaningful people/factions involved;
- replay information where appropriate;
- replay/continue action.

Do not make the primary ending screen a numerical score screen.

## 14. Motion language

Motion is functional and restrained.

Use:

- fade/slide for navigation;
- short state transition for choice resolution;
- subtle resource movement;
- gentle page/chronicle transition for History;
- restrained ending reveal.

Avoid:

- constant particles;
- bouncing buttons;
- reward explosions;
- long blocking animations;
- motion that changes meaning.

Every meaningful transition must have a reduced-motion alternative.

## 15. Interaction states

Every interactive element must define:

- idle;
- focused;
- pressed;
- resolving;
- disabled;
- completed/resolved where applicable.

Touch targets must remain comfortable at all supported screen sizes and text scales.

## 16. Responsive composition

Reference target: portrait Android phone.

The layout must survive:

- small screens;
- tall screens;
- large accessibility text;
- long translations;
- RTL;
- gesture-navigation insets.

Never fix a critical composition using absolute coordinates that cannot adapt to text growth.

## 17. Accessibility as visual quality

Accessibility is part of the premium design, not a later compliance pass.

Required:

- scalable text;
- screen-reader semantics;
- visible focus;
- sufficient contrast;
- non-color state communication;
- large touch targets;
- reduced motion;
- RTL mirroring;
- locale-aware numbers/dates;
- safe font fallback.

## 18. Quality gate before calling a screen designed

A screen is not considered visually complete until:

- hierarchy is clear at a glance;
- long narrative remains readable;
- choices remain dominant;
- no important state depends only on color;
- localization expansion does not break layout;
- accessibility text scaling does not destroy the decision surface;
- motion has a reduced-motion equivalent;
- the screen looks like Choice Kingdom rather than a generic game template;
- real `GameSession` content can occupy the intended layout without redesigning the runtime contract.

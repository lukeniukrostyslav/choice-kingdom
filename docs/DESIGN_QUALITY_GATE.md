# Choice Kingdom — Design Quality Gate

## Purpose

This document is the hard gate for visual quality before the first production UI implementation is considered complete.

The target is not a collection of attractive screens. The target is a coherent premium political chronicle in which typography, illustration, interaction, state feedback, accessibility, and narrative hierarchy all communicate the same product identity.

## 1. Visual identity gate

- [ ] The product reads immediately as a political chronicle, not a generic mobile game.
- [ ] Parchment/stone warmth is restrained; surfaces do not become decorative wallpaper.
- [ ] Antique brass is an accent, never the dominant color.
- [ ] Burgundy/forest/warning/danger roles are semantic and consistent.
- [ ] No glossy fantasy-game chrome, reward explosions, excessive gradients, or ornamental frames.
- [ ] Illustration style is consistent across event art and portraits.
- [ ] Characters communicate personality through expression, posture, clothing, and context.

## 2. Event screen gold-standard gate

The Event screen is the reference screen for every other screen.

Required hierarchy:

1. immediate situation;
2. illustration or intentional art absence;
3. event title;
4. narrative;
5. human reaction/context;
6. decision surfaces;
7. compact realm state;
8. secondary navigation.

Required interaction states:

- idle;
- focused;
- pressed;
- resolving;
- disabled;
- completed/resolved.

The choice must remain the strongest interactive object on the screen. The interface must never calculate or display invented consequences; runtime data comes through `GameSession`.

## 3. Typography gate

- [ ] Narrative is readable before decorative typography is noticed.
- [ ] Display typography is reserved for meaningful hierarchy.
- [ ] Long prose never uses all-caps styling.
- [ ] Line length remains comfortable on small portrait screens.
- [ ] Large accessibility text is tested without shrinking the narrative into illegibility.
- [ ] Long translated strings wrap naturally.
- [ ] Font fallback remains visually coherent.

## 4. Composition gate

Every screen must have one dominant player question and one clear focal point.

Avoid:

- five competing status bars;
- dashboard density;
- card grids without grouping purpose;
- oversized resource numbers;
- fixed coordinates that break when text grows;
- navigation competing with the decision.

Whitespace is an intentional structural element, not unused space.

## 5. Illustration gate

Event illustrations must:

- support the scene rather than explain the decision mechanically;
- preserve readable areas for UI;
- keep important faces clear of status overlays;
- use a consistent cinematic crop family;
- survive light/dark surface variation where applicable;
- remain meaningful when the UI is localized.

An event without art must still look designed rather than unfinished.

## 6. Realm / History / Character / Faction gate

### Realm

State must read as a political situation, not a spreadsheet. Five resources are a coherent composition, supported by faction pressure, relationships, delayed consequences, and investigation knowledge.

### History

History must feel like a royal record. Chronology, people, factions, consequences, and authored markers matter more than metadata.

### Characters

Portrait, personality, relationship language, recent history, and current context must form one human presentation. A numeric relationship value may support the presentation but cannot replace it.

### Factions

Factions must read as competing constituencies with understandable interests. Visual treatment must not permanently encode good versus evil.

## 7. Investigation gate

The investigation interface is an evidence structure, not a checklist or puzzle-game imitation.

Every visible connection must originate from authored/runtime evidence. The UI must never invent conclusions, certainty, or relationships between evidence nodes.

## 8. Consequence gate

After a decision:

1. the selected choice settles;
2. the changed state is acknowledged once;
3. relevant relationship/history changes appear;
4. delayed consequences appear only when runtime exposes them;
5. the next event takes focus.

No reward shower. No casino-like feedback. Political consequences should feel weighty.

## 9. Accessibility gate

The design is not complete until these are checked:

- scalable text;
- screen-reader labels and roles;
- visible keyboard/focus equivalent where platform-relevant;
- contrast;
- non-color state communication;
- comfortable touch targets;
- reduced motion;
- RTL mirroring;
- locale-aware numbers and dates;
- safe-area / gesture insets;
- long translations;
- small and tall portrait devices.

## 10. Visual regression gate

For each production screen, retain reference captures for at least:

- compact portrait device;
- tall portrait device;
- large text;
- long narrative;
- long choice labels;
- RTL;
- resolving/disabled state;
- no-art fallback where applicable.

A visual change is accepted only when hierarchy and readability remain intact.

## 11. Vercel prototype gate

Before Android UI is treated as visually approved, the same design language should be represented in a real interactive web prototype.

The prototype must:

- render real authored Choice Kingdom content where available;
- use the same visual tokens and hierarchy;
- allow event → choice → consequence → next-event flow;
- demonstrate Realm/History navigation;
- work on a phone browser;
- tolerate long text;
- demonstrate the major interaction states.

The prototype is a visual validation surface, not a replacement for the production Android runtime.

## 12. Final design definition

Design reaches 100% only when:

- the Event screen is implemented and visually reviewed;
- all major screen families share one coherent language;
- responsive behavior is demonstrated;
- accessibility behavior is demonstrated;
- real `GameSession` content fits without semantic duplication;
- Vercel prototype has been visually reviewed;
- remaining changes are polish rather than unresolved structural decisions.

Documentation alone cannot close the implementation gate.

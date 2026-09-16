# Choice Kingdom — Design QA Matrix

This is the design validation contract for the visual prototype and later Android presentation layer. It does not define gameplay semantics.

## 1. Decision surface

- [ ] A/B choices render with balanced hierarchy.
- [ ] A/B/C choices render with three equally legitimate visual options.
- [ ] 3-choice layouts stack safely on narrow phones.
- [ ] Long choice labels wrap without clipping or changing hierarchy.
- [ ] Long supporting text wraps without overlapping controls.
- [ ] Choice order remains authored order.
- [ ] Selected, resolving, disabled and resolved states are distinct without relying on color alone.
- [ ] Double submission is impossible during resolution.
- [ ] The UI never displays hidden future outcomes merely because runtime data contains them.
- [ ] Choice controls remain comfortable at enlarged text sizes.

## 2. Event reading experience

- [ ] Situation is understood before the decision controls.
- [ ] Human stakes remain visible without competing with the decision.
- [ ] Artwork supports the scene and never hides essential text.
- [ ] No-artwork state still looks intentional.
- [ ] Long narrative remains readable and scrollable.
- [ ] Metadata can collapse before narrative typography becomes uncomfortably small.
- [ ] Event IDs are never shown as player-facing copy.

## 3. Realm and persistent state

- [ ] Gold, Trust, Security, Power and Reputation have a coherent visual grouping.
- [ ] Resources do not become five competing dashboard bars.
- [ ] Relationship presentation communicates people and context, not only numbers.
- [ ] Delayed consequences are readable without exposing future hidden information.
- [ ] Faction pressure is contextual rather than a morality meter.

## 4. History / People / Factions / Investigation

- [ ] History reads as a royal record rather than an analytics feed.
- [ ] People surfaces prioritize portrait, role, context and remembered interactions.
- [ ] Factions remain visually neutral toward political constituencies.
- [ ] Investigation presents evidence as an authored connected chain.
- [ ] Uncertainty remains visible when authored.
- [ ] Multiple evidence routes do not visually collapse into an invented single explanation.

## 5. Consequences and endings

- [ ] Consequence feedback is restrained and legible.
- [ ] Only authored-visible changes are presented.
- [ ] Ending feels like a final chronicle page, not a score screen.
- [ ] Ending causes can be presented without inventing causality in the UI.
- [ ] Replay information is clearly separated from the completed run.

## 6. Responsive / localization

- [ ] Small Android portrait width.
- [ ] Tall modern Android portrait.
- [ ] Large accessibility text.
- [ ] Long translated strings.
- [ ] RTL mirroring.
- [ ] Locale-aware numbers and dates.
- [ ] Font fallback for release locales.
- [ ] Safe-area and gesture-navigation insets.
- [ ] No critical content depends on fixed absolute coordinates.

## 7. Accessibility and interaction

- [ ] Screen-reader names and roles are meaningful.
- [ ] Focus is visible.
- [ ] Contrast remains sufficient across semantic states.
- [ ] Meaning is never communicated by color alone.
- [ ] Touch targets remain large enough.
- [ ] Reduced-motion mode removes nonessential motion.
- [ ] Keyboard/focus equivalent states are deterministic where applicable.

## 8. Visual quality gate

A design block is not considered 100% merely because a specification exists. It reaches 100% only after implementation, interaction-state review, responsive review, localization/RTL review, accessibility review, and visual regression against the intended art direction.

The prototype is a validation surface; it must remain visually coherent while the Android UI later consumes the real `GameSession` presentation seam.

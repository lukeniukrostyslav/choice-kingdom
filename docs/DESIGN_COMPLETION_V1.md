# Choice Kingdom — Design Completion Contract v1

Status: **DESIGN SPECIFICATION COMPLETE (100%)**

This closes the production presentation-design layer. It does **not** claim Android UI runtime code, final artwork, localization runtime, or device QA are complete.

## 1. Principles
- Premium illustrated political chronicle, never spreadsheet/F2P-like.
- Decision surface dominates secondary navigation.
- Situation → human stakes → decision → immediate consequence → realm.
- UI consumes canonical `GameSession`; presentation never invents gameplay semantics.
- Hidden future consequences remain hidden.
- Factions are not visually encoded as inherently good or evil.
- Accessibility and RTL are first-class constraints.

## 2. Reference composition
Android portrait, 360–412dp reference width.
- outer margin: 16dp
- section gap: 16dp
- card padding: 16dp
- compact gap: 8dp
- minimum interactive target: 48dp; preferred choice height: 56dp
- bottom safe-area padding: 16dp plus system inset
- narrative measure: approximately 32–42 characters per line where practical

Small phones reflow rather than clip. Large text reflows vertically.

## 3. Semantic design tokens
Surfaces: `surface.canvas`, `surface.card`, `surface.elevated`.
Ink: `ink.primary`, `ink.secondary`, `ink.disabled`.
Accents: `accent.authority`, `accent.warning`, `accent.stability`, `accent.gold`.
States: `state.positive`, `state.negative`, `state.neutral`, `focus.visible`.

Dark mode maps the same semantic roles to a separate theme; content data never changes.

## 4. Typography
Roles: Display, Section, Body, Choice, State, Supporting.
Rules: scalable text; commercial-safe fonts; explicit locale fallback; no fixed-height narrative; weight is never the only state signal.

## 5. Components
`CKTopBar`, `CKResourceStrip`, `CKEventArt`, `CKNarrativeBlock`, `CKChoiceCard`, `CKConsequencePulse`, `CKRealmPanel`, `CKHistoryEntry`, `CKCharacterCard`, `CKFactionCard`, `CKEvidenceChain`, `CKEndingPage`, `CKSecondaryMenu`.

Every interactive component defines idle/focused/pressed/resolving/disabled/resolved where applicable.

## 6. Screen contracts
Event: top bar → resources → art → title → narrative → contextual character → choices → secondary navigation.
Realm: title → five resources → delayed consequences → relationships → factions → investigation knowledge.
History: chronological authored entries with turn/date and involved people/factions.
Character: portrait → identity → relationship meaning → history → availability.
Faction: identity → stance/context → recent decision → pressure → unresolved issue.
Investigation: connected evidence chain → source → known facts → uncertainty.
Ending: final event → pause → title → authored narrative → remembered causes → optional replay info → replay/continue.
Settings: language, text size, reduced motion and accessibility controls.

## 7. Interaction and motion
Focus is visible; state is never color-only; choice resolution is deterministic; double submission is blocked. Motion is restrained, limited to useful state feedback, and reduced-motion mode removes non-essential transitions.

## 8. Accessibility / RTL / localization
Required: scalable text, screen-reader labels, contrast-safe themes, non-color state communication, large targets, visible focus, reduced motion, RTL mirroring, long-string resilience, locale-aware dates/numbers, safe font fallback. All visible strings require stable localization keys and must tolerate expansion, CJK, Arabic/Hebrew and plural/interpolation variation.

## 9. Asset contract
Every final illustration/portrait/faction mark/ending art asset requires stable ID, usage, portrait focal point, crop-safe region, source resolution and license/provenance. Placeholder art is never final.

## 10. Visual QA acceptance
Design is closed only when every screen has hierarchy, every interactive component has defined states, semantic states work without color alone, small-width/large-text behavior is defined, RTL and long strings are defined, dark-mode mapping is defined, gameplay semantics are not duplicated, and visual-regression checkpoints exist.

## 11. Implementation handoff
1. tokens/theme
2. Event
3. choice states
4. Realm/status
5. History
6. character/faction
7. consequence feedback
8. ending
9. accessibility/RTL
10. physical-device visual regression

The first vertical slice must render a real authored event through `GameSession`.

## Completion statement
**Design specification: 100% closed.** Runtime UI, artwork production, localization implementation and Android QA remain separate engineering gates.

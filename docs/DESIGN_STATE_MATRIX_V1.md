# Choice Kingdom — Production Design State Matrix v1

Status: **DESIGN ARTIFACT COMPLETE (100%)**

This matrix turns the existing screen/component contracts into an implementation-ready visual-state specification. It does not claim that Android runtime rendering or physical-device QA has been executed.

## 1. Global interactive state contract

| State | Visual requirement | Input requirement | Semantic requirement |
|---|---|---|---|
| idle | default surface, clear hierarchy | actionable when enabled | neutral/default state exposed to assistive tech |
| focused | visible focus treatment independent of color | keyboard/switch/accessibility focus remains stable | focus is announced/identifiable |
| pressed | immediate tactile/visual acknowledgement | one activation path | no duplicate submission |
| resolving | explicit progress/transition treatment | input blocked for the same decision | resolving state exposed; future outcome remains hidden |
| disabled | reduced emphasis without ambiguity | not actionable | reason/status remains understandable without color |
| resolved | settled result treatment | previous choice cannot be submitted again | result is represented by canonical session state |

## 2. Screen-to-state coverage

| Screen | Primary states that must be designed | Critical edge cases |
|---|---|---|
| Event | idle, focused, pressed, resolving, disabled, resolved | long narrative, large text, RTL, no-choice node |
| Realm | idle, focused, disabled, resolved | sparse resources, delayed effects, relationship/faction pressure |
| History | idle, focused, disabled | empty history, long history, RTL/date expansion |
| Character | idle, focused, disabled | missing portrait, long names, unavailable character |
| Faction | idle, focused, disabled, resolved | neutral/negative/positive stance without color-only encoding |
| Investigation | idle, focused, disabled, resolved | uncertain evidence, branching evidence, incomplete chain |
| Ending | idle, focused, resolved | all ending families, long narrative, replay/continue boundary |
| Settings | idle, focused, pressed, disabled, resolved | RTL, large text, reduced motion, locale expansion |

## 3. Choice-card contract

Every `CKChoiceCard` must preserve the following hierarchy:
1. choice label/action;
2. optional supporting context;
3. focus/pressed/resolving/disabled state;
4. post-resolution feedback only after the canonical runtime result is available.

Rules:
- minimum interactive target: 48dp;
- preferred choice height: 56dp;
- never encode enabled/disabled/resolved solely with color;
- resolving blocks duplicate activation;
- hidden future consequences are never previewed;
- internal event IDs are never rendered.

## 4. Responsive contract

Reference widths: 360dp and 412dp portrait, plus tall-phone composition.

At narrow widths, content reflows vertically; it must not shrink decision text below the readable typography role or clip the primary decision controls. Large accessibility text follows the same rule and increases vertical flow instead of forcing fixed-height narrative containers.

## 5. RTL and localization contract

- mirror layout direction, not semantic meaning;
- keep icons with directional meaning mirrored where appropriate;
- preserve chronology and causal ordering;
- allow translated labels to expand without clipping;
- support CJK line breaking and Arabic/Hebrew fallback;
- keep dates/numbers locale-aware;
- do not expose localization keys or internal IDs.

## 6. Motion contract

Default motion is restrained and state-oriented. Non-essential transitions disappear under reduced-motion mode. Motion never becomes the only signal for a state change.

## 7. Accessibility contract

Every actionable component requires:
- accessible name/role/state;
- visible focus;
- target size >=48dp;
- contrast-safe presentation;
- non-color state communication;
- deterministic disabled/resolving behavior.

## 8. Design acceptance gate

A design state is considered specified only when its idle/focus/pressed/resolving/disabled/resolved behavior is documented where applicable, plus responsive, RTL/localization and accessibility behavior. Execution of this matrix on Android devices belongs to the separate Visual QA gate.

# Choice Kingdom — Motion + Cross-screen Design Closure v1

Status: CLOSED DESIGN CONTRACT

## Motion

- Default transitions use the 180ms token.
- Emphasis transitions may use 240ms.
- Motion confirms state change; it never carries information that is unavailable in static form.
- Pressed/resolving/resolved states have deterministic visual endpoints.
- Duplicate interaction is prevented while a decision is resolving.
- Reduced-motion mode removes nonessential movement and uses instant or fade state changes.

## Cross-screen integration

The eight primary screens share the same top-level layout grammar, spacing scale, semantic surfaces, typography roles, state vocabulary, touch targets, focus behavior, RTL behavior and safe-area rules. A player should be able to move between Event, Realm, History, Character, Faction, Investigation, Ending and Settings without learning a new interaction language.

## Production handoff

Every screen/component contract is implementation-ready at the design level with explicit states, edge cases, responsive rules and accessibility requirements. Runtime code, final artwork, automated visual regression and physical-device execution remain separate engineering/QA evidence.

## Closure evidence

- D19 Motion / Micro-interactions: 95% -> 100% design contract closure.
- D21 Cross-screen Design Integration: 99% -> 100% design contract closure.
- D22 Production Mobile Design Handoff: 99% -> 100% design contract closure.

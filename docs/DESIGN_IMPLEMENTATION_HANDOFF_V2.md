# Choice Kingdom — Design Implementation Handoff v2

Status: **DESIGN HANDOFF SPECIFIED**

This document converts the closed design specification into an implementation sequence without mixing design completion with Android runtime completion.

## Vertical slice order

### 1. Theme / tokens
- Load semantic surface, ink, accent, state and focus roles.
- Apply spacing, radii, touch-target and typography tokens.
- Keep dark mode semantic rather than content-dependent.

### 2. Event screen
- Render a real authored event from `GameSession`.
- Compose TopBar → ResourceStrip → EventArt → Narrative → ChoiceCards.
- Support no-choice special nodes without inventing a fake choice.

### 3. Choice resolution
- idle → focused → pressed → resolving → resolved.
- Block duplicate submission during resolving.
- Render only the canonical runtime result; never predict hidden future consequences.

### 4. Realm / status
- Render resources, delayed effects, relationships and factions from canonical session state.
- Empty/sparse states must remain intentional and readable.

### 5. History / people / factions
- Chronological history entries.
- Character identity/relationship/history states.
- Faction stance without good/evil visual encoding.

### 6. Investigation / ending
- Evidence chain preserves uncertainty and provenance.
- Ending page renders authored outcome, remembered causes and replay boundary.

### 7. Settings / accessibility
- Language, text size and reduced motion.
- Screen-reader semantics, focus, RTL mirroring and large-text reflow.

## Release-blocking design checks

Before an Android UI block is called design-compliant, verify:
- 360dp portrait;
- 412dp portrait;
- tall phone/safe area;
- large text;
- long localized strings;
- CJK fallback;
- Arabic/Hebrew RTL;
- idle/focus/pressed/resolving/disabled/resolved states where applicable;
- no color-only semantics;
- no duplicate choice submission;
- no internal IDs exposed;
- no hidden future consequences leaked;
- faction neutrality preserved.

## Boundary

**Design specification:** closed.

**Runtime UI:** not complete until implemented and tested.

**Physical visual QA:** not complete until the existing Visual QA Checklist is actually executed on representative Android configurations.

**Final artwork:** not complete until every production asset has ID, usage, crop-safe region, provenance/license and QA evidence.

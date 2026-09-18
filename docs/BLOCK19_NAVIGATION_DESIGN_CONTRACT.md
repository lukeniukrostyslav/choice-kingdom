# Choice Kingdom — P19 Navigation / Information Architecture Design Contract

## Premium intent
Navigation should preserve narrative context rather than behave like a generic dashboard. The active journey is visually and semantically primary; secondary surfaces expose people, investigation, chronicle, replay and settings without obscuring the player's current place.

## Surface contract
- Current Journey is the primary navigation destination and exposes the active-thread state.
- Secondary destinations remain visually subordinate and consistently ordered.
- The navigation hierarchy is understandable without relying on color alone.
- Keyboard users receive a skip path into the navigation region and visible focus treatment.
- RTL mirrors directional presentation without breaking focus placement or reading order.
- Mobile collapses to a single-column information hierarchy without horizontal overflow.
- Large text and long labels must remain readable without clipping.
- Reduced-motion behavior remains explicit.
- Safe-area-compatible viewport metadata is present.
- Back/return navigation remains a minimum 48px interaction target.

## Evidence
Representative surface: `web-preview/design-navigation-p19-premium.html`.
V15 matrix inclusion: `tools/v15_visual_closure.mjs`.
Current implementation commits:
- `deea2993d41f634b8790dd7ef65b376f52b8468e` — initial premium contextual navigation surface.
- `1053158151b2fc13f6788bf20fe9c703704603b4` — added to V15 visual closure matrix.
- `c9e9f038fd335742ca51c377d40a6cd2e113ba45` — keyboard skip path and RTL focus path.
- `9da6df3a9ba2062c1107125e3cbb39bdc4eb48f9` — explicit active-journey hierarchy.

## Closure rule
P19 must not be marked 100% until the post-change V15 cross-viewport regression run is observed green. This contract alone is not closure evidence.

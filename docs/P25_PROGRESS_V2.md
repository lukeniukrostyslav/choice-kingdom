# Choice Kingdom — P25 Premium Design Progress

## Current state
- P25 overall: **94%**
- 25.4 Choice chamber / decision interaction: **100% — CLOSED**
- 25.5 Consequence / memory reveal: **100% — CLOSED**
- P25 overall remains 94% because the final visual-regression/deployed-proof gate is still open.

## P25 sub-blocks

| Sub-block | Completion | State |
|---|---:|---|
| 25.1 Visual game shell / cinematic composition | 100% | CLOSED |
| 25.2 Main menu / first impression | 100% | CLOSED |
| 25.3 Event / situation scene | 100% | CLOSED |
| 25.4 Choice chamber / decision interaction | 100% | CLOSED |
| 25.5 Consequence / memory reveal | 100% | CLOSED |
| 25.6 Kingdom / realm presentation | 100% | CLOSED |
| 25.7 People / character presentation | 100% | CLOSED |
| 25.8 Factions / institutional presentation | 100% | CLOSED |
| 25.9 Investigation / evidence board | 100% | CLOSED |
| 25.10 History / decision chronicle | 100% | CLOSED |
| 25.11 Endings / resolution landing | 100% | CLOSED |
| 25.12 Settings / accessibility presentation | 100% | CLOSED |
| 25.13 Navigation / information architecture | 100% | CLOSED |
| 25.14 Responsive / safe-area composition | 97% | OPEN |
| 25.15 Visual regression / final acceptance | 79% | OPEN |

## 25.4 closure record

The choice chamber now has:
- explicit decision hierarchy inside the cinematic event panel;
- numbered choice affordances;
- selected/focused visual state;
- semantic radiogroup/radio semantics with aria-selected;
- keyboard Arrow Up/Down and Left/Right focus navigation;
- Enter/Space confirmation;
- touch/click confirmation;
- immediate selection feedback;
- double-activation protection while a choice resolves;
- responsive mobile sizing and focus-visible treatment;
- regression coverage for keyboard selection state.

Canonical event/choice text and effects were not changed or invented.

## 25.6 closure record

The Kingdom / realm surface is now closed at 100% with:
- canonical institutional vocabulary only: Crown, Commons, Noble, Guild, Border / Security, Civic / Medical;
- removal of the non-canonical placeholder realm name from the presentation surface;
- premium map composition with layered depth, atmospheric treatment, ring/path texture and restrained gold hierarchy;
- six interactive institutional nodes with selected state and visible focus treatment;
- keyboard left/right/up/down navigation between realm nodes;
- current-run metrics for Resources, Trust, Security and Authority;
- selected institutional context panel with an explicit canon boundary so visual placement does not imply territory, alliances, relationships or hidden state;
- responsive compact composition for mobile widths;
- dedicated gate coverage for node count, canonical labels, selection state, keyboard navigation, run metrics and non-canonical name leakage.

No new kingdom names, territories, alliances, relationships, mottos or lore were invented.

The implementation, gate hardening and progress record are committed to `main`. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.

## 25.7 closure record

The People / character presentation is now closed at 100% with:
- all six verified recurring People presented: Mara, Rowan, Seris, Ivo, Amara and Toma;
- canonical narrative hooks preserved without adding invented age, appearance, title, motive, relationship, faction membership or hidden state;
- premium character-card treatment with cinematic framing, atmospheric depth, identity monogram and readable narrative anchor;
- explicit "Verified narrative anchor" labeling to distinguish canon from presentation treatment;
- semantic interactive character cards with dialog semantics and visible keyboard focus;
- Enter/Space activation plus directional keyboard navigation between People cards;
- existing detail-dialog focus management retained, including focus return and trap behavior;
- responsive two-column mobile/tablet presentation while preserving readable card hierarchy;
- dedicated gate coverage for all six People, card interactivity, keyboard navigation and detail-dialog behavior.

No new character lore, relationships, factions, titles or visual canon was invented.

The implementation, gate hardening and progress record are committed to main. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.

## 25.8 closure record

The Factions / institutional presentation is now closed at 100% with:
- all six verified institutional positions presented: Crown, Commons, Noble, Guild, Border / Security and Civic / Medical;
- premium institutional cards with layered banner framing, restrained gold hierarchy and cinematic depth;
- neutral abstract visual marks used strictly as presentation treatment, not as canonical crests or heraldry;
- semantic interactive cards with dialog semantics and visible keyboard focus;
- Enter/Space activation plus directional keyboard navigation between institution cards;
- detail dialog coverage for canonical institutional context with an explicit boundary against invented territory, mottos, crest lore, relationship states or character membership;
- responsive card composition retained for the premium surface;
- dedicated gate coverage for all six institutions, card interactivity, keyboard navigation, dialog state and canon-boundary text.

No new faction names, territories, alliances, relationships, mottos, heraldry or lore were invented. The implementation, gate hardening and progress record are committed to main. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.

## 25.9 closure record

The Investigation / evidence board is now closed at 100% with:
- four verified investigation routes preserved: Mara's route, Toma's route, Seris's route and Direct account route;
- premium evidence-board composition with layered material depth, restrained lighting, connection-line treatment and readable evidence cards;
- route cards converted to semantic keyboard-operable controls with visible focus treatment;
- Enter/Space activation through native buttons plus directional arrow navigation between the four evidence routes;
- route detail dialog with an explicit canonical boundary: the board presentation does not invent hidden connections, conclusions or additional narrative facts;
- responsive board presentation retained without adding new lore;
- dedicated gate coverage for route count, canonical labels, interaction, keyboard navigation, dialog state and canon-boundary text.

No new investigation facts, relationships, hidden connections, conclusions or lore were invented. The implementation, gate hardening and progress record are committed to main. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.

## 25.10 closure record

The History / decision chronicle is now closed at 100% with:
- the run history rendered as a premium cinematic chronicle rather than plain text rows;
- recorded event ID, event title and exact selected choice preserved from the existing runtime state;
- each recorded decision exposed as a native keyboard-operable button with visible focus treatment;
- directional keyboard navigation retained inside the chronicle;
- decision-detail dialog showing the recorded choice and an explicit boundary that the entry reflects current run memory only and does not invent additional consequences or narrative facts;
- responsive timeline/panel composition retained for compact layouts;
- dedicated gate coverage for timeline presence, recorded E01, interactive history entry, keyboard behavior, dialog state and canon boundary.

No new event, choice, consequence, relationship, faction, ending or lore was invented.

The implementation, gate hardening and progress record are committed to `main`. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.

## 25.11 closure record

The Endings / resolution landing is now closed at 100% with:
- the seven verified canonical ending identities presented as a premium resolution catalogue: Steward, Iron Crown, Golden Compact, People’s Charter, Broken Diadem, Quiet Throne and Second Founder;
- ending identity cards upgraded to semantic keyboard-operable controls with visible focus treatment;
- directional keyboard navigation between ending identities;
- detail dialog presentation for each canonical ending identity;
- explicit boundary that the visual prototype does not claim which ending is currently reached and does not invent additional resolution facts;
- responsive premium card composition retained for compact layouts;
- dedicated gate coverage for all seven identities, interaction, keyboard navigation, dialog state and canon-boundary text.

No new ending identity, outcome, consequence, relationship, faction or lore was invented.

The implementation, gate hardening and progress record are committed to `main`. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.


## 25.13 closure record

The Navigation / information architecture sub-block is now closed at 100% with:
- stable screen-key navigation independent of localized labels;
- canonical route/hash continuity for the premium surface;
- browser back and forward continuity verified against the actual interactive surface;
- active navigation state and URL hash restored together after browser history traversal;
- direct route restoration through the existing URL-state entry path;
- dedicated gate coverage for Kingdom → People navigation, browser Back, browser Forward, restored active surface and restored URL hash;
- no new story facts, routes, characters, factions or lore introduced.

The implementation and acceptance coverage are committed to `main`. P25 remains open at 94% because 25.14 responsive live-device evidence and 25.15 final visual-regression/deployed-proof acceptance remain open.

## 25.12 closure record

The Settings / accessibility presentation is now closed at 100% with:
- four grouped presentation controls: Large text, RTL preview, Reduced motion and Light / dark presentation;
- semantic `aria-pressed` state on every toggle, with visible focus and selected-state treatment;
- persistent local preferences for text scale, document direction, motion reduction and theme;
- a live local-state summary that exposes the current presentation configuration;
- responsive premium setting cards with numbered hierarchy, descriptions and cinematic panel treatment;
- an explicit boundary that these controls change presentation only and do not alter canonical story facts, choices or outcomes;
- dedicated gate coverage for settings grouping, all four controls, initial state semantics, keyboard activation, state summary, canon boundary, persistence and compact-layout overflow.

No story facts, characters, factions, endings, relationships or lore were invented or changed.

The implementation, gate hardening and progress record are committed to `main`. Final P25 acceptance remains open because fresh runtime/visual evidence and deployed proof are still required; no green CI or live Vercel verification is claimed without actual evidence.

## Verification boundary

The implementation and gate are committed to main. A new green GitHub Actions run has not yet been produced for this direct main commit, so automated green status is intentionally not claimed here. Final P25 acceptance still requires fresh runtime/visual evidence on the current commit/deployed surface.

## 25.5 closure record

The consequence scene now has:
- explicit decision-recorded marker;
- exact selected choice surfaced as the consequence headline;
- consequence explanation kept bound to the existing canonical choice text;
- immediate-effect section with structured effect cards;
- persistent run-memory confirmation;
- clear continuation hierarchy;
- mobile-safe action layout;
- gate coverage for the selected option, effect grid and memory status.

No new narrative facts, factions, relationships or lore were introduced.

The implementation and gate are committed to `main`. A fresh green GitHub Actions run is not claimed until one is actually produced for the current commit.

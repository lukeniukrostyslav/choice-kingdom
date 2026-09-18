# P25 V2 Implementation Checkpoint — 2026-09-19

## Status
- P1–P24: 100%
- P25: 93%
- Premium Design aggregate: 99.72%
- P25 remains OPEN.

## Work completed in this checkpoint
1. Deepened the People presentation in `web-preview/game-premium.html`.
   - Six canonical People remain unchanged: Mara, Rowan, Seris, Ivo, Amara, Toma.
   - Added keyboard-accessible detail interaction.
   - Added a focused detail dialog that distinguishes canonical narrative anchors from visual presentation.
   - No invented relationship, faction membership, title, age, quote or hidden state was added.
2. Deepened the institutional/faction presentation.
   - Vocabulary remains exactly: Crown, Commons, Noble, Guild, Border / Security, Civic / Medical.
   - Added accessible detail interaction.
   - Detail copy explicitly preserves the canonical boundary: no invented territory, motto, crest lore, relationship state or character membership.
3. Hardened Settings presentation.
   - Replaced the previous partial theme-variable toggle with a real document theme state and light-theme overrides.
4. Hardened the P25 browser gate.
   - Gate now targets `game-premium.html` for both expanded and compact proof.
   - Gate checks People detail dialog and institutional canonical-boundary copy.
   - Gate still checks the playable E01 → E02 → E05 flow, all six People, all six institutional positions, Investigation, History, Endings, Settings, responsive screenshots and legacy-text exclusion.

## Honest verification boundary
- These repository changes are saved on `main`.
- The gate source is updated, but this checkpoint does not claim a new green GitHub Actions run unless one is independently observed.
- Live Vercel visual review against the frozen reference images remains open.
- P25 100% still requires deployed visual review plus final cross-screen regression sign-off.
- CSS-generated portrait/faction treatment is an implementation approximation; approved reference artwork is not being claimed as production art.

## Diagnostic P25 sub-blocks
- 25.1 Visual game shell / cinematic composition — 96%
- 25.2 Main menu / first impression — 95%
- 25.3 Event / situation scene — 96%
- 25.4 Choice chamber / decision interaction — 95%
- 25.5 Consequence / memory reveal — 95%
- 25.6 Kingdom / realm presentation — 94%
- 25.7 People / character presentation — 94%
- 25.8 Factions / institutional presentation — 94%
- 25.9 Investigation / evidence board — 94%
- 25.10 History / decision chronicle — 95%
- 25.11 Endings / resolution landing — 93%
- 25.12 Settings / accessibility presentation — 97%
- 25.13 Navigation / information architecture — 97%
- 25.14 Responsive / safe-area composition — 94%
- 25.15 Visual regression / final acceptance — 72%

The sub-block values are diagnostic and are not averaged to calculate P25 overall.

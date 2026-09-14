# PLAN — Choice Kingdom

## Governing rule

**Build the full game design first. Build the engine last among the major development layers, and build the APK only after the game, systems and QA are actually ready.**

This project must not become a short card demo. The full-release target is approximately 250–350+ meaningful authored events/story nodes, substantial branching and delayed consequences, 8–12 recognizable endings, and multi-hour first playthroughs with materially different replay paths. Quality and causal depth outrank a mechanical event-count target.

## Phase 0 — Foundation

- [x] Establish product direction
- [x] Establish original/non-clone boundary
- [x] Establish engineering rules
- [x] Establish continuation handoff
- [x] Establish complete project state file
- [x] Establish full-release scale and content-first rule
- [ ] Finalize decision log

## Phase 1 — Full narrative/content design (CURRENT PRIORITY)

- [x] Define original setting and creative promise
- [x] Define main cast and relationship arcs
- [x] Define five-act campaign structure
- [x] Define initial authored event network
- [x] Define immediate/near-term/delayed/legacy consequence philosophy
- [x] Define replay differentiation rules
- [x] Define ending philosophy
- [ ] Finish the complete campaign spine and final act
- [ ] Expand to approximately 250–350+ meaningful authored events/story nodes
- [ ] Ensure every major event has downstream consequences
- [ ] Ensure delayed consequences and callbacks are distributed across the campaign
- [ ] Ensure mutually exclusive branches are intentional and recoverable
- [ ] Ensure each major character has positive and negative arcs
- [ ] Ensure every major faction gets credible positions and wins/losses
- [ ] Ensure investigation routes reveal different useful information
- [ ] Ensure late crises remember earlier preparation
- [ ] Ensure 8–12 endings have recognizable causal paths
- [ ] Complete pacing/replayability review

## Phase 2 — Content QA and production specification

- [ ] Create complete content QA matrix covering every event/node
- [ ] Audit branch dead-ends
- [ ] Audit contradictions and impossible states
- [ ] Audit repetitive choices and filler content
- [ ] Audit consequence horizons and delayed triggers
- [ ] Audit resource pressure and pacing
- [ ] Audit replay divergence
- [ ] Audit ending reachability and independence of critical prerequisites
- [ ] Freeze the narrative/content specification only after review

## Phase 3 — Architecture from real authored content

- [x] Define preliminary state model
- [x] Define preliminary event schema
- [x] Define preliminary choice schema
- [x] Define preliminary condition operators
- [x] Define preliminary effect operators
- [x] Define history/flag model
- [x] Define delayed-consequence model
- [x] Define deterministic RNG/replay contract
- [x] Define save schema/versioning
- [x] Define localization contract
- [ ] Reconcile all contracts against the complete production catalog
- [ ] Define content validation rules

## Phase 4 — Decision engine (DELIBERATELY AFTER CONTENT)

- [ ] Create/finish Godot project foundation
- [ ] Implement state engine
- [ ] Implement event resolver
- [ ] Implement conditions and consequences
- [ ] Implement history and branch state
- [ ] Implement delayed consequences
- [ ] Implement deterministic replay seed handling
- [ ] Implement persistence/save versioning
- [ ] Implement ending resolution
- [ ] Implement content loading/validation

## Phase 5 — Real playable game / UI

- [ ] Build real event presentation UI
- [ ] Build choice interaction
- [ ] Build state/history presentation where appropriate
- [ ] Build character/relationship presentation
- [ ] Build menus/settings/save flow
- [ ] Build actual campaign flow using authored production content
- [ ] No placeholder/demo path presented as the finished game

## Phase 6 — Localization, verification and balance

- [ ] Implement 20+ locales
- [ ] Device locale detection and persisted language
- [ ] Missing-key validation
- [ ] RTL validation
- [ ] Long-string/overflow validation
- [ ] Unit tests for state transitions
- [ ] Event contract tests
- [ ] Deterministic replay tests
- [ ] Save/load round-trip tests
- [ ] Delayed consequence tests
- [ ] Invalid-data rejection tests
- [ ] Headless gameplay smoke tests
- [ ] Full-catalog content validation
- [ ] Balance resources and consequence pacing
- [ ] Accessibility/polish
- [ ] Audio/haptics

## Phase 7 — Android QA and APK (LAST TECHNICAL GATE)

- [ ] Android debug build
- [ ] Install/run on physical device
- [ ] Touch/UI verification
- [ ] Save/reload verification
- [ ] Performance sanity check
- [ ] Localization verification on device
- [ ] Final APK smoke/regression pass

## Phase 8 — Production release

- [ ] Production AAB
- [ ] Production signing boundary
- [ ] Store assets
- [ ] Store listing
- [ ] Privacy/data-safety review
- [ ] Final release QA
- [ ] Owner publication actions

## Gate rule

No phase is considered complete because files exist. The implementation must pass the verification appropriate to that phase. Percentages must reflect actual work and verification, not documentation volume.

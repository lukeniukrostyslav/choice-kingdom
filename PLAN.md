# PLAN — Choice Kingdom

## Phase 0 — Foundation

- [x] Establish product direction
- [x] Establish original/non-clone boundary
- [x] Establish engineering rules
- [x] Establish continuation handoff
- [ ] Establish complete project state file
- [ ] Establish decision log

## Phase 1 — Architecture

- [ ] Define canonical state model
- [ ] Define event schema
- [ ] Define choice schema
- [ ] Define condition operators
- [ ] Define effect operators
- [ ] Define history/flag model
- [ ] Define delayed-consequence model
- [ ] Define deterministic RNG/replay contract
- [ ] Define save schema/versioning
- [ ] Define localization contract

## Phase 2 — Vertical slice

- [ ] Create Godot project
- [ ] Implement state engine
- [ ] Implement event resolver
- [ ] Implement history
- [ ] Implement delayed consequences
- [ ] Implement persistence
- [ ] Implement basic event UI
- [ ] Implement one character relationship
- [ ] Implement resource threshold logic
- [ ] Implement one history-dependent event
- [ ] Implement at least one ending

## Phase 3 — Verification

- [ ] Unit tests for state transitions
- [ ] Event contract tests
- [ ] Deterministic replay tests
- [ ] Save/load round-trip tests
- [ ] Delayed consequence tests
- [ ] Invalid-data rejection tests
- [ ] Headless gameplay smoke test

## Phase 4 — Android

- [ ] Android debug build
- [ ] Install/run on physical device
- [ ] Touch/UI verification
- [ ] Save/reload verification
- [ ] Performance sanity check
- [ ] Production signing boundary

## Phase 5 — Content

- [ ] Expand event catalog
- [ ] Expand characters
- [ ] Add event chains
- [ ] Add endings
- [ ] Balance resources
- [ ] Localization
- [ ] Accessibility/polish

## Phase 6 — Release

- [ ] Release build
- [ ] Store assets
- [ ] Store listing
- [ ] Privacy/data-safety review
- [ ] Final QA
- [ ] Owner publication actions

## Gate rule

No phase is considered complete because files exist. The implementation must pass the verification appropriate to that phase.

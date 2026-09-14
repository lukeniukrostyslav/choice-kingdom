# PLAN — Choice Kingdom

## Phase 0 — Foundation

- [x] Establish product direction
- [x] Establish original/non-clone boundary
- [x] Establish engineering rules
- [x] Establish continuation handoff
- [x] Establish complete project state file
- [ ] Finalize decision log

## Phase 1 — Narrative & gameplay design

- [x] Define original setting and creative promise
- [x] Define main cast and relationship arcs
- [x] Define five-act campaign structure
- [x] Define first 40-event authored network
- [x] Define immediate/near-term/delayed/legacy consequence philosophy
- [x] Define replay differentiation rules
- [x] Define ending philosophy and seven target endings
- [ ] Review event network for branch dead-ends
- [ ] Balance event frequency and resource pressure
- [ ] Expand first campaign to 40–60 fully authored production events
- [ ] Create localization keys for all authored content

## Phase 2 — Architecture from authored content

- [x] Define canonical state model
- [x] Define event schema
- [x] Define choice schema
- [x] Define condition operators
- [x] Define effect operators
- [x] Define history/flag model
- [x] Define delayed-consequence model
- [x] Define deterministic RNG/replay contract
- [x] Define save schema/versioning
- [x] Define localization contract
- [ ] Map every authored event to machine-readable contracts
- [ ] Define content validation rules

## Phase 3 — Vertical slice

- [ ] Create Godot project
- [ ] Implement state engine
- [ ] Implement event resolver
- [ ] Implement history
- [ ] Implement delayed consequences
- [ ] Implement persistence
- [ ] Implement basic event UI
- [ ] Implement one character relationship
- [ ] Implement resource threshold logic
- [ ] Implement history-dependent event
- [ ] Implement at least one authored ending

## Phase 4 — Verification

- [ ] Unit tests for state transitions
- [ ] Event contract tests
- [ ] Deterministic replay tests
- [ ] Save/load round-trip tests
- [ ] Delayed consequence tests
- [ ] Invalid-data rejection tests
- [ ] Headless gameplay smoke test
- [ ] Full-catalog content validation

## Phase 5 — Android

- [ ] Android debug build
- [ ] Install/run on physical device
- [ ] Touch/UI verification
- [ ] Save/reload verification
- [ ] Performance sanity check
- [ ] Production signing boundary

## Phase 6 — Content & polish

- [ ] Expand event catalog to release target
- [ ] Expand character arcs
- [ ] Add all event chains
- [ ] Add all ending variants
- [ ] Balance resources and consequence pacing
- [ ] 20+ locale implementation
- [ ] RTL and long-string UI tests
- [ ] Accessibility/polish
- [ ] Audio/haptics

## Phase 7 — Release

- [ ] Release build
- [ ] Store assets
- [ ] Store listing
- [ ] Privacy/data-safety review
- [ ] Final QA
- [ ] Owner publication actions

## Gate rule

No phase is considered complete because files exist. The implementation must pass the verification appropriate to that phase.

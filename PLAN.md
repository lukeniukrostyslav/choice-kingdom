# PLAN — Choice Kingdom

## Non-negotiable development order

**Story/content first → content QA → data contracts → engine → full game/UI → verification/polish → Android QA → APK last → production release.**

The project must not jump ahead to engine, UI or APK work to compensate for unfinished game design. The engine is an implementation of the finished gameplay design, not the place where the game is invented.

---

## Phase 0 — Foundation

- [x] Establish product direction
- [x] Establish original/non-clone boundary
- [x] Establish engineering rules
- [x] Establish continuation handoff
- [x] Establish complete project state file
- [ ] Finalize decision log
- [x] Lock full-release scale and duration targets
- [x] Lock content-first / engine-late / APK-last rule

## Phase 1 — Full narrative and content design

- [x] Define original setting and creative promise
- [x] Define main cast and relationship arcs
- [x] Define five-act campaign structure
- [x] Define initial authored event network
- [x] Define immediate/near-term/delayed/legacy consequence philosophy
- [x] Define replay differentiation rules
- [x] Define ending philosophy
- [ ] Expand campaign to approximately 250–350+ meaningful authored events/content nodes
- [ ] Expand to 8–12 meaningful endings
- [ ] Complete all major character positive/negative arcs
- [ ] Complete faction arcs and mutually conflicting legitimate positions
- [ ] Complete investigation routes and information asymmetry
- [ ] Complete delayed consequences and callbacks
- [ ] Complete crisis chains and final constitutional/endgame branches
- [ ] Ensure multiple independent routes into important endings
- [ ] Ensure replay reveals materially different information/routes
- [ ] Review event network for branch dead-ends
- [ ] Review pacing for first run and later runs
- [ ] Balance resource pressure and consequence density

## Phase 2 — Content QA / campaign gate

- [ ] Every production event has a purpose and downstream effect
- [ ] No filler events added only to increase count
- [ ] No critical branch depends on one character relationship alone
- [ ] At least 10 delayed consequences of 3+ turns
- [ ] At least 6 mutually exclusive future branch locks
- [ ] At least 6 callback events
- [ ] At least 4 investigation decisions that change interpretation/routes
- [ ] At least 4 earlier costly choices become useful later
- [ ] Every major character has both positive and negative arc outcomes
- [ ] Every major faction has at least one situation where its reasonable position is correct
- [ ] Each act recontextualizes at least one earlier decision
- [ ] Ending prerequisites have recognizable, non-single-character paths
- [ ] First-run pacing target ~3–5 hours
- [ ] Multiple-run target ~10–20+ hours
- [ ] Deep exploration target ~20–30+ hours
- [ ] Full campaign content review completed

**Gate:** Do not begin engine implementation until the content gate is substantially satisfied and the remaining gaps are explicitly documented.

## Phase 3 — Architecture derived from authored content

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
- [ ] Map every final authored event to machine-readable contracts
- [ ] Define content validation rules from the final catalog
- [ ] Freeze gameplay contracts before implementation

## Phase 4 — Decision engine implementation

- [ ] Create Godot project
- [ ] Implement state engine
- [ ] Implement event resolver
- [ ] Implement conditions/consequences
- [ ] Implement history and flags
- [ ] Implement delayed consequences
- [ ] Implement persistence/versioning
- [ ] Implement deterministic replay
- [ ] Implement ending resolver
- [ ] Validate engine against the real authored catalog

**Gate:** No “engine complete” claim until real authored content, not placeholder cards, runs through it successfully.

## Phase 5 — Full game/UI implementation

- [ ] Implement real event presentation
- [ ] Implement choice interaction and availability
- [ ] Implement resource/state presentation
- [ ] Implement character/relationship presentation
- [ ] Implement history/information presentation where designed
- [ ] Implement ending presentation
- [ ] Implement save/load UI
- [ ] Implement offline-first behavior
- [ ] Implement accessibility and touch UX
- [ ] Implement audio/haptics where appropriate

## Phase 6 — Localization

- [ ] Implement 20+ release locales
- [ ] Localize all authored content
- [ ] Missing-key validation
- [ ] Fallback validation
- [ ] Device-locale detection
- [ ] Persisted language selection
- [ ] RTL validation for Arabic/Hebrew
- [ ] Long-string/overflow UI tests
- [ ] Locale smoke tests across real gameplay

## Phase 7 — Verification, balance and polish

- [ ] Unit tests for state transitions
- [ ] Event contract tests
- [ ] Deterministic replay tests
- [ ] Save/load round-trip tests
- [ ] Delayed consequence tests
- [ ] Invalid-data rejection tests
- [ ] Headless gameplay smoke test
- [ ] Full-catalog content validation
- [ ] Campaign pacing/balance pass
- [ ] Resource economy balance
- [ ] Branch reachability analysis
- [ ] Ending reachability analysis
- [ ] Regression pass after content changes

## Phase 8 — Android integration and device QA

- [ ] Android project/build configuration
- [ ] Debug Android build
- [ ] Install/run on physical device
- [ ] Touch/UI verification
- [ ] Save/reload verification
- [ ] Offline verification
- [ ] Performance/memory sanity check
- [ ] Localization/device-locale verification
- [ ] Long-session stability check

## Phase 9 — APK LAST

**The APK is intentionally the final technical build step.**

- [ ] Final content freeze
- [ ] Final engine/UI verification
- [ ] Final automated test pass
- [ ] Final physical-device QA
- [ ] Final release configuration
- [ ] Build release APK for final acceptance/testing
- [ ] Verify the APK on a physical Android device

An APK must never be treated as proof that the game is complete. The game must already be complete and verified before this phase.

## Phase 10 — Production release

- [ ] Production AAB
- [ ] Production signing
- [ ] Store assets
- [ ] Store listing
- [ ] Privacy/data-safety review
- [ ] Final QA
- [ ] Owner publication actions

## Gate rule

No phase is considered complete because files exist. The implementation must pass the verification appropriate to that phase. Progress reports must be based on actual repository state and test evidence.

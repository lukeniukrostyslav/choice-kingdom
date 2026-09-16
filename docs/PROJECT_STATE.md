# Choice Kingdom — Project State

Status: ACTIVE — local runtime/application implementation and canonical-data closure.

## Current position

Choice Kingdom is an original premium offline-first Android decision-and-consequence game set in Avelune. The frozen production campaign scope is E01–E272; E273–E277 remains outside the production catalog.

Source-level canonicalization, producer/consumer contracts, delayed-consequence contracts, replay/meta contracts, ending precedence, save/load integrity, deterministic replay boundaries, and the application-facing `GameSession` seam have now been implemented and locally verified at their defined boundaries.

The production catalog projection is also implemented as a deterministic compiler from the authored markdown source. It covers all 272 in-scope events and 520 parsed choice rows without inventing gameplay semantics. The generated JSON is a build artifact, not a second source of truth.

## Major block status

| Block | Status | Completion | Boundary |
|---|---:|---:|---|
| Foundation / rules | CLOSED | 100% | project rules and canonical scope |
| Authored content | CLOSED at frozen catalog boundary | 90% | E01–E272 frozen; narrative scenario QA remains distinct |
| Canonical IDs / continuity | CLOSED | 100% | source/graph boundary |
| Producer / consumer QA | CLOSED | 100% source-level | canonical source contracts |
| Derived predicate contracts | CLOSED | 100% source-level | executable contract vocabulary |
| Delayed consequences | CLOSED | 100% runtime-verified | lifecycle, exactly-once and persistence boundaries |
| Replay / meta-state | CLOSED | 100% runtime-verified | export/import and replay boundary |
| Endings / precedence | CLOSED at executable boundary | 100% | deterministic resolver and precedence table |
| Reachability / causal graph | CLOSED at source level | 100% source-level | full gameplay scenario still required |
| Production data schema | PARTIAL / advancing | 50% | deterministic machine catalog projection implemented |
| Runtime state / persistence | CLOSED for current foundation | 100% | save/load, integrity and recovery |
| Decision Engine / application runtime | IN PROGRESS | 35% | authored choice execution + `GameSession`; full campaign semantics still open |
| UI / UX | NOT STARTED | 0% | Android presentation layer not implemented |
| Localization / RTL | FOUNDATION ONLY | 5% | requirements exist; full locale implementation open |
| Android implementation | NOT STARTED | 0% | no Android project/build verification yet |
| Android/device QA | HEADLESS ONLY | 15% | Python runtime verified; device QA open |
| APK / AAB | NOT STARTED | 0% | owner signing/build gate open |
| Store / release | NOT STARTED | 0% | production release gates open |

Percentages are engineering progress estimates by defined block; they are not a claim that the whole product is commercially release-ready.

## Latest local verification

- `python -m pytest -q` → **179 passed**.
- `python tools/validate_runtime_session_boundary.py` → **PASS**, E01–E272 catalog loaded, current event E01, turn 2, 47 available events.
- `python tools/validate_production_catalog.py` → **PASS**, 272 events, 520 choices, 13 no-choice nodes.
- Canonical graph/catalog, delayed lifecycle, ending precedence, replay, and scenario-source validators remain part of the regression surface.

## Current implementation boundary

`runtime/GameSession` is the application-facing seam for a future UI. It exposes presentation-neutral views, event selection, choice execution, save/load, recovery, replay export/import, delayed-consequence activation and ending resolution while delegating gameplay mutations to the canonical runtime.

The machine production catalog compiler projects authored choices into structured data containing event identity, trigger, prerequisites, choice effects, state-token mutations and explicit immediate unlocks. It deliberately does not infer delayed prose, missing predicates, ending qualification, or special-node behavior.

## Remaining high-value work

1. Expand runtime execution into exhaustive full-campaign scenario simulation using only authored semantics.
2. Classify and close the 13 no-choice/special nodes at the correct application boundary without inventing choice semantics.
3. Resolve the remaining runtime/data ambiguities surfaced by scenario simulation rather than hiding them behind generic fallback behavior.
4. Build the Android presentation layer on top of `GameSession`.
5. Implement localization and RTL behavior across the frozen catalog.
6. Add Android build configuration, automated Android checks and physical-device QA.
7. Produce signed APK/AAB and complete owner-controlled store/release gates.

## Rules

- Never manufacture gameplay semantics to make a scenario pass.
- The authored catalog remains the source of truth; generated machine data is derived.
- History markers are not current predicates unless an explicit contract says so.
- Delayed prose is not an immediate route unless an explicit immediate unlock is authored.
- E273–E277 cannot contribute production semantics while the frozen scope is E01–E272.
- Android/device and owner-controlled release gates must never be marked complete without real verification.

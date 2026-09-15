# Choice Kingdom — Scenario QA Worklog

Frozen scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**  
Purpose: durable handoff ledger so completed QA work is not repeated.

## Latest continuation update — 2026-09-15

### S20 — exhaustive E01–E272 source inventory green verification
- Triggered a fresh `Choice Kingdom Scenario Source Inventory` run on commit `d33325c39ed5cf4876c6d236357a42434c27d038` after the semantic inventory correction.
- GitHub Actions run `35024365701` completed **SUCCESS**.
- Verified `events=272 expected=272`; the frozen production denominator is complete in the machine inventory.
- Verified `unique_output_tokens=243`, `trigger_tokens=90`, `duplicate_output_tokens=3`, `semantic_writer_collisions=1`, `same_event_shared_writers=2`.
- Verified `undefined_consumers=59`, `undefined_predicate_consumers=8`, `predicate_cycles=0`.
- The generated inventory passed its shape assertions and was uploaded as the `scenario-source-inventory` artifact.
- The remaining undefined consumers/predicates are explicit source-QA findings and are not promoted into invented producers.

### S19 — composite predicate evidence-boundary repair
- Inspected the failed `Choice Kingdom Canonical Graph` attempt on commit `8a559295e4245c5972550f904681914790e220dd` and retrieved the exact failing step/log rather than inferring the cause.
- The composite source-closure validator had over-specific coalition evidence needles that did not match the authoritative wording.
- Reconciled the validator to the frozen source vocabulary: `cross-faction package`, `named participants`, and `positive mutual-concession outcome`.
- This is a validator correctness repair only; it does not promote runtime semantics, reachability, replay, or ending behavior.
- Commit: `91d68e8ce221598e7ad0d2f53d021f18d45d783f`.

### S18 — exhaustive-source inventory semantic correction
- Corrected `tools/compile_scenario_source_inventory.py` so the same canonical token emitted by both mutually-exclusive A/B choices is recorded as `same_event_shared_writers` instead of being treated as a contradiction by default.
- Added conservative clear/reset/invalidate/revoke/cancel recognition so explicit clears are not counted as positive producers.
- Preserved cross-event duplicate writers as `semantic_writer_collisions` review findings.
- Preserved predicate dependency cycle detection and undefined predicate-consumer reporting.
- Updated `.github/workflows/scenario-source-inventory.yml` to validate inventory schema `choice-kingdom-scenario-source-inventory-2`.
- Commits: `31e3373124a8d2f26f757cea24c510335dd1aba4` and `0f7e41819d422b919550dce93d783b2e57b51039`.

### S17 — exhaustive-source validator hardening
- Added machine detection for same-event contradictory writers and preserved legitimate multi-event duplicate writers as review findings.
- Repaired predicate contract parity normalization so `SOURCE-CLOSED` and the authoritative `SOURCE CONTRACT CLOSED` wording compare as the same frozen status.

### S16 — frozen scenario contract closure gate
- Added `tools/validate_scenario_contract_closure.py` and `.github/workflows/scenario-contract-closure.yml`.
- The gate validates the frozen E01–E272 denominator, explicit E273–E277 exclusion, authored event blocks, source-closed producer event/choice boundaries, delayed-candidate scope, hard-negative rules and predicate-cycle absence.
- GitHub Actions `Choice Kingdom Scenario Contract Closure` completed **SUCCESS** on the corrected validator.
- The gate explicitly reports runtime reachability, replay reachability, ending execution and Android as NOT_CLAIMED.

### S15 — E270 authoritative systemic-convergence closure
- Verified E270-A as the convergence step for `pred.systemic_explanation_verified` from the authoritative event catalog.
- Reconciled the producer registry and bounded closure audit so E270-A is consistently SOURCE-CLOSED at source level.
- Preserved runtime evidence aggregation, persistence, contradiction handling, fresh-run reachability and replay `meta.*` promotion as OPEN.

### S14 — machine predicate dependency validation
- Extended `tools/compile_scenario_source_inventory.py` to build a predicate-only dependency graph from authored trigger/output tokens.
- Added deterministic DFS cycle detection and explicit unresolved predicate-consumer reporting.
- Commit: `b8ca0599cbfc314353b98e504960c317e4e16be0`.

## Current QA position

The scenario is being driven toward 100% by evidence, not planned work. A block is promoted only when its source contract, machine checks, chronology/lifecycle requirements and required verification are actually closed. Runtime engine verification, fresh-run reachability and Android execution remain downstream gates and are not counted as closed by documentation alone.

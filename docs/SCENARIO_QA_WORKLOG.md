# Choice Kingdom — Scenario QA Worklog

Frozen scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**  
Purpose: durable handoff ledger so completed QA work is not repeated.

## Latest continuation update — 2026-09-15

### S19 — composite predicate evidence-boundary repair
- Inspected the failed `Choice Kingdom Canonical Graph` attempt on commit `8a559295e4245c5972550f904681914790e220dd` and retrieved the exact failing step/log rather than inferring the cause.
- The composite source-closure validator had over-specific coalition evidence needles (`Explicit cooperation package`, `identified participants`, `positive cooperation outcome`) that did not match the authoritative wording.
- Reconciled the validator to the frozen source vocabulary: `cross-faction package`, `named participants`, and `positive mutual-concession outcome`.
- This is a validator correctness repair only; it does not promote runtime semantics, reachability, replay, or ending behavior.
- Commit: `91d68e8ce221598e7ad0d2f53d021f18d45d783f`.
- Percentages remain frozen until fresh CI executes against the repaired commit.

### S18 — exhaustive-source inventory semantic correction
- Corrected `tools/compile_scenario_source_inventory.py` so the same canonical token emitted by both mutually-exclusive A/B choices is recorded as `same_event_shared_writers` instead of being treated as a contradiction by default.
- This directly removes the false-positive failure class observed in the prior exhaustive inventory run (including the E136/E144 cases already identified during diagnosis).
- Added conservative clear/reset/invalidate/revoke/cancel recognition: explicitly clearing a token is recorded under a choice's `clears` field and is not counted as a positive producer.
- Preserved cross-event duplicate writers as `semantic_writer_collisions` review findings.
- Preserved predicate dependency cycle detection and undefined predicate-consumer reporting.
- Updated `.github/workflows/scenario-source-inventory.yml` to validate inventory schema `choice-kingdom-scenario-source-inventory-2` and the new shared-writer/clearing fields.
- Commits: `31e3373124a8d2f26f757cea24c510335dd1aba4` and `0f7e41819d422b919550dce93d783b2e57b51039`.
- Fresh GitHub Actions verification was triggered by the changes; percentages remain frozen until the resulting exhaustive inventory and dependent gates are green.

### S17 — exhaustive-source validator hardening
- Added machine detection for same-event contradictory writers: one canonical token emitted by both mutually-exclusive A and B choices is now a source-QA failure rather than an undocumented ambiguity.
- Preserved legitimate multi-event duplicate writers as review findings; duplicate occurrence alone is not treated as contradiction.
- Added `contradictory_same_event_writers` to the compiled scenario inventory.
- Repaired the composite predicate source-closure gate after CI exposed an over-specific wording assertion; the correction is tied to the authoritative audit text.
- Repaired predicate contract parity normalization so `SOURCE-CLOSED` and the authoritative `SOURCE CONTRACT CLOSED` wording compare as the same frozen status.
- All changes remain subject to fresh CI verification; no scenario percentage is promoted merely because the validator was changed.

### S16 — frozen scenario contract closure gate
- Added `tools/validate_scenario_contract_closure.py` and `.github/workflows/scenario-contract-closure.yml`.
- The gate validates the frozen E01–E272 denominator, explicit E273–E277 exclusion, authored event blocks, source-closed producer event/choice boundaries, delayed-candidate scope, hard-negative rules and predicate-cycle absence.
- The first CI run intentionally failed because the validator assumed every source-level producer was backtick-tokenized. The failure exposed a real distinction between prose-level canonical facts and machine tokens.
- Corrected the validator to validate producer declarations at the authored event/choice boundary instead of inventing tokenization requirements.
- Normalized compact expansion choice syntax and allowed the graph-declared catalog duplicate set.
- GitHub Actions `Choice Kingdom Scenario Contract Closure` run #3 completed **SUCCESS** on commit `cf5938649cea372180d914d45e7c94046c39bf4c`.
- `Choice Kingdom Contract Readiness` and `Choice Kingdom Delayed Lifecycle Gate` also completed **SUCCESS** on the same commit.
- The gate explicitly reports runtime reachability, replay reachability, ending execution and Android as NOT_CLAIMED; no downstream work was counted as scenario closure.

### S15 — E270 authoritative systemic-convergence closure
- Re-read the authoritative `docs/EVENT_CATALOG_EXPANSION_211_270.md` source directly from its Git blob rather than relying on the graph artifact.
- Verified that E270-A explicitly records `systemic_explanation_convergence` and is the convergence step for `pred.systemic_explanation_verified`.
- Verified the prerequisite boundary: warehouse/financial, document/language and witness/organizational evidence families must already exist before E270-A; the `Amara and Toma both active` trigger is not evidence.
- Reconciled the producer registry and bounded closure audit so E270-A is now consistently marked SOURCE-CLOSED at source level.
- Preserved runtime evidence aggregation, persistence, contradiction handling, fresh-run reachability and replay `meta.*` promotion as OPEN.

### S14 — machine predicate dependency validation
- Extended `tools/compile_scenario_source_inventory.py` to build a predicate-only dependency graph from authored trigger/output tokens.
- Added deterministic DFS cycle detection and explicit unresolved predicate-consumer reporting.
- Commit: `b8ca0599cbfc314353b98e504960c317e4e16be0`.

## Current QA position

The scenario is being driven toward 100% by evidence, not planned work. A block is promoted only when its source contract, machine checks, chronology/lifecycle requirements and required verification are actually closed. Runtime engine verification, fresh-run reachability and Android execution remain downstream gates and are not counted as closed by documentation alone.

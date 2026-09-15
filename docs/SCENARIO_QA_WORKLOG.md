# Choice Kingdom — Scenario QA Worklog

Frozen scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**  
Purpose: durable handoff ledger so completed QA work is not repeated.

## Latest continuation update — 2026-09-15

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

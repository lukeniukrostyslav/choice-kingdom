# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game set in Avelune. Meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings and replayable paths.

## Release target
- Android-first premium one-time purchase, approximately €2.99–€4.99.
- No ads, no subscription, no mandatory backend for core gameplay.
- 20+ locales including RTL and long-string validation.
- Full authored campaign target: approximately 250–350+ meaningful nodes and 8–12 recognizable endings.

## Frozen authored scope
Production catalog is **E01–E272**. E273–E277 are expansion candidates and are excluded from production semantics, producer/consumer edges and reachability.

## Development order
**Content → canonical QA → machine-readable contracts → Decision Engine → UI → localization/tests → Android QA → APK → release.**

No mock/stub gameplay or premature production-readiness claims.

## Current phase
**S11 ending source closure is fully CI-verified GREEN; next phase is downstream Decision Engine implementation.** Authored checkpoint E01–E272. Source-level canonical graph, causal closure and S02 choice/state transition closure are green. S11 qualification, precedence and exact alias-boundary validation are green in the dedicated workflow.

## Current verified S01–S12 scorecard
- S01 **84%** — authored-event coverage structurally validated; semantic/gameplay reachability remains.
- S02 **100%** — authored choice → state/effect transition closure is source-level closed and CI-verified. Runtime Decision Engine execution, persistence and gameplay reachability remain downstream and are not included in this source-level percentage.
- S03 **100%** — source-level producer/consumer closure closed.
- S04 **100%** — production predicate contracts source-closed; explicit frozen exclusions are machine-gated.
- S05 **60%** — delayed consequence cancellation/supersession and full lifecycle semantics remain.
- S06 **65%** — replay/meta source contracts advanced; runtime replay execution/reset/isolation remain.
- S07 **100%** — source-level causal graph closed and CI-verified.
- S08 **100%** — source/producer QA closed and CI-verified.
- S09 **100%** — canonical graph source closure closed and CI-verified.
- S10 **83%** — delayed lifecycle source gate green; runtime persistence/cancellation semantics remain.
- S11 **100%** — final CI verification GREEN. Ending qualification, exact prerequisite/blocker sets, deterministic precedence and exact runtime-identifier alias boundary are implemented and verified by GitHub Actions workflow run #6 on commit `847502b` (run completed successfully in 9s; 1 warning only for actions/checkout Node.js runtime deprecation).
- S12 **100%** — scope/integrity gates closed.

**Scenario QA aggregate: S11 final CI verification GREEN; downstream runtime gates remain.**

## Latest verified work
### S02 — Choice → State Transition: SOURCE-CLOSED 100%
- Added `docs/S02_CHOICE_STATE_TRANSITION_CLOSURE_01.md` defining the frozen S02 source contract.
- Added `tools/validate_s02_choice_state_transition_closure.py` as an executable S02 closure gate.
- Added `.github/workflows/s02-choice-state-transition-closure.yml` for push/PR verification.
- Frozen source cardinality is **272 events / 259 normal / 13 special / 520 choice rows**.
- E51-C and E108-C are the confirmed authored additional alternatives.
- Base transition validator reports **semantic_gaps=0**, explicit transition payloads, distinct alternative signatures and authored event coverage for all 272 events.
- S02 closure gate additionally rejects numeric contextual sixth-resource patterns and confirms the frozen 520-row cardinality.
- GitHub Actions S02 run **35100082164**, job **104806986908**, head `3bf2d8f8bbb1fdb75ef2084e9d1ed25a9f598bdc`, completed **success** on 2026-09-16. The job log reports `S02_CHOICE_STATE_TRANSITION_CLOSURE: PASS`.
- This is source-level closure only. Runtime Decision Engine execution, save/load persistence, replay execution and gameplay reachability remain downstream gates.

### S11 — Ending / Replay QA: SOURCE-CLOSED 100%, CI GREEN
- Added `docs/MACHINE_ENDING_QUALIFICATION_CONTRACT_01.json` with exact machine-readable positive prerequisite and negative blocker sets for all seven ending families.
- Added `docs/MACHINE_ENDING_PRECEDENCE_TABLE_01.json` with deterministic evaluation order, explicit positive-ending priority data and pairwise precedence coverage.
- Preserved the conservative alias boundary: canonical identifiers remain `thread.border_crisis`, `thread.ivo_market`, `pred.coalition_cooperation` and `pred.systemic_explanation_verified`; stale aliases cannot manufacture prerequisites.
- Added `tools/validate_ending_source_closure.py` as the executable S11 source-closure gate.
- Added `tools/validate_ending_alias_boundary.py` exact identifier matching so canonical IDs containing an old alias as a prefix are not false positives.
- Added `.github/workflows/s11-ending-source-closure.yml` and wired both source closure and alias boundary validation into the same S11 gate.
- GitHub Actions manual workflow run **#6**, commit **847502b**, branch **main**, completed **Success** in **9s**. The run verified the S11 ending source closure and alias boundary gate. The only annotation is a non-blocking Node.js 20 deprecation warning for `actions/checkout@v4`.
- The source contract explicitly keeps runtime execution, fresh-run reachability and replay reachability false until those downstream systems exist; this is not hidden or counted as runtime completion.
- People's Charter remains explicitly dependent on runtime aggregation of `pred.final_charter_prerequisites`; Second Founder remains explicitly dependent on replay/meta transfer keys and runtime systemic convergence. These are tracked downstream blockers, not invented away.

## S11 remaining downstream gates
After source-level S11 closure, the following remain deliberately downstream and must not be counted as already implemented:
1. Decision Engine execution of the exact prerequisite/blocker contract;
2. runtime deterministic ending selection;
3. fresh-run gameplay reachability;
4. replay gameplay reachability and meta transfer execution;
5. save/load equivalence at ending resolution.

## Major downstream blocks
- Foundation / Rules: **95%**
- Authored Content: **90%**
- Canonical Event IDs / Continuity: **100%**
- Producer / Consumer QA: **100%**
- Derived Predicates / Machine Contracts: **90%**
- Delayed Consequences: **98%**
- Replay / Meta-state: **65%**
- Endings / precedence: **100% source-level + CI GREEN; runtime ending execution remains**
- Reachability / Causal Graph: **100% source-level**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. This deliberately does not treat source-level QA closure as runtime/gameplay completion.

## NEXT ACTION
**Begin downstream Decision Engine implementation from the frozen E01–E272 contracts. Do not reopen S02 or S11 source closure.**

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

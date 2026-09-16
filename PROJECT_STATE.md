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
**Narrative/content canonicalization and QA.** Authored checkpoint E01–E272. Production schema and Decision Engine remain blocked until canonical contracts and reachability are sufficiently closed.

## Scenario QA
Dedicated Scenario QA score remains approximately **92.7%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **60%** — all ten currently enumerated delayed source identities are now explicitly closed against the canonical graph; runtime scheduler/persistence/replay lifecycle remains open for all ten.
- S07 **80%**
- S08 **100%** — source-closure contract is now executable and CI-verified on the frozen E01–E272 scope. Runtime lifecycle, exact predicate aggregation, save/load and fresh-run reachability remain outside S08 source-closure scope.
- S09 **74%** — replay semantic classification is frozen and machine-validated; E131 is the only explicit previous-run producer candidate found in the inspected authored catalogs (`all_voices_heard`). E186 is only PARTIAL because it does not explicitly bind to that key; E247/E248 remain OPEN. Exact producer/key tuples remain unclosed.
- S10 **78%** — delayed source-choice identities plus structural graph reconciliation and lifecycle-boundary matrix verified; executable scheduler/runtime lifecycle remains open.
- S11 **65%** — E33/E34 source recovery, canonical integration, quarantine removal and ending-boundary mismatch are now closed at source level; exact deterministic ending prerequisites, tie-break/terminal order and runtime/fresh-run/replay reachability remain open.
- S12 **95%** — canonical graph CI gates replay semantic classification and replay producer provenance; all E01–E272 remain structurally reachable in the frozen design graph. Gameplay/runtime reachability remains unverified.

## Latest QA work
- **S08 executable source-closure gate:** added `tools/validate_s08_source_closure.py`. It validates frozen E01–E272 scope, excluded E273–E277, required explicit producer identities, source-closed composite predicates, and rejection of excluded events from production source contracts. Commit `34d8b30dfa15d4749306e756805e96c7aff4c4b1`.
- **S08 CI wiring:** added `.github/workflows/s08-source-closure.yml` to run the executable gate on pushes to `main` and on manual dispatch. Commit `53ba5994137930542fee8c5d08ee33963afa115f`.
- **S08 CI verification:** GitHub Actions run `35089513173` (`Choice Kingdom S08 Source Closure`, run #1) completed with **success**; job `s08-source-closure` and step `Validate S08 source closure` both completed successfully. This is the evidence for S08 source-closure completion.
- **Delayed source identity reconciliation:** updated `docs/SCENARIO_QA_DELAYED_LIFECYCLE_MATRIX_01.md` from the current canonical graph. E184 is explicitly E25-B / `secret_evidence_route`; E242 is explicitly E118-B / `estate_exception`; E245 is explicitly E20-A / `soldier_compensation`. Relative timing remains unconverted to invented absolute turns. Commit `1ba3f11a8b4962141a72cbc5b8be72715ceda867`.
- **Systemic predicate reconciliation:** current machine graph explicitly recognizes E270-A as the canonical producer of `pred.systemic_explanation_verified` via `systemic_explanation_convergence`; runtime verification remains false. The current graph also records E192-B/E192-A as the source/clear pair for `pred.food_stable`; runtime verification remains false.
- **Machine predicate dependency gate:** the predicate dependency audit remains conservative and does not promote consumers into producers. Open runtime/reachability gates are preserved.
- **S11.1 E33/E34 Canonical Closure 01:** added `docs/SCENARIO_QA_S11_1_E33_E34_CANONICAL_CLOSURE_01.md`. Verified authored-source recovery/integration, canonical production status, quarantine removal and final ending-boundary closure. Commit `1bb2e09f61d20d0d12d2b92708351b34bc5350bc`.
- **E33/E34 ending-boundary closure:** final repository commit `c335d2793e6f24452489de8eb9c4c45026c56b11` changed the canonical ending-boundary contract to explicitly treat E33/E34 as canonical production events and closed the source-level mismatch.
- **Replay Producer Provenance 01:** added `docs/SCENARIO_QA_REPLAY_PRODUCER_PROVENANCE_01.md`. Re-read the authoritative E131/E186/E247/E248 source boundary and froze the only explicit previous-run producer candidate found: E131 → `all_voices_heard`. E186 remains PARTIAL because its authored trigger does not explicitly name that key; E247/E248 remain OPEN. No inferred replay producer was promoted. Commit `18ee920025199d06685ce76376dee89f30e4b771`.
- **Machine Replay Producer Provenance 01:** added `docs/MACHINE_REPLAY_PRODUCER_PROVENANCE_01.json` and conservative machine statuses for E186/E247/E248. Commit `0ffc4b338afe3a9ed68f43d85d2f9614dab2ea38`.
- **Replay Producer Provenance Validator:** added `tools/validate_replay_producer_provenance.py`; it rejects invented producers and requires E186 to remain partial and E247/E248 open until authored bindings exist. Commit `d77049823df82f2252f56baedd35b5f8cc84c926`.
- **Canonical Graph CI wiring:** replay producer provenance is now a blocking canonical-graph stage and its machine report is uploaded with the QA artifact. Commit `bebf61e6557b33f3fa95db25fbd8880238909884`.
- **Replay Semantic Classification 01:** added `docs/SCENARIO_QA_REPLAY_SEMANTIC_CLASSIFICATION_01.md`. Audited the six previously grouped replay-sensitive nodes and separated genuine replay dependencies (E186/E247/E248) from ordinary authored state (E249/E250/E270). Commit `089e9a43ec15a484b76d28e1eaca2115a62086d4`.
- **Delayed Lifecycle Matrix 01:** added `docs/SCENARIO_QA_DELAYED_LIFECYCLE_MATRIX_01.md`, freezing source identity, timing language, lifecycle blockers and hard negatives for E181–E185 and E242–E246. The matrix is now reconciled with the current canonical graph; lifecycle remains open.
- **Structural Reachability Closure 01:** added `docs/SCENARIO_QA_STRUCTURAL_REACHABILITY_CLOSURE_01.md`, freezing 272/272 structurally reachable and 0 structurally unreachable while explicitly separating this from gameplay/fresh-run reachability. Commit `bc4d412dfb039391e80810e1695b96005ae4a7da`.
- **Canonical Graph CI run #158:** SUCCESS. All 18 canonical QA stages passed; this is not gameplay/runtime proof.

## Current canonical source status

### E33/E34 source boundary
- E33/E34 are canonical production events and are no longer quarantined.
- E33 `emergency_power` and `constitutional_limit`, and E34 `people_heard`, remain evidence/flags until explicit ending-consumer contracts exist.
- Boundary validation is case-sensitive against canonical event IDs and does not rely on graph-node presence alone.
- **Source-level boundary: CLOSED.**

### Replay producer provenance boundary
- E131 explicitly contains the authored previous-run trigger `all_voices_heard` and is the only explicit producer candidate found in the inspected catalogs.
- E186 is **PARTIAL_SOURCE_EVIDENCE**: its authored trigger allows an equivalent previous-run informational unlock but does not explicitly bind to `all_voices_heard`.
- E247 is **OPEN**: no exact producer/key tuple found.
- E248 is **OPEN**: no exact producer/key tuple found.
- The provenance contract is machine-validated and CI-gated.

### Delayed lifecycle boundary
- Source identities for E181–E185/E242–E246 are **10/10 source-closed** against the current canonical graph.
- Runtime lifecycle remains **0/10 closed**: exactly-once scheduling, due-turn semantics, cancellation/supersession, save/load persistence, replay isolation and fresh-run reachability remain unverified.

### Predicate dependency status
- `pred.guild_influence_strong`: OPEN.
- `pred.systemic_explanation_verified`: **SOURCE-CLOSED / RUNTIME OPEN**; canonical producer E270-A → `systemic_explanation_convergence`.
- `pred.coalition_cooperation`: **SOURCE-CLOSED / RUNTIME OPEN**; canonical producer E148-A with explicit cooperation/participant/blocker requirements.
- `pred.constitutional_prepared_strong`: **SOURCE-CLOSED / RUNTIME OPEN**; canonical multi-domain evidence contract.
- `pred.budget_reform`: source-closed; runtime qualification open.
- `pred.final_charter_prerequisites`: **SOURCE-CLOSED / RUNTIME OPEN**; E209 remains consumer-only and cannot manufacture the predicate.
- `pred.food_stable`: **SOURCE-CLOSED / RUNTIME OPEN**; canonical producer E192-B and clear E192-A.
- `pred.border_crisis`: source-closed lifecycle identity; runtime semantics open.

### Ending prerequisite status
- Steward: blockers/precedence/fresh-run reachability OPEN.
- Iron Crown: blockers/precedence/reachability OPEN.
- Golden Compact: blockers/precedence/reachability OPEN.
- People's Charter: **OPEN/BLOCKED** until its complete executable qualification contract and reachability are verified; E209 remains consumer-only.
- Broken Diadem: deterministic failure precedence OPEN.
- Quiet Throne: blocker precedence OPEN.
- Second Founder: **OPEN/BLOCKED** by replay meta producer/key plus fresh-run/replay separation and runtime convergence qualification.

## Major unresolved gates
- executable producer compilation for `pred.guild_influence_strong`;
- runtime qualification/invalidation for source-closed composite predicates;
- replay exact producer/key inventory for E186/E247/E248; E131/`all_voices_heard` is only a partial candidate and must not be silently promoted;
- delayed cancellation/supersession rules and runtime persistence/isolation;
- E185 later military-crisis resolution lifecycle;
- exact ending positive/negative prerequisite sets and deterministic tie-break/terminal order;
- gameplay/fresh-run reachability beyond structural graph reachability;
- replay reachability and cross-run isolation proof;
- machine graph ↔ authoritative catalog semantic equality beyond ID parity.

## Current honest progress
- Foundation / rules: **95%**
- Authored Content: **90%**
- Canonical Event IDs / Continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **99%**
- Delayed Consequences: **98%**
- Replay / Meta-state: **74%**
- Endings / precedence: **65%**
- Reachability / Causal Graph: **73%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA remains approximately **92.7%**; S08 source closure is now independently verified at 100%, while the composite Scenario QA score is retained until its scoring methodology is recalculated across all S01–S12 gates.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

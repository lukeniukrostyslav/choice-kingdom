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
Dedicated Scenario QA score is approximately **92.7%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **60%** — delayed E181–E185/E242–E246 source identities and hard semantic negatives are frozen in a dedicated lifecycle matrix; runtime scheduler/persistence/replay lifecycle remains open.
- S07 **80%**
- S08 **78%**
- S09 **74%** — replay semantic classification is frozen and machine-validated; a new source-provenance pass found E131 as the only explicit previous-run producer candidate in the inspected authored catalogs (`all_voices_heard`). E186 is only PARTIAL because it does not explicitly bind to that key; E247/E248 remain OPEN. Exact producer/key tuples remain unclosed.
- S10 **78%** — delayed source-choice identities plus structural graph reconciliation and lifecycle-boundary matrix verified; executable scheduler/runtime lifecycle remains open.
- S11 **60%** — ending prerequisite satisfiability screen plus conservative ending-precedence boundary contract; exact deterministic tie-break/terminal order remains open.
- S12 **95%** — canonical graph CI gates replay semantic classification and replay producer provenance; all E01–E272 remain structurally reachable in the frozen design graph. Gameplay/runtime reachability remains unverified.

## Latest QA work
- **Replay Producer Provenance 01:** added `docs/SCENARIO_QA_REPLAY_PRODUCER_PROVENANCE_01.md`. Re-read the authoritative E131/E186/E247/E248 source boundary and froze the only explicit previous-run producer candidate found: E131 → `all_voices_heard`. E186 remains PARTIAL because its authored trigger does not explicitly name that key; E247/E248 remain OPEN. No inferred replay producer was promoted. Commit `18ee920025199d06685ce76376dee89f30e4b771`.
- **Machine Replay Producer Provenance 01:** added `docs/MACHINE_REPLAY_PRODUCER_PROVENANCE_01.json` and conservative machine statuses for E186/E247/E248. Commit `0ffc4b338afe3a9ed68f43d85d2f9614dab2ea38`.
- **Replay Producer Provenance Validator:** added `tools/validate_replay_producer_provenance.py`; it rejects invented producers and requires E186 to remain partial and E247/E248 open until authored bindings exist. Commit `d77049823df82f2252f56baedd35b5f8cc84c926`.
- **Canonical Graph CI wiring:** replay producer provenance is now a blocking canonical-graph stage and its machine report is uploaded with the QA artifact. Commit `bebf61e6557b33f3fa95db25fbd8880238909884`.
- **Replay Semantic Classification 01:** added `docs/SCENARIO_QA_REPLAY_SEMANTIC_CLASSIFICATION_01.md`. Audited the six previously grouped replay-sensitive nodes and separated genuine replay dependencies (E186/E247/E248) from ordinary authored state (E249/E250/E270). Commit `089e9a43ec15a484b76d28e1eaca2115a62086d4`.
- **Delayed Lifecycle Matrix 01:** added `docs/SCENARIO_QA_DELAYED_LIFECYCLE_MATRIX_01.md`, freezing source identity, timing language, lifecycle blockers and hard negatives for E181–E185 and E242–E246. Commit `b9a2adcabea8c6705cbcb468dc04b3f7a9df529d`.
- **Structural Reachability Closure 01:** added `docs/SCENARIO_QA_STRUCTURAL_REACHABILITY_CLOSURE_01.md`, freezing 272/272 structurally reachable and 0 structurally unreachable while explicitly separating this from gameplay/fresh-run reachability. Commit `bc4d412dfb039391e80810e1695b96005ae4a7da`.
- **Canonical Graph CI run #158:** SUCCESS. All 18 canonical QA stages passed; this is not gameplay/runtime proof.

## Current canonical source status

### Replay producer provenance boundary
- E131 explicitly contains the authored previous-run trigger `all_voices_heard` and is the only explicit producer candidate found in the inspected catalogs.
- E186 is **PARTIAL_SOURCE_EVIDENCE**: its authored trigger allows an equivalent previous-run informational unlock but does not explicitly bind to `all_voices_heard`.
- E247 is **OPEN**: no exact producer/key tuple found.
- E248 is **OPEN**: no exact producer/key tuple found.
- The provenance contract is now machine-validated and CI-gated.

### Delayed lifecycle boundary
Runtime lifecycle is **0/10 closed** for E181–E185/E242–E246: exactly-once scheduling, due-turn semantics, cancellation/supersession, save/load persistence, replay isolation and fresh-run reachability remain unverified.

### Predicate dependency status
- `pred.guild_influence_strong`: OPEN.
- `pred.systemic_explanation_verified`: OPEN.
- `pred.coalition_cooperation`: OPEN.
- `pred.constitutional_prepared_strong`: OPEN.
- `pred.budget_reform`: source-closed; runtime qualification open.
- `pred.final_charter_prerequisites`: OPEN/BLOCKED; E209 remains consumer-only.
- `pred.food_stable`: OPEN/BLOCKED.
- `pred.border_crisis`: source-closed lifecycle identity; runtime semantics open.

### Ending prerequisite status
- Steward: blockers/precedence/fresh-run reachability OPEN.
- Iron Crown: blockers/precedence/reachability OPEN.
- Golden Compact: blockers/precedence/reachability OPEN.
- People's Charter: **OPEN/BLOCKED** because E209 is consumer-only.
- Broken Diadem: deterministic failure precedence OPEN.
- Quiet Throne: blocker precedence OPEN.
- Second Founder: **OPEN/BLOCKED** by replay meta producer/key plus systemic convergence and fresh-run/replay separation.

## Major unresolved gates
- authoritative source recovery or explicit authored correction for E33/E34 exact headings/effects;
- `pred.food_stable` vs `food_logistics_stabilized`;
- exact executable producer compilation for `pred.guild_influence_strong`;
- explicit convergence producer/key for `pred.systemic_explanation_verified`;
- runtime qualification/invalidation for `pred.coalition_cooperation`;
- executable ordering for `pred.constitutional_prepared_strong`;
- `pred.final_charter_prerequisites`;
- replay exact producer/key inventory for E186/E247/E248; E131/`all_voices_heard` is only a partial candidate and must not be silently promoted;
- delayed cancellation/supersession rules and runtime persistence/isolation;
- E184 producer closure and E185 crisis resolution;
- exact ending positive/negative prerequisite sets and deterministic tie-break/terminal order;
- gameplay/fresh-run reachability beyond structural graph reachability;
- machine graph ↔ authoritative catalog semantic equality beyond ID parity.

## Current honest progress
- Foundation / rules: **95%**
- Authored Content: **90%**
- Canonical Event IDs / Continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **99%**
- Delayed Consequences: **98%**
- Replay / Meta-state: **74%**
- Endings / precedence: **74%**
- Reachability / Causal Graph: **73%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA is now approximately **92.7%**; the increase reflects source-level replay producer provenance narrowing plus machine/CI enforcement, not runtime implementation.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

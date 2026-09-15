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
Dedicated Scenario QA score is approximately **92.5%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **60%** — delayed E181–E185/E242–E246 source identities and hard semantic negatives are frozen in a dedicated lifecycle matrix; runtime scheduler/persistence/replay lifecycle remains open.
- S07 **80%**
- S08 **78%**
- S09 **73%** — replay semantic classification is now frozen and machine-validated: E186/E247/E248 are genuinely replay-dependent; E249/E250/E270 are ordinary authored state and do not require replay meta producers. Exact producer/key tuples for the three true replay-dependent branches remain open.
- S10 **78%** — delayed source-choice identities plus structural graph reconciliation and lifecycle-boundary matrix verified; executable scheduler/runtime lifecycle remains open.
- S11 **60%** — ending prerequisite satisfiability screen plus conservative ending-precedence boundary contract; exact deterministic tie-break/terminal order remains open.
- S12 **95%** — canonical graph CI now also gates the replay semantic classification contract; all E01–E272 remain structurally reachable in the frozen design graph. Gameplay/runtime reachability remains unverified.

## Latest QA work
- **Replay Semantic Classification 01:** added `docs/SCENARIO_QA_REPLAY_SEMANTIC_CLASSIFICATION_01.md`. Audited the six previously grouped replay-sensitive nodes and separated genuine replay dependencies (E186/E247/E248) from ordinary authored state (E249/E250/E270). This removes a false-positive requirement for persistent `meta.*` producers on ordinary fresh-run nodes. Commit `089e9a43ec15a484b76d28e1eaca2115a62086d4`.
- **Machine Replay Semantic Classification 01:** added `docs/MACHINE_REPLAY_SEMANTIC_CLASSIFICATION_01.json` plus `tools/validate_replay_semantic_classification.py`. Commit `72c66c2d7848d3fc70e8afee76fce3617333fd3c`.
- **Canonical Graph CI wiring:** replay semantic classification is now a blocking canonical-graph stage and its machine report is uploaded with the QA artifact. Commit `393b025a874fc4a0c555ef52174eefa5ac22cc11`.
- **Replay Consumer Trigger Closure 01:** added `docs/SCENARIO_QA_REPLAY_CONSUMER_TRIGGER_CLOSURE_01.md`, freezing the authored consumer-side trigger boundary for E186/E247/E248/E249/E250/E270 without inventing persistent `meta.*` state. Commit `a3c1c198d54552ba43c00ba534aaf06c4571293f`.
- **Machine Replay Consumer Contract 01:** added `docs/MACHINE_REPLAY_CONSUMER_TRIGGER_CLOSURE_01.json` and `tools/validate_replay_consumer_trigger_closure.py`; the contract is now part of canonical-graph CI. Commit `149eee6d7c0060cf2c3e4563ebd4847b0186cf74`.
- **Delayed Lifecycle Matrix 01:** added `docs/SCENARIO_QA_DELAYED_LIFECYCLE_MATRIX_01.md`, freezing source identity, timing language, lifecycle blockers and hard negatives for E181–E185 and E242–E246. Commit `b9a2adcabea8c6705cbcb468dc04b3f7a9df529d`.
- **Structural Reachability Closure 01:** added `docs/SCENARIO_QA_STRUCTURAL_REACHABILITY_CLOSURE_01.md`, freezing the verified result of 272/272 structurally reachable and 0 structurally unreachable while explicitly separating this from gameplay/fresh-run reachability. Commit `bc4d412dfb039391e80810e1695b96005ae4a7da`.
- **Canonical delayed producer graph reconciliation:** added explicit source-backed producer edges for E09-B→E244, E17-A→E185, E18-B→E243, E20-A→E245 and E45-B→E181, while retaining already-established E117/E118/E136/E160 chains. Commit `07456d4f1d73f866fb00e6901899f54f13b3d112`.
- **Canonical Graph CI run #158:** SUCCESS. All 18 canonical QA stages passed, including delayed source-token validation, producer/consumer collision screen, ending prerequisite satisfiability, ending precedence boundary, predicate dependency audit, scenario-QA gate matrix and structural reachability. The machine structural reachability audit reports **272/272 structurally reachable and 0 structurally unreachable**; this is not gameplay/runtime proof.

## Current canonical source status

### Source-closed delayed producers
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E160-A → `winter_rent_ceiling` → E246
- E136-B → `history.guild_logistics_cooperation` → E194
- E20-A → `soldier_compensation` → E245
- E45-B → `infrastructure_concession` / toll-concession evidence → E181

### Delayed lifecycle boundary
The source-level matrix freezes E181–E185 and E242–E246 as separate lifecycle records. Source identity is closed for seven consumers, partial for E242, and open for E184. Runtime lifecycle is **0/10 closed**: exactly-once scheduling, due-turn semantics, cancellation/supersession, save/load persistence, replay isolation and fresh-run reachability remain intentionally unverified.

### Replay semantic boundary
Replay semantics are now split into two source-level classes:
- **Replay-dependent:** E186 previous-run branch, E247 second-run route, E248 replay callback. These require an explicit persistent `meta.*` producer/key contract.
- **Ordinary authored state:** E249 archive route, E250 related-clue threshold, E270 simultaneous Amara/Toma state. These do not require replay metadata and must remain valid on ordinary fresh-run routes.

The older six-node consumer-trigger contract remains in place as a conservative boundary record, while the new classification prevents E249/E250/E270 from being falsely treated as replay producers/consumers.

### Predicate dependency status
- `pred.guild_influence_strong`: OPEN; explicit multi-domain producer remains required.
- `pred.systemic_explanation_verified`: OPEN; explicit convergence producer/key remains required.
- `pred.coalition_cooperation`: OPEN; support evidence cannot silently become final qualification.
- `pred.constitutional_prepared_strong`: OPEN; component ordering remains unresolved.
- `pred.budget_reform`: source-closed from three component predicates; runtime qualification remains open.
- `pred.final_charter_prerequisites`: OPEN/BLOCKED; E209 remains consumer-only.
- `pred.food_stable`: OPEN/BLOCKED; no safe producer alias is promoted.
- `pred.border_crisis`: source-closed lifecycle identity; runtime exactly-once/re-entry semantics remain open.

### Ending prerequisite status
- Steward: positive route candidates exist; blockers/precedence/fresh-run reachability OPEN.
- Iron Crown: authority/security support candidates exist; blockers/precedence/reachability OPEN.
- Golden Compact: economic/faction legitimacy candidates exist; blockers/precedence/reachability OPEN.
- People's Charter: **OPEN/BLOCKED** because E209 is consumer-only for `pred.final_charter_prerequisites`.
- Broken Diadem: failure routes exist; deterministic failure precedence OPEN.
- Quiet Throne: narrative withdrawal/stability route exists; blocker precedence OPEN.
- Second Founder: **OPEN/BLOCKED** by replay meta producer/key plus systemic convergence and fresh-run/replay separation.

## Major unresolved gates
- authoritative source recovery or explicit authored correction for E33/E34 exact headings/effects;
- `pred.food_stable` vs `food_logistics_stabilized`;
- exact executable producer compilation for `pred.guild_influence_strong`;
- explicit convergence producer/key for `pred.systemic_explanation_verified`;
- runtime qualification/invalidation for `pred.coalition_cooperation`;
- executable ordering for `pred.constitutional_prepared_strong`;
- `pred.final_charter_prerequisites`;
- replay `meta.*` producer/key inventory for E186/E247/E248;
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
- Replay / Meta-state: **73%**
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

Overall project progress remains approximately **60%**. Scenario QA is now approximately **92.5%**; the increase reflects source-level replay semantic classification and CI enforcement, not runtime implementation.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

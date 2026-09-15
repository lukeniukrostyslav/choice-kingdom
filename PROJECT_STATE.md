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
Dedicated Scenario QA score is approximately **88%**. This is distinct from overall project completion and is not runtime/Android readiness.

### S01–S12 working indicators
- S01 **80%**
- S02 **70%**
- S03 **70%**
- S04 **70%**
- S05 **60%**
- S06 **55%**
- S07 **80%**
- S08 **78%**
- S09 **60%**
- S10 **72%**
- S11 **56%** — ending incoming-path / precedence review boundary materially tightened; source closure remains partial/open.
- S12 **86%** — source-level machine QA includes structural diagnostics, bounded catalog↔graph ID coverage, explicit contract readiness, delayed-lifecycle identity checks, predicate-contract parity, the E33/E34 recovery audit, delayed cancellation/supersession boundary work, bounded contract closure, composite-predicate source-closure enforcement, the foundation integrity audit, producer→graph reconciliation, delayed-edge closure matrix, and endgame incoming-path matrix. This remains source-level QA, not semantic equality or gameplay reachability proof.

## Latest QA work
- **Endgame Incoming-Path Matrix 01:** added `docs/SCENARIO_QA_ENDGAME_INCOMING_PATH_MATRIX_01.md`. It freezes the E261–E272 convergence spine and seven ending-family closure requirements, while explicitly keeping fresh-run reachability, precedence, final-charter prerequisites, coalition qualification and replay separation open. Commit `182d019f5aaa1bbc0233c48327969153b3f81a75`.
- **Delayed Edge Closure Matrix 01:** added `docs/SCENARIO_QA_DELAYED_EDGE_CLOSURE_MATRIX_01.md`. It turns E181–E185 and E242–E246 into a bounded source/timing/graph/lifecycle closure matrix, preserving E20-A as the exclusive E245 source and refusing to infer scheduler semantics. Commit `6d8a52ea4f69756837e2ffdd209f6adf38bd9f23`.
- **Producer→Graph Reconciliation Audit 01:** added `docs/SCENARIO_QA_PRODUCER_GRAPH_RECONCILIATION_AUDIT_01.md`. It reconciles source-closed producers with graph context without promoting graph edges to executable reachability. Commit `8798ad08d9a62aaa5944472e80184aeaad8a295b`.
- **Foundation Integrity Audit 01:** added `docs/SCENARIO_QA_FOUNDATION_INTEGRITY_AUDIT_01.md`. It freezes the current foundation invariants for event identity, producer/consumer separation, predicate separation, delayed-lifecycle boundaries, reachability, and the non-invention rule. It does not promote unresolved E33/E34 or other open contracts into production semantics. Commit `744db826ab43850b9abc5f69e35a66a9b49589c6`.
- **S12.63 composite-predicate source closure gate:** added `tools/audit_composite_predicate_source_closure.py` and wired it into `.github/workflows/canonical-graph.yml`. The gate verifies the frozen source evidence for guild influence, systemic explanation, coalition cooperation, constitutional preparation and final-charter prerequisites; it also enforces explicit non-promotion assertions and E273–E277 quarantine. It deliberately does not infer missing producers, runtime lifecycle, reachability or semantic equality. Commit `b073e02ebf7f48b97001658acb7e831c833f55a0`, workflow wiring commit `ae46d8c8344666c2cd8df191181f1b3cfede7efa`.
- **CI status for the composite gate:** GitHub Actions run `34998835831` for `ae46d8c8344666c2cd8df191181f1b3cfede7efa` was observed **QUEUED** at the time of the latest recorded check. Therefore no GREEN claim is made until a fresh completed run is verified.
- **S12.62 bounded contract-closure audit:** added `docs/SCENARIO_QA_CONTRACT_CLOSURE_AUDIT_02.md`. Audited `pred.food_stable`, `pred.systemic_explanation_verified`, `pred.final_charter_prerequisites`, and replay `meta.*` separation. The audit explicitly refuses to promote `food_logistics_stabilized` into `pred.food_stable`, keeps systemic convergence and final-charter convergence producers OPEN, and keeps ordinary history isolated from replay `meta.*` without an authored promotion contract. Commit `087e3c68fdaefa165031148456ab8b80698e4289`.
- **S12.61 delayed cancellation/supersession boundary audit:** added `docs/CANONICAL_DELAY_CANCELLATION_MATRIX_01.md`. It records the high-risk delayed consumers E181–E185 and E242–E246, separates source-identity closure from runtime lifecycle closure, and explicitly keeps missing cancellation/supersession/exactly-once semantics OPEN rather than inferring them. Commit `2a1861c80c8b3ca452255d3079cd5a56e55158df`.
- **S12.60 E33/E34 source-recovery audit:** added `docs/SCENARIO_QA_E33_E34_SOURCE_RECOVERY_01.md`. Current authoritative evidence confirms E33/E34 remain unresolved: the restored foundational catalog is explicitly E01–E32, while the Act V expansion starts at E35 with an `E33 resolved` trigger. Git-history inspection did not recover an authoritative E33/E34 body. No replacement semantics were invented. Commit `b579f821a726a1856e50473146518c329225385b`.
- **S12.59 delayed lifecycle identity expansion:** extended `tools/validate_delayed_lifecycle_gate.py` through E242–E246. The gate now checks source-backed candidate identities while preserving the distinction between identity closure and runtime scheduling/cancellation. The dedicated delayed lifecycle run `34992811608` completed **SUCCESS**.
- **S12.58 predicate contract parity correction:** corrected `tools/validate_predicate_contract_parity.py` so it validates exactly the seven predicates represented by the machine graph `composite_predicates` section. The corrected gate passed the dedicated `Choice Kingdom Contract Readiness` workflow on commit `c55eab2f400749c65a379b2b232728ff0cd2752b`.

## Current canonical source status

### Source-closed delayed producers
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E160-A → `winter_rent_ceiling` → E246
- E136-B → `history.guild_logistics_cooperation` → E194
- **E20-A → `soldier_compensation` → E245**

### Delayed lifecycle status
- E181: exact source says `5+ turns after a toll concession`; producer **E45-B is source-identified/closed at identity level**, while runtime scheduler anchor remains open.
- E182: E117-B `veteran_patronage`, `4+ turns later`; source identity closed, scheduler anchor open.
- E183: E118-B `estate_exception`, `5+ turns later`; source identity closed, scheduler anchor open.
- E184: `secret evidence route`, `4+ turns later`; no safe canonical producer alias, therefore OPEN.
- E185: E17-A `cheap_weapons` plus separate later military crisis; A prevents later failure, B schedules severe delayed loss; cancellation/supersession identity remains OPEN.
- E192-B `food_logistics_stabilized` is explicitly not `pred.food_stable`.
- E242: E118-B remains a candidate, but the authored trigger says any prior noble exception; identity is only PARTIAL and runtime selection/lifecycle remains open.
- E243: E18-B source identity closed; authored delay remains `5+ turns later`, runtime scheduling remains open.
- E244: E09-B source identity closed; authored delay remains `5+ turns later`, runtime scheduling remains open.
- E245: E20-A source identity CLOSED; authored timing remains `6+ turns later`; absolute due-turn/cancellation semantics are OPEN.
- E246: E160-A source identity CLOSED; authored timing remains relative; runtime scheduler and cancellation semantics are OPEN.

### S12.62 contract closure boundary
`docs/SCENARIO_QA_CONTRACT_CLOSURE_AUDIT_02.md` records bounded source evidence for food stability, systemic explanation, final charter convergence and replay metadata. None of these contracts is promoted to executable production semantics by inference.

### S12.63 composite predicate source boundary
`tools/audit_composite_predicate_source_closure.py` now freezes a machine-checkable evidence boundary for the remaining composite predicates. It verifies source evidence and hard non-promotion rules but intentionally leaves producer identity, runtime lifecycle, reachability and semantic equality unresolved where the authoritative source is unresolved.

### Foundation integrity boundary
`docs/SCENARIO_QA_FOUNDATION_INTEGRITY_AUDIT_01.md` freezes the current non-invention and separation rules before production-schema compilation. It is a foundation QA document, not an implementation-completion claim.

### Producer/graph reconciliation boundary
`docs/SCENARIO_QA_PRODUCER_GRAPH_RECONCILIATION_AUDIT_01.md` establishes that source-closed producer identity and graph context are compatible but not semantically equivalent. It identifies E45-B/E181, E18-B/E243, E09-B/E244, E20-A/E245 and related delayed routes as requiring exact source-choice, scheduler, lifecycle and reachability closure.

### Delayed edge closure boundary
`docs/SCENARIO_QA_DELAYED_EDGE_CLOSURE_MATRIX_01.md` records the executable tuple still missing for E181–E185 and E242–E246. No guessed due-turns or aliases were introduced; E184 remains producer-OPEN, E185 and E242 remain partial, and E245 remains exclusively E20-A.

### Endgame incoming-path boundary
`docs/SCENARIO_QA_ENDGAME_INCOMING_PATH_MATRIX_01.md` freezes the E261–E272 convergence spine and separates support evidence from final predicates. All seven ending families remain open until positive/negative conditions, precedence and fresh-run reachability are explicitly satisfiable; replay-required endings additionally need isolated replay evidence.

## Major unresolved gates
- authoritative source recovery or explicit authored correction for E33/E34 exact headings/effects;
- `pred.food_stable` vs `food_logistics_stabilized`;
- exact executable producer compilation for `pred.guild_influence_strong`;
- explicit convergence producer/key for `pred.systemic_explanation_verified`;
- runtime qualification/invalidation for `pred.coalition_cooperation`;
- executable ordering for `pred.constitutional_prepared_strong`;
- `pred.final_charter_prerequisites`;
- replay `meta.*` producer/key inventory;
- remaining delayed cancellation/supersession rules;
- E184 producer closure and E185 crisis resolution;
- ending incoming paths and deterministic precedence;
- exhaustive E01–E272 graph and fresh-run reachability;
- machine graph ↔ authoritative catalog semantic equality beyond ID parity.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **99%**
- Delayed Consequences: **97%**
- Replay / Meta-state: **65%**
- Endings / precedence: **70%**
- Reachability / Causal Graph: **64%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA is approximately **88%** and must not be conflated with overall project completion.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

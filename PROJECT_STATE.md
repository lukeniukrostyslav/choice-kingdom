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
- S12 **86%** — source-level machine QA includes structural diagnostics, bounded catalog↔graph ID coverage, explicit contract readiness, delayed-lifecycle identity checks, predicate-contract parity, the E33/E34 recovery audit, and the delayed cancellation/supersession boundary matrix. This remains source-level QA, not semantic equality or gameplay reachability proof.

## Latest QA work
- **S12.61 delayed cancellation/supersession boundary audit:** added `docs/CANONICAL_DELAY_CANCELLATION_MATRIX_01.md`. It records the high-risk delayed consumers E181–E185 and E242–E246, separates source-identity closure from runtime lifecycle closure, and explicitly keeps missing cancellation/supersession/exactly-once semantics OPEN rather than inferring them. Commit `2a1861c80c8b3ca452255d3079cd5a56e55158df`.
- **S12.60 E33/E34 source-recovery audit:** added `docs/SCENARIO_QA_E33_E34_SOURCE_RECOVERY_01.md`. Current authoritative evidence confirms E33/E34 remain unresolved: the restored foundational catalog is explicitly E01–E32, while the Act V expansion starts at E35 with an `E33 resolved` trigger. Git-history inspection did not recover an authoritative E33/E34 body. No replacement semantics were invented. Commit `b579f821a726a1856e50473146518c3292253852`.
- **S12.59 delayed lifecycle identity expansion:** extended `tools/validate_delayed_lifecycle_gate.py` through E242–E246. The gate now checks the source-backed candidate identities for the renewed exception, bridge callback, flexible-account callback, soldier compensation callback and rent-ceiling callback while preserving the distinction between identity closure and runtime scheduling/cancellation. Commit `312786982fae8b1b0a0f19b0b5a116cc2d04c3ac`. The resulting dedicated CI run `34992811608` completed **SUCCESS**.
- **S12.58 predicate contract parity correction:** corrected `tools/validate_predicate_contract_parity.py` so it validates exactly the seven predicates represented by the machine graph `composite_predicates` section. Source-closed producer predicates are no longer incorrectly treated as composite predicates. The corrected gate passed the dedicated `Choice Kingdom Contract Readiness` workflow on commit `c55eab2f400749c65a379b2b232728ff0cd2752b`. This is source-level parity, not gameplay semantic equality.
- **S12.57 predicate contract parity gate:** added `tools/validate_predicate_contract_parity.py` and `.github/workflows/predicate-contract-parity.yml`. The gate cross-checks frozen predicate statuses between `docs/CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md` and `docs/MACHINE_CANONICAL_GRAPH_01.json` without promoting OPEN/PARTIAL items or claiming gameplay equality. Commit `3c317988a9682767e22ad55e09bef9ba4f9305b8`; workflow commit `b5ca167da222a6d028edf93c693d73033c83394c`.

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
- E242: machine source candidate remains E118-B, but the authored trigger says any prior noble exception; identity is only PARTIAL and runtime selection/lifecycle remains open.
- E243: E18-B source identity closed; authored delay remains `5+ turns later`, so runtime scheduling remains open.
- E244: E09-B source identity closed; authored delay remains `5+ turns later`, so runtime scheduling remains open.
- E245: E20-A source identity CLOSED; authored timing remains `6+ turns later`; absolute due-turn/cancellation semantics are OPEN.
- E246: E160-A source identity CLOSED; authored timing remains relative; runtime scheduler and cancellation semantics are OPEN.

### S12.61 lifecycle boundary
`docs/CANONICAL_DELAY_CANCELLATION_MATRIX_01.md` is the current bounded audit for E181–E185/E242–E246. It closes no runtime lifecycle row by inference. Missing consequence identity, target, cancellation/supersession rule and exactly-once semantics remain explicit blockers.

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

## Next autonomous work
1. Verify fresh GitHub Actions after S12.61; do not claim GREEN until relevant new runs and jobs pass.
2. Continue source-backed producer compilation for guild influence, coalition cooperation and constitutional preparation where evidence permits.
3. Reconcile `pred.food_stable` vs `food_logistics_stabilized` without admitting expansion-only E273.
4. Complete systemic explanation convergence producer/key.
5. Complete `pred.final_charter_prerequisites`.
6. Inventory replay `meta.*` producer/key sources.
7. Continue E33/E34 exact canonical source recovery; if no authoritative source is recoverable, require explicit authored correction.
8. Determine ending incoming paths and deterministic precedence.
9. Build fresh-run and representative replay reachability models.
10. Prove catalog↔machine graph semantic equality or produce a bounded explicit delta beyond ID coverage.
11. Freeze production contracts only after machine validation and reachability gates pass.
12. Then Decision Engine → UI → localization → runtime/Android QA → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

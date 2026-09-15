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
- S12 **86%** — source-level machine QA includes structural diagnostics, bounded catalog↔graph ID coverage, explicit contract readiness, delayed-lifecycle identity checks, and predicate-contract parity. This remains source-level QA, not semantic equality or gameplay reachability proof.

## Latest QA work
- **S12.57 predicate contract parity gate:** added `tools/validate_predicate_contract_parity.py` and `.github/workflows/predicate-contract-parity.yml`. The gate cross-checks frozen predicate statuses between `docs/CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md` and `docs/MACHINE_CANONICAL_GRAPH_01.json` without promoting OPEN/PARTIAL items or claiming gameplay equality. Commit `3c317988a9682767e22ad55e09bef9ba4f9305b8`; workflow commit `b5ca167da222a6d028edf93c693d73033c83394c`.
- **S12.56 catalog↔graph parity correction:** the design graph is intentionally a partial causal map and does not enumerate every catalog event. The parity gate now treats catalog-only IDs as an explicit coverage delta rather than an integrity failure, while still failing on out-of-scope graph/catalog IDs and unexpected duplicate headings. It continues to refuse semantic-equality claims. Commit `24eb3e28b91c238b967d3eaeebf16fae74d8d7c1`.
- **S12.55 frozen event graph integrity gate:** added `tools/validate_event_graph_integrity.py` and wired it into `.github/workflows/canonical-graph.yml`. The first CI execution exposed that the design graph intentionally does not enumerate every catalog event: 235 graph nodes versus the frozen E01–E272 catalog, with 37 catalog IDs not represented as graph nodes in the validator's event-ID set. The gate was corrected to validate every graph-represented ID and every causal edge against the frozen scope, while reporting graph coverage rather than incorrectly treating non-node catalog events as integrity failures. Fix commit `cf0582b6b6fc514b8b40390cbab5f5e84d251e3e`.
- **S12.54 delayed lifecycle gate:** added `tools/validate_delayed_lifecycle_gate.py`. It validates the high-risk delayed identity boundary for E181/E182/E183/E184/E185/E245/E246, preserves source-identity vs runtime-lifecycle separation, and refuses invented absolute turns. Dedicated CI is `.github/workflows/delayed-lifecycle-gate.yml`; QA record: `docs/SCENARIO_QA_S12_54_DELAYED_LIFECYCLE_GATE_01.md`.
- **S12.53 machine contract readiness:** added `tools/validate_canonical_contract_readiness.py`. It validates frozen scope, required composite predicate inventory, explicit delayed lifecycle statuses and hard-negative presence, and emits `docs/MACHINE_CONTRACT_READINESS_01.json`. OPEN/PARTIAL contracts remain visible and never promote automatically.
- **S12.53 dedicated CI:** added `.github/workflows/canonical-contract-readiness.yml`, running the readiness validator on push/PR and uploading the readiness ledger.
- **S12.52 bounded catalog↔graph parity gate:** added `tools/validate_catalog_graph_parity.py` and `docs/MACHINE_CATALOG_GRAPH_PARITY_01.json` generation. The gate checks frozen E01–E272 catalog IDs against graph-chain IDs, rejects non-frozen/non-excluded graph IDs, unexpected catalog IDs and unexpected duplicate headings, while explicitly refusing to claim semantic equality from ID parity alone.

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

### Composite/source domains
- E142-A → `auditor_independence`
- E154-A → `crown_audited`
- E198-A → `legislative_budget_lock`
- **Budget reform source closure:** E142-A + E154-A + E198-A; E142-B/E154-B/E198-B are negative blockers; E155-A is same-domain downstream evidence and does not count independently.
- E271-A → active `pred.border_crisis`; E272-A/B clear it
- E32 → active `pred.transport_disruption`; E136-A/B clear it
- Guild influence: representation, tribunal, market/credit and qualified logistics domains are source-backed; at least two distinct domains required.
- Coalition cooperation: positive cooperation + participant identity + no unresolved collapse blocker; four-way bargain alone is rejected.
- Constitutional preparation: civic + institutional + factional + military source domains; at least three distinct domains required.

### Delayed lifecycle status
- E181: exact source says `5+ turns after a toll concession`; producer **E45-B is source-identified/closed at identity level**, while runtime scheduler anchor remains open.
- E182: E117-B `veteran_patronage`, `4+ turns later`; source identity closed, scheduler anchor open.
- E183: E118-B `estate_exception`, `5+ turns later`; source identity closed, scheduler anchor open.
- E184: `secret evidence route`, `4+ turns later`; no safe canonical producer alias, therefore OPEN.
- E185: E17-A `cheap_weapons` plus separate later military crisis; A prevents later failure, B schedules severe delayed loss; cancellation/supersession identity remains OPEN.
- E192-B `food_logistics_stabilized` is explicitly not `pred.food_stable`.

### E245
**Producer identity CLOSED:** E20-A `soldier_compensation`. Authored timing remains `6+ turns later`; absolute due-turn/cancellation semantics are OPEN.

### Systemic explanation
Three evidence families are frozen as distinct machine domains: warehouse/financial, document/language, and witness/organizational. The exact immutable convergence producer/key remains OPEN. E207 is consumer-only.

### Replay meta
E186/E247/E248/E270 remain OPEN for exact producer/key identity. Ordinary history/flags cannot cross the completed-run boundary without explicit authored promotion.

### E33/E34
Exact authored headings/effects/delayed semantics remain **QUARANTINED / UNRECOVERED** after renewed content and commit-history search. No invented replacement was admitted.

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
1. Verify fresh GitHub Actions after S12.57; do not claim GREEN until the relevant new runs and jobs pass.
2. Audit delayed cancellation/supersession matrix, especially E181/E184/E185/E245.
3. Close source-backed producer matrices for guild influence, coalition cooperation and constitutional preparation where evidence permits.
4. Reconcile `pred.food_stable` vs `food_logistics_stabilized` without admitting expansion-only E273.
5. Complete systemic explanation convergence producer/key.
6. Complete `pred.final_charter_prerequisites`.
7. Inventory replay `meta.*` producer/key sources.
8. Resolve E33/E34 exact canonical headings/effects/delayed semantics from authoritative evidence only.
9. Determine ending incoming paths and deterministic precedence.
10. Build fresh-run and representative replay reachability models.
11. Prove catalog↔machine graph semantic equality or produce a bounded explicit delta beyond ID coverage.
12. Freeze production contracts only after machine validation and reachability gates pass.
13. Then Decision Engine → UI → localization → runtime/Android QA → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

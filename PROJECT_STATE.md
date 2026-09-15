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
- S12 **83%** — source-level machine QA now includes deeper structural graph diagnostics (roots, structural reachability, sink candidates and weakly connected graph islands) in addition to graph validation, classification, producer/consumer compilation, conservative triage, qualification/lifecycle gates, ending/replay reconciliation, E245 synchronization, semantic candidate-boundary auditing, frozen production-scope enforcement, CI hardening, ending/replay incoming-path matrix, budget-reform reconciliation and delayed-source evidence reconciliation.

## Latest QA work
- **S12.51 structural graph audit hardening:** `tools/audit_structural_reachability.py` now emits sink-candidate and weakly-connected-component diagnostics alongside roots and structural reachability. These are explicitly source-review signals, not gameplay reachability or orphan proof. Commit: `8fb7b6dc48c225bc227b6209442ecf477f7df55f`.
- **S12.50** re-read authoritative E151–E210 delayed sources and tightened E181–E185 lifecycle boundaries. E182/E183 source identities are closed while relative scheduler anchors remain open; E184 has no safe producer alias; E185 separates source-closed `cheap_weapons` from the later crisis/supersession condition; E192 `food_logistics_stabilized` is explicitly kept distinct from blocked `pred.food_stable`. Commit: `83064432b59a2728c06c62df65966313defcf862`.
- **CI persistence hardening** updated canonical graph CI to upload all generated machine QA reports, including structural reachability, as a workflow artifact. Commit: `91461206694eecacf40a25492e130eb4ace0680d`.
- **S12.49** reconciled `pred.budget_reform` between the derived-predicate contract and canonical producer inventory. E142-A + E154-A + E198-A are now consistently source-closed; E142-B/E154-B/E198-B are negative blockers; E155-A is same-domain downstream evidence and cannot count twice. Runtime invalidation/reachability remain open. Commits: contract `286e03b8c4a5aad08b602432152766c831d2e6df`; QA record `3b7a9659738c15a99e10c991bb2c0d6123828189`.
- **S12.48** added structural graph reachability diagnostics and wired them into `.github/workflows/canonical-graph.yml`. Commit: `49a62e56ec3273ecad9911b1328568f2a6b032f8c`.
- **S12.47** added `docs/SCENARIO_QA_S12_47_ENDING_REPLAY_INCOMING_PRECEDENCE_MATRIX_01.md`, consolidating ending incoming-path, precedence and replay boundaries without inventing missing producers or `meta.*` keys. Commit: `7afbb8a2d3ba7097cfeac4e50416c45ec9bc174d`.
- **S12.46 CI hardening** repaired the scope-boundary workflow so it executes the same source-level graph/classification/matrix/triage prerequisites before `validate_scope_boundaries.py`. Commit: `e28ba4ef2f6a7a04689f26cc6c3ccaccf75c19ac`.
- Canonical Graph run **#51** (`34984719123`) was verified GREEN; all five source-level QA steps succeeded.
- Scope Boundary run **#14** (`34985532104`) was verified GREEN; canonical graph validation, classification, producer/consumer matrix, candidate triage and frozen-scope validation all succeeded.

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
- E181: exact source says `5+ turns after a toll concession`; producer candidate E45-B remains open for canonical closure.
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
- machine graph ↔ authoritative catalog semantic equality.

## Hard rules
- Consumer cannot manufacture prerequisite.
- `rel.ivo` ≠ strong guild influence.
- E197 cannot create constitutional preparedness.
- E209 cannot create final charter prerequisites.
- E210 is convergence-only.
- `four_way_bargain` ≠ coalition cooperation by itself.
- security alone ≠ border crisis.
- ordinary history/flag ≠ `meta.*`.
- E273–E277 excluded.
- generic compensation route cannot union E20/E125/E156 without explicit authored rule.
- E155-A cannot count as an independent second budget-reform domain.
- vague `later`/`N+ turns` cannot be converted into invented absolute turns.
- QA summaries cannot substitute for missing authoritative authored prose.
- `food_logistics_stabilized` ≠ `pred.food_stable`.

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **98%**
- Delayed Consequences: **96%**
- Replay / Meta-state: **65%**
- Endings / precedence: **70%**
- Reachability / Causal Graph: **63%**
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
1. Audit the 69 no-outbound and 54 unreferenced candidates against authoritative source text using the semantic-boundary queues.
2. Separate ROOT/SOURCE, ordinary producer, consumer-only, terminal/ending, qualification, delayed callback, replay-only and true orphan semantics.
3. Verify the latest canonical CI and uploaded machine reports; use structural output to prioritize candidate source review.
4. Complete delayed cancellation/supersession matrix, especially E181/E184/E185/E245.
5. Close source-backed producer matrices for guild influence, coalition cooperation and constitutional preparation where evidence permits.
6. Build fresh-run and representative replay reachability models with strict `meta.*` isolation.
7. Prove catalog↔machine graph semantic equality or produce a bounded, explicit delta.
8. Freeze production contracts only after machine validation and reachability gates pass.
9. Then Decision Engine → UI → localization → runtime/Android QA → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

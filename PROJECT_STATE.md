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
Dedicated Scenario QA score is approximately **87%**. This is distinct from overall project completion and is not runtime/Android readiness.

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
- S11 **55%**
- S12 **80%** — source-level machine QA through S12.42 is green for graph validation, classification, producer/consumer compilation, conservative triage, qualification/lifecycle gates, ending/replay reconciliation, E245 source synchronization, semantic candidate-boundary auditing, and frozen production-scope boundary enforcement. Semantic orphan/reachability closure remains open.

## Latest QA work
- **S12.42** added `tools/validate_scope_boundaries.py` plus `.github/workflows/scope-boundary.yml` and a QA report. The gate enforces E01–E272 production scope, excludes E273–E277, and pins ending/replay candidate queues to E265–E270 and E247–E250. It explicitly does not claim reachability or semantic orphan closure. The latest canonical graph workflow run #43 after the S12.42 commit was GREEN.
- **S12.41** added `tools/audit_candidate_semantic_boundary.py` and wired it into canonical graph CI. It deterministically separates source-missing, replay-only, delayed-callback, ending/terminal, root/source, consumer-only and isolated review queues without declaring semantic orphans.
- **S12.40** synchronized machine canonical graph with the already source-closed E245 producer identity: E20-A `soldier_compensation` only. E125-A and E156-A remain independent compensation outcomes. GitHub Actions canonical graph run #36 passed all four previous QA stages.
- **S12.39** reconciled ending producer gaps with replay meta closure. Ending resolver and replay transfer remain blocked by source-level gaps; no ordinary flag or degree heuristic was promoted to ending prerequisite or `meta.*` producer.
- **S12.38** normalized delayed lifecycle identity/timing/cancellation/supersession/save-load boundaries for E181–E185 and E242–E246 without inventing absolute turns from vague authored timing.
- **S12.37** freezes three independent evidence families for `pred.systemic_explanation_verified` and leaves the fourth immutable convergence producer/key explicitly OPEN; E207 remains consumer-only.
- **S12.36** added machine candidate triage and ending/replay reconciliation without declaring graph-degree candidates to be semantic orphans.
- **S12.35** added deterministic producer/consumer matrix compilation and CI enforcement.
- **S12.34** added deterministic machine graph node classification.
- **S12.33** closed E245 producer identity to E20-A `soldier_compensation`.
- **S12.32** verified the degree baseline: 270/272 discoverable catalog headings, 296 unique design edges, 69 no-outbound candidates, 15 inbound-only candidates and 54 unreferenced candidates. These are not reachability verdicts.
- **S12.31** verified the E33/E34 authoritative-source gap; no content was invented.
- **S12.30** added machine graph manifest, validator, CI workflow and QA report.

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
- E271-A → active `pred.border_crisis`; E272-A/B clear it
- E32 → active `pred.transport_disruption`; E136-A/B clear it

### E245
**Producer identity CLOSED:** E20-A `soldier_compensation`. Authored timing remains `6+ turns later`; absolute due-turn/cancellation semantics are OPEN.

### Systemic explanation
Three evidence families are frozen as distinct machine domains: warehouse/financial, document/language, and witness/organizational. The exact immutable convergence producer/key remains OPEN. E207 is consumer-only.

### Budget reform
Source identity is CLOSED: E142-A + E154-A + E198-A. Negative blockers E142-B/E154-B/E198-B are explicit. Runtime lifecycle/invalidation and reachability remain OPEN.

## Major unresolved gates
- authoritative source recovery for E33/E34 exact authored headings/effects;
- `pred.food_stable` vs `food_logistics_stabilized`;
- exact machine producer compilation for `pred.guild_influence_strong`;
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

## Current honest progress
- Foundation / rules: **95%**
- Authored content: **90%**
- Canonical Event IDs / continuity: **100%**
- Producer / Consumer QA: **99%**
- Derived Predicates / Machine Contracts: **98%**
- Delayed Consequences: **95%**
- Replay / Meta-state: **65%**
- Endings / precedence: **69%**
- Reachability / Causal Graph: **60%**
- Production Data Schema: **36%**
- Decision Engine: **0%**
- UI / UX: **0%**
- Localization 20+: **5%**
- Android Implementation: **0%**
- Runtime / Android QA: **0%**
- APK: **0%**
- Release: **0%**

Overall project progress remains approximately **60%**. Scenario QA is approximately **87%** and must not be conflated with overall project completion.

## Next autonomous work
1. Search repository history and remaining catalog/checkpoint sources for exact E33/E34 authored material; otherwise formally quarantine them as unrecovered.
2. Use the compiled producer/consumer matrix plus semantic-boundary queues to audit the 69 no-outbound candidates and 54 unreferenced candidates against authoritative source text.
3. Separate ROOT/SOURCE, ordinary producer, consumer-only, terminal/ending, qualification, delayed callback, replay-only and true orphan semantics.
4. Compile guild influence, coalition cooperation and constitutional preparation into exact producer/consumer matrices.
5. Complete delayed cancellation/supersession matrix, including E245/E185/E184.
6. Reconcile S11 endings and deterministic precedence.
7. Build fresh-run and representative replay reachability models with strict `meta.*` isolation.
8. Freeze production contracts only after machine validation and semantic catalog↔graph equality pass.
9. Then Decision Engine → UI → localization → runtime/Android QA → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

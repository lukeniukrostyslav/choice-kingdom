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
Dedicated Scenario QA score is now approximately **84%**. This is distinct from overall project completion and is not runtime/Android readiness.

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
- S12 **75%** — S12.30 machine graph gate + S12.31 E33/E34 source reconciliation + S12.32 machine node classification are now verified. Semantic orphan/reachability closure remains open.

## Latest QA work
- **S12.32** added `docs/SCENARIO_QA_S12_32_GRAPH_NODE_CLASSIFICATION_01.md` and extended the canonical graph validator. CI verified 270/272 catalog headings, 296 unique graph edges, 69 catalog events without outbound edges, 15 inbound-only candidates and 54 unreferenced catalog candidates. These are classification candidates, not orphan/reachability verdicts.
- **S12.31** added `docs/SCENARIO_QA_S12_31_E33_E34_SOURCE_RECONCILIATION_01.md`. It verified that `docs/EVENT_CATALOG.md` currently ends at E32, while S01 independently records E33/E34 only at QA-inventory level. Exact E33/E34 authored prose/effects/delayed semantics remain unrecovered; no content is invented.
- **S12.30** added `docs/MACHINE_CANONICAL_GRAPH_01.json`, `tools/validate_canonical_graph.py`, `.github/workflows/canonical-graph.yml` and `docs/SCENARIO_QA_S12_30_MACHINE_GRAPH_COMPILATION_01.md`. CI run reached a successful validation step after fixing parser semantics.
- S12.30 machine gate reports: 296 unique design-level event edges, 43 repeated documentation edges, 216 event nodes referenced by the design graph, 10 delayed consumer rows, 21 source-closed producer rows and 7 hard-negative rules.
- `E271` appears as an intentional post-catalog bridge in the E211–E270 source and as the lifecycle source in E271–E280; it is explicitly allowed in the machine contract rather than treated as a silent duplicate.
- The stale duplicate catalog source `EVENT_EXPANSION_071_110.md` was removed from the machine authoritative source set because `EVENT_CATALOG_EXPANSION_02.md` is the canonical E71–E110 source.
- **S12.29** reconciled `docs/CANONICAL_PRODUCER_INVENTORY_01.md`, commit `9c6589b22b53fb2c3a03014c89e826593bc97d57`.
- **S12.28** added `docs/SCENARIO_QA_S12_28_CANONICAL_INVENTORY_CONTRADICTION_AUDIT_01.md`, commit `e329d232df8d2573fb31a50d9f4a7115b1fa98f5`.
- **S12.27** added `docs/SCENARIO_QA_S12_27_DELAYED_LIFECYCLE_GATE_MATRIX_01.md`, commit `1bc4298a647dd51b56df6f0e2ce4a33e671367ac`.
- **S12.26** added `docs/SCENARIO_QA_S12_26_SYSTEMIC_EVIDENCE_IDENTITY_FREEZE_01.md`, commit `1a1dbd679a16570e4cbc766b0f711fe4a42fca67`.

## Current canonical source status

### Source-closed delayed producers
- E18-B → `public_bridge` → E243
- E09-B → `flexible_accounts` → E244
- E117-B → `veteran_patronage` → E182
- E118-B → `estate_exception` → E183/E242
- E17-A → `cheap_weapons` → E185
- E160-A → `winter_rent_ceiling` → E246
- E136-B → `history.guild_logistics_cooperation` → E194

### Composite/source domains
- E142-A → `auditor_independence`
- E154-A → `crown_audited`
- E198-A → `legislative_budget_lock`
- E271-A → active `pred.border_crisis`; E272-A/B clear it with exact recovered semantics
- E32 → active `pred.transport_disruption`; E136-A/B clear it

### E245 remains intentionally open
Candidates are E20-A `soldier_compensation`, E125-A `border_compensation`, and E156-A `requisition_compensation`. The authoritative source must prove a single source, explicit composite, or explicit source-family rule before any union is implemented.

### Systemic explanation
Evidence families are materially frozen, but exact immutable convergence producer/key remains OPEN. E207 is consumer-only and cannot manufacture convergence.

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
- E184 producer closure, E185 crisis resolution, E245 source disambiguation;
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

Overall project progress remains approximately **60%**. Scenario QA is approximately **84%** and must not be conflated with overall project completion.

## Next autonomous work
1. Search repository history and remaining catalog/checkpoint sources for exact E33/E34 authored material; otherwise formally quarantine them as unrecovered.
2. Compile the actual producer→consumer token matrix for the 69 graph candidates, starting with the 54 unreferenced catalog candidates and ending/epilogue nodes.
3. Separate ROOT/SOURCE, ordinary producer, consumer-only, terminal/ending, qualification, delayed callback, replay-only and true orphan semantics.
4. Close E245 only from authoritative evidence; never union compensation candidates implicitly.
5. Close systemic convergence identity or preserve it explicitly OPEN.
6. Compile guild influence, coalition cooperation and constitutional preparation into exact producer/consumer matrices.
7. Complete delayed cancellation/supersession matrix.
8. Reconcile S11 endings and deterministic precedence.
9. Build fresh-run and representative replay reachability models with strict `meta.*` isolation.
10. Freeze production contracts only after machine validation and semantic catalog↔graph equality pass.
11. Then Decision Engine → UI → localization → runtime/Android QA → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.
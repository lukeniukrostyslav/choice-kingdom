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
Dedicated Scenario QA score is now approximately **87%**. This is distinct from overall project completion and is not runtime/Android readiness.

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
- S12 **80%** — S12.30 machine graph gate, S12.31 E33/E34 source reconciliation, S12.32 degree classification, S12.33 E245 producer closure, S12.34 node classification, S12.35 producer/consumer compilation, S12.36 ending/replay reconciliation and S12.37 systemic-convergence machine gate are verified at source-QA level. Semantic orphan/reachability closure remains open.

## Latest QA work
- **S12.37** added `docs/SCENARIO_QA_S12_37_SYSTEMIC_CONVERGENCE_MACHINE_GATE_01.md`. It freezes three independent evidence families for `pred.systemic_explanation_verified`, makes the fourth convergence decision an explicit unresolved machine term, preserves E207 as consumer-only, and defines anti-double-counting rules.
- **S12.36** reconciled ending producer gaps with replay/meta closure and confirmed that ending/replay boundaries remain source-open; no degree heuristic or ordinary flag is promoted into an ending prerequisite or `meta.*` producer.
- **S12.35** added `tools/compile_producer_consumer_matrix.py` and wired it into canonical graph CI. It converts the working producer/consumer registry into deterministic derived QA data, rejects out-of-scope references, and preserves OPEN/PARTIAL rows without invented aliases.
- **S12.34** added `tools/classify_graph_nodes.py` and its QA report. It deterministically separates source-missing, replay, delayed-consumer, terminal/endgame, isolated, root, terminal/consumer and ordinary graph-node candidates without promoting degree heuristics to semantic truth.
- **S12.33** closed E245's producer identity to **E20-A `soldier_compensation`**. E125-A and E156-A remain independent compensation outcomes. Delayed timing/cancellation lifecycle remains open.
- **S12.32** verified 270/272 catalog headings, 296 unique graph edges, 69 catalog events without outbound edges, 15 inbound-only candidates and 54 unreferenced catalog candidates. These are classification candidates, not orphan/reachability verdicts.
- **S12.31** verified the E33/E34 authoritative-source gap; exact authored prose/effects/delayed semantics remain unrecovered and no content is invented.
- **S12.30** added the machine graph manifest, validator, CI workflow and QA report; the source-level validation gate passed after parser correction.

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
**Producer identity CLOSED:** E20-A `soldier_compensation`. The authored source uses `6+ turns later` and does not yet provide an absolute due turn/cancellation contract.

### Systemic explanation
Three evidence families are now frozen as distinct machine domains: warehouse/financial, document/language, and witness/organizational. The exact immutable convergence producer/key remains OPEN. E207 is consumer-only and cannot manufacture convergence. S12.37 defines the executable qualification boundary without inventing the missing producer.

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
- E184 producer closure, E185 crisis resolution;
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
2. Use the compiled producer/consumer matrix to audit the 69 no-outbound candidates and 54 unreferenced candidates against authoritative source text.
3. Separate ROOT/SOURCE, ordinary producer, consumer-only, terminal/ending, qualification, delayed callback, replay-only and true orphan semantics.
4. Compile guild influence, coalition cooperation and constitutional preparation into exact producer/consumer matrices.
5. Complete delayed cancellation/supersession matrix, including E245/E185/E184.
6. Reconcile S11 endings and deterministic precedence.
7. Build fresh-run and representative replay reachability models with strict `meta.*` isolation.
8. Freeze production contracts only after machine validation and semantic catalog↔graph equality pass.
9. Then Decision Engine → UI → localization → runtime/Android QA → APK → release.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

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
- S12 **87%** — source-level machine QA includes delayed source-token extraction and validation plus a producer/consumer collision screen and machine contract. This remains source-level QA, not semantic equality or gameplay reachability proof.

## Latest QA work
- **Producer/Consumer Collision Audit 01:** added `docs/SCENARIO_QA_PRODUCER_CONSUMER_COLLISION_AUDIT_01.md`. It screens delayed consumers for accidental producer widening, duplicate semantic merges and forbidden implicit predicate promotions. E245 remains exclusively E20-A; E242 remains partial; E184 remains open; E185 source identity and later crisis lifecycle remain separate. Commit `ce2f20b9664dd37b0c0f9ddc5362f5748b851a3b`.
- **Machine Producer/Consumer Collision Contract 01:** added `docs/MACHINE_PRODUCER_CONSUMER_COLLISION_01.json`. It freezes the collision outcomes and forbidden implicit promotions for machine validation. Commit `f221fd3a8649ac6cf91b70f27d0c5bc57d4ceef7`.
- **Producer/Consumer Collision Validator:** added `tools/validate_producer_consumer_collision.py`. It checks the frozen collision records and hard-negative E245 rule while explicitly refusing runtime/reachability claims. Commit `adf6796f78a665fb333556a78dc7db8cef0b454e`.
- **CI wiring:** `.github/workflows/canonical-graph.yml` now runs the producer/consumer collision validator and uploads `docs/MACHINE_PRODUCER_CONSUMER_COLLISION_VALIDATION_01.json`. Wiring commit `41286730fc5e071d4b9efe4d8959eee31fe5910e`.
- **Delayed Source Token Extraction 01:** added `docs/SCENARIO_QA_DELAYED_SOURCE_TOKEN_EXTRACTION_01.md`. The affected delayed consumers now have an explicit source event, source choice and canonical token record where authoritative evidence exists; E184 remains intentionally producer-open and E242 remains partial. This is source identity closure, not runtime lifecycle closure. Commit `2316821ebb3909d8d23a5b0ac17729805fce4894`.
- **Machine Delayed Source Tokens 01:** added `docs/MACHINE_DELAYED_SOURCE_TOKENS_01.json` as the structured contract for E181–E185 and E242–E246. It preserves hard negatives for E245, E242, E184, relative timing, E33/E34 quarantine and E273–E277 exclusion. Commit `c3534d5fb18749816b1aa9b9a5d7bf8a9bcea4e1`.
- **Delayed Source Token Validator:** added `tools/validate_delayed_source_tokens.py`. It checks exact event+choice+token+status identity against the machine producer inventory and explicitly refuses to claim runtime scheduling, cancellation, persistence or reachability. Commit `069e7555d410526e44386dab66fbc52e7f8a4462`.
- **Endgame Incoming-Path Matrix 01:** added `docs/SCENARIO_QA_ENDGAME_INCOMING_PATH_MATRIX_01.md`. It freezes the E261–E272 convergence spine and seven ending-family closure requirements, while explicitly keeping fresh-run reachability, precedence, final-charter prerequisites, coalition qualification and replay separation open. Commit `182d019f5aaa1bbc0233c48327969153b3f81a75`.
- **Delayed Edge Closure Matrix 01:** added `docs/SCENARIO_QA_DELAYED_EDGE_CLOSURE_MATRIX_01.md`. It turns E181–E185 and E242–E246 into a bounded source/timing/graph/lifecycle closure matrix, preserving E20-A as the exclusive E245 source and refusing to infer scheduler semantics. Commit `6d8a52ea4f69756837e2ffdd209f6adf38bd9f23`.
- **Producer→Graph Reconciliation Audit 01:** added `docs/SCENARIO_QA_PRODUCER_GRAPH_RECONCILIATION_AUDIT_01.md`. It reconciles source-closed producers with graph context without promoting graph edges to executable reachability. Commit `8798ad08d9a62aaa5944472e80184aeaad8a295b`.
- **Foundation Integrity Audit 01:** added `docs/SCENARIO_QA_FOUNDATION_INTEGRITY_AUDIT_01.md`. It freezes the current foundation invariants for event identity, producer/consumer separation, predicate separation, delayed-lifecycle boundaries, reachability, and the non-invention rule. It does not promote unresolved E33/E34 or other open contracts into production semantics. Commit `744db826ab43850b9abc5f69e35a66a9b49589c6`.

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
- E181: E45-B source identity closed; runtime scheduler anchor remains open.
- E182: E117-B source identity closed; scheduler anchor open.
- E183: E118-B source identity closed; scheduler anchor open.
- E184: no safe canonical producer alias; OPEN.
- E185: E17-A source identity closed; later military crisis lifecycle remains open.
- E242: E118-B candidate only; broader authored trigger keeps identity PARTIAL.
- E243: E18-B source identity closed; runtime scheduling remains open.
- E244: E09-B source identity closed; runtime scheduling remains open.
- E245: E20-A source identity CLOSED; timing/cancellation semantics remain OPEN.
- E246: E160-A source identity CLOSED; scheduler/cancellation semantics remain OPEN.

### Producer/consumer collision boundary
`docs/SCENARIO_QA_PRODUCER_CONSUMER_COLLISION_AUDIT_01.md` and `docs/MACHINE_PRODUCER_CONSUMER_COLLISION_01.json` now freeze the source-level collision rules. Consumer wording cannot widen a producer token; E245 cannot merge compensation sources; E185's source token cannot be treated as its later crisis lifecycle; and unresolved E184/E242 semantics remain open.

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
- Delayed Consequences: **98%**
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

Overall project progress remains approximately **60%**. Scenario QA remains approximately **88%**; S12 remains **87%**. These source-QA percentages must not be conflated with overall project completion or runtime/Android readiness.

## Honest progress rule
Documentation alone never makes implementation complete. Source edits count only when authoritative evidence is changed/re-read. No block is ready until its applicable verification passes.

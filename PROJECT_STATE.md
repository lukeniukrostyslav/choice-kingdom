# Choice Kingdom — Project State

## Product
Original premium offline-first decision-and-consequence mobile game. Working theme: ruling the kingdom of Avelune. The core appeal is meaningful choices, recurring characters, delayed consequences, hidden information, systemic event chains, multiple endings, and replayable paths.

## Full-release content target
This is a real full game, not a short card demo. The release target is approximately 250–350+ meaningful authored events/story nodes, with interconnected branches rather than filler repetition, plus approximately 8–12 recognizable endings and substantial replay variation.

## Commercial target
Android-first premium product, approximately €2.99–€4.99. No ads. No subscriptions. No mandatory backend or online service for core gameplay.

## Language requirement
Release must ship with localization from day one. Target is 20+ locales, including RTL and long-string validation.

## Engineering rule
No mock gameplay, fake completion, placeholder business logic presented as finished, or premature readiness claims. Every major block must progress through implementation, automated verification, runtime verification where applicable, and Android QA.

## Non-negotiable development order
Content and canonical QA come before production contracts, engine, UI, localization, automated/runtime verification and Android release.

## Current phase
**Narrative/content canonicalization and QA.** Authored checkpoint: E01–E272. Immediate goal: reconcile authored sources and causal graph into canonical production representation and prove internal consistency/reachability.

## Authored content checkpoints
- E01–E70: authored spine/endgame
- E71–E110: authored expansion
- E111–E150: authored expansion
- E151–E210: authored expansion
- E211–E270: authored expansion
- E271: border-crisis declaration producer bridge
- E272: border-crisis active-resolution producer bridge
- Total authored node identifiers: **E01–E272**.

## Narrative QA artifacts
- `docs/EVENT_CATALOG.md`
- `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`
- `docs/EVENT_EXPANSION_071_110.md`
- `docs/EVENT_CATALOG_EXPANSION_111_150.md`
- `docs/EVENT_CATALOG_EXPANSION_151_210.md`
- `docs/EVENT_CATALOG_EXPANSION_211_270.md`
- `docs/EVENT_CATALOG_EXPANSION_271_280.md`
- `docs/CONTENT_QA_MATRIX.md`
- `docs/CANONICAL_STATE_VOCABULARY.md`
- `docs/CANONICAL_DELAY_CONTRACT.md`
- `docs/CANONICALIZATION_BACKLOG.md`
- `docs/CANONICAL_PRODUCER_CONSUMER_REGISTRY_01.md`
- `docs/CANONICAL_CLOSURE_AUDIT_01.md`
- `docs/CANONICAL_CONTRACT_CLOSURE_PASS_01.md`
- `docs/CANONICAL_ROUTE_CONTRACT_01.md`
- `docs/CANONICAL_TRIGGER_NORMALIZATION_03.md`
- `docs/PRODUCER_AUDIT_E01_E070_01.md`
- `docs/REACHABILITY_PREAUDIT_E01_E070_01.md`
- `docs/PRODUCER_AUDIT_E071_E110_01.md`
- `docs/REACHABILITY_PREAUDIT_E071_E110_01.md`
- `docs/FULL_REACHABILITY_CLOSURE_MATRIX_01.md`
- `docs/PRODUCER_AUDIT_E111_E180_01.md`
- `docs/PRODUCER_AUDIT_E143_E150_01.md`
- `docs/PRODUCER_AUDIT_E181_E210_01.md`
- `docs/PRODUCER_AUDIT_E195_E210_02.md`
- `docs/PRODUCER_AUDIT_E211_E250_01.md`
- `docs/REACHABILITY_PREAUDIT_E211_E250_01.md`
- `docs/PRODUCER_AUDIT_E251_E272_01.md`
- `docs/LEGACY_SEMANTIC_AUDIT_01.md`
- `docs/SEMANTIC_COLLISION_RESOLUTION_01.md`
- `docs/LEGACY_SOURCE_COMPARISON_02.md`
- `docs/CANONICAL_SOURCE_CORRECTIONS_02.md`
- `docs/CANONICAL_DERIVED_PREDICATE_CONTRACT_01.md`
- `docs/CANONICAL_DELAY_INVENTORY_01.md`
- `docs/CANONICAL_EARLY_PREDICATE_PRODUCER_AUDIT_02.md`
- `docs/CANONICAL_LATE_PREDICATE_PRODUCER_AUDIT_03.md`
- `docs/CANONICAL_INDEPENDENT_SOURCE_FREEZE_01.md`
- `docs/AUTHORED_SOURCE_PATCHSET_01.md`
- `docs/AUTHORED_CATALOG_PATCH_APPLICATION_01.md`

## Current QA checkpoint
Producer inventories and static reachability pre-audits cover the authored scope E01–E272. The consolidated reachability matrix remains **OPEN** and is not a proof of runtime reachability.

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. In particular, E136-B now supplies the upstream `history.guild_logistics_cooperation` marker and E194 consumes that upstream marker rather than self-consuming the qualified predicate. This closes the identified authored E136/E194 circularity at source level; runtime predicate evaluation remains unimplemented.

The independent-source freeze is **PROVISIONAL/PARTIAL**. Guild-influence and constitutional-preparation candidate domains are identified, but exact full-catalog anti-double-counting reconciliation is still required before those contracts can be CLOSED.

The remaining high-risk producer gaps are still not allowed to be invented in the engine layer. Food stability, transport disruption, winter severity, market pressure, guild labor tension and high information pressure require explicit upstream authored semantics or an authoritative source correction before schema freeze. Budget reform, final-charter convergence, coalition participant/outcome qualification, delayed consequence identity/timing/cancellation, replay metadata and ending precedence also remain open.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until the canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `c18e8a4bf0680536a5261fb2c2ac398a0a4fea7a` — provisional independent predicate source freeze.
- `48961044360d596548c64da985d0ced7a82a8928` — late predicate producer audit E151–E272.
- `7a9d59848423ed948e0e94853ff5d3d2dea8dab6` — early predicate producer audit E01–E150.
- `b9b529ce9934391075dfb6d68800b99238bb103f` — broad canonical predicate producer audit.
- `15300a355da15e8a93c16d29c9bc5abc36f846b9` — canonical delayed consequence inventory.
- `e021f13a0e7e4726177b641112987d7bc1a8d017` — canonical derived predicate contract.
- `33d9cd1c9c7ffe2f88358994aa043a643d4a2a33` — E136/E194 source correction marked applied and verified.
- `d529ff3d0a44bcb4c7cce54d70103e0b78883686` — E136 guild-logistics history producer.
- `1d2ca828bf59cf5ddf56f152ec80957a05e3c280` — canonical producer bridge fixes E136–E210.
- `f84930589b1879045f799da818b5c7ec48954621` — producer registry refresh after E136/E144/E148 source closure.
- `52a057fada8bdd4e7c10c6955ec631667bba8dbf` — canonical route identity contract 01.
- `1c34444d4cba9e6e5d0e3614afd45ba5dbb75dfb` — consolidated E01–E272 reachability closure matrix.

## Next highest-value work
1. Resolve explicit upstream producers for food stability, transport disruption, winter severity, market pressure, guild labor tension and information pressure.
2. Complete exact independent guild-influence and constitutional-preparation source reconciliation.
3. Close coalition participant/outcome/blocker semantics.
4. Close constitutional preparation, budget reform and final-charter prerequisites without circularity.
5. Extract delayed consequence source identity, timing, cancellation/supersession and exactly-once contracts.
6. Freeze replay meta-state and ending qualification/precedence.
7. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation.
8. Freeze production data contracts.
9. Build the real static validator against the frozen schema.
10. Implement the actual Decision Engine and runtime.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

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

## Current QA checkpoint
Producer inventories and static reachability pre-audits now cover the authored scope E01–E272. A consolidated `docs/FULL_REACHABILITY_CLOSURE_MATRIX_01.md` records the cross-range causal closure state and global blockers.

A new `docs/CANONICAL_CONTRACT_CLOSURE_PASS_01.md` consolidates the remaining production-contract blockers and hard invariants. It confirms source-level closure for guild representation, guild logistics cooperation, and the border-crisis lifecycle while keeping food stability, transport disruption, winter severity, market pressure, guild labor tension, information pressure, route identity, evidence convergence, coalition semantics, constitutional preparation, final-charter prerequisites, delayed consequences, replay metadata and ending precedence explicitly open where source contracts are not yet sufficient.

The consolidated matrix remains **OPEN**, not a proof of runtime reachability. Reachability is static/pre-audit only. Production schema and runtime implementation remain blocked until canonical contracts are frozen. No validator has been introduced prematurely.

## Latest source-level commits
- `af9d308062ac57d7fbfb55e944a1f8a43c664c29` — canonical contract closure pass 01.
- `1c34444d4cba9e6e5d0e3614afd45ba5dbb75dfb` — consolidated E01–E272 reachability closure matrix.
- `422f22f38a7b92eee1e9b5f9aef03f2e470fb908` — producer/consumer audit E01–E70.
- `7e282f2a68a56ae84e1fccf973299db612fe7d20` — reachability pre-audit E01–E70.
- `b60427459ad04c9f9e09e09f7521731d1a381987` — reachability pre-audit E071–E110.
- `288b52384b0b544c9d1b7fbf5f49e11a9cf45b2d` — producer/consumer audit E071–E110.
- `21a5c782890733b94c50858ea7d0b7021379c941` — producer/consumer audit E251–E272.
- `2d22b3809e753928ca02d4c8b530ca4dc1e93d53` — reachability pre-audit E211–E250.
- `14d99ed300c32be7285bd599320a8198da5333fe` — producer/consumer audit E211–E250.

## Next highest-value work
1. Resolve exact upstream producers for food stability, transport disruption, winter severity, market pressure, guild labor tension and information pressure.
2. Freeze independent evidence/faction route identities and coalition cooperation semantics.
3. Close constitutional preparation, budget reform and final-charter prerequisites without circularity.
4. Extract delayed consequence source identity, timing, cancellation/supersession and exactly-once contracts.
5. Freeze replay meta-state and ending qualification/precedence.
6. Re-run complete E01–E272 contradiction/cycle/reachability reconciliation.
7. Freeze production data contracts.
8. Build the real static validator against the frozen schema.
9. Implement the actual Decision Engine and runtime.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

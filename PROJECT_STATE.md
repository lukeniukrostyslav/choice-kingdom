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
- `docs/CANONICAL_TRIGGER_NORMALIZATION_03.md`
- `docs/PRODUCER_AUDIT_E071_E110_01.md`
- `docs/REACHABILITY_PREAUDIT_E071_E110_01.md`
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
E071–E110 now have dedicated producer/consumer and static reachability pre-audits. The audit inventories durable authored outputs and flags semantic collisions, independent evidence-cardinality requirements, delayed callback identity, route-predicate ambiguity, transport/food predicate separation, forgery producer dependencies and coalition semantics.

E211–E250 have dedicated producer/consumer and reachability pre-audits. E251–E272 have an exact authored producer/consumer audit. E271-A is the canonical border-crisis declaration producer; E272-A/B are canonical resolution producers. The border lifecycle preserves historical declaration while clearing the active crisis predicate on resolution.

E095 remains distinct from E36/E226: `mara_independence` is an earlier resignation-letter consequence, while `mara_independent_mandate` is the later institutional mandate. E269 remains distinct from E55 as the late Ivo evidence handoff.

E136-B remains the upstream producer of `history.guild_logistics_cooperation`; E194 consumes that marker and later qualifies the logistics predicate through neutral inspectors and no unresolved immunity risk.

Reachability remains static/pre-audit only. Production schema and runtime implementation remain blocked until canonical contracts are frozen. No validator has been introduced prematurely.

## Latest source-level commits
- `b60427459ad04c9f9e09e09f7521731d1a381987` — reachability pre-audit E071–E110.
- `288b52384b0b544c9d1b7fbf5f49e11a9cf45b2d` — producer/consumer audit E071–E110.
- `21a5c782890733b94c50858ea7d0b7021379c941` — producer/consumer audit E251–E272.
- `2d22b3809e753928ca02d4c8b530ca4dc1e93d53` — reachability pre-audit E211–E250.
- `14d99ed300c32be7285bd599320a8198da5333fe` — producer/consumer audit E211–E250.
- `935a7512ce6dfc66e191c456f1d95e72a6ba0efa` — producer audit E143–E150.
- `9556b6be8e6641e0067ea183a3171ec0ccdbc8c9` — producer audit E111–E180 verified subset.
- `b0c9410aa2bd30fcc0e49793f8ab0dffde8ac5ee` — canonical trigger normalization pass 03.
- `d529ff3d0a44bcb4c7cce54d70103e0b78883686` — E136-B guild-logistics history marker.
- `c08379167f311c3ce674ace63475f3be839855a8` — E194 upstream history trigger correction.
- `249e01981cb97603aac669dc5686dab46731615d` — E226/E269 semantic distinctions.

## Next highest-value work
1. Complete exact producer/consumer inventory for E01–E070.
2. Reconcile trigger families and route predicates without collapsing ambiguous concepts.
3. Build the full reachability matrix from the frozen authored source set.
4. Resolve delayed/replay source identity and exactly-once semantics.
5. Verify semantic-collision downstream roles.
6. Resolve remaining open derived predicates/contracts.
7. Freeze production data contracts.
8. Build the real static validator, then implement the engine.

## Honest progress rule
Percentages represent actual state. Documentation alone does not make implementation complete. Source edits count only when the authoritative catalog is changed and re-read. No block may be called ready until its appropriate verification has passed.

## Project separation
`rulebreak8` is unrelated to this project and must not be modified or used as a source of readiness metrics.

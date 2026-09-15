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

## Current QA checkpoint
Producer inventories and static reachability pre-audits cover the authored scope E01–E272. The consolidated reachability matrix remains **OPEN** and is not a proof of runtime reachability.

The authored producer bridge corrections for E136/E144/E148 and the later E151–E210 trigger/semantic corrections have been applied to the authoritative catalogs and re-read. E136-B supplies the upstream `history.guild_logistics_cooperation` marker and E194 consumes that upstream marker rather than self-consuming the qualified predicate. E29-A/B now explicitly establish `pred.winter_severe` for the current severe-winter cycle while retaining `history.winter_severity_declared`; this closes the winter-severity producer gap at source level. Runtime predicate evaluation and deterministic cycle expiry remain unimplemented.

The independent-source freeze is **PROVISIONAL/PARTIAL**. Guild-influence and constitutional-preparation candidate domains are identified, but exact full-catalog anti-double-counting reconciliation is still required before those contracts can be CLOSED.

The remaining high-risk producer gaps are still not allowed to be invented in the engine layer. Food stability, active transport disruption, market pressure, guild labor tension and high information pressure require explicit upstream authored semantics or authoritative source corrections before schema freeze. Budget reform, final-charter convergence, coalition participant/outcome qualification, delayed consequence identity/timing/cancellation, replay metadata and ending precedence also remain open.

No validator has been introduced prematurely. Production schema and runtime implementation remain blocked until the canonical contracts are frozen and the complete catalog reconciliation passes.

## Latest source-level commits
- `e1b10d4fefaea7415fff3ec57f6fcd1be1a2eac1` — producer registry updated for verified winter-severity source.
- `4968322515da7e754f6d7802e225494d23b44f3e` — derived predicate contract updated for winter-severity closure.
- `5d315aa71610f5c7582bf03a292dc86439a8b72e` — E29-A/B explicit winter-severity producer source correction.
- `047d45174c8cbfd62057b1784225ab7b9fd3e7d5` — project state synchronized after source-level QA pass.
- `c18e8a4bf0680536a5261fb2c2ac398a0a4fea7a` — provisional independent predicate source freeze.
- `48961044360d596548c64da985d0ced7a82a8928` — late predicate producer audit E151–E272.
- `7a9d59848423ed948e0e94853ff5d3d2dea8dab6` — early predicate producer audit E01–E150.
- `b9b529ce9934391075dfb6d68800b99238bb103f` — broad canonical predicate producer audit.
- `15300a355da15e8a93c16d29c9bc5abc36f846b9` — canonical delayed consequence inventory.
- `e021f13a0e7e4726177b641112987d7bc1a8d017` — canonical derived predicate contract.
- `1d2ca828bf59cf5ddf56f152ec80957a05e3c280` — canonical producer bridge fixes E136–E210.
- `52a057fada8bdd4e7c10c6955ec631667bba8dbf` — canonical route identity contract 01.
- `1c34444d4cba9e6e5d0e3614afd45ba5dbb75dfb` — consolidated E01–E272 reachability closure matrix.

## Next highest-value work
1. Resolve explicit upstream producers for food stability, active transport disruption, market pressure, guild labor tension and information pressure.
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

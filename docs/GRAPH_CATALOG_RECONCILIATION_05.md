# Choice Kingdom — Graph ↔ Catalog Reconciliation 05

Date: 2026-09-15
Status: SOURCE-LEVEL QA / E151–E270

## Purpose

This pass records the latest source reconciliation of the authored E151–E270 layer against the canonical producer/consumer rules. It is not runtime verification and does not authorize engine implementation.

## E151–E180

- E151 produces `clerks_oath_public` / `clerks_oath_private`; these are durable authored markers, but neither is itself equivalent to `pred.institutional_reform`.
- E153 produces archive-access markers from `office_network_mapped`; this supports `thread.archive` but does not independently prove the archive ending prerequisite.
- E154 depends on `auditor_independence` plus high institutional trust. The exact canonical institutional-trust predicate remains unresolved.
- E157 uses food shortage as a trigger. This must compile to an existing food-pressure predicate or explicit authored marker; no sixth resource may be introduced.
- E160 uses severe winter. `pred.winter_severe` remains a derived/canonicalization item, not a raw prose condition.
- E161-A is a verified producer of `history.house_assembly`.
- E165–E169 provide guild/market evidence, but `pred.guild_influence_strong` and `pred.guild_logistics_cooperation` still lack frozen canonical producers.
- E170–E172 must preserve the separation between veteran route, border tension and military/security state.
- E173 explicitly distinguishes `army readiness low` from `security low`.
- E174–E176 provide Amara route evidence but relationship value alone must not activate `thread.amara_civic`.
- E177–E180 provide Toma/information evidence but `rel.toma` alone must not satisfy `pred.information_pressure_high`.

## E181–E200

- E181–E185 are delayed callbacks and require exact-once scheduling semantics in the eventual engine.
- E186 contains replay-exclusive information. Any cross-run transfer must remain under `meta.*` until an explicit transfer contract exists.
- E187–E190 add investigation evidence. Evidence count is not sufficient for `pred.systemic_explanation_verified`; distinct evidence IDs and a convergence rule are required.
- E192 exposes both road pressure and a food-stability consequence. `pred.transport_disruption` and `pred.food_stable` therefore need durable definitions.
- E193 requires low gold + high security; both thresholds remain pending canonical freeze.
- E194 consumes guild cooperation without a frozen canonical producer for `pred.guild_logistics_cooperation`.
- E195 consumes border escalation without a frozen producer for `pred.border_crisis`.
- E196–E199 provide constitutional preparation evidence, but `pred.constitutional_prepared_strong` remains an open compound predicate.
- E200 remains blocked by the unresolved `pred.guild_influence_strong` contract.

## E201–E210

- `history.cross_faction_package` is verified upstream through E148-A.
- `history.house_assembly` is verified upstream through E161-A.
- `hist.guild_representation` remains OPEN: no exact canonical producer has been verified despite the E144 guild-seat concept.
- Military constitutional route must remain distinct from generic military/security state.
- Amara and Toma route activation rules remain partial.
- Systemic evidence + coalition cooperation require authored convergence, not raw event counts.
- Final constitutional phase and final charter prerequisites remain open and must not depend circularly on E210.
- E210 is a convergence node only and must never resolve an ending by itself.

## E211–E260

The downstream catalog contains numerous compound prose triggers: institutional reform, market oversight, food pressure, veteran route, Amara route, information pressure, procurement clues, public accountability, guild logistics, border route, succession route, budget reform and archive reform. These are not yet equivalent to canonical runtime predicates unless a verified producer contract exists.

Evidence-cardinality triggers such as `at least two procurement clues` and `three or more related clues` require immutable evidence IDs and deterministic counting. Graph adjacency does not satisfy this requirement.

Replay callbacks must not leak `meta.*` into current-run state without an explicit transfer rule.

## E261–E270

E261 introduces the legacy-style `four_way_bargain` marker. Under the current canonical contract this is not an accepted production predicate alias. Production logic must use the explicit coalition/history vocabulary, particularly `pred.coalition_cooperation` and `history.cross_faction_package` where appropriate.

E262–E264 deepen coalition/endgame convergence and require explicit durable state if later qualification depends on them.

E265–E270 are ending-qualification inputs. They must consume deterministic canonical predicates/history and must not infer an ending from the last event, a relationship value, a vague route name, or an undocumented graph edge.

## Confirmed closure blockers

1. `hist.guild_representation` — no verified exact producer.
2. `pred.food_stable` — no frozen durable representation.
3. `pred.transport_disruption` — producer/persistence semantics open.
4. `pred.border_crisis` — escalation producer open.
5. `pred.guild_logistics_cooperation` — exact combination/producer open.
6. `pred.guild_influence_strong` — exact combination/producer open.
7. `pred.systemic_explanation_verified` — evidence-ID convergence open.
8. `pred.coalition_cooperation` — distinct cooperation semantics open.
9. `pred.constitutional_prepared_strong` — exact acyclic combination open.
10. `pred.final_charter_prerequisites` — exact prerequisite set open.

## Result

**E151–E270 source reconciliation: 70% closure.**

The important change is not a fabricated readiness increase: the remaining gaps are now explicitly bounded. The correct next engineering artifact is a static validator for the future canonical catalog that rejects duplicate IDs, missing event references, unresolved trigger keys, stale aliases, illegal legacy IDs and circular ending dependencies.

Production schema remains BLOCKED until these producer contracts are closed.

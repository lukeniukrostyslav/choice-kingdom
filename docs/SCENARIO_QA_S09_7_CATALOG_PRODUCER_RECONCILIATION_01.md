# Choice Kingdom — Scenario QA S09.7 Catalog Producer Reconciliation 01

Date: 2026-09-15
Status: **PARTIAL PASS — SOURCE-LEVEL QA**
Frozen production scope: **E01–E272**
Expansion candidates: **E273–E277 excluded**

## Purpose

Reconcile the authoritative authored catalogs and existing range producer audits against the S09.6 composite-predicate surface. This pass is intentionally source-level: it records exact authored evidence and unresolved canonical boundaries without promoting prose triggers into runtime facts.

## Coverage reconciled

The following source surfaces were re-read/reconciled:

- `EVENT_CATALOG.md` — E01–E70;
- `PRODUCER_AUDIT_E071_E110_01.md` — E71–E110;
- `EVENT_CATALOG_EXPANSION_111_150.md` and `PRODUCER_AUDIT_E111_E180_01.md` — E111–E180;
- `EVENT_CATALOG_EXPANSION_151_210.md` and `PRODUCER_AUDIT_E181_E210_01.md` — E151–E210;
- `EVENT_CATALOG_EXPANSION_211_270.md` and `PRODUCER_AUDIT_E211_E250_01.md` — E211–E250;
- `PRODUCER_AUDIT_E251_E272_01.md` and `EVENT_CATALOG_EXPANSION_271_280.md` — E251–E272.

The catalog itself remains the authoritative narrative source; producer audits are verification registers, not substitutes for authored meaning.

## Confirmed source-backed producer families

### Early / institutional
- E09-B → `flexible_accounts`.
- E17-A → cheap-weapons durability source for the later E185 crisis callback.
- E18-B → `public_bridge`.
- E28-A/B → `royal_forgery_proven` / `forgery_leverage`.
- E29-A/B → `pred.winter_severe` for the current winter cycle.
- E32 → `pred.transport_disruption` active producer.
- E33 → emergency-power / constitutional-limit outputs.
- E36 outputs remain distinct from E95/E226 semantic variants.
- E45 → `public_infrastructure_trust` / `infrastructure_concession`.
- E49 → guild political representation evidence; E144-A/B normalizes the durable marker to `history.guild_representation`.
- E50 → `people_charter_endorsed`.
- E55 and E269 remain distinct evidence events.
- E60 → replay/endgame history surface, not an automatic meta transfer.

### E111–E180
- E117-B → `veteran_patronage`.
- E118-B → `estate_exception`.
- E124/A → public trade standards.
- E125-A → `border_compensation`.
- E126-A → `river_compact`.
- E136-A/B → transport recovery/clear; E136-B additionally establishes `history.guild_logistics_cooperation`.
- E139-A/B → frontier-warning infrastructure only; neither declares border crisis.
- E142-A → `auditor_independence`.
- E144-A/B → `history.guild_representation`.
- E148-A → `history.cross_faction_package` and `coalition_candidate_package`.
- E154-A → `crown_audited`; E155-A → `full_crown_audit_published`.
- E160-A → `winter_rent_ceiling`.
- E161-A → `history.house_assembly`.
- E165-A → `official_credit_disclosure`.
- E166-A → `audited_monopoly`.
- E168-A → `guild_tribunal_independent`.
- E172-A → `civilian_signal_authority`.

### E181–E250
- E181–E185 durable outputs are source-closed, but delayed identities remain open.
- E192-A/B produce `food_logistics_unstable` / `food_logistics_stabilized`; neither is `pred.food_stable`.
- E194 consumes upstream `history.guild_logistics_cooperation`; A supplies `guild_neutral_inspectors`, B supplies `guild_logistics_immunity_risk`. The qualified predicate requires upstream evidence plus neutral inspection and no unresolved blocker.
- E195 consumes active `pred.border_crisis`; it is not a producer.
- E197 consumes `pred.constitutional_prepared_strong`; it is not a producer.
- E200 consumes `pred.guild_influence_strong`; it is not a producer.
- E201 consumes `pred.coalition_cooperation`; it is not a producer.
- E207 consumes systemic-explanation and coalition predicates; it is convergence/consumer-only.
- E209 consumes `pred.final_charter_prerequisites`; it is consumer-only.
- E210 is convergence-only.
- E242–E246 are delayed callbacks whose source choice, due turn, cancellation and exactly-once identity remain open.
- E247/E248 are replay-oriented and require explicit `meta.*` gating.

### E251–E272
- E253/E255 consume active border crisis; they do not manufacture it.
- E261-A produces `four_way_bargain`, which is not itself qualified coalition cooperation.
- E264/E265 require an explicit coalition trust/collapse lifecycle.
- E269 is a late evidence handoff and must remain distinct from E55.
- E270-A/B produce distinct `dual_witness_account` / `single_witness_account` convergence outputs and must not be silently equated with E207 systemic convergence.
- E271-A is the only source-closed active border-crisis declaration producer.
- E272-A/B are the source-closed active border-crisis resolution producers; historical declaration remains queryable while the active predicate clears.

## Duplicate / contradictory writer findings

### Confirmed safe duplicates
- `history.guild_representation`: E144-A and E144-B intentionally write the same immutable institutional marker.
- `history.guild_logistics_cooperation`: E136-B is the upstream source; E194-A may repeat the historical marker but cannot self-qualify the downstream predicate.

### Semantic collision requiring contract handling
- `mara_independent_mandate` appears in early and late institutional-stress contexts (E36/E226). It must be treated as the same fact only if the canonical fact identity explicitly permits multi-producer writes; otherwise an outcome identity split is required. No semantic invention is permitted.
- E95 `mara_independence` remains distinct from `mara_independent_mandate`.
- E55 guild evidence remains distinct from E269 late commercial evidence.

### Contradictory/unsafe promotion patterns rejected
- E197/E200/E207/E209 cannot manufacture their own prerequisites.
- E192 cannot create `pred.food_stable` by alias.
- E136 recovery cannot become active transport disruption without an explicit reactivation producer.
- E261 `four_way_bargain` cannot automatically become qualified coalition cooperation.
- E271-B warning resolution cannot satisfy active `pred.border_crisis`.
- E273–E277 contribute no production edges.

## Composite predicate reconciliation

| Predicate | Current source position | Gate |
|---|---|---|
| `pred.guild_influence_strong` | representation + tribunal + commercial/market + qualified logistics domains identified; exact minimum formula/open source set unresolved | PARTIAL |
| `pred.constitutional_prepared_strong` | civic + audit + house + military domains identified; exact source/negative semantics unresolved | PARTIAL |
| `pred.systemic_explanation_verified` | four evidence families identified; exact immutable source IDs unresolved | PARTIAL |
| `pred.coalition_cooperation` | package + participant identity + positive outcome + no collapse blocker required | PARTIAL |
| `pred.budget_reform` | E142-A/E154-A/E198-A layers identified; exact E198 role and ordering unresolved | OPEN |
| `pred.final_charter_prerequisites` | convergence shape established; complete upstream set unresolved | BLOCKED |
| `pred.food_stable` | no E01–E272 source-closed producer | BLOCKED |
| `pred.transport_disruption` | E32 active source, E136-A/B clear/recovery | PARTIAL |

## Cycle audit disposition

No new source-backed cycle is authorized by this pass. The known self-satisfaction classes remain hard rejects. A true exhaustive transitive-cycle proof still requires normalized token-level dependency data rather than prose review.

## Gate result

**S09.7 PARTIAL PASS.**

Source coverage is materially reconciled across the frozen E01–E272 campaign. The remaining blockers are now concentrated in composite predicate formulas, route identities, delayed/replay identity, and machine-level graph proof rather than missing basic authored-output inventories.

**S09 remains 60%. Scenario QA remains 65%.** No percentage increase is claimed from documentation-only reconciliation.

## Next

1. Freeze the remaining composite formulas and exact producer sets only where authored evidence supports them.
2. Build the normalized token-level dependency graph from the reconciled source inventory.
3. Run duplicate-writer, contradictory-writer, undefined producer/consumer and transitive-cycle checks.
4. Reconcile S10 delayed source/target identities against the same producer chronology.
5. Then advance S11 ending/replay closure and S12 fresh-run reachability.

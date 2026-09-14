# Choice Kingdom — Canonical Trigger Gap Register 02

Date: 2026-09-15
Status: **SOURCE-LEVEL QA WORKING REGISTER — NOT ENGINE INPUT**
Scope: E191–E210, with cross-campaign canonical namespace rules.

## Purpose

Convert the open prose triggers identified by `PRODUCER_CONSUMER_INVENTORY_05` into explicit closure tasks. This register does **not** invent runtime producers. A trigger becomes production-eligible only after an authored source choice/history/thread producer is verified.

## Canonical normalization table

| Prose trigger | Canonical target | Closure requirement |
|---|---|---|
| unresolved warehouse/market crisis | `pred.warehouse_market_crisis` | explicit warehouse loss + market-pressure composition; source producers required |
| road pressure | `pred.transport_disruption` | unique producer and persistence/clear rule |
| food stability | `pred.food_stable` / authored food-stability marker | must remain derived/history state, never numeric resource |
| low gold | `pred.gold_low` | numeric threshold already defined provisionally; source/balance verification pending |
| high security | `pred.security_high` | exact threshold must be frozen from balance/source review |
| guild cooperation | `pred.guild_logistics_cooperation` + `thread.ivo_market` where appropriate | route/history producer required |
| border escalation | `pred.border_crisis` + `thread.border_crisis` | escalation producer must be explicit; security alone cannot satisfy it |
| late constitutional route | `thread.constitutional_late` | exact producer + timing contract required |
| strong constitutional preparation | `pred.constitutional_prepared_strong` | minimum authored combination required; no self-derived predicate |
| audit reform | `pred.budget_reform` or `pred.institutional_reform` | semantic split must be determined from authored effects |
| military constitutional route | `thread.military_constitutional` | must be distinct from `rel.rowan` and generic military events |
| strong guild influence | `pred.guild_influence_strong` | explicit route/history evidence; never `rel.ivo` alone |
| cross_faction_package | `hist.cross_faction_package` + `thread.coalition` | unique producer and constituent route set required |
| house_assembly | `hist.house_assembly` | E161 candidate producer; verify exact output and downstream use |
| guild representation | `hist.guild_representation` | unique producer required |
| military route | `thread.rowan_security` or dedicated military constitutional thread | choose based on authored semantics; relationship is insufficient |
| Amara civic route | `thread.amara_civic` | route activation producer must be canonicalized |
| Toma information route | `thread.toma_information` | route activation producer must be canonicalized |
| verified systemic evidence | `pred.systemic_explanation_verified` | explicit convergence, not generic clue count |
| cross-faction cooperation | `pred.coalition_cooperation` | canonical coalition producer required |
| final constitutional phase | `thread.final_constitutional_phase` | deterministic activation rule required |
| final charter prerequisites | `pred.final_charter_prerequisites` | explicit prerequisite set required |
| final constitutional convergence | `thread.endgame_convergence` | convergence node only; must not become second ending resolver |

## Rules locked by this register

1. A canonical name is not a producer.
2. A graph edge is not a producer unless the source choice establishes durable state consumed by the target.
3. Relationships do not substitute for route/thread state.
4. Contextual pressures remain derived predicates or durable authored markers; they are not added as new numeric resources.
5. E210 remains a convergence node feeding E265–E270; it cannot independently resolve an ending.
6. `pred.systemic_explanation_verified` requires authored convergence and cannot be inferred from a raw evidence count.
7. Four-faction qualification uses distinct route identities, not repeated events.
8. Replay-only state must remain under explicit `meta.*` and may enter ordinary predicates only through a documented transfer rule.

## Immediate audit queue

- Enumerate exact producers for every OPEN row above.
- Verify E161 as the `house_assembly` producer and record its durable output.
- Enumerate all E01–E270 producers for food, winter, border, guild, evidence and constitutional routes.
- Freeze thresholds only after source evidence and balance review.
- Re-run graph/catalog reconciliation after producer closure.
- Re-run reachability after canonicalization; do not treat this register as proof of reachability.

## Gate

**Result: OPEN.** This register materially reduces naming ambiguity but does not close producer reachability or runtime readiness.

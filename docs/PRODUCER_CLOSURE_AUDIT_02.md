# Choice Kingdom — Producer Closure Audit 02

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — NOT PRODUCTION SCHEMA**
Scope: E111–E210, with explicit distinction between verified producer, semantic candidate and unresolved prose trigger.

## Purpose

Cross-check the open trigger families from E191–E210 against actual authored choices in the E111–E210 source catalog. The goal is to stop treating similar wording as proof of causality.

## Verified durable producers

| Canonical state candidate | Source | Authored output | Status |
|---|---|---|---|
| `hist.house_assembly` | E161-A | `house_assembly` | VERIFIED producer |
| `thread.ivo_market` / guild route evidence | E124-A/B, E140-A/B, E148 | `public_trade_standards`, `guild_trade_standards`, `trade_risk_insurance`, `market_self_adjustment`, `cross_faction_package` | PARTIAL route family; needs canonical route activation rule |
| `thread.amara_civic` | E120-A/B, E139-A/B | `lanterns_protected`, `lanterns_dependent`, `frontier_lantern_network`, `frontier_military_watch` | PARTIAL; route identity must be separated from relationship value |
| `thread.toma_information` | E121-A/B, E131, E135 | `protected_sources`, `named_sources_only`, `emergency_language_compared`, `conflicting_testimony_recorded` | PARTIAL; information route requires explicit activation/continuation marker |
| `thread.mara_audit` | E116-A/B, E142-A/B | `auditor_apprentices`, `palace_auditors`, `auditor_independence`, `auditor_crown_control` | PARTIAL; audit route and institutional reform still distinct |
| `thread.rowan_security` | E117-A/B, E137-A/B, E143 | `veteran_patronage`, `veterans_examined`, `civilian_watch_training`, `royal_patrol_expansion` | PARTIAL; military constitutional route must not equal generic security route |
| `thread.seris_houses` | E118-A/B, E127-A/B, E161-A/B | `equal_estate_law`, `estate_exception`, `privilege_renewed_again`, `house_assembly`, `crown_confiscation_power` | PARTIAL; noble route identity can be established but exact qualification remains open |
| `thread.ledger_investigation` | E132, E133, E134, E135 | `redaction_reconstructed`, `form_pattern_tested`, `office_network_mapped`, `conflicting_testimony_recorded` | PARTIAL; evidence cardinality still requires distinct evidence IDs |
| `thread.archive` | E131-A, E134-A/B | `emergency_language_compared`, `office_network_mapped`, `map_destroyed_after_copy` | PARTIAL; archive access and archive reform must remain separate |
| `thread.coalition` | E146, E148, E149 | `six_signatures_public/private`, `cross_faction_package`, `selective_coalition`, `coalition_cost_public/hidden` | PARTIAL → strong producer family, but coalition qualification set is not frozen |

## Open triggers with candidate evidence but no production closure

### 1. `road pressure`

E136 produces `roads_public_labor` or `roads_guild_contract` after `winter severity`. This is related to transport disruption, but it does **not** prove that either choice should set a persistent `pred.transport_disruption` state. E192 therefore remains OPEN until a canonical producer/effect is explicitly authored.

### 2. `food stability`

E138 produces `grain_recount`; E167 produces `import_risk_guarantee`; E192 consumes food pressure/stability. These are useful ingredients, but none alone proves a stable food predicate. Keep food as a derived condition or explicit authored marker, never a sixth resource.

### 3. `guild cooperation`

E140-A produces `trade_risk_insurance`; E148-A produces `cross_faction_package`; E124 creates public/guild trade standards. These support a guild/economic route but are not identical semantics. A dedicated canonical cooperation marker still needs to be chosen from authored intent.

### 4. `border escalation`

E139 can produce `frontier_military_watch`; E170–E172 and later border events provide pressure. These are border/security producers, but escalation into `pred.border_crisis` must require an explicit escalation event/state. Generic security remains insufficient.

### 5. `late constitutional route`

E146/E148/E150 are late constitutional preparation/convergence candidates. They do not currently define one stable route identity by themselves. A route activation rule and timing window are still needed.

### 6. `strong constitutional preparation`

E142, E145, E146, E148, E150 provide possible ingredients. No single source defines the required minimum combination. This predicate remains OPEN.

### 7. `audit reform`

E142 creates auditor independence, E154/E155 concern Crown audit, while E198 consumes `audit reform`. This proves semantic neighborhood but not equivalence. Budget reform must remain separate from generic institutional/document audit until the authored chain is explicitly defined.

### 8. `military constitutional route`

E143 is military budget; E199 directly produces `army_constitution_oath` or `army_crown_oath`. E199 is the strongest concrete producer candidate for the constitutional military route. The route should not be derived from `rel.rowan` or generic security.

### 9. `strong guild influence`

E165, E168, E169 and E194 provide merchant/guild choices and relationship effects. None should be converted automatically into `pred.guild_influence_strong`. A route/history combination is required.

### 10. `cross_faction_package`

**VERIFIED producer:** E148-A explicitly creates `cross_faction_package`. This closes producer identity, but downstream qualification still requires exact coalition membership/validity semantics.

### 11. `guild representation`

E144 consumes `guild_political_representation`, but the fetched source does not show a unique producer for that exact marker. Therefore this remains OPEN despite the clear semantic route.

### 12. `military route`

E171 consumes military route; E199 creates an explicit constitutional military choice. Generic Rowan relationship and generic military events are insufficient. Candidate canonical family: `thread.rowan_security` plus separate `thread.military_constitutional` for constitutional qualification.

### 13. `verified systemic evidence`

E132/E133/E134/E135 create multiple evidence developments. They provide a source base, but `pred.systemic_explanation_verified` must require explicit convergence rather than arbitrary clue count.

### 14. `cross-faction cooperation`

E146 and E148 are concrete coalition producers. However, cooperation must be distinguished from simply having four active character routes. Final qualification remains OPEN.

### 15. `final constitutional phase`

E150 is a late constitutional preparation node; E196–E210 are endgame preparation. There is no single frozen marker in the reviewed source proving final-phase activation. OPEN.

### 16. `final charter prerequisites`

E197/E198/E199 and E202–E209 provide candidate ingredients, but the exact prerequisite set is not frozen. OPEN.

## Important negative findings

- `rel.ivo` does not prove guild cooperation or strong guild influence.
- `rel.rowan` does not prove military constitutional route.
- `security` does not prove border crisis.
- `trust` does not prove institutional reform.
- evidence count does not automatically prove systemic explanation.
- E210 must not become an independent ending resolver.
- Similar narrative wording is not sufficient to establish a producer.

## Closure score

| Area | Status |
|---|---:|
| E111–E150 producer discovery | 72% |
| E151–E180 producer discovery | 68% |
| E181–E190 delayed/replay producers | 61% |
| E191–E210 trigger closure | 48% |
| Route namespace closure | 65% |
| Predicate producer closure | 62% |
| Ending-input producer closure | 54% |

## Gate

The audit confirms several real producers, especially `house_assembly` and `cross_faction_package`, but it also confirms that many apparently obvious triggers are still only semantic candidates. Production schema freeze remains blocked until the remaining open families receive explicit authored producers and reachability proof.

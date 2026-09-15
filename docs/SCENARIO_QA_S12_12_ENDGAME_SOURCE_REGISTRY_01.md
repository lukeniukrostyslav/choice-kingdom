# Choice Kingdom — S12.12 Endgame Source Registry 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA
Frozen production scope: E01–E272.

## Purpose
Convert authoritative E197–E210 rows into an immutable producer/consumer registry without inventing runtime producers.

## Consumer registry

| Event | Consumes | Contract boundary |
|---|---|---|
| E197 | `pred.constitutional_prepared_strong` | consumer-only |
| E200 | `pred.guild_influence_strong` | consumer-only |
| E201 | `pred.coalition_cooperation` | consumer-only |
| E202 | `history.house_assembly` | historical institutional evidence |
| E203 | `history.guild_representation` | canonical guild representation |
| E204 | `thread.military_constitutional` | military constitutional route |
| E205 | `thread.amara_civic` | civic/medical route |
| E206 | `thread.toma_information` | information route |
| E207 | `pred.systemic_explanation_verified` + `pred.coalition_cooperation` | independent evidence + convergence |
| E208 | `thread.final_constitutional_phase` | phase gate |
| E209 | `pred.final_charter_prerequisites` | all required domains must already exist |
| E210 | `thread.endgame_convergence` | convergence-only |

## Direct branch producers

E198-A → `legislative_budget_lock`; E198-B → `executive_budget_override_retained`.

E199-A/B → `army_constitution_oath` / `army_crown_oath`.

E200-A/B → `merchant_political_separation` / `merchant_influence_disclosed`.

E201-A/B → `coalition_renegotiated` / `coalition_shortfall_hidden`.

E202-A/B → `noble_veto_rejected` / `noble_limited_veto`.

E203-A/B → `guild_advisory_seat` / `guild_binding_seat`.

E204-A/B → `military_constitutional_refusal` / `military_crown_obedience`.

E205-A/B → `medical_neutrality_protected` / `medical_neutrality_overridden`.

E206-A/B → `press_protection` / `emergency_censorship`.

E207-A/B → `founder_authority_refused` / `founder_authority_accepted`.

E208-A/B → `empty_chair_memorial` / `permanent_emergency_chair`.

E209-A/B → `charter_publicly_ratified` / `charter_council_ratified`.

## Composite prerequisite contracts

### `pred.constitutional_prepared_strong`
At least 3 distinct preparation domains: civic/commons (`people_charter_endorsed`); institutional/audit (`crown_audited` or downstream `full_crown_audit_published`, same domain); faction/house (`house_assembly`); military/law (`military_red_line`). E197 cannot create a missing domain.

### `pred.guild_influence_strong`
At least 2 distinct guild institutional domains. Canonical domains include representation, independent tribunal, commercial disclosure/audited monopoly, and qualified logistics cooperation. Same-domain aliases/alternatives count once. `rel.ivo` is not a domain. E200 cannot create guild influence.

### `pred.coalition_cooperation`
Requires an explicit positive cooperation outcome, canonical participant identity and no unresolved collapse blocker. `history.cross_faction_package` and `four_way_bargain` are evidence but insufficient alone. E201 cannot create cooperation.

### `pred.systemic_explanation_verified`
Requires distinct warehouse/financial, document/language and witness/organizational evidence plus explicit convergence. E207 consumes the convergence; it does not produce it.

### `pred.budget_reform`
Requires E142-A `auditor_independence`, E154-A `crown_audited`, and E198-A `legislative_budget_lock`. Negative branches remain blockers where applicable.

### `pred.final_charter_prerequisites`
Requires all seven E209 domains: civic/commons legitimacy; institutional/audit legitimacy; faction/house/guild representation; military/security constitutional route; information/evidence legitimacy; coalition cooperation; absence of unresolved mandatory crisis blockers. E209 cannot manufacture missing prerequisites.

## Acceptance tests

1. Every E197–E210 consumed state has an upstream source or remains explicitly OPEN.
2. No E197–E210 consumer is accepted as its own prerequisite producer.
3. E198-A is the canonical budget-lock producer.
4. Negative branches remain distinct from positive domains.
5. Same-domain alternatives do not inflate cardinality.
6. E273–E277 contribute no production evidence.
7. E210 produces no prerequisite or route qualification.
8. Ending incoming paths are reconciled before engine implementation.

## Gate

S12.12 PASS for authoritative E197–E210 source extraction and registry normalization. Overall graph closure remains PARTIAL pending immutable evidence IDs, chronology, fresh-run reachability, replay isolation and ending precedence.

# Choice Kingdom — S08.7 Domain Qualification Audit 01

Date: 2026-09-15  
Scope: frozen production E01–E272 only  
Status: SOURCE-LEVEL QA — PARTIAL CLOSURE

## Purpose
Audit remaining high-value derived predicates whose semantics depend on independent institutional domains. This does not create runtime facts; unresolved producer identities remain OPEN.

## Scope integrity
Only E01–E272 may contribute production producer, consumer, predicate, delayed-source or reachability edges. E273–E277 remain excluded.

## Guild influence — `pred.guild_influence_strong`
Qualification requires at least two distinct institutional domains from: representation (`guild_political_representation` / `history.guild_representation`), tribunal (`guild_tribunal_independent`), market/credit (`official_credit_disclosure` / `audited_monopoly` as one domain), and independently qualified logistics cooperation.

Hard rule: `rel.ivo` cannot qualify the predicate alone. A single domain cannot be counted twice through aliases.

Status: PARTIAL — domain model frozen, but exhaustive E01–E272 producer identity and chronological availability remain to be verified.

## Constitutional preparation — `pred.constitutional_prepared_strong`
Qualification requires any three independent domains: civic (`people_charter_endorsed`), institutional (`crown_audited` / `full_crown_audit_published`), factional (`history.house_assembly`), and military (`military_red_line` / military-constitutional evidence).

`crown_audited` and `full_crown_audit_published` are one institutional domain, not two. Generic power/security or relationship strength cannot substitute for an independent domain.

Status: PARTIAL — source families identified; exhaustive chronology and negative-branch handling remain open.

## Systemic explanation — `pred.systemic_explanation_verified`
Current contract: three independently qualified evidence domains plus an explicit convergence/verification decision. Candidate evidence is concentrated in E132–E135 and E232–E236.

The convergence decision cannot manufacture missing evidence, and downstream consumers cannot retroactively create earlier prerequisites.

Status: PARTIAL / PRODUCERS OPEN.

## Coalition cooperation — `pred.coalition_cooperation`
Requires positive cooperation evidence plus participant identity. E148-A `history.cross_faction_package` is upstream evidence but does not by itself prove the complete predicate.

Hard negatives: `thread.coalition` alone is insufficient; `four_way_bargain` alone is insufficient; downstream consumers cannot self-satisfy the predicate.

Status: PARTIAL / PRODUCERS OPEN.

## Final charter prerequisites — `pred.final_charter_prerequisites`
This is a derived gate over prerequisite domains feeding E209/E210. E209/E210 are consumers/convergence nodes and cannot manufacture their own prerequisites.

Status: PARTIAL / PRODUCERS OPEN. Final formula waits for exhaustive prerequisite-domain reconciliation.

## Four faction routes — `pred.faction_routes_4`
Requires four distinct faction-route identities. A generic coalition/package marker cannot fill multiple route slots.

Status: OPEN — exact four producer families are not yet source-closed.

## Cross-domain machine gates
Before production schema admission:
1. Every positive producer is E01–E272.
2. Producer precedes consumer chronologically.
3. Failed branches cannot leak positive markers.
4. Aliases cannot create duplicate evidence domains.
5. Consumers cannot manufacture prerequisites.
6. Predicate cycles/self-satisfaction are rejected.
7. Save/load and replay preserve only explicitly authorized state.
8. E273–E277 never appear in production edges.

## Gate decision
This batch closes the qualification-domain boundaries but not all producer identities. S08 remains IN PROGRESS; S09 remains IN PROGRESS; production schema remains BLOCKED.

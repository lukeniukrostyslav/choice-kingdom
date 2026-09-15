# Choice Kingdom — Scenario QA S09.5 Normalized Dependency Edge Inventory 01

Date: 2026-09-15  
Status: **PARTIAL PASS — SOURCE-LEVEL QA**  
Frozen production scope: **E01–E272**  
Expansion candidates: **E273–E277 excluded**

## Purpose

Create the first normalized dependency-edge surface using only source-backed producer/consumer facts already admitted by the canonical producer inventory and derived-predicate contract. This pass deliberately does not infer missing producers from prose, route names or consumer reachability.

## Edge rules

1. Only E01–E272 may contribute production edges.
2. A source producer must be explicitly identified by event and choice/outcome where available.
3. Clear/recovery edges are lifecycle edges, not active-predicate producer edges.
4. A consumer may not be promoted into an upstream producer merely because its trigger names the predicate.
5. Historical facts and current-cycle predicates remain distinct.
6. Relationship scores and route cardinality do not become institutional predicates without an authored contract.
7. E273–E277 contribute zero production edges.

## Source-backed normalized edges

| Upstream source | Produced fact / lifecycle state | Downstream consumer(s) | Disposition |
|---|---|---|---|
| E18-B | `public_bridge` | E243 | CLOSED source edge |
| E09-B | `flexible_accounts` | E244 | CLOSED source edge |
| E117-B | `veteran_patronage` | E182 | CLOSED source edge |
| E118-B | `estate_exception` | E183/E242 | CLOSED source edge; E242 broader alias remains open |
| E136-B | `history.guild_logistics_cooperation` | E194 | CLOSED upstream edge |
| E144-A/B | `history.guild_representation` | later guild institutional consumers | CLOSED source edge |
| E148-A | `history.cross_faction_package` | E149/E201/E261+ | CLOSED package edge; does not itself qualify cooperation |
| E19-B | active `pred.market_pressure` cycle | market-pressure consumers | CLOSED source producer; lifecycle reconciliation remains open |
| E19-A | clear active `pred.market_pressure` | later market-pressure state | CLOSED clear edge |
| E29-A/B | active `pred.winter_severe` cycle | E136/E160/E251+ | CLOSED source producer; cycle expiry remains open |
| E32 crisis outcome | active `pred.transport_disruption` | E192/E251+ | CLOSED active source edge; persistence/order remains open |
| E136-A/B | clear `pred.transport_disruption` + stable network | downstream transport lifecycle | CLOSED recovery edge; not an active producer |
| E271-A | `border_crisis_declared` / active border thread | E195/E253/E255+ | CLOSED declaration edge; runtime active window open |
| E272-A/B | border resolution + clear active marker | later border callbacks/ending QA | CLOSED resolution edge |
| E199-A | military constitutional evidence / oath | E204/E227/E256+ and constitutional preparation | STRONG source edge; exact composite qualification remains open |
| E142-A | `auditor_independence` | budget reform composite | CLOSED source layer |
| E154-A | `crown_audited` | budget reform / institutional qualification | CLOSED source layer |
| E198-A | `legislative_budget_lock` | budget reform composite | CLOSED source layer; E198 consumer role must remain separate |

## Composite predicate edges — source domains only

### `pred.guild_influence_strong`

Admitted upstream domains:
- representation: E49-A / E144 representation family, counted once;
- tribunal: E168 institutional tribunal outcome family;
- commercial/market: E166 governance/credit family;
- logistics: E136-B followed by E194-A qualified cooperation.

Consumer: E200.

**No E200 → predicate edge is admitted.** `rel.ivo` is not an edge into this predicate.

Status: **PARTIAL — threshold and exhaustive source-token compilation open.**

### `pred.constitutional_prepared_strong`

Admitted upstream domains:
- civic: E50-A / `people_charter_endorsed`;
- institutional/audit: E154-A / published audit family;
- factional: E161-A / `house_assembly`;
- military/law: E199-A / constitutional military family.

Consumer: E197.

**No E197–E210 downstream outcome is admitted as an upstream producer.**

Status: **PARTIAL — exact three-of-four formula and chronology still open.**

### `pred.systemic_explanation_verified`

Required upstream evidence domains:
- warehouse/financial evidence;
- document/language evidence;
- witness/organizational evidence;
- explicit convergence decision.

Consumer: E207.

Status: **PARTIAL — immutable authored evidence IDs and exact convergence source remain to be compiled.**

### `pred.coalition_cooperation`

Required upstream facts:
- E148-A cooperation package with participant identities;
- distinct positive cooperation evidence;
- no unresolved coalition-collapse blocker.

Consumers include E201/E207/E261+.

**`thread.coalition` alone is not an upstream qualification edge.**

Status: **PARTIAL — exact positive producer and invalidation lifecycle remain open.**

### `pred.final_charter_prerequisites`

Required upstream domains include civic, institutional/audit, faction/house/guild, military/security where applicable, information/evidence, coalition cooperation and cleared mandatory blockers.

Consumer: E209/E210 qualification layer.

**Hard exclusion:** E209 is consumer-only and cannot produce this predicate. E210 is convergence-only and cannot manufacture prerequisites.

Status: **BLOCKED pending exhaustive concrete producer enumeration.**

## Cycle / self-satisfaction disposition

Confirmed hard negatives:
- E209 → `pred.final_charter_prerequisites` → E209 is rejected.
- E200 → `pred.guild_influence_strong` → E200 is rejected.
- E197 → `pred.constitutional_prepared_strong` → E197 is rejected.
- E207 → `pred.systemic_explanation_verified` → E207 is rejected.
- coalition thread → `pred.coalition_cooperation` → same-thread self-qualification is rejected.
- recovery/clear → active predicate without independent reactivation is rejected.
- E273–E277 → any production predicate is rejected.

## Remaining unresolved edges

1. Exhaustive output-token extraction for all E01–E272.
2. Exact E184 producer/evidence identity.
3. Exact E245 compensation-source semantics.
4. Exact E246 price-ceiling vocabulary policy.
5. Replay `meta.*` producer/key identities for E247/E248/E270.
6. Full systemic-evidence source IDs.
7. Full coalition positive-outcome identity and blocker lifecycle.
8. Exact composite threshold/formula for guild influence and constitutional preparation.
9. Final-charter upstream producer set and chronology.
10. Delayed callback source/target identity reconciliation against these edges.

## Gate result

**S09.5 PARTIAL PASS.**

The normalized source-backed edge surface is now explicit for the currently closed families, and known self-satisfaction patterns are hard-rejected. This is not yet exhaustive E01–E272 machine validation and does not justify production-schema or engine readiness.

## Next pass

Continue event-by-event output/trigger extraction, then compile a complete dependency graph and run transitive cycle detection before promoting any composite predicate to production schema.

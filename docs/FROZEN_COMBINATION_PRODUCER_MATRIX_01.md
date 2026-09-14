# Choice Kingdom — Frozen Combination Producer Matrix 01

Status: SOURCE-LEVEL CLOSURE WORK / PRE-SCHEMA

Purpose: convert the frozen nine bridge contracts into an explicit producer inventory. A contract is not considered closed merely because ingredients exist somewhere in the catalog.

## 1. Food stability

Canonical predicate: `pred.food_stable`

Required durable states:
- `food_logistics_stabilized`
- `food_logistics_unstable`

Known producer:
- E192-A/B were canonicalized to these durable markers.

Rule:
- no numeric food resource;
- no `+4 food stability` semantics;
- later events may invalidate stability explicitly.

Status: **SOURCE PRODUCER CLOSED / RUNTIME OPEN**.

## 2. Transport disruption

Canonical predicate: `pred.transport_disruption`

Required durable states:
- `transport_network_stable`
- `transport_disruption_active`

Known producers:
- E136-A/B establish stable transport and clear disruption.
- A later disruption event must establish `transport_disruption_active`.

Status: **PARTIAL** — stable/clear producer closed; active-disruption producer still requires exact source closure.

## 3. Border crisis

Canonical predicate: `pred.border_crisis`

Required lifecycle:
1. E271-A declares active crisis.
2. E272-A/B resolves active crisis.

Known consumers:
- E195, E253, E255 consume the active crisis.

Status: **SOURCE LIFECYCLE CLOSED / RUNTIME OPEN**.

## 4. Guild logistics cooperation

Canonical predicate: `pred.guild_logistics_cooperation`

Frozen qualification:
- E194-A produces `history.guild_logistics_cooperation`;
- neutral inspectors are part of the authored evidence;
- no unresolved guild-immunity risk may invalidate the qualification.

Important non-producers:
- E194-B creates immunity/risk semantics, not cooperation.
- generic `guild logistics route` is insufficient.
- relationship `rel.ivo` is insufficient.

Status: **SOURCE CONTRACT FROZEN / EXACT DERIVED FORMULA STILL OPEN**.

## 5. Strong guild influence

Canonical predicate: `pred.guild_influence_strong`

Frozen requirement:
at least two distinct institutional guild domains, selected from:
- political representation (`history.guild_representation`);
- commercial institutional influence (`guild_binding_seat` or equivalent canonical marker);
- market/credit leverage;
- guild tribunal outcome;
- durable guild logistics cooperation.

Known producer:
- E144-A/B establish `history.guild_representation`.
- E194-A establishes durable logistics cooperation evidence.

Open:
- exact second-domain producer inventory must be enumerated;
- combination formula must freeze before schema.

Status: **PARTIAL / P0 OPEN**.

## 6. Systemic explanation verified

Canonical predicate: `pred.systemic_explanation_verified`

Frozen evidence classes:
1. warehouse/financial evidence;
2. document/language evidence;
3. witness/organizational evidence;
4. explicit convergence decision.

Known source ingredients include:
- E232 `intermediary_chain_traced`;
- E233 `seal_forensics`;
- E234 `payment_pattern_public` or `payment_pattern_private`;
- E235 `middleman_family_archive`;
- E236 witness-ledger evidence;
- E270 `dual_witness_account` as late evidence.

Critical rule:
- E207/E209/E210 may consume/converge but must not manufacture missing evidence.
- raw clue count does not prove systemic explanation.

Status: **INGREDIENTS VERIFIED / EXPLICIT CONVERGENCE PRODUCER OPEN / P0**.

## 7. Coalition cooperation

Canonical predicate: `pred.coalition_cooperation`

Frozen requirement:
1. E148-A establishes `history.cross_faction_package`;
2. cooperation evidence from at least 3 distinct faction identities;
3. no unresolved coalition-collapse marker.

Known producer:
- E148-A records participation from Mara, Rowan, Seris, Ivo, Amara and Toma in the cross-faction package.

Non-producers:
- four faction routes;
- E261 `four_way_bargain`;
- E264/E265 coalition durability outcomes;
- relationship levels alone.

Status: **PACKAGE SOURCE CLOSED / THREE-DISTINCT-FACTION COOPERATION PRODUCERS STILL OPEN / P0**.

## 8. Strong constitutional preparation

Canonical predicate: `pred.constitutional_prepared_strong`

Frozen requirement:
three independent institutional domains:
- civic/commons;
- audit/institutional;
- cross-faction or constitutional.

Rule:
- E197 may consume this qualification;
- E197–E210 cannot retroactively create it;
- ending results cannot be prerequisites for it.

Status: **CONTRACT FROZEN / EXACT DOMAIN PRODUCERS OPEN / P0**.

## 9. Final charter prerequisites

Canonical predicate: `pred.final_charter_prerequisites`

Required before E209:
- civic/commons legitimacy;
- institutional/audit legitimacy;
- faction/house/guild representation;
- military/security constitutional route where applicable;
- information/evidence legitimacy;
- coalition cooperation;
- no unresolved mandatory crisis blocker.

Rule:
- E209 consumes the qualification;
- E210 only converges;
- neither event may manufacture missing upstream domains.

Status: **CONTRACT FROZEN / EXACT ENUMERATION AND PRODUCERS OPEN / P0**.

## Global closure rule

A frozen predicate is production-ready only when:
- every required component has a unique canonical producer;
- every producer has a stable event ID and choice identity;
- every consumer uses the canonical predicate rather than prose aliases;
- contradictory producers are explicitly mutually exclusive or superseded;
- delayed effects are exactly-once;
- save/load preserves the durable markers;
- graph and catalog agree;
- at least one reachable path establishes the predicate and at least one downstream consumer is reachable from it.

This matrix is source-level. Runtime engine readiness remains 0%.

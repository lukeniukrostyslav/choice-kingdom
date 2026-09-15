# Choice Kingdom — Early Predicate Producer Audit 02

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — VERIFIED / NO FALSE CLOSURE**
Scope: E01–E150, focused on unresolved derived predicates.

## Purpose

Inspect the early authored catalog for exact durable outputs that can safely serve as upstream producers. A trigger, consequence description, relationship change, or thematic reference is not sufficient. A producer must establish an explicit canonical fact with deterministic lifecycle semantics.

## Findings

| Predicate | Early authored candidates | Verdict |
|---|---|---|
| `pred.food_stable` | E03 releases grain reserves or allows imports; E12 funds local medicine; E29/E30 later granary/warehouse consequences | **NO SAFE DIRECT PRODUCER** — these are resource/policy outcomes, not a frozen stability fact |
| `pred.transport_disruption` | E05 missing patrol supplies; E10 local command; E16 border marker; E18 bridge/toll consequences; E31–E34 emergency/war material | **NO SAFE DIRECT PRODUCER** — movement/security effects must not be conflated with transport-disruption lifecycle |
| `pred.winter_severe` | E03 grain reserve depletion, E12 winter mortality consequence, E29/E30 winter/granary callbacks | **NO SAFE DIRECT PRODUCER** — winter severity remains a distinct authored state requirement |
| `pred.market_pressure` | E03 free imports, E08 merchant charter, E09 flexible accounts, E14 market reform, E19 price-fixing chain | **NO SAFE DIRECT PRODUCER** — these establish policies/flags but do not by themselves define a pressure predicate |
| `pred.guild_labor_tension` | Early dock/guild events establish merchant and dock relationships; no inspected early choice explicitly writes a durable labor-tension marker | **NO SAFE PRODUCER** |
| `pred.information_pressure_high` | E07 market inquiry, E13 Toma recruitment/rejection, E23 ledger/inquiry chain, E27 decoy/scandal material | **NO SAFE DIRECT PRODUCER** — information-network activity is not equivalent to information pressure |
| `pred.guild_influence_strong` | E08 merchant charter, E14 market reform, E39 emergency credit, E49 political representation | **PARTIAL** — several institutional domains exist, but exact independent domain/cardinality rule must be frozen across full catalog |
| `pred.constitutional_prepared_strong` | E10 command choice, E11 advisory seats, E35 expiry, E37 army oath, E47 constitution-first, E48 emergency clause, E50 people's charter | **PARTIAL** — many candidate domains, but independent-source set and exclusions must be frozen |
| `pred.budget_reform` | E04 public accounts, E09 audit office/flexible accounts, E23 ledger scrutiny, later E154/E155 audit legitimacy | **PARTIAL** — audit legitimacy exists, but legislative budget lock remains separately required |

## Important source-level conclusions

1. E03's grain-release choice must not be promoted to `pred.food_stable`; it spends reserves and explicitly creates a later shortage risk if reserves reach zero.
2. E08's merchant charter is a commercial-power marker, not automatically `pred.market_pressure` or `pred.guild_influence_strong` by itself.
3. E10's military command choice is route material, but a route milestone must remain distinct from a composite constitutional-preparation predicate.
4. E23/E27 investigation and information branches can contribute evidence/history but cannot manufacture `pred.information_pressure_high` without an explicit deterministic pressure rule.
5. E04/E09/E23 provide a credible upstream audit lineage for later budget reform, but a budget reform predicate still needs the separate legislative budget-lock condition already identified by the canonical contract.

## Result

This pass increases producer/consumer confidence without closing unresolved predicates by semantic approximation. Early content contains useful upstream ingredients for guild influence, constitutional preparation, and budget reform, but the final predicates still require exact source-set contracts.

## Required next work

- inspect E251–E272 for late producers and lifecycle resolution;
- freeze exact independent source IDs for guild influence and constitutional preparation;
- map the budget-reform legislative-lock source;
- audit all delayed callbacks against exact source choices and consequence IDs;
- only after those passes, patch authoritative catalog predicates and freeze production schema.

## Gate

Production schema: **BLOCKED**.

Runtime reachability: **NOT VERIFIED**.

Decision Engine: **BLOCKED by contract freeze**.

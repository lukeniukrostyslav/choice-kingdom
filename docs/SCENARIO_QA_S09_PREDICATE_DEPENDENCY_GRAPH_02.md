# Choice Kingdom — Scenario QA S09 — Predicate Dependency Graph 02

Date: 2026-09-15  
Frozen scope: **E01–E272**  
Status: **IN PROGRESS — STATIC CYCLE / SELF-SATISFACTION ANALYSIS**

## Purpose

Continue S09 without inventing missing predicates. This checkpoint classifies the currently verified dependency families into lifecycle edges, consumer edges, qualification edges and unresolved contract nodes.

## 1. Static cycle classification

### A. Lifecycle edges — not a closed dependency cycle
- E19-B establishes `pred.market_pressure(active)`; E19-A clears the current cycle.
- E29-A/B establish `pred.winter_severe(active)` for the current winter cycle; expiry/recovery remains open.
- E32 establishes `pred.transport_disruption(active)`; E136-A/B clear it.
- E271-A establishes `pred.border_crisis(active)`; E272-A/B clear it while retaining historical evidence.

These are state lifecycles. They must not be treated as graph cycles merely because a clear operation targets the same predicate.

### B. Consumer chains — no static self-cycle established
- E195 consumes `pred.border_crisis` and produces refugee/border outputs.
- E192 consumes `pred.transport_disruption` and produces logistics markers.
- E194 consumes upstream `history.guild_logistics_cooperation` and produces inspection/immunity facts.
- E197 consumes `pred.constitutional_prepared_strong` and produces succession-policy outputs.
- E201 consumes `pred.coalition_cooperation` and produces coalition renegotiation/shortfall outputs.
- E207 consumes `pred.systemic_explanation_verified` + `pred.coalition_cooperation` and produces founder-authority outputs.
- E209 consumes `pred.final_charter_prerequisites` and produces charter-ratification outputs.

No event above is allowed to manufacture its own prerequisite.

## 2. Self-satisfaction matrix

| Consumer | Required qualification | Self-satisfaction allowed? | Result |
|---|---|---:|---|
| E194 | upstream guild cooperation + neutral inspectors + no unresolved immunity risk | No | STATIC HARD-NEGATIVE CLOSED |
| E197 | `pred.constitutional_prepared_strong` | No | STATIC HARD-NEGATIVE CLOSED |
| E201 | `pred.coalition_cooperation` | No | STATIC HARD-NEGATIVE CLOSED |
| E207 | systemic explanation + coalition cooperation | No | STATIC HARD-NEGATIVE CLOSED |
| E209 | multi-domain final-charter prerequisites | No | STATIC HARD-NEGATIVE CLOSED |
| E210 | existing endgame convergence route | No | STATIC HARD-NEGATIVE CLOSED |

## 3. Independent-domain qualification

### Coalition
Candidate inputs from E261–E265 are not individually equivalent to `pred.coalition_cooperation`. A future executable contract must require the independent domains defined by the authored coalition route rather than accepting one late choice as sufficient.

### Constitutional preparedness
E256–E260 and E199 provide constitutional/military evidence, but no single event may silently become `pred.constitutional_prepared_strong` without the canonical multi-domain contract.

### Systemic explanation
E207 explicitly requires distinct warehouse/financial, document/language, witness/organizational and explicit convergence evidence. E269/E270 cannot collapse those domains by themselves.

### Final charter prerequisites
E209 is a consumer. Its prerequisite bundle remains multi-domain: civic legitimacy, institutional/audit legitimacy, faction representation, military/security constitutional route, information/evidence legitimacy, coalition cooperation and absence of a mandatory crisis blocker. The bundle is not yet machine-normalized.

## 4. Undefined / unresolved nodes

Repository search and direct source checks did not establish an authored producer for `shared_crisis_command`. It remains an undefined-producer defect candidate until a source-level producer is found or the consumer is removed/reworded.

The following remain contract gaps rather than invented facts:

- `full_ledger_published` producer vocabulary;
- `temporary_noble_exemption` canonical producer/alias;
- `all_voices_heard` replay/meta semantics;
- `mastermind_hunt` canonical investigation representation;
- E184 secret-evidence producer route;
- E245 compensation route identity;
- E246 price-ceiling vocabulary;
- food-pressure derived predicate semantics.

## 5. Delayed-cycle boundary

E181–E185 have authored triggers and outputs, but delayed callbacks are not yet executable dependency edges. Their source identity, timing, persistence, cancellation/supersession and exactly-once identity belong to S10. Therefore S09 does not close cycles through those callbacks prematurely.

## 6. Result

- Static self-satisfaction hazards: **CLOSED for the enumerated nodes**.
- Lifecycle-vs-cycle distinction: **CLOSED at static QA level**.
- Independent-domain hard negatives: **CLOSED for current enumerated cases**.
- Full dependency graph: **OPEN**.
- Machine cycle detection: **OPEN** until lifecycle and delayed contracts are normalized.
- Undefined/underspecified nodes: **OPEN**.
- Runtime reachability: **NOT VERIFIED**.

**S09: 55% / IN PROGRESS.**

Global Scenario QA remains **65%**. This checkpoint does not claim runtime completion.

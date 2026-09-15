# Choice Kingdom — Scenario QA S09 — Predicate Dependency Graph 01

Date: 2026-09-15  
Frozen scope: **E01–E272**  
Status: **IN PROGRESS — STATIC CONTRACT ONLY**

## Purpose

Compile the first dependency graph from already source-verified producer/consumer facts. This artifact does not invent missing predicates and does not claim runtime reachability.

## Verified dependency edges

### Market pressure
- E19-B → `pred.market_pressure(active)`.
- E19-A → clear `pred.market_pressure` for the current cycle.
- Downstream market-pressure consumers must not manufacture the predicate.

### Winter severity
- E29-A/B → `pred.winter_severe(active)` for the current winter cycle.
- E160 and later winter nodes consume the severe-winter condition; they are not source-level producers of the authored predicate.
- A future recovery/expiry contract remains open.

### Transport disruption
- E32 → `pred.transport_disruption(active)`.
- E192 consumes `pred.transport_disruption`.
- E136-A/B clear the active disruption state.
- E251 is a downstream consumer and cannot self-create the predicate.

### Border crisis
- E271-A → `pred.border_crisis(active)`.
- E195/E253/E255 consume the active border-crisis state.
- E272-A/B clear the active predicate while retaining historical declaration/resolution evidence.
- `thread.border` and generic border tension are forbidden aliases.

### Guild logistics cooperation
- `history.guild_logistics_cooperation` is established upstream by E136-B.
- E194 consumes that history and adds neutral-inspector / immunity-risk facts.
- Qualified `pred.guild_logistics_cooperation` therefore requires independent upstream cooperation plus inspection and no unresolved immunity risk.
- E194 cannot self-satisfy the qualified predicate.

### Coalition cooperation
- E261 `four_way_bargain`, E262 fifth-voice participation, E263 published costs and E265 final-text agreement are candidate inputs, not equivalent to `pred.coalition_cooperation`.
- E201/E207 consume the qualified coalition predicate.
- No single late event may manufacture the predicate from its own trigger.
- Exact independent-domain qualification remains OPEN.

### Constitutional preparedness
- E197 consumes `pred.constitutional_prepared_strong`.
- E256–E260 are constitutional stress/test nodes, but do not independently create the qualified predicate.
- The qualification must remain multi-domain and independently sourced.

### Final charter prerequisites
- E209 consumes `pred.final_charter_prerequisites`.
- E209 cannot manufacture its own prerequisites.
- The prerequisite set includes multiple independent domains recorded in S05 QA; exact canonical predicate definitions remain OPEN.

### Systemic explanation
- E207 consumes `pred.systemic_explanation_verified` plus coalition cooperation.
- E269/E270 provide late evidence handoff/convergence but cannot silently self-satisfy systemic explanation.
- Evidence domains must remain independent until explicit convergence.

## Known dependency hazards

1. **Self-satisfaction:** E194, E197, E201/E207 and E209 cannot use their own trigger/outputs to create the predicate they consume.
2. **Alias collapse:** `four_way_bargain`, `thread.border`, `pred.food_stable`, and generic pressure prose must not be promoted to canonical predicates without authored contracts.
3. **Cycle risk:** delayed callbacks and derived pressure predicates can form runtime cycles if their lifecycle semantics are not separated from source facts. Cycle analysis is therefore still OPEN.
4. **Independent-domain qualification:** coalition, constitutional preparedness, systemic explanation and final-charter predicates require independent evidence/state domains rather than one late event.
5. **Replay contamination:** ordinary run-local facts cannot become `meta.*` predicates implicitly.

## Undefined/underspecified dependency nodes carried forward

- `shared_crisis_command` (E104): no source-verified producer currently established.
- `full_ledger_published`: consumer observed; exact producer vocabulary requires reconciliation.
- `temporary_noble_exemption`: canonical producer/alias unresolved.
- `all_voices_heard`: replay/meta contract unresolved.
- `mastermind_hunt`: investigation representation unresolved.
- E184 secret-evidence route: source producer unresolved.
- E245 compensation route: must not union distinct compensation facts silently.
- E246 price-ceiling route: exact canonical vocabulary unresolved.
- Food-pressure derived predicate: `food_logistics_unstable/stabilized` are authored outputs; `pred.food_stable` remains an OPEN derived-contract candidate.

## Cycle disposition

No dependency cycle is declared CLOSED by this checkpoint. The graph contains lifecycle edges and consumer dependencies, but exact runtime transition semantics, expiry, delayed ordering and derived-predicate evaluation are not yet machine-defined.

## S09 gate

- Verified producer/consumer edges: **PARTIAL CLOSED**
- Hard-negative/self-satisfaction rules: **CLOSED at static QA level for the listed cases**
- Full predicate graph: **OPEN**
- Cycle detection: **OPEN**
- Independent-domain qualification: **OPEN**

**S09: 50% / IN PROGRESS.**

Global Scenario QA remains **65%**.

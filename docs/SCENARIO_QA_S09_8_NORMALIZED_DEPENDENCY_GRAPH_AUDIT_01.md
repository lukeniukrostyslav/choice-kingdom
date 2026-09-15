# Choice Kingdom — Scenario QA S09.8 Normalized Dependency Graph Audit 01

Date: 2026-09-15
Status: **PARTIAL PASS — MACHINE-READY GRAPH SURFACE, SOURCE-LEVEL QA**
Frozen production scope: **E01–E272**
Expansion candidates: **E273–E277 excluded**

## Purpose

Convert the reconciled S09.5/S09.6/S09.7 producer surface into a normalized dependency graph suitable for deterministic machine checking. This artifact deliberately distinguishes closed source-backed edges from partial composite predicates and unresolved lifecycle contracts.

## Normalized source-backed edges

| Source | Token / lifecycle fact | Consumer | Status |
|---|---|---|---|
| E18-B | `public_bridge` | E243 | CLOSED |
| E09-B | `flexible_accounts` | E244 | CLOSED |
| E117-B | `veteran_patronage` | E182 delayed callback | CLOSED SOURCE / delayed identity OPEN |
| E118-B | `estate_exception` | E183 / E242 | CLOSED SOURCE / delayed identity OPEN |
| E136-B | `history.guild_logistics_cooperation` | E194 / guild-logistics qualification | CLOSED UPSTREAM |
| E144-A/B | `history.guild_representation` | guild-influence qualification / E203 | CLOSED SOURCE |
| E148-A | `history.cross_faction_package` | coalition qualification | CLOSED EVIDENCE / qualification OPEN |
| E19-B | `pred.market_pressure` active | downstream food/economic consumers | CLOSED SOURCE |
| E19-A | market pressure clear | lifecycle consumers | CLOSED CLEAR |
| E29-A/B | `pred.winter_severe` active | winter consumers | CLOSED SOURCE |
| E32 | `pred.transport_disruption` active | E192 / downstream logistics | CLOSED SOURCE |
| E136-A/B | transport recovery/clear | transport lifecycle | CLOSED CLEAR / recovery |
| E271-A | `pred.border_crisis` active | E195/E253/E255 | CLOSED SOURCE |
| E272-A/B | border crisis resolution | active-crisis lifecycle | CLOSED CLEAR |
| E199-A | military constitutional evidence | constitutional-prepared domain | CLOSED SOURCE |
| E142-A | `auditor_independence` | budget-reform domain | CLOSED SOURCE |
| E154-A | `crown_audited` | budget-reform domain | CLOSED SOURCE |
| E198-A | legislative budget lock candidate | budget-reform domain | OPEN EXACT CONTRACT |

## Composite predicate nodes

### `pred.guild_influence_strong`
Required independent domains currently recognized:
1. guild representation;
2. commercial tribunal independence;
3. commercial/market governance;
4. qualified logistics cooperation.

Hard negatives: `rel.ivo` and duplicate aliases cannot satisfy an independent domain. E194 cannot self-create `history.guild_logistics_cooperation`.

Status: **PARTIAL** — domain boundary closed, minimum formula/source set not yet frozen.

### `pred.constitutional_prepared_strong`
Recognized domains:
1. civic / people charter;
2. institutional/audit;
3. house assembly/factional;
4. military/security constitutional route.

E197 is consumer-only and cannot manufacture this predicate.

Status: **PARTIAL**.

### `pred.systemic_explanation_verified`
Recognized evidence families:
1. warehouse/financial;
2. document/language;
3. witness/organizational;
4. explicit convergence.

E207 is consumer-only and cannot manufacture systemic explanation.

Status: **PARTIAL** — exact immutable source token set unresolved.

### `pred.coalition_cooperation`
Required shape:
- explicit participant identities;
- positive cooperation outcome;
- no collapse blocker;
- deterministic invalidation lifecycle.

E148-A is evidence/package input, not a perpetual qualified predicate. E261 `four_way_bargain` is explicitly insufficient by itself.

Status: **PARTIAL**.

### `pred.budget_reform`
Known layers:
- E142-A auditor independence;
- E154-A Crown audit;
- E198-A legislative budget lock candidate.

Status: **OPEN** — exact formula and E198 ordering semantics remain unresolved.

### `pred.final_charter_prerequisites`
This is a convergence predicate, not a producer shortcut. E209 consumes it; E210 is convergence-only. No self-satisfaction edge is authorized.

Status: **BLOCKED** until exhaustive upstream enumeration is frozen.

### `pred.food_stable`
No source-closed producer has been verified in E01–E272. E192-A/B are concrete logistics outcomes only.

Status: **BLOCKED**.

## Cycle / self-satisfaction audit

The normalized graph rejects the following edge classes:

- consumer → its own prerequisite;
- E209 → `pred.final_charter_prerequisites` as producer;
- E197 → `pred.constitutional_prepared_strong` as producer;
- E200 → `pred.guild_influence_strong` as producer;
- E207 → `pred.systemic_explanation_verified` as producer;
- E261 → `pred.coalition_cooperation` by alias;
- E192 → `pred.food_stable` by alias;
- recovery/clear → active predicate without an explicit reactivation producer;
- E271 resolution/warning → active `pred.border_crisis`;
- any E273–E277 event → production dependency edge.

No newly authorized source-backed cycle was found in the normalized closed edge set. This is not yet a mathematical proof over the complete campaign because unresolved composite and delayed/replay nodes remain outside the closed graph.

## Undefined producer / consumer audit

### Explicitly undefined or unresolved producers
- `pred.food_stable`
- exact full producer set for `pred.guild_influence_strong`
- exact full producer set for `pred.constitutional_prepared_strong`
- exact systemic-explanation source set
- exact coalition lifecycle/qualification producer
- exact `pred.budget_reform` contract
- exact final-charter upstream convergence set
- several `thread.*` late constitutional route identities
- replay `meta.*` producers for E247/E248/E270

### Delayed identities still unresolved
- E184
- E185
- E242–E246
- later E251–E272 delayed consequences where source choice, target, cancellation or exactly-once identity is not yet frozen.

## Scope integrity

The production graph accepts only E01–E272. E273–E277 are quarantined expansion candidates and are rejected by the graph admission rule.

## Gate result

**S09.8 PARTIAL PASS.**

The machine-normalized closed edge surface is now explicit and safe for subsequent validator construction. Composite predicates, delayed/replay identity and complete transitive closure remain open, so this pass does not authorize production schema or Decision Engine implementation.

**S09 remains 60%. Scenario QA remains 65%.** No percentage increase is claimed until the remaining graph domains are exhaustively closed and mechanically checked.

## Next autonomous block

1. Reconcile S10 delayed source/target/exactly-once identities against this graph.
2. Close E184/E185/E242–E246 delayed contracts where authored evidence permits.
3. Audit replay/meta producers and ending precedence for S11.
4. Run S12 fresh-run reachability against the normalized graph and authored chronology.
5. Only then freeze production schema and begin Decision Engine implementation.

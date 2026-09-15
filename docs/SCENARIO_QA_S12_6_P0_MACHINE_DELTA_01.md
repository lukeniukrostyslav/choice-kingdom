# Choice Kingdom — S12.6 P0 Machine Delta 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — MACHINE CONTRACT PREPARATION**  
Scope: E01–E272 frozen production catalog.

## 1. Purpose

Turn the verified P0 source reconciliation into a deterministic producer/consumer delta without inventing missing producers.

## 2. P0 normalized edges

| Token / predicate | Producer | Consumer | Lifecycle / notes |
|---|---|---|---|
| `transport_network_stable` | E136-A/B | later transport-dependent routes | durable repair state; E136 also clears active disruption |
| `history.guild_logistics_cooperation` | E136-B | E194 | immutable historical marker; E194 cannot self-create it |
| `history.guild_representation` | E144-A/B | guild institutional routes / E200 domain qualification | same semantic domain; do not double-count E49/E144 |
| `history.cross_faction_package` | E148-A | E149 and coalition qualification | necessary evidence, not equivalent to coalition predicate |
| `food_logistics_unstable` | E192-A | food-pressure consumers | canonical logistics outcome only |
| `food_logistics_stabilized` | E192-B | food-pressure consumers | canonical logistics outcome only; **not** an implicit `pred.food_stable` producer |
| `guild_neutral_inspectors` | E194-A | qualified guild logistics formula | requires upstream cooperation history |
| `guild_logistics_immunity_risk` | E194-B | qualified guild logistics blocker | unresolved blocker prevents qualified cooperation |
| `pred.transport_disruption` | E32 | E192 and transport-dependent routes | E136-A/B clear; recovery cannot reactivate |
| `pred.border_crisis` | E271-A | E195/E253 and later crisis routes | E272-A/B resolve; generic security/border tension cannot substitute |
| `auditor_independence` | E142-A | budget reform / institutional routes | independent institutional layer |
| `crown_audited` | E154-A | audit/budget routes | distinct from publication choice |
| `full_crown_audit_published` | E155-A | public-audit routes | publication evidence, not audit independence |
| `legislative_budget_lock` | E198-A | budget reform | distinct legislative layer |

## 3. Composite predicates — deliberately unresolved

### `pred.guild_influence_strong`
Candidate independent domains include representation, commercial tribunal, market governance/credit, labor standards and qualified logistics cooperation. The exact minimum domain set and invalidation semantics remain OPEN. Relationship score and raw event count are forbidden substitutes.

### `pred.constitutional_prepared_strong`
Candidate independent domains include civic legitimacy, institutional/audit legitimacy, factional representation, military/security constitutional legitimacy and explicit constitutional design/signature evidence. Exact formula remains OPEN.

### `pred.systemic_explanation_verified`
Required evidence families are warehouse/financial, document/language, witness/organizational and explicit convergence. Each family requires immutable evidence IDs. Exact authored IDs remain OPEN.

### `pred.coalition_cooperation`
E148-A provides six named participants and a cross-faction package. Runtime qualification requires explicit participant identity, positive cooperation evidence and no unresolved collapse blocker. Package marker alone is insufficient.

### `pred.budget_reform`
Source layers are E142-A, E154-A/E155-A and E198-A. Exact boolean/cardinality formula and negative-blocker semantics remain OPEN.

### `pred.final_charter_prerequisites`
Upstream dependency boundary is defined, but exact formula and incoming-path completeness remain OPEN. E209 is consumer-only; E210 is convergence-only.

## 4. Zero-producer / alias guard

`pred.food_stable` is currently **ZERO VERIFIED PRODUCERS** within E01–E272. E192's `food_logistics_stabilized` must not be promoted by name similarity. E273-A remains excluded.

Legacy source-language aliases requiring normalization include:
- `guild_political_representation` → E144 producer route;
- prose `high market oversight`, `severe winter`, `food pressure`, `border tension`, etc. → deterministic predicates or canonical state markers, never arbitrary booleans.

## 5. Machine acceptance checks

A future production registry must reject:
- producer IDs outside E01–E272;
- consumer-as-producer edges;
- alias edges without explicit contract;
- two semantic writers with no lifecycle rule;
- a predicate satisfied only by the event that consumes it;
- replay metadata leaking into current-run state;
- delayed callbacks without exact source choice, timing window, target and exactly-once identity;
- ending qualification with no independent incoming path.

## 6. Gate

**S12.6: PARTIAL PASS.**

P0 source-level edges are now normalized where authoritative evidence is closed. Composite formulas, exhaustive E01–E272 coverage, delayed rows, endings and fresh-run/replay reachability remain open.

Production schema and Decision Engine remain blocked.

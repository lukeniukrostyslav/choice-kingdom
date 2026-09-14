# Choice Kingdom — Predicate Closure 01

Status: **CANONICALIZATION WORKING CONTRACT — NOT ENGINE INPUT**

## Rule
Every non-trivial trigger must resolve to a canonical `pred.*`, `hist.*`, `thread.*`, `rel.*`, `meta.*`, event-completion or explicit turn-window condition. Prose labels such as "food pressure" or "institutional reform" are not production conditions by themselves.

## Threshold predicates

| Predicate | Provisional deterministic definition | Required producer evidence |
|---|---|---|
| `pred.trust_high` | trust >= 6 | resource state |
| `pred.trust_low` | trust <= 3 | resource state |
| `pred.security_high` | security >= 6 | resource state |
| `pred.security_low` | security <= 3 | resource state |
| `pred.gold_low` | gold <= 5 | resource state |
| `pred.power_high` | power >= 6 | resource state |
| `pred.reputation_high` | reputation >= 6 | resource state |

These thresholds remain subject to balance simulation before production freeze.

## Food

`pred.food_pressure` must be derived from explicit authored food-related history/effects, not stored as a resource.

Required distinction:
- pressure: one or more unresolved food causes;
- severe: pressure plus an authored escalation condition;
- crisis: severe pressure plus an authored crisis trigger;
- stability/resilience: explicit recovery history that can suppress pressure where the catalog permits it.

No event may create `pred.food_pressure` merely by mentioning bread, grain or markets.

## Winter

Required distinctions:
- `pred.winter_pressure` — seasonal/logistics stress;
- `pred.winter_severe` — explicit severe winter escalation;
- `pred.winter_illness` — health consequence with an authored producer;
- `pred.winter_transport_disruption` — transport-specific condition.

These predicates must not be aliases for one another.

## Border and security

Keep separate:
- `pred.border_tension`;
- `pred.border_crisis`;
- `pred.security_low`;
- `pred.security_high`;
- `pred.army_readiness_low`;
- `thread.border`;
- `thread.military_constitutional`;
- `thread.border_intelligence`.

A low security resource does not automatically imply border crisis, and a border crisis does not automatically imply low army readiness.

## Market and guild

Keep separate:
- `pred.market_pressure`;
- `thread.market_oversight`;
- `thread.guild_leverage`;
- `thread.guild_labor_tension`;
- `thread.guild_logistics`;
- `thread.trade_risk_insurance`.

A high Ivo relationship does not automatically satisfy any of these route conditions.

## Information and evidence

Evidence must be represented as auditable markers. Recommended structure:
- `hist.evidence.<stable_id>` for each discovered clue;
- `pred.evidence_count_ge_2` derived from distinct qualifying clue IDs;
- `pred.evidence_count_ge_3` derived similarly;
- `thread.witness`;
- `thread.protected_sources`;
- `thread.forgery`;
- `thread.payment_pattern`;
- `pred.systemic_explanation_verified` only after the authored evidence set satisfies the systemic-conclusion contract.

Repeated observations of the same clue must not inflate cardinality unless the content explicitly defines them as distinct evidence.

## Institutional reform

`thread.institutional_reform` must be produced by explicit institutional decisions. High trust, high reputation or a single audit alone cannot satisfy it.

Candidate qualifying families include independent audit, transparent appointment, public rules, independent budget, constitutional expiry and durable accountability. Exact minimum combination remains to be locked after full producer inventory.

## Multi-crisis

`pred.multi_crisis_3` = simultaneous satisfaction of:
1. `pred.food_pressure` or stronger food crisis predicate;
2. `pred.border_tension` or stronger border crisis predicate;
3. an authored civic-pressure predicate.

Evaluation occurs at event eligibility time from current canonical state/history. It is not a UI flag and not a sixth resource.

## Replay boundary

`meta.*` can only satisfy current-run conditions through an explicit replay-transfer rule. A replay discovery cannot silently become a current-run historical fact.

## Closure status

Closed enough for design review:
- resource thresholds;
- namespace separation;
- evidence cardinality model;
- multi-crisis evaluation rule.

Still open:
- exact food producers and escalation thresholds;
- exact winter producers;
- border/army readiness producers;
- market/guild producers;
- institutional reform minimum combination;
- all route producers E01–E270;
- ending simulations.

Therefore this contract is **not** yet a production engine schema.

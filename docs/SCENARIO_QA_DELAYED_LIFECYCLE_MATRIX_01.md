# Scenario QA — Delayed Lifecycle Matrix 01

## Purpose
Freeze the exact source-evidence boundary for delayed consumers E181–E185 and E242–E246 without inventing missing authored semantics.

## Source identity closure

The source identities below are reconciled against the current canonical machine graph and the authoritative authored event catalog. **Source identity closure is distinct from runtime lifecycle closure.**

| Consumer | Authoritative source | Delay language | Source status | Lifecycle status |
|---|---|---|---|---|
| E181 | E45-B → `infrastructure_concession` | 5+ turns | CLOSED | OPEN |
| E182 | E117-B → `veteran_patronage` | 4+ turns | CLOSED | OPEN |
| E183 | E118-B → `estate_exception` | 5+ turns | CLOSED | OPEN |
| E184 | E25-B → `secret_evidence_route` | 4+ turns | CLOSED | OPEN |
| E185 | E17-A → `cheap_weapons` + later military crisis | later military crisis | CLOSED_IDENTITY | OPEN_MULTI_STAGE |
| E242 | E118-B → `estate_exception` | 6+ turns | CLOSED | OPEN |
| E243 | E18-B → `public_bridge` | 5+ turns | CLOSED | OPEN |
| E244 | E09-B → `flexible_accounts` | 5+ turns | CLOSED | OPEN |
| E245 | E20-A → `soldier_compensation` | 6+ turns | CLOSED | OPEN |
| E246 | E160-A → `winter_rent_ceiling` | 5+ turns | CLOSED | OPEN |

## Reconciliation decisions

- **E184:** the prior `unresolved` source status is stale. The current canonical graph explicitly binds E184 to E25-B / `secret_evidence_route`. This closes the source identity only; it does not close its runtime lifecycle.
- **E242:** the prior `PARTIAL_ALIAS_ONLY` label is stale for the selected canonical source identity. E118-B is the authored source represented by the current canonical graph. This does **not** authorize treating E118-B as a universal alias for every noble-exception history.
- **E245:** the current canonical graph explicitly selects E20-A / `soldier_compensation`. E125-A and E156-A must not be silently unioned into this producer family.
- Relative timing remains relative. `5+`, `6+`, `4+`, and `later military crisis` are not converted into invented absolute turns.

## Runtime closure contract

A delayed record is not runtime-closed until all of these are explicit:

1. source event and exact source choice;
2. consequence token;
3. earliest eligible turn / authored relative timing;
4. deterministic resolution target;
5. exactly-once identity key;
6. cancellation or supersession rule;
7. save/load persistence behavior;
8. replay isolation behavior;
9. fresh-run reachability evidence.

Current matrix: **0/10 runtime lifecycles closed**. This remains intentional; no runtime semantics are fabricated to increase percentages.

## Hard negatives

- E184 must not be re-opened merely because its runtime scheduler semantics are unresolved; its source identity is now closed to E25-B.
- E242 does not treat E118-B as a universal alias for every prior noble exception.
- E245 remains uniquely sourced to E20-A; do not union E125-A or E156-A.
- Relative delay wording is not converted into an absolute due turn without authored evidence.
- E185 is multi-stage: `cheap_weapons` plus a later military crisis.
- E273–E277 remain outside production semantics.

## Acceptance

PASS — all ten currently enumerated delayed consumers have an explicit source identity in the current canonical graph.
PASS — no generic producer aliases were introduced.
PASS — authored relative timing was preserved without invented turns.
PASS — E184 and E242 source-boundary stale statuses were reconciled.
PASS — E245 remains explicitly isolated to E20-A.
OPEN — cancellation/supersession lifecycle.
OPEN — exactly-once scheduling/resolution.
OPEN — save/load persistence.
OPEN — replay isolation.
OPEN — fresh-run reachability.

## Next closure target

The next executable scenario-QA work must convert these source identities into machine-checkable lifecycle records without inventing cancellation, supersession, resolution timing, persistence, or replay semantics that are absent from authoritative content. Runtime scheduler implementation remains outside the scenario phase until the canonical lifecycle contract is sufficiently closed.

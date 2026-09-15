# Scenario QA — Delayed Lifecycle Matrix 01

## Purpose
Freeze the exact source-evidence boundary for delayed consumers E181–E185 and E242–E246 without inventing missing authored semantics.

## Source identity closure

| Consumer | Authoritative source | Delay language | Source status | Lifecycle status |
|---|---|---|---|---|
| E181 | E45-B → `infrastructure_concession` | 5+ turns | CLOSED | OPEN |
| E182 | E117-B → `veteran_patronage` | 4+ turns | CLOSED | OPEN |
| E183 | E118-B → `estate_exception` | 5+ turns | CLOSED | OPEN |
| E184 | unresolved | 4+ turns | OPEN | BLOCKED_SOURCE |
| E185 | E17-A → `cheap_weapons` | later military crisis | CLOSED_IDENTITY | OPEN_MULTI_STAGE |
| E242 | E118-B → `estate_exception` | 5+ turns | PARTIAL_ALIAS_ONLY | BLOCKED_SEMANTIC_ALIAS |
| E243 | E18-B → `public_bridge` | delayed callback | CLOSED | OPEN |
| E244 | E09-B → `flexible_accounts` | delayed callback | CLOSED | OPEN |
| E245 | E20-A → `soldier_compensation` | 6+ turns | CLOSED | OPEN |
| E246 | E160-A → `winter_rent_ceiling` | relative delayed consequence | CLOSED | OPEN |

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

Current matrix: **0/10 runtime lifecycles closed**. This is intentional; no runtime semantics are being fabricated to increase percentages.

## Hard negatives

- E184 has no invented producer.
- E242 does not treat E118-B as a universal alias for every prior noble exception.
- E245 remains uniquely sourced to E20-A; do not union E125-A or E156-A.
- Relative delay wording is not converted into an absolute due turn without authored evidence.
- E185 is multi-stage: `cheap_weapons` plus a later military crisis.
- E33/E34 remain quarantined; E273–E277 remain outside production semantics.

## Next closure target

The next executable scenario-QA work should resolve only fields supported by authoritative authored text, then promote the machine contract and CI gate. Runtime scheduler implementation remains blocked until this source-level boundary is sufficiently closed.

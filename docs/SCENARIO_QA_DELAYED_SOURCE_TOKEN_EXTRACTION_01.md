# Choice Kingdom — Scenario QA Delayed Source Token Extraction 01

Status: **SOURCE-LEVEL QA — EXTRACTION PASS**  
Scope: E09, E17, E18, E20, E45, E117, E118, E160 and delayed consumers E181–E185/E242–E246.  
Date: 2026-09-15.

## Purpose

Make the already identified delayed producers concrete at the authored-choice level without inventing runtime semantics. This pass records the exact source choice identity where the authoritative producer inventory closes it, and distinguishes that identity from the consumer's broader trigger wording.

## Extracted source identities

| Fact | Exact producer | Source token | Consumer(s) | Extraction status |
|---|---|---|---|---|
| `flexible_accounts` | E09-B | `flexible_accounts` | E244 | CLOSED |
| `cheap_weapons` | E17-A | `cheap_weapons` | E185 | CLOSED at source identity |
| `public_bridge` | E18-B | `public_bridge` | E243 | CLOSED |
| `soldier_compensation` | E20-A | `soldier_compensation` | E245 | CLOSED; exclusive source |
| `infrastructure_concession` | E45-B | `infrastructure_concession` | E181 | CLOSED at source identity |
| `veteran_patronage` | E117-B | `veteran_patronage` | E182 | CLOSED |
| `estate_exception` | E118-B | `estate_exception` | E183/E242 | CLOSED for E183; PARTIAL for broad E242 wording |
| `winter_rent_ceiling` | E160-A | `winter_rent_ceiling` | E246 | CLOSED |

## Consumer wording reconciliation

### E181
The consumer's `infrastructure/toll concession` wording is not itself a producer token. The authoritative source identifies E45-B and its `infrastructure_concession` flag. Therefore the source identity is closed, but the authored wording must not be widened into an arbitrary toll/concession alias.

### E242
The consumer says `any prior noble exception`. E118-B is a verified source candidate, but the wording is broader than one producer. E118-B therefore remains a candidate, not a universal alias. No additional producer is invented.

### E185
`cheap_weapons` identifies E17-A, but the later military crisis is a separate lifecycle condition. Source identity is closed; delayed resolution remains open.

### E243
`public bridge investment` is normalized to the canonical source token `public_bridge` from E18-B. This is vocabulary normalization only; it does not create a new authored fact.

### E245
`compensation route` is normalized to E20-A / `soldier_compensation` because the source audit explicitly matches the Soldier's Son / compensated-family identity. E125-A and E156-A remain separate and are not unioned.

### E246
`price ceiling` is normalized to E160-A / `winter_rent_ceiling`. The normalization is source-backed; timing and invalidation remain open.

## What remains deliberately OPEN

This extraction does **not** close:

- earliest executable due turn;
- scheduler anchor;
- exactly-once key;
- cancellation/supersession semantics;
- pending-delay persistence through save/load;
- fresh-run reachability;
- replay reachability;
- E184 producer identity;
- broad E242 producer set;
- E185 military-crisis resolution;
- semantic equality between graph edges and producer records.

## Hard negatives

1. A normalized source token is not a runtime predicate.
2. A consumer trigger phrase cannot manufacture a producer.
3. E245 cannot merge E20-A with E125-A/E156-A.
4. E242 cannot be reduced to E118-B while its authored trigger remains broader.
5. E33/E34 remain quarantined and cannot be used to fill missing source tokens.
6. E273–E277 remain outside production semantics.

## Result

This pass materially improves the source-level delayed contract boundary: the closed producer identities are now represented as exact event+choice+token tuples, while all unresolved runtime and reachability fields remain explicitly blocked.

No Decision Engine promotion is authorized by this document.

# Constitutional Preparation — Runtime Gate 01

Status: **SOURCE CONTRACT CLOSED / RUNTIME OPEN**

## Predicate
`pred.constitutional_prepared_strong`

The source contract requires at least three distinct preparation domains. Current authoritative candidates are E50-A civic/commons, E154-A institutional/audit, E161-A factional/house, and E199-A military/law. E154/E155 count as one domain. `constitutional_limit`, raw trust, relationship values, and E227 `military_red_line` are not silently promoted into the predicate.

## Runtime gate
The predicate must be evaluated from persisted authored state/history keys, not from trigger text or narrative inference. A valid evaluation requires:

1. at least three distinct domains present;
2. all negative blockers clear;
3. deterministic ordering of producer updates before predicate evaluation;
4. save/load preservation of the contributing keys;
5. no same-run consumer may manufacture an upstream producer key;
6. fresh-run reachability demonstrated for every qualifying domain combination used by production endings.

## Explicit blockers
- `permanent_emergency_power_active`
- unresolved constitutional contradiction

## Not yet verified
- executable runtime ordering;
- persistence/reload semantics;
- fresh-run gameplay reachability;
- contradiction/cycle validation against the full production graph;
- Decision Engine promotion.

This document is a gate definition, not an implementation claim.

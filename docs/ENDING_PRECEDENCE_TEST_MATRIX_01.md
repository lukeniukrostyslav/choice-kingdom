# Choice Kingdom — Ending Precedence Test Matrix 01

Status: **CANONICAL QA CONTRACT — NOT RUNTIME IMPLEMENTATION**
Scope: seven current ending families and E265–E270.

## Purpose

This matrix defines the minimum deterministic test surface required before the ending resolver can be implemented. It deliberately does not invent missing producers or pretend that authored prose is executable state.

## Ending families under test

| ID | Ending | Primary qualification shape |
|---|---|---|
| END_STEWARD | Steward | institutional reform + restrained emergency power + stable/high legitimacy + no terminal collapse |
| END_IRON_CROWN | Iron Crown | border/military route + concentrated security authority + retained emergency authority/weak constitutional limits |
| END_GOLDEN_COMPACT | Golden Compact | commercial route + durable guild/economic leverage + sufficient treasury/economic stability |
| END_PEOPLES_CHARTER | People's Charter | civic legitimacy + institutional/civic route + durable public participation + no authoritarian/collapse blocker |
| END_BROKEN_DIADEM | Broken Diadem | deterministic terminal failure predicate with unresolved major crises/institutional breakdown |
| END_QUIET_THRONE | Quiet Throne | explicit withdrawal/abdication/low-intervention history + no stronger positive ending |
| END_SECOND_FOUNDER | Second Founder | investigation/archive evidence + `pred.systemic_explanation_verified` + `pred.coalition_cooperation` + constitutional redesign + constrained/expired emergency power |

## Deterministic precedence order

The resolver must evaluate in this exact semantic order, with the final positive-ending order represented as authored data rather than hard-coded code order:

1. Validate terminal state and save version.
2. Evaluate collapse/failure predicates.
3. Evaluate explicit withdrawal / Quiet Throne condition.
4. Evaluate all positive ending qualification predicates.
5. If multiple positive endings qualify, apply an explicit authored priority table.
6. Record one immutable ending identity.
7. Never mutate prior history or invent a prerequisite to force an ending.

## Test matrix

| Test | State construction | Expected result | Status |
|---|---|---|---|
| P01 | Complete Steward prerequisites; no blockers | Steward | BLOCKED — runtime not implemented |
| P02 | Complete Steward prerequisites through alternate institutional path | Steward | BLOCKED — alternate path producers not fully closed |
| P03 | Steward prerequisites + permanent emergency authority | Not Steward; another qualified result or failure according to authored state | BLOCKED |
| P04 | Complete Iron Crown prerequisites; no collapse | Iron Crown | BLOCKED |
| P05 | Iron Crown prerequisites + independent constitutional reform blocker | Not Iron Crown unless explicit preserving condition exists | BLOCKED |
| P06 | Complete Golden Compact prerequisites; stable economy | Golden Compact | BLOCKED |
| P07 | Golden Compact route + terminal economic collapse | Not Golden Compact | BLOCKED |
| P08 | Complete People's Charter prerequisites; no authoritarian/collapse blocker | People's Charter | BLOCKED |
| P09 | People's Charter route + terminal authoritarian condition | Not People's Charter | BLOCKED |
| P10 | Complete Second Founder prerequisites; constrained/expired emergency power | Second Founder | BLOCKED — systemic/coalition producers still require closure |
| P11 | Second Founder evidence + only `history.cross_faction_package`, without `pred.coalition_cooperation` | Not Second Founder | BLOCKED |
| P12 | Explicit withdrawal + no stronger positive ending | Quiet Throne | BLOCKED |
| P13 | Low trust/low power only, without withdrawal history | Not Quiet Throne | BLOCKED |
| P14 | Two or more unresolved major crises + deterministic failure predicate | Broken Diadem | BLOCKED — failure predicate not frozen |
| P15 | Low trust only, no deterministic collapse predicate | Not Broken Diadem | BLOCKED |
| P16 | Simultaneous Steward + People's Charter qualification | Authored priority decides deterministically | BLOCKED — priority table not yet authored |
| P17 | Simultaneous Golden Compact + Second Founder qualification | Authored priority decides deterministically | BLOCKED — priority table not yet authored |
| P18 | Simultaneous positive ending + explicit collapse predicate | Collapse/failure wins according to contract | BLOCKED |
| P19 | Explicit Quiet Throne + positive ending | Quiet Throne wins only if positive ending is not stronger/qualified under authored precedence | BLOCKED |
| P20 | Same state/history/seed/data executed twice | Identical ending identity and immutable ending history | BLOCKED — engine absent |
| P21 | Save/load immediately before ending resolution | Same ending as uninterrupted run | BLOCKED — save/load runtime absent |
| P22 | Delayed consequence resolves immediately before ending | Ending reflects resolved callback exactly once | BLOCKED — callback runtime absent |
| P23 | Delayed consequence is cancelled/superseded before ending | Cancelled callback cannot alter ending | BLOCKED — lifecycle contract still open for several callbacks |
| P24 | Replay starts from prior run with pending callbacks/active crises | New run does not inherit run-local state | BLOCKED — replay runtime absent |
| P25 | Replay transfers an explicitly authored `meta.*` discovery | Only the declared `meta.*` effect influences current run | BLOCKED — explicit producers/keys not yet closed |
| P26 | Replay has ordinary `hist.*`, `thread.*`, or `pred.*` state from prior run but no `meta.*` transfer | Prior run state does not leak | BLOCKED |
| P27 | Invalid/stale identifier `thread.border` supplied to ending resolver | Must not alias to `thread.border_crisis` | BLOCKED — validator absent |
| P28 | `thread.guild` supplied where commercial route is required | Must not alias to `thread.ivo_market` | BLOCKED |
| P29 | `four_way_bargain` supplied without `pred.coalition_cooperation` | Must not qualify coalition prerequisite | BLOCKED |
| P30 | `systemic_explanation_verified` supplied without canonical `pred.` namespace | Must not qualify Second Founder | BLOCKED |

## Required authored priority table

Before runtime implementation, the data contract must explicitly declare a priority for any pair of positive endings that can simultaneously qualify. At minimum, the implementation QA must test:

- Steward × People's Charter
- Steward × Golden Compact
- Steward × Iron Crown
- Golden Compact × People's Charter
- Golden Compact × Second Founder
- People's Charter × Second Founder
- Iron Crown × Steward
- Iron Crown × People's Charter
- Quiet Throne × every positive ending
- Broken Diadem × every positive ending

A priority value must be data, not inferred from source file order, event ID, enum order, or code branch order.

## Independence requirements

A test is not sufficient if it proves an ending only through one character relationship score or one terminal event. Each major ending must have at least two authored viable paths where the narrative design requires path resilience.

## Negative-control requirements

Every positive ending test suite must contain at least one near-miss state that differs by exactly one required prerequisite and one blocker state. This prevents accidental qualification from broad route names, stale aliases, or partial evidence.

## Delayed-consequence interaction

Ending tests must include callbacks from E127–E130, E141, E181–E185 and E242–E246 whenever those callbacks can modify a qualification predicate, blocker, history marker or route state. Each callback must have a deterministic identity and exactly-once behavior before it can be trusted by the ending resolver.

## Replay interaction

Replay tests must distinguish run-local state from explicit `meta.*` transfer. Pending callbacks, active crisis predicates, unresolved crises, ordinary history, threads and ordinary predicates are run-local. Only an authored `meta.*` contract can cross the replay boundary.

## Exit criteria

This matrix is considered **VERIFIED** only when:

1. every test case has an executable state fixture;
2. all referenced producers are canonical and source-closed;
3. all ending prerequisites and blockers are machine-readable;
4. authored priority is explicit and deterministic;
5. delayed callbacks used by the tests have complete lifecycle contracts;
6. replay transfer keys are explicit;
7. the same state/history/seed/data produces the same ending repeatedly;
8. save/load and replay tests pass without state leakage;
9. no stale alias can manufacture an ending prerequisite.

Until these gates pass, this document is a QA contract and not evidence that ending reachability is verified.

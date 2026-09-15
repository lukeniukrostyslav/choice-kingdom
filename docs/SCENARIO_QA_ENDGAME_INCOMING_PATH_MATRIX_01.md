# Choice Kingdom — Scenario QA Endgame Incoming-Path Matrix 01

Status: **SOURCE-LEVEL QA — ENDGAME PATH GATE**  
Scope: E261–E272 and seven authored ending families.  
Date: 2026-09-15.

## Purpose

Bound the incoming-path problem for the endgame without claiming gameplay reachability. The event graph is a causal design map; it does not by itself prove that every ending can be reached from a fresh run.

## Endgame spine

`E261 -> E262/E263/E264/E265`  
`E262 -> E263/E265`  
`E263 -> E265/E266`  
`E264 -> E265/E267`  
`E265 -> ending qualification`

Support evidence routes:

- E266 → ending qualification
- E267 → Iron Crown / Steward / People's Charter support
- E268 → Steward / Golden Compact / People's Charter support
- E269 → Golden Compact / Second Founder / legitimacy support
- E270 → Second Founder / coalition / information qualification

E271/E272 are border-crisis lifecycle nodes and remain in production scope; they do not become ending predicates merely through graph proximity.

## Ending-family contract boundary

| Ending family | Required closure | Current boundary |
|---|---|---|
| Steward | positive institutional/civic prerequisites + blockers + precedence + fresh-run path | OPEN |
| Iron Crown | positive authority/security route + blockers + precedence + fresh-run path | OPEN |
| Golden Compact | economic/faction legitimacy route + blockers + precedence + fresh-run path | OPEN |
| People’s Charter | final charter prerequisites + coalition/constitutional support + blockers | OPEN |
| Broken Diadem | failure conditions + precedence + deterministic fallback | OPEN |
| Quiet Throne | qualifying withdrawal/stability state + blockers + precedence | OPEN |
| Second Founder | replay/meta qualification + systemic explanation support + fresh-run/replay separation | OPEN |

## Hard endgame rules

1. `four_way_bargain` from E261 is not by itself `pred.coalition_cooperation`.
2. E267–E270 are support evidence and cannot silently become final predicates.
3. E209 remains the consumer-only source for final-charter prerequisites until an explicit producer is authored.
4. Replay qualification cannot be satisfied by ordinary history flags.
5. Ending precedence must be deterministic when multiple positive families qualify.
6. Every ending family needs at least one satisfiable fresh-run route; replay-required endings additionally need an isolated replay route.
7. E33/E34 remain quarantined and cannot be used to fill missing endgame prerequisites.

## Next closure task

Extract the exact positive and negative authored conditions for each ending family, then compare them with incoming graph paths. The comparison must report missing producers, circular/self-manufactured prerequisites, mutually exclusive conditions, and paths that are structurally present but semantically unsatisfied.

**No ending is declared reachable from this matrix.**

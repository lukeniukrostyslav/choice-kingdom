# Choice Kingdom — Full Reachability Closure Matrix E01–E272

Status: **STATIC CLOSURE MATRIX — NOT RUNTIME VERIFIED**

This document consolidates the completed source-level producer/consumer audits. It is a closure map, not engine data. A row is `OPEN` when the authored source is known but its machine-safe predicate, delay contract, or runtime path is not yet proven.

| Range | Producer inventory | Main consumers / chain | Closure state |
|---|---|---|---|
| E01–E14 | petition, emergency decree, grain, accounts, guard, noble, market, merchant, audit, military, Amara, Toma, market-reform producers | E06–E14, E19, E21, E23–E28, later faction routes | OPEN — prose timing + route predicates |
| E15–E34 | diplomacy, border survey, steel, bridge, price, soldier, evidence, festival, ledger, auditor, witness, forgery, winter, warehouse, mobilization, crisis, emergency, people | E35+, E61–E67 and later expansion | OPEN — derived crisis predicates + delays |
| E35–E70 | constitutional, faction, welfare, evidence, military and ending producers | E61–E70, later expansion consumers | OPEN — ending qualification + replay/history |
| E71–E110 | expansion producer inventory audited | E111+, investigation/evidence, guild, Amara, military, border and coalition routes | OPEN — cardinality, delayed identity, route predicates |
| E111–E150 | institutional/faction producers audited | E151–E210 and late coalition/constitution | OPEN — derived predicates |
| E151–E180 | audit, noble, guild, border, Amara, Toma, witness producers audited | E181–E210 | OPEN — transport/food/coalition semantics |
| E181–E210 | delayed callbacks, institutional, military, guild, border, final constitutional producers | E207–E210 and E211+ | OPEN — delay/replay and convergence contracts |
| E211–E250 | exact producer inventory + reachability pre-audit | E251+ and ending convergence | OPEN — institutional/food/guild/evidence predicates |
| E251–E272 | exact producer inventory; E271 declaration and E272 resolution lifecycle | late crisis/endgame consumers | OPEN — route identities + runtime reachability |

## Canonical lifecycle checks

### Border crisis
`E271-A declaration` → active border crisis → `E272-A/B resolution` → resolved history retained + active predicate cleared.

E195/E253/E255 are consumers of the active crisis and are not producers. Any implementation that lets those consumers create the crisis is invalid.

### Guild logistics
E136-B produces immutable `history.guild_logistics_cooperation`. E194 consumes it and qualifies the later logistics predicate with neutral inspectors and absence of unresolved immunity risk. The E194 predicate must not be satisfied by the history marker alone.

### Mara semantics
E36 `mara_independent_mandate` and E95 `mara_independence` are separate facts. E226 is a later institutional-stress test and must not overwrite the earlier fact identity.

### Ivo evidence
E55 is an early guild-books evidence node. E269 is a late commercial evidence handoff. They are semantically distinct and must remain distinct in replay/history.

### Investigation evidence
Evidence cardinality must operate on independent source identities. A count of raw flags is invalid when multiple flags originate from the same evidence chain.

## Global blockers before production schema freeze

1. Freeze all derived predicates and their exact inputs.
2. Freeze relationship-route qualification separately from relationship numeric values.
3. Freeze delayed consequence identity, due-turn, cancellation/invalidation and exactly-once behavior.
4. Freeze replay-only metadata and previous-run callbacks.
5. Freeze evidence-source identity/cardinality.
6. Freeze ending qualification and deterministic precedence.
7. Resolve remaining prose triggers and any producerless durable consumer states.
8. Re-run this matrix against machine-readable catalog once the contract is frozen.

## Gate

Source inventories: **COVERED E01–E272**.

Static closure: **PARTIAL / OPEN**.

Runtime reachability: **NOT VERIFIED**.

Production schema: **BLOCKED until closure contracts freeze**.

Validator: **BLOCKED until production schema freeze**.

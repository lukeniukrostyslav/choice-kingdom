# Choice Kingdom — Graph ↔ Catalog Reconciliation 01

Status: **AUDIT CHECKPOINT — DESIGN GRAPH NOT YET CANONICAL**
Scope: E71–E110 first-pass verification, with implications for later graph integration.

## Purpose

`EVENT_GRAPH.md` is explicitly a design-level causal map. This audit compares representative graph edges against the actual authored event triggers/effects so that graph edges are not mistaken for runtime dependencies.

## Verified discrepancies / corrections

| Graph claim | Catalog evidence | Finding | Required action |
|---|---|---|---|
| `E73 -> E94/E105` | E73 produces `named_authority` or `overlapping_authority`; E94 requires `Ivo >= 2 + ledger chain`; E105 requires `land_weighted_council` or `Seris >= 2` | No direct producer-consumer dependency proven | Keep as design candidate only; do not compile as runtime edge |
| `E75 -> E86` | E75 produces `crossing_fund` or `guild_social_contract`; E86 requires `quiet_accounts` or `ledger_secret` | No direct dependency proven | Remove from canonical runtime graph unless an intermediate causal contract is authored |
| `E81 -> E88 -> E89 -> E90` | E81 produces handwriting evidence; E88 requires `Rowan >= 2`; E89 requires `noble_advisory_council` or `noble_transition`; E90 requires `lantern_funded` or `lantern_network` | Chain is not a producer-consumer chain | Preserve only as thematic/design adjacency; runtime edges must follow actual conditions |
| `E90` described as systemic-corruption fork | E90 is `The Healer's Exception`; systemic-vs-conspiracy choice is E100 | Graph annotation is factually wrong | Correct graph commentary; systemic/conspiracy fork belongs to E100 |
| `E93 -> E100` | E93 produces `duplicate_invoice_witness` or `duplicate_invoice_arrest`; E100 requires at least three independent evidence routes | E93 can contribute evidence, but cannot alone prove the edge | Represent E93 as one possible evidence producer, not deterministic prerequisite |
| `E94 -> E105` | E94 produces merchant-book outcomes; E105 is gated by noble council/Seris | No direct dependency proven | Do not compile as runtime edge |

## Canonical interpretation rule

A graph edge is eligible for production only when at least one of the following is true:

1. target trigger directly consumes a flag/history/thread produced by the source;
2. target trigger explicitly counts source completion/history;
3. source schedules a delayed consequence that activates the target;
4. a documented derived predicate aggregates the source's durable effect and the aggregation is defined in the canonical predicate matrix.

Thematic similarity, same-act placement, shared character, or conceptual relevance is not sufficient.

## Immediate normalization findings

- `systemic corruption` is not an E90 state; E100 is the authored systemic-vs-conspiracy decision.
- `evidence route` must become a canonical history/thread contribution and must support deterministic cardinality for E100.
- `lantern_funded` / `lantern_network` are valid producers for E90; they must not be replaced by generic character affinity.
- `noble_advisory_council` / `noble_transition` are the valid E89 gates.
- `Ivo >= 2` and `ledger chain` must remain separate canonical predicates for E94.

## Scope limitation

This is not yet the complete E01–E270 graph audit. It intentionally records only source-verified findings from the first E71–E110 pass. The next passes must cover E111–E150, E151–E210 and E211–E270, then compare every remaining graph edge with its target trigger and source effect.

## Gate impact

- Graph/catalog reconciliation: **in progress**.
- Production graph: **blocked**.
- Production data schema: **blocked**.
- Decision engine: **must not compile this design graph directly**.
- Reachability simulation: waits for canonical event/trigger representation.

## Next checks

1. Audit all E71–E110 edges against every choice effect and trigger.
2. Record valid, invalid and conditional edges separately.
3. Repeat for E111–E150.
4. Repeat for E151–E210.
5. Repeat for E211–E270.
6. Reconcile ending qualification edges only after canonical predicates are locked.
7. Generate machine-readable graph only after the catalog has a stable canonical ID and trigger contract.

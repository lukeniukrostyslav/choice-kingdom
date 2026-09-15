# Choice Kingdom — S12.3 Canonical Invariant Audit 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — PARTIAL PASS**  
Frozen production scope: **E01–E272**. E273–E277 are excluded.

## Purpose

This pass converts the latest producer/consumer registry into an explicit invariant audit before exhaustive reachability. It is QA-only and is not production runtime data.

## Invariants checked

| Invariant | Result | Evidence / rule |
|---|---|---|
| Production scope excludes E273–E277 | PASS | No excluded event may create a production producer, consumer, delay or reachability edge. |
| Consumer cannot manufacture own prerequisite | PASS | E194, E197, E209 and E210 remain consumer/convergence boundaries. |
| Transport active/clear lifecycle | PASS at source level | E32 activates `pred.transport_disruption`; E136-A/B clear/recover. |
| Border active/clear lifecycle | PASS at source level | E271-A activates `pred.border_crisis`; E272-A/B resolve. |
| Recovery cannot silently reactivate crisis | PASS | E136 recovery is a clear operation, not an activation alias. |
| Food stability has an admitted in-scope producer | FAIL / OPEN | No E01–E272 producer verified for `pred.food_stable`. |
| Relationship score substitutes for guild influence | REJECTED | `rel.ivo` is not `pred.guild_influence_strong`. |
| Four-way bargain substitutes for coalition cooperation | REJECTED | E261 alone cannot qualify positive coalition cooperation. |
| Security substitutes for border crisis | REJECTED | `resource.security` is not an active crisis marker. |
| Ordinary run state substitutes for replay meta | REJECTED | Only explicitly authored `meta.*` may cross replay boundary. |
| Final-charter consumer creates prerequisites | REJECTED | E209 consumes; it does not produce its own qualification. |
| Convergence node creates missing prerequisites | REJECTED | E210 is convergence-only. |
| Delayed callback has complete executable identity | FAIL / OPEN | Remaining E184/E245/E246 and later families still need exact source/target/timing/cancellation closure. |
| Ending incoming paths fully enumerated | FAIL / OPEN | S11 and S12 still require exhaustive incoming-path proof and deterministic precedence. |
| Fresh-run reachability proven | FAIL / OPEN | Canonical initial-state graph has not yet been exhaustively executed. |
| Replay reachability proven | FAIL / OPEN | Representative meta producer/key inventory remains incomplete. |

## Canonical lifecycle boundaries

### Transport

`E32 → active pred.transport_disruption → E192 consumers → E136-A/B clear/recovery`.

The active state is cycle-scoped. Historical occurrence and current active state must remain distinct. A recovery result cannot be interpreted as a future activation without a separately authored producer.

### Border

`E271-A → active pred.border_crisis → E195/E253/E255 consumers → E272-A/B resolution`.

Resolution produces historical outcome markers but does not leave the active predicate true.

## Open producer classes

The following remain explicitly open rather than receiving guessed aliases:

- `pred.food_stable`;
- exact formula/producers for `pred.guild_influence_strong`;
- exact evidence IDs for `pred.systemic_explanation_verified`;
- exact participant/positive-outcome proof for `pred.coalition_cooperation`;
- exact independent-domain evaluation for `pred.constitutional_prepared_strong`;
- `pred.final_charter_prerequisites` incoming set;
- replay `meta.*` producers/keys for E247/E248/E270;
- remaining delayed source/target/timing/cancellation contracts;
- deterministic negative/failure producer sets for ending qualification.

## Machine-check specification for next pass

The exhaustive inventory must produce one row per concrete edge with at least:

`source_event_id | source_choice_id | output_token | token_namespace | consumer_event_id | trigger_token | producer_status | delayed_identity | timing | cancellation_rule | replay_scope`

Required checks:

1. Event IDs are within E01–E272.
2. Every consumer trigger has zero, one or more explicitly qualified producers.
3. Zero-producer consumers are classified OPEN, not fabricated.
4. Multiple producers are checked for semantic compatibility.
5. Contradictory writers are flagged.
6. Cycles are checked independently from ordinary causal chains.
7. Active and historical lifecycle tokens are not conflated.
8. Delayed callbacks cannot manufacture eligibility predicates.
9. Replay state is isolated unless explicitly marked `meta.*`.
10. Every ending has at least one independent incoming qualification path.

## Gate

**S12.3: PARTIAL PASS.**

The invariant boundary is now explicit and machine-checkable, but this does not constitute exhaustive E01–E272 reachability. Production schema and Decision Engine remain blocked.

## Next autonomous block

Build the exhaustive E01–E272 producer/consumer edge inventory from authoritative authored catalogs, then run duplicate/contradiction/cycle checks and reconcile ending incoming paths. Continue exact source extraction for E218/E225 and E251–E272 before production-contract freeze.

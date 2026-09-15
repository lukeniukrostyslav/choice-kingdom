# Choice Kingdom — Undefined Consumer Classification 01

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Status: **SOURCE-LEVEL TRIAGE — NOT PRODUCER PROMOTION**

## Purpose

The exhaustive source inventory is now green and reports 59 trigger tokens with no machine-extracted producer. This document classifies only cases for which an authoritative source-level status is already available. It does **not** invent producers and does not convert prose into runtime state.

## Machine baseline

Fresh `Choice Kingdom Scenario Source Inventory` run `35024365701` on commit `d33325c39ed5cf4876c6d236357a42434c27d038`:

- 272/272 authored events present.
- 243 unique output tokens.
- 90 trigger tokens.
- 3 duplicate output tokens.
- 1 cross-event semantic writer collision.
- 2 same-event shared-writer tokens.
- 59 undefined consumers.
- 8 undefined predicate consumers.
- 0 predicate dependency cycles.

## Authoritatively classified undefined predicate consumers

| Token | Source-level classification | Runtime status |
|---|---|---|
| `pred.transport_disruption` | E32 active source; E136-A/B recovery/clear boundary | OPEN lifecycle/persistence |
| `pred.border_crisis` | E271-A declaration; E272-A/B resolution | OPEN lifecycle/runtime |
| `pred.systemic_explanation_verified` | E232–E236 evidence families + E270-A explicit convergence | SOURCE-CLOSED / runtime OPEN |
| `pred.coalition_cooperation` | E148-A + E261-A cooperation-package candidates | PARTIAL / sources frozen |
| `pred.constitutional_prepared_strong` | four independent preparation domains; source families frozen | PARTIAL / anti-double-counting and reachability open |
| `pred.guild_influence_strong` | representation + tribunal + market/credit + logistics domains | PARTIAL / sources frozen |
| `pred.final_charter_prerequisites` | E197/E198/E199/E202–E209 candidates | CONTRACT FROZEN / producers open |
| `pred.border_tension` | No canonical producer is currently frozen in the producer/consumer registry | OPEN / producer not verified |

The first seven rows have explicit registry evidence; `pred.border_tension` remains genuinely unresolved. No E273–E277 source is admitted.

## Authoritatively classified non-predicate trigger forms

The inventory also contains trigger forms that are source-level facts but are not emitted as machine backtick output tokens in the same form. These are retained as **source-backed non-token facts**, not promoted automatically:

- `history.house_assembly` — E161-A source in the canonical registry.
- `people_charter_endorsed` — E50-A source in the canonical registry.
- `guild_political_representation` — E49-A source in the canonical registry.
- `history.cross_faction_package` — verified E148-A producer and therefore not an unresolved canonical producer despite parser-shape differences elsewhere.
- `thread.amara_civic`, `thread.endgame_convergence`, `thread.final_constitutional_phase`, `thread.military_constitutional`, `thread.toma_information` — source-level route/thread families whose runtime qualification remains contract-bound.

These rows require contract-aware extraction or explicit machine mapping before they can be considered executable state. The inventory remains deliberately conservative.

## Stale/noncanonical forms detected by inventory

- `thread.border` is prohibited in favor of canonical `thread.border_crisis`.
- `thread.border_crisis = active` is a prose predicate expression, not a canonical producer token.

Neither form is promoted into runtime state.

## Remaining unresolved set

The remaining undefined consumers are not automatically failures. They are divided into three follow-up classes:

1. **Source-backed non-token facts** — require a canonical machine mapping.
2. **Stale/prose aliases** — require normalization to the canonical vocabulary or explicit rejection.
3. **Genuinely unresolved producers** — remain OPEN until an E01–E272 event/choice source is verified.

## Hard rules

- Never use an undefined consumer as proof that a producer exists.
- Never use E273–E277 to close an E01–E272 gap.
- Never promote a stale alias merely because it appears in an older narrative or graph artifact.
- A source-level producer is not runtime-closed until its lifecycle, invalidation, persistence and replay semantics are separately verified where applicable.
- This audit does not claim fresh-run reachability, replay reachability, ending execution or engine behavior.

## Next QA block

Resolve the remaining 59 undefined consumers by direct authoritative catalog inspection, starting with the single cross-event semantic writer collision and the stale/prose trigger forms. Then reconcile only verified results into the canonical producer/consumer registry and rerun the exhaustive inventory.

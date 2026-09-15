# Choice Kingdom — Undefined Consumer Classification 01

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Status: **SOURCE-LEVEL TRIAGE — ACTIVE CLOSURE**

## Purpose

The exhaustive source inventory is the machine baseline. This document classifies undefined trigger forms only where an authoritative source-level decision can be made without inventing producers or converting prose into runtime state.

## Verified closure updates

### S21 — `history.guild_logistics_cooperation` semantic collision

Authoritative inspection established that E136-B is the durable cooperation producer and E194-A repeats that upstream marker while introducing neutral-inspector evidence. E194-A is therefore an **idempotent reaffirmation**, not a second independent semantic writer. The machine inventory was hardened to recognize this explicit exception; the subsequent source-inventory verification reported `semantic_writer_collisions=0` and `reaffirmed_tokens=1`.

### S22 — stale/prose border trigger normalization

Two previously unresolved trigger forms are now formally classified and frozen as **noncanonical evidence**, not missing producers:

| Raw trigger form | Canonical treatment | Producer status |
|---|---|---|
| `thread.border` | reject as stale alias; use `thread.border_crisis` | **REJECTED / NOT A PRODUCER** |
| `thread.border_crisis = active` | reject as prose predicate expression; use canonical `pred.border_crisis` lifecycle | **REJECTED / NOT A PRODUCER** |

These forms remain visible in raw consumer evidence for auditability. They must not be promoted into executable state merely to make the inventory appear more complete.

## Machine baseline before normalization

The prior exhaustive inventory established:

- 272/272 authored events present.
- 243 unique output tokens.
- 90 trigger tokens.
- 3 duplicate output tokens.
- 1 cross-event semantic writer collision, subsequently closed by S21 as an explicit reaffirmation.
- 2 same-event shared-writer tokens.
- 59 undefined consumers.
- 8 undefined predicate consumers.
- 0 predicate dependency cycles.

The next inventory must distinguish the two rejected border forms from the genuinely unresolved producer set rather than silently deleting their raw evidence.

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

## Rejected stale/prose forms

- `thread.border` is prohibited in favor of canonical `thread.border_crisis`.
- `thread.border_crisis = active` is a prose predicate expression, not a canonical producer token.

Both are now frozen as explicit **rejections**, not unresolved producers and not executable state.

## Remaining unresolved set

The remaining undefined consumers are divided into three classes:

1. **Source-backed non-token facts** — require a canonical machine mapping.
2. **Genuinely unresolved producers** — remain OPEN until an E01–E272 event/choice source is verified.
3. **Runtime-only lifecycle/predicate forms** — source evidence may be closed while lifecycle, persistence, invalidation, ordering or reachability remains OPEN.

The stale/prose border forms are no longer part of class 2.

## Hard rules

- Never use an undefined consumer as proof that a producer exists.
- Never use E273–E277 to close an E01–E272 gap.
- Never promote a stale alias merely because it appears in an older narrative or graph artifact.
- A source-level producer is not runtime-closed until its lifecycle, invalidation, persistence and replay semantics are separately verified where applicable.
- A rejected alias remains auditable in raw inventory evidence.
- This audit does not claim fresh-run reachability, replay reachability, ending execution or engine behavior.

## Next QA block

Continue direct authoritative inspection of the remaining undefined consumers, prioritizing source-backed non-token facts and the eight predicate contracts. Reconcile only verified results into the canonical producer/consumer registry, then run the exhaustive inventory again. After source closure, proceed to delayed lifecycle, replay, ending precedence and fresh-run/replay reachability gates.

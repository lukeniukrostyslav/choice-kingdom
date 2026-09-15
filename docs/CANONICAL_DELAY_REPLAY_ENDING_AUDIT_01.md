# Choice Kingdom — Canonical Delay / Replay / Ending Audit 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — CONTRACT CLOSURE PASS
Scope: E01–E277

## Objective

Freeze the QA requirements for delayed consequences, replay isolation and ending qualification before any runtime implementation.

## Delayed Consequences

Every delayed consequence must carry the canonical identity tuple:

`sourceEventId + sourceChoiceId + consequenceId + earliestTurn + resolutionTarget + exactlyOnceKey + cancellationOrSupersessionRule`

The audit must reject:
- vague timing such as `later` or `5+ turns` without normalized earliest turn;
- callback execution without an exact source choice;
- duplicate execution after save/load;
- callbacks surviving an explicit cancellation/supersession branch;
- callbacks manufacturing a derived predicate that has no qualifying producer;
- replay runs inheriting pending callbacks from a previous run.

## Replay Isolation

A new run must start with no mutable pending-delay queue, no transient active crisis markers, no unresolved callback execution state and no previous-run-only flags unless the canonical replay contract explicitly identifies them as historical seed data.

Historical facts may be retained only where the authored replay design explicitly requires them; active-cycle predicates must not leak between runs.

## Ending Qualification

Ending evaluation must be predicate-based and causal. An ending consumer cannot manufacture missing prerequisites.

The final-charter/endgame gate must distinguish:
- civic/commons preparation;
- institutional/audit preparation;
- faction/house/guild preparation;
- military/security preparation where applicable;
- information/evidence legitimacy;
- explicit coalition cooperation and positive outcome;
- mandatory blockers and unresolved crisis state.

A route count, relationship score or generic high-resource state cannot substitute for an explicit qualifying source.

## Current Status

Delayed Consequences: PARTIAL.
Replay Design: PARTIAL.
Ending Qualification: PARTIAL.

No runtime/schema promotion is permitted from this document alone. Exact event-by-event delay extraction, normalized timing, cancellation keys, replay reset semantics and final ending consumer reconciliation remain required before runtime contracts are frozen.

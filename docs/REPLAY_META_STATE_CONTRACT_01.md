# Choice Kingdom — Replay Meta-State Contract 01

Date: 2026-09-15
Status: CANONICAL DESIGN CONTRACT — PRE-RUNTIME
Scope: replay boundary, E265–E270 ending qualification, delayed consequences

## Purpose

Define exactly what may cross from a completed run into a new run. Replay information must add variation without allowing mutable state from the previous run to contaminate the new campaign.

## State classes

### Never transferred

- current resource values (`gold`, `trust`, `security`, `power`, `reputation`);
- character relationship scores;
- active `thread.*` state;
- active `pred.*` cycle state;
- unresolved crisis state;
- pending delayed callbacks;
- callback execution markers;
- cancellation/supersession state;
- current turn;
- current event availability/unlock state;
- temporary run-local flags.

### Transfer only through explicit `meta.*`

Replay discoveries may cross the boundary only when an authored replay rule explicitly writes a `meta.*` value. Examples include a discovered evidence variant, replay-exclusive clue, deliberately unlocked narrative perspective, or canonical replay achievement used to alter future availability.

A `meta.*` value is metadata, not an implicit replacement for `hist.*`, `thread.*`, or `pred.*`.

### Immutable run record

A completed run may retain an immutable record for analytics/debugging and ending history, but that record must not be interpreted as active gameplay state in the next run unless an explicit transfer rule exists.

## Delayed consequence boundary

At run creation:

- pending-delay queue = empty;
- resolved-delay keys = empty;
- cancellation/supersession registry = empty;
- active-cycle predicates = empty;
- unresolved crisis registry = empty.

A completed run's pending callback queue is never copied into the next run.

## Ending boundary

Ending qualification in the new run may inspect only:

1. current-run state/history;
2. explicit `meta.*` values allowed by the replay contract;
3. canonical authored event data.

An ending consumer must never treat the previous run's ending as a prerequisite for the current run unless an explicit replay rule says so.

## Save/load invariants

Save/load within the same run must preserve all active mutable state and pending callbacks exactly. Loading a save is not a replay reset.

Starting a new run is a hard mutable-state reset followed by application of allowed `meta.*` seed data.

## Determinism

For identical canonical content version, seed, current-run state/history, explicit `meta.*` transfer set, and event data, ending qualification and delayed-consequence scheduling must produce identical results.

## QA cases

- fresh run contains no previous-run callback;
- fresh run contains no previous active crisis;
- explicit meta transfer survives new-run initialization;
- meta transfer cannot satisfy a predicate without an authored consumer rule;
- save/load preserves a scheduled callback exactly once;
- cancelled callback cannot execute after reload;
- previous ending cannot silently force current ending;
- active `pred.*` state never survives a replay reset.

## Gate

**Replay mutable-state isolation: contract closed.**

**Exact authored `meta.*` transfer inventory: OPEN.**

**Runtime implementation: NOT STARTED.**

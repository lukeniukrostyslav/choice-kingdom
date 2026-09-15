# Choice Kingdom — Transport Disruption Reconciliation 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — NOT RUNTIME DATA**

## Canonical lifecycle currently proven

### Producer / activation
**E32 — Three Fires** explicitly establishes `pred.transport_disruption` for the current compound-crisis cycle and records `history.transport_disruption_declared`.

This is a source-level state transition. The predicate must not be inferred from low gold, low security, border pressure, winter, or from E192.

### Recovery / clear
**E136 — The Frozen Road** is the explicit authored repair producer:
- E136-A public labor effort → `transport_network_stable`; clears `transport_disruption_active`.
- E136-B guild transport → `transport_network_stable`; clears `transport_disruption_active`; also records `history.guild_logistics_cooperation`.

The source text therefore establishes the intended recovery semantics and preserves historical cooperation evidence separately from the active transport state.

### Consumer
**E192 — The Broken Cart** consumes `pred.transport_disruption`. It must not create the predicate merely because medicine/grain movement is impaired.

E192 branches into local consequences (`food_logistics_unstable` or `food_logistics_stabilized`) and character pressure; these are downstream effects, not replacement transport lifecycle producers.

### Candidate future recovery
**E277** is an authored candidate that can establish broader transport stability and clear disruption. It remains outside the frozen E01–E272 catalog. It must not be admitted as a competing recovery producer until the E136 recovery semantics, reachability and duplicate-producer checks are complete.

## Important distinction

`transport_network_stable`, `transport_disruption_active` and `pred.transport_disruption` are not automatically interchangeable. The production schema must define whether the active predicate is the canonical runtime representation and whether the legacy/author-facing names are aliases, historical markers, or separate state. The source evidence currently proves the lifecycle relationship but not the final runtime field mapping.

## Cycle semantics

The source explicitly describes a **current compound-crisis cycle** and permits a later authored disruption after recovery. Therefore the runtime contract must be cycle-aware:

1. E32 activates one disruption cycle.
2. E136-A/B resolves that active cycle.
3. Historical `history.transport_disruption_declared` remains queryable after recovery.
4. A later disruption may create a new active cycle without erasing prior history.
5. E192 must resolve only against the active cycle that exists when it fires.

## Open machine contracts

Still unresolved and must not be invented:
- exact cycle ID / active-instance identity;
- expiry semantics if no recovery event is chosen;
- whether E136 recovery is available once or repeatedly within one cycle;
- cancellation/supersession behavior for competing recovery choices;
- save/load representation of the active cycle;
- replay isolation;
- exact interaction between `transport_network_stable` and `pred.transport_disruption` in production schema;
- admission/rejection of E277;
- deterministic behavior if E192 and E136 become eligible in the same turn.

## QA gate

**Activation producer:** SOURCE CLOSED (E32).  
**Primary recovery producer:** SOURCE CLOSED (E136-A/B).  
**Consumer:** SOURCE CLOSED (E192).  
**Historical preservation:** SOURCE CLOSED.  
**Runtime lifecycle:** NOT IMPLEMENTED.  
**Cycle/persistence contract:** OPEN.  
**E277 admission:** OPEN.

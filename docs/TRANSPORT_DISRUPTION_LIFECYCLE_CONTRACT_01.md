# Choice Kingdom — Transport Disruption Lifecycle Contract 01

Status: **SOURCE-LEVEL RECONCILIATION — NOT ENGINE IMPLEMENTATION**

## Purpose

Freeze one canonical identity for the active transport-disruption condition before production schema work. The condition must not be represented by competing aliases.

## Canonical active identity

- Active predicate: `pred.transport_disruption`
- Historical declaration: `history.transport_disruption_declared`
- Recovery history: `history.transport_recovery_established`
- `transport_disruption_active` is a **legacy expansion-document alias only** and must not enter production state, save-state schema, exactly-once keys, or replay metadata.

## Producer / recovery lifecycle

1. **E32** is the current canonical authored producer for the first compound-crisis transport-disruption cycle.
   - establishes `pred.transport_disruption`;
   - records `history.transport_disruption_declared`;
   - does not infer the condition from gold, security, border pressure, or consumer reachability.
2. **E136-A/B** are authored recovery outcomes.
   - clear the active `pred.transport_disruption` cycle;
   - retain historical evidence;
   - E136-B may also establish `history.guild_logistics_cooperation` through the explicitly authored guild-transport outcome.
3. **E277-A/B** are later recovery candidates outside the E01–E272 canonical freeze.
   - they must not be runtime inputs until E273–E277 are integrated into the canonical catalog;
   - when integrated, their clear semantics must use the same canonical predicate identity.

## Cycle rules

- A recovery event clears the current active cycle; it does not erase `history.transport_disruption_declared`.
- A later authored producer may establish a new transport-disruption cycle, but cannot retroactively satisfy an earlier consumer.
- Current predicate and historical evidence are separate state concepts.
- No numeric resource may substitute for the authored predicate.

## QA gate before schema freeze

Verify, against the full integrated catalog:

- producer-before-consumer ordering;
- trigger reachability;
- clear/expiry behavior;
- exactly-once delay identity where transport disruption participates in delayed consequences;
- save/load preservation of active and historical identity;
- replay isolation;
- no remaining production use of `transport_disruption_active`.

## Current status

**Source producer:** CLOSED at E32.

**Lifecycle:** OPEN pending integrated recovery, expiry, persistence, delayed-consequence and replay verification.

**Runtime:** NOT IMPLEMENTED.

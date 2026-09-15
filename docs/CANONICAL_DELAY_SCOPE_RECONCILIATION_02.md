# Choice Kingdom — Canonical Delay Scope Reconciliation 02

Status: **P0 QA RECONCILIATION — DOCUMENTED FINDING, NOT ENGINE IMPLEMENTATION**

## Finding

The delayed-consequence inventory currently lists an `E31–E35` callback family, but the authoritative `docs/EVENT_CATALOG.md` was later reduced to a canonical boundary ending at E32. The prior E33–E40 ending block was removed from the canonical first-campaign file and later authored content is maintained in dedicated expansion catalogs.

Therefore the delay inventory must not treat E33–E35 as canonical source events until those IDs are explicitly reintroduced into the authoritative catalog. A delay reference to a non-canonical event is a source-of-truth defect, even if an older draft contained that event.

## Reconciliation rule

1. Canonical delay rows may reference only event IDs present in the authoritative production catalog or an explicitly integrated expansion catalog.
2. Historical/draft event IDs must be retained only as audit provenance, never as runtime source IDs.
3. E31–E32 remain candidates for delay extraction only after their exact current semantics and source choices are re-read.
4. E33–E35 are **not** currently canonical runtime source IDs.
5. The same rule applies to any other delayed row whose event ID was removed, renumbered, or moved outside the canonical catalog boundary.

## Impact

This does not change the authored story percentage by itself. It increases the precision of the delayed-consequence QA gate by removing stale source-ID assumptions before schema/runtime work begins.

## Gate

Before production delay schema freeze, reconcile every inventory row against the authoritative event catalog and expansion integration boundary. No stale event ID may enter engine data, save-state identity, exactly-once keys, or replay metadata.

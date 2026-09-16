# Production Catalog Projection Closure 01

Status: **LOCAL IMPLEMENTATION + VERIFICATION CLOSED**

## What was completed

The frozen authored E01–E272 catalog now has a deterministic machine-readable production-data projection at:

`docs/MACHINE_PRODUCTION_CATALOG_01.json`

The projection is generated mechanically from `AuthoredCatalog.from_repository`. It does **not** invent missing triggers, effects, routes, delays, predicates, endings, or UI semantics.

Each event record contains:

- event identity, title and authored trigger;
- authored event prerequisites;
- authoritative source file;
- every parsed authored choice;
- choice body text;
- resource deltas;
- relationship deltas;
- state tokens and clear tokens;
- explicit immediate unlock targets only.

The frozen scope is exactly E01–E272, with E273–E277 excluded.

## Verification

`tools/validate_production_catalog.py` recompiles the projection and compares the committed JSON to the deterministic authored projection.

Local result:

- events: **272**
- choices: **520**
- no-choice authored nodes: **13**
- excluded expansion nodes: **5**
- full test suite: **179 passed**

## Boundary

This closes the **machine-readable catalog projection** boundary. It does not claim that the entire campaign is already executable end-to-end. Remaining runtime work includes complete gameplay scenario semantics, special/no-choice node handling where required by authored design, exhaustive causal simulation, presentation/UI, localization/RTL, Android build/device QA, and release gates.

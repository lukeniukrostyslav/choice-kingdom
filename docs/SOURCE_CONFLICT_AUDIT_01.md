# Choice Kingdom — Source Conflict Audit 01

Date: 2026-09-14
Scope: E01–E70
Status: **BLOCKING CANONICALIZATION ISSUE — NOT CONTENT READY**

## Purpose

This audit records a direct conflict found by reading the authored source files themselves. It must be resolved before stable machine-readable IDs are generated.

## 1. E35–E40 numbering conflict

Two authored files currently assign different narrative nodes to the same stable IDs:

### `docs/EVENT_CATALOG.md`
The original catalog defines:
- E35 — The Last Council
- E36 — The Ledger Opens
- E37 — The Choice of Heir
- E38 — The Final Speech
- E39 — The Crown's Answer
- E40 — Epilogue: What Remains

### `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`
The expanded Act V source defines:
- E35 — The Day After Emergency
- E36 — Mara's Resignation
- E37 — Rowan's Oath
- E38 — Seris and the Old Houses
- E39 — Ivo's Last Bargain
- E40 — Amara's Winter List
- E41 onward — additional Act V / endgame nodes

The expanded file explicitly describes itself as a continuation of the original E01–E34 skeleton and is also the source used by the event graph for the E35+ expansion. However, the original catalog still contains executable-looking E35–E40 definitions.

## 2. Why this is blocking

Stable IDs cannot be generated while one ID can mean two different events. If both definitions are imported, the engine would have duplicate IDs. If one is silently discarded, authored content is lost without an explicit canonical decision.

This also affects existing audit material: a previous correction correctly withdrew several mistaken title claims, but it was based on one source view and did not resolve this broader ID collision.

## 3. Required canonical resolution

Before production schema generation:

1. Treat the expanded Act V file as the candidate current Act V source because it explicitly extends the E01–E34 skeleton and contains the E35–E70 expansion used by the graph.
2. Preserve the original E35–E40 material as authored legacy material until each concept is either merged into an expanded node or assigned a new stable ID.
3. Do **not** silently overwrite or delete the original nodes.
4. Update `EVENT_GRAPH.md`, `CONTENT_QA_MATRIX.md`, and all audit artifacts after the ID mapping is frozen.
5. Add a canonical mapping table such as `legacy_event_id -> canonical_event_id` where a legacy node survives under a new ID.
6. Re-run duplicate-ID, incoming-edge, outgoing-edge and ending-reachability checks after the mapping.

## 4. Other directly observed source-level risks

- E73 and E156 both use **The Widow's Petition** and need downstream/context comparison.
- E99 and E173 both use **The Empty Barracks** and need downstream/context comparison.
- E212 contains the authored token `clerk_discipled`, which is a likely spelling error and must be normalized before schema lock.
- Multiple sources use free-form route names (`institutional reform`, `commercial route`, `veteran route`, `Amara route`, `Toma route`, etc.) that still require canonical thread/predicate identities.
- Food, winter, border, market and information pressure are repeatedly expressed as prose predicates and are not yet deterministic runtime conditions.

## Gate

This finding increases QA coverage but does **not** increase implementation readiness. The project remains in narrative canonicalization. No engine or APK work should consume E35–E40 until the ID conflict is resolved explicitly.

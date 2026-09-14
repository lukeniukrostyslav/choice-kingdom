# Choice Kingdom — Event ID Reconciliation 03

Status: **CANONICAL RECONCILIATION DECISION — PRE-PRODUCTION**

## Scope

This resolves the direct E35–E40 collision between the original campaign catalog and the Act V expansion.

The source files must both remain intact during authoring review. No authored material is silently deleted.

## Source conflict

`docs/EVENT_CATALOG.md` contains:
- E35 — The Last Council
- E36 — The Ledger Opens
- E37 — The Choice of Heir
- E38 — The Final Speech
- E39 — The Crown's Answer
- E40 — Epilogue: What Remains

`docs/EVENT_CATALOG_ACT_V_EXPANSION.md`, explicitly described as the continuation of E01–E34, contains:
- E35 — The Day After Emergency
- E36 — Mara's Resignation
- E37 — Rowan's Oath
- E38 — Seris and the Old Houses
- E39 — Ivo's Last Bargain
- E40 — Amara's Winter List
- and subsequent Act V nodes through the endgame.

The graph uses the Act V identities in downstream edges. For example, E105 points to E37/E46/E52, while E37 in the Act V continuation is Rowan's Oath. Therefore the Act V continuation is the canonical production numbering for E35 onward.

## Canonical rule

### E01–E34
Keep the original `EVENT_CATALOG.md` IDs unchanged.

### E35–E270
Use `EVENT_CATALOG_ACT_V_EXPANSION.md` and subsequent expansion catalogs as the canonical production numbering.

This matches the documented statement that Act V is a continuation of E01–E34 and matches the current `EVENT_GRAPH.md` downstream identity model.

## Legacy ending material

The six original E35–E40 ending-resolution entries are not deleted. They become **legacy source material**, not executable production IDs.

Canonical semantic aliases for later migration:

| Legacy source ID | Legacy title | Production role |
|---|---|---|
| LEGACY-END-35 | The Last Council | Endgame proposal/convergence node; candidate input to E261–E265 |
| LEGACY-END-36 | The Ledger Opens | Ledger resolution; candidate evidence/ending input to E250/E265/E270 |
| LEGACY-END-37 | The Choice of Heir | Succession qualification; candidate input to E256 and ending qualification |
| LEGACY-END-38 | The Final Speech | Presentation/epilogue layer; must not independently alter ending |
| LEGACY-END-39 | The Crown's Answer | Legacy ending resolver specification; superseded by canonical E265–E270 qualification |
| LEGACY-END-40 | Epilogue: What Remains | Post-ending presentation; candidate replacement for final epilogue UI/content layer |

These aliases are semantic review identifiers only. They must not be accepted as runtime event IDs.

## Why this resolution is safe

1. It preserves every authored scene.
2. It prevents two different events from sharing one stable runtime ID.
3. It agrees with the Act V continuation contract.
4. It agrees with graph references that already use the Act V E35+ meanings.
5. It lets the old ending concepts be reused without allowing legacy IDs to contaminate the production graph.
6. It allows E265–E270 to become the canonical ending qualification layer rather than maintaining two competing ending resolvers.

## Migration requirements

Before production schema freeze:

1. Search every `E35`–`E40` reference in all docs.
2. Classify each reference as Act V event, legacy ending material, or ambiguous.
3. Convert production references to canonical Act V IDs.
4. Convert legacy ending references to `LEGACY-END-*` review aliases.
5. Confirm no runtime candidate references a legacy alias.
6. Re-run graph/catalog reconciliation.
7. Re-run reachability and ending simulations.
8. Only then freeze stable IDs in machine-readable data.

## Additional semantic duplicates

The title pairs below remain candidates for semantic duplicate review, but are **not** ID collisions:

- E73 / E156 — The Widow's Petition
- E99 / E173 — The Empty Barracks

Their downstream consequences must be compared before either title is renamed or merged.

## Current status

**ID collision decision: resolved at the design level.**

**Runtime migration: not yet implemented.**

The repository still intentionally retains both source catalogs so the migration can be audited against original authored material.

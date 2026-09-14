# Choice Kingdom — Legacy / Duplicate Semantic Audit 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — OPEN ITEMS RECORDED, NO SILENT MERGES**
Scope: E35–E40 legacy collision review plus known duplicate semantic pairs.

## Findings

### E35–E40 legacy collision set

The original Act V catalog remains a canonical authored source and must not be deleted merely because later expansion nodes reuse a character/topic. Several later nodes have overlapping semantics and therefore need explicit identity treatment before production schema freeze.

- **E36 Mara's Resignation** and **E226 Mara's Resignation** share the same narrative event identity. They must not become two unrelated runtime events. Preferred treatment: preserve the earliest authored event as the canonical node and classify the later occurrence as either a deliberate recurrence with a distinct event ID/trigger or a duplicate that should be removed from the playable catalog after narrative review. This decision must be made before schema freeze.
- **E39 Ivo's Last Bargain** and **E229 Ivo's Last Shortcut** are different situations but both represent late Ivo fiscal leverage. They are not automatically duplicates; keep both only if the downstream consequences and player information are materially distinct.
- **E40 Amara's Winter List** and **E241 The Lanterns Were Right** are different civic/medical beats. They can coexist if E241 consumes the route established by earlier Amara decisions rather than merely repeating the same reward.
- **E37 Rowan's Oath** and **E227 Rowan's Line** overlap around military constitutional limits. They should remain distinct only if E227 is a later consequence/test of the oath rather than a second copy of the same choice.
- **E38 Seris and the Old Houses** and later house representation events overlap thematically but are not duplicates by title alone. Their institutional outputs must be canonicalized separately.

### Known later duplicate pair: E55 / E269

- E55 is titled **Ivo's Last Account** and establishes `guild_books_submitted` or `guild_books_sealed`.
- E269 is also titled **Ivo's Last Account** and has a different late-game choice set.
- These cannot share a runtime event identity. Production catalog must assign distinct semantic identities, for example by retaining E55 as the earlier ledger-disclosure node and renaming/reframing E269 as a later consequence node before schema freeze.
- This is a **P0 content-schema issue**, not a reason to silently renumber events.

### E73 / E156

Exact source comparison is still required before declaring these duplicates or distinct recurrences. No merge is authorized based on ID proximity or thematic similarity alone.

### E99 / E173

Exact source comparison is still required before declaring these duplicates or distinct recurrences. No merge is authorized based on ID proximity or thematic similarity alone.

## Required resolution rules

1. Event IDs are stable authored identifiers; do not renumber solely to hide collisions.
2. Same title does not prove same semantic node, but identical title + overlapping trigger + overlapping choice purpose is a strong collision signal.
3. A deliberate recurrence must have explicit recurrence semantics, distinct trigger timing, and distinct downstream consequences.
4. Duplicate content must be removed or reframed before production schema freeze; it must not be allowed to create ambiguous runtime identities.
5. Any rename/reframe must be reflected in graph references, delayed consequence source IDs, replay metadata, QA matrix and ending simulations.

## Gate impact

- Legacy semantic audit: **IN PROGRESS**.
- E55/E269 collision: **CONFIRMED P0**.
- E36/E226 collision: **CONFIRMED HIGH PRIORITY**, final treatment pending full graph review.
- E73/E156: **OPEN** pending exact source comparison.
- E99/E173: **OPEN** pending exact source comparison.
- Production schema remains blocked.

# Choice Kingdom — Semantic Reframe Application 01

Status: SOURCE-LEVEL RECONCILIATION / PRE-SCHEMA

This document applies the frozen semantic-collision policy without renumbering event IDs. It is the authoritative source patch specification for the next catalog edit.

## 1. E55 vs E269 — confirmed semantic collision

### Canonical E55 remains the primary ledger-disclosure event

`E55 — Ivo's Last Account` remains in `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`.

Role:
- first major disclosure of the guild's books;
- exposes evidence capable of implicating nobles and Ivo's own family;
- establishes the protected-submission vs private-sealing fork;
- canonical source markers remain `guild_books_submitted` and `guild_books_sealed`.

### E269 is reframed as a late consequence, not another first disclosure

Current source title:
- `E269 — Ivo's Last Account`

Required replacement:
- `E269 — Ivo's Final Disclosure`

Required trigger:
- `Ivo active`;
- late endgame phase / final-act route active;
- at least one prior guild-book outcome from E55 (`guild_books_submitted` or `guild_books_sealed`);
- no requirement to rediscover the same evidence.

Required narrative role:
E269 must answer what Ivo does after the consequences of E55 have matured. It is a late accountability/consequence beat, not a second discovery of the same books.

Required choice distinction:
- A — `Accept the guild's final accounting`: records a new late institutional/accountability outcome and may improve trust/reputation without reproducing `guild_books_submitted`.
- B — `Protect the guild's remaining interests`: records a distinct late political/commercial consequence and may improve Ivo while reducing public trust; it must not recreate `guild_books_sealed`.

Suggested canonical markers:
- `history.guild_final_accounting_accepted`
- `history.guild_remaining_interests_protected`

QA rule:
E269 must consume the consequences of E55 and produce new late-state history. It must not introduce another source of the same evidence, duplicate E55's markers, or silently renumber either event.

## 2. E36 vs E226 — distinct-role freeze

The authoritative Act V source contains:
- `E36 — Mara's Resignation` in `docs/EVENT_CATALOG_ACT_V_EXPANSION.md`.
- `E226 — Mara's Resignation` in `docs/EVENT_CATALOG_EXPANSION_211_270.md`.

E36 remains the earlier constitutional rupture / resignation decision.

E226 is retained only as a later consequence/test of repeated executive overrides. Its role must be explicitly downstream from the earlier institutional history rather than a duplicate resignation scene.

Required E226 distinction:
- Trigger must require late institutional stress (`Mara <= -1` or repeated executive overrides) plus evidence that the earlier Mara institutional route has already occurred or failed.
- E226 choice A must represent a late independent-mandate renewal/repair, not repeat E36's initial offer.
- E226 choice B may accept a late resignation as a consequence of accumulated governance, but must produce distinct downstream markers.

Suggested late markers:
- `history.mara_late_mandate_renewed`
- `history.mara_late_resignation`

QA rule:
If later graph analysis proves E226 has no materially distinct downstream consequences, remove/reframe E226 rather than keeping two copies of the same scene.

## 3. E37/E227, E39/E229, E40/E241

These pairs remain distinct-role candidates and require downstream verification before schema freeze:

- E37 = early constitutional/military oath decision; E227 = later institutional stress test.
- E39 = early guild emergency bargain; E229 = later fiscal shortcut consequence.
- E40 = early winter/local-relief policy; E241 = later proof that the Lanterns' local intelligence was correct.

No ID renumbering is permitted.

## 4. Source-of-truth rule

For E35–E60, the Act V expansion is the authoritative authored continuation over the original E01–E34 skeleton. The older E35–E40 skeleton in `docs/EVENT_CATALOG.md` must be treated as legacy source during reconciliation, not as an additional set of production events.

For E211–E270, `docs/EVENT_CATALOG_EXPANSION_211_270.md` remains authoritative for those IDs. E271/E272 belong only to `docs/EVENT_CATALOG_EXPANSION_271_280.md`; E271 must not remain duplicated as a post-catalog extension in the E211–E270 source after the next cleanup pass.

## 5. Schema gate

The following are now frozen as prerequisites before production event schema generation:

1. unique semantic role per event ID;
2. canonical trigger for every event;
3. distinct durable outputs for late consequence nodes;
4. no duplicate producer semantics;
5. graph/catalog agreement;
6. reachability of every retained event;
7. ending and replay consumers verified;
8. delayed effects carry stable source/consequence identity.

This document is a source-level application specification. Runtime execution remains unimplemented and production schema remains blocked until the broader canonicalization gate closes.

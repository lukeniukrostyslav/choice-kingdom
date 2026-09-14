# Choice Kingdom — Semantic Collision Verification 01

Status: SOURCE-LEVEL VERIFIED / PRE-SCHEMA

This pass verifies the known event pairs against their current authored source text. It does not claim runtime reachability.

## E55 / E269 — P0 collision

**Status: CONFIRMED COLLISION → REFRAME REQUIRED**

E55 (`docs/EVENT_CATALOG_ACT_V_EXPANSION.md`) is the primary guild-book disclosure: Ivo reveals that guild books contain evidence capable of destroying nobles while exposing his family. Choices establish `guild_books_submitted` or `guild_books_sealed`.

E269 (`docs/EVENT_CATALOG_EXPANSION_211_270.md`) currently repeats the title `Ivo's Last Account` and again presents Ivo handing over an account showing where emergency profits went. Its choices create another publication/leverage fork. This is semantically too close to E55 to freeze as two independent authored discoveries.

Decision: keep both IDs, retain E55 as the discovery node, reframe E269 as a late consequence/disclosure that explicitly consumes E55 history and creates new late-state history.

## E36 / E226 — P0 collision requiring downstream distinction

**Status: CONFIRMED SAME CORE SCENE → DISTINCT ROLE REQUIRED**

E36 (`docs/EVENT_CATALOG_ACT_V_EXPANSION.md`) is Mara's early Act V resignation confrontation: independent mandate versus accepting resignation.

E226 (`docs/EVENT_CATALOG_EXPANSION_211_270.md`) currently repeats the title `Mara's Resignation` and presents another resignation/independence choice. The current trigger is later institutional stress (`Mara <= -1` or repeated executive overrides), so the intended distinction is plausible but not yet encoded strongly enough in the authored semantics.

Decision: retain IDs; E36 is the initial constitutional rupture, E226 becomes a late consequence/test. If graph analysis cannot show distinct downstream consumers, E226 must be reframed or removed rather than treated as another copy.

## E37 / E227

**Status: DISTINCT ROLE, DOWNSTREAM VERIFICATION REQUIRED**

E37 asks whether the army obeys law or Crown during the early Act V constitutional confrontation. E227 is a later institutional test that writes or refuses a concrete military red line. The second can legitimately consume the first's constitutional history.

## E39 / E229

**Status: DISTINCT ROLE, DOWNSTREAM VERIFICATION REQUIRED**

E39 is an early emergency-grain-credit bargain that creates guild political/commercial leverage. E229 is a later fiscal-shortcut choice. They must not share a producer marker that makes E229 a duplicate of the E39 bargain.

## E40 / E241

**Status: DISTINCT ROLE, DOWNSTREAM VERIFICATION REQUIRED**

E40 establishes local relief policy. E241 is a later proof/credibility beat in which the Lanterns detect a crisis before officials. E241 should consume prior Amara/local-relief history and produce institutional early-warning consequences rather than re-run E40's policy decision.

## E73 / E156

**Status: CLOSED — NOT DUPLICATES**

E73 concerns audit accountability and named responsibility. E156 concerns civic relief/compensation. Different narrative function and different downstream domain.

## E99 / E173

**Status: CLOSED — NOT DUPLICATES**

E99 concerns seal/forgery evidence integrity. E173 concerns military infrastructure/readiness. Different narrative function and different downstream domain.

## Freeze rule

No event pair may be declared schema-safe solely because titles differ. Each retained event must have a unique semantic role, canonical trigger, distinct durable outputs, distinct downstream consumers, and a reachable path that does not require another event to silently manufacture its prerequisites.

Runtime engine execution is still 0%: these are authored-source verification results only.

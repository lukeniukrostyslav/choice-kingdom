# Choice Kingdom — Semantic Collision Resolution 01

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — E55/E269 AND E36/E226 AUTHORITATIVE CATALOG DISTINCTIONS APPLIED; GRAPH/CATALOG INTEGRATION STILL REQUIRED**
Scope: confirmed and suspected duplicate/overlapping event identities before production schema freeze.

## Purpose

Prevent ambiguous runtime identities without silently renumbering authored IDs. An event ID remains stable; semantic identity is resolved by explicit narrative role, trigger context, and downstream consequence.

## Frozen resolutions

### E55 / E269 — confirmed title collision

- E55 remains the canonical **early/primary ledger-disclosure node**: Ivo exposes guild books and chooses protected submission versus private sealing.
- E269 remains the authored **late endgame consequence/evidence node**, now titled **“Ivo's Late Account”** so its title and presentation cannot imply that it is the same event as E55.
- IDs remain stable; neither node was merged or renumbered.
- E269's source text now explicitly identifies its late consequence/evidence role and its distinction from E55.
- Required dependent verification remains: event graph, producer/consumer registry, delayed consequence source IDs if any, replay metadata if any, QA matrix and ending simulations.

### E36 / E226 — same narrative premise, different role

- E36 remains the canonical early constitutional/resignation node.
- E226 is retained as **“Mara's Final Resignation Test”**, a late consequence/test of accumulated executive overrides and institutional strain.
- E226's source text now explicitly says it is not a second generic resignation scene and must reference accumulated institutional strain in presentation.
- Its downstream role must consume earlier institutional history and create materially different late-game consequences.
- If that distinction cannot be demonstrated in graph/reachability QA, E226 should be removed from the playable catalog rather than duplicated at runtime.

### E37 / E227 — constitutional military overlap

- E37 is the foundational military-law oath.
- E227 is retained as a later constitutional stress test only if its trigger depends on the earlier route and its effects test or extend that commitment.
- No second copy of the oath semantics is permitted.

### E40 / E241 — civic/medical overlap

- Both may coexist because E40 establishes an early local-relief direction while E241 is a later validation/early-warning consequence.
- E241 must consume meaningful Amara/civic history and must not become a duplicate reward event.

### E39 / E229 — fiscal leverage overlap

- Both may coexist because E39 is an early emergency-credit bargain and E229 is a late shortcut/loophole decision.
- Their player information, risk, and downstream consequences must remain materially distinct.

### E38 / later house representation

- E38 is an early constitutional bargain with hereditary houses.
- Later representation nodes must consume or transform that history rather than restating the same bargain.

## Closed source-level comparisons

### E73 / E156

`docs/LEGACY_SOURCE_COMPARISON_02.md` confirms these are distinct source-level nodes.

- **E73 — Three Stamps:** institutional accountability / named responsibility; trigger family `audit_office`; outputs include `named_authority` and `overlapping_authority`.
- **E156 — The Widow's Petition:** compensation after military requisition; high-trust / civic-relief context; outputs include `requisition_compensation` and `requisition_tax_credit`.

**Resolution:** retain both stable IDs; no merge and no renumbering. The duplicate concern is closed at source level. Graph/catalog integration remains pending.

### E99 / E173

`docs/LEGACY_SOURCE_COMPARISON_02.md` confirms these are distinct source-level nodes.

- **E99 — The Forgery's Shadow:** forgery evidence / coercion; trigger family includes `royal_forgery_proven` or `forgery_leverage`; outputs include `seal_comparison_public` and `seal_pressure`.
- **E173 — The Empty Barracks:** army readiness / security infrastructure; trigger is low army readiness; outputs include `barracks_rebuilt` and `barracks_shelter`.

**Resolution:** retain both stable IDs; no merge and no renumbering. The duplicate concern is closed at source level. Graph/catalog integration remains pending.

## Schema-freeze rule

A collision is resolved for production only when all of the following are true:

1. stable authored ID is preserved;
2. semantic role is unique or explicit recurrence is declared;
3. trigger is canonical and distinguishable;
4. choice effects are materially distinct;
5. downstream consumers are distinguishable;
6. delayed/replay references use the correct source identity;
7. graph and catalog agree;
8. reachability/endings QA confirms the node is not dead or redundant.

Documentation alone does not mark a collision fully resolved. The authoritative authored catalog must be edited and re-read, then the resulting graph/QA surfaces must be updated.

## Current gate impact

- E55/E269: **AUTHORITATIVE CATALOG DISTINCTION APPLIED; graph/consumer/delayed/replay verification pending**.
- E36/E226: **AUTHORITATIVE CATALOG DISTINCTION APPLIED; graph/reachability verification pending**.
- E37/E227: **later-stress-test policy frozen; downstream verification pending**.
- E39/E229: **distinct-role policy frozen; downstream verification pending**.
- E40/E241: **distinct-role policy frozen; downstream verification pending**.
- E73/E156: **SOURCE-LEVEL CLOSED; graph/catalog integration pending**.
- E99/E173: **SOURCE-LEVEL CLOSED; graph/catalog integration pending**.
- Production schema: **BLOCKED** until full reconciliation pass.

# Choice Kingdom — Endgame Source Closure Pass 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — OPEN / NO RUNTIME CLAIM**  
Scope: E151–E272 and seven ending families.

## Purpose

Perform a conservative source-level closure pass over the endgame. A consumer trigger, prose qualification, relationship score, or route label is not promoted to a producer unless an authored source explicitly establishes the canonical state.

## Findings

### E184 — The Quiet Evidence

Canonical trigger text is `secret evidence route`. The authored outcome markers `quiet_evidence_published` / `quiet_evidence_kept` are consequences of E184 itself and therefore cannot be used as its prerequisite. No source-closed producer for the exact trigger identity was found in the current searchable index.

**Decision:** keep E184 producer OPEN. Do not alias generic information/evidence routes into `secret evidence route`.

### E243 — The Old Bridge

The delayed trigger is `public bridge investment`. Existing source audit identifies E18-B as the exact semantic candidate via `public_bridge`.

**Decision:** candidate is source-closed semantically, but runtime vocabulary must normalize `public bridge investment` to canonical `public_bridge` in the production contract. Do not treat E224 bridge safety, E126/E129 infrastructure relations, or generic public infrastructure as equivalent producers.

### E245 — The Soldier's Son Returns

The delayed trigger is `compensation route`. E125-A (`border_compensation`) and E156-A (`requisition_compensation`) are distinct authored compensation outcomes. They cannot be silently collapsed into a generic compensation alias.

**Decision:** producer closure remains OPEN pending an explicit authored normalization rule defining whether either source alone qualifies or whether a declared OR-union is intended. Runtime must not infer this from substring/semantic similarity.

### E246 — The Price Ceiling Memory

The delayed trigger is `price ceiling`. E160-A establishes `winter_rent_ceiling`, which is the exact semantic candidate identified by source review.

**Decision:** normalization remains OPEN. `price ceiling` must not be broadened to every future price-control concept unless the canonical contract explicitly defines the vocabulary relation.

## Replay / Meta-state

E186, E247, E248 and E270 contain replay-oriented consumer intent. No ordinary `flag.*` or `history.*` marker is promoted to `meta.*` by inference. Explicit replay producer/key closure remains OPEN.

## Ending families

- Steward: PARTIAL producer closure.
- Iron Crown: PARTIAL producer closure.
- Golden Compact: PARTIAL; `pred.guild_influence_strong` remains unresolved.
- People's Charter: PARTIAL; civic participation and blockers remain unresolved.
- Broken Diadem: OPEN; terminal failure predicate and independent failure paths not frozen.
- Quiet Throne: OPEN; explicit withdrawal producer not frozen.
- Second Founder: PARTIAL; systemic evidence convergence, coalition qualification, constitutional preparation and replay metadata remain unresolved.

## Graph/reachability consequence

The four delayed nodes above are not all equivalent graph states. E243 has a credible exact incoming producer candidate; E245 has a multi-source semantic ambiguity; E246 has a vocabulary ambiguity; E184 lacks a source-closed producer. These distinctions must be retained by the causal graph audit rather than represented as one generic "missing trigger" bucket.

## Gate result

**Endgame source closure:** NOT CLOSED.  
**Canonical vocabulary freeze:** NOT CLOSED.  
**Replay meta producers:** NOT CLOSED.  
**Ending runtime fixtures:** BLOCKED.  
**Decision Engine:** remains correctly blocked.

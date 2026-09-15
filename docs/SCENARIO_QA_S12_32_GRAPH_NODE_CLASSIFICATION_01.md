# Choice Kingdom — S12.32 Graph Node Classification

Date: 2026-09-15
Scope: frozen E01–E272
Status: **MACHINE-VERIFIED CANDIDATE CLASSIFICATION — NOT REACHABILITY PROOF**

## Purpose

S12.32 extends the S12.30 machine graph validator so that an event missing from the outbound design graph is not automatically called an orphan.

The validator now distinguishes:

1. **Inbound-only candidates** — referenced as a graph target but with no outbound causal edge.
2. **Unreferenced catalog candidates** — present in the authoritative catalog but absent from both inbound and outbound design edges.
3. **Source-gap events** — frozen IDs without an authoritative catalog heading.

None of these categories is itself a runtime reachability verdict.

## Machine result

CI run for commit `4338b47321a4494ebb30747f7238025bd9d08457` completed successfully.

- Frozen scope: **272 events**
- Authoritative catalog headings found: **270 / 272**
- Missing authoritative headings: **E33, E34**
- Unique design edges: **296**
- Repeated documentation edges: **43**
- Graph-referenced events: **216 / 272**
- Catalog events without outbound design edges: **69**
- Inbound-only candidates: **15**
- Unreferenced catalog candidates: **54**
- Delayed consumer rows: **10**
- Source-closed producers: **21**
- Hard-negative rules: **7**

## Inbound-only candidates

`E04, E42, E52, E54, E55, E56, E57, E58, E59, E60, E90, E209, E270, E272`

These are plausible consumer/terminal/qualification/lifecycle nodes and must not be labelled orphaned without semantic inspection.

## Unreferenced catalog candidates

`E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31, E32, E35, E36, E38, E39, E40, E43, E44, E45, E47, E48, E61, E62, E63, E64, E65, E66, E67, E68, E69, E70, E77, E80, E87, E112, E113, E115`

This list exposes a structural limitation of the current design graph: many early source events and the seven ending/epilogue nodes are not represented as outbound causal edges. They cannot be treated as missing content solely because the graph does not encode their outgoing edge.

## Important interpretation

The current graph is explicitly a **design-level causal map**, not the authoritative producer registry. Therefore:

- early events may be roots or producer sources whose consumers are represented elsewhere;
- ending nodes may intentionally terminate a path;
- epilogues may be consumer-only nodes;
- qualification events may consume multiple upstream predicates without producing a new event edge;
- a real orphan exists only when an authoritative event has no valid narrative role, no producer/consumer semantics, and no terminal/qualification purpose.

## Next machine pass

The next pass must compile the actual event-token producer/consumer matrix from authoritative catalog text and canonical inventories. It should then classify the 69 candidates using semantic evidence rather than graph shape.

Required classifications:

- ROOT / SOURCE
- ORDINARY PRODUCER
- CONSUMER-ONLY
- TERMINAL / ENDING
- QUALIFICATION / CONVERGENCE
- DELAYED CALLBACK
- REPLAY-ONLY
- TRUE ORPHAN
- SOURCE GAP

No runtime reachability claim is made by S12.32.

## Gate

**S12.32 machine classification gate: PASS.**

**Semantic orphan gate: OPEN.**

**Fresh-run/replay reachability: OPEN.**

**Production schema: BLOCKED.**

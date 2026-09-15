# Scenario QA S12.35 — Producer / Consumer Matrix Compiler 01

## Objective

Turn the working canonical producer/consumer registry into deterministic machine-readable QA data so OPEN/PARTIAL rows can be enumerated and audited without inventing producers, aliases, or runtime semantics.

## Change

Added `tools/compile_producer_consumer_matrix.py` and wired it into the canonical graph CI workflow after the graph validator and node classifier.

The compiler extracts:

- canonical key/family;
- resource/history/relationship/thread/predicate/ending type;
- concrete E01–E272 producer event references when explicitly present;
- concrete E01–E272 consumer event references when explicitly present;
- registry status;
- QA note.

It rejects excluded E273–E277 references and any out-of-scope event references in registry producer/consumer fields.

## Safety rule

This matrix is **derived QA data, not runtime input**. An OPEN or PARTIAL registry row stays open. Text such as `candidates`, `throughout campaign`, or `later consumers` is not promoted into a fabricated producer or absolute event dependency.

## Why this matters

The next reachability stage needs a distinction between:

1. an event that is merely present in the authored graph;
2. an event that explicitly produces a canonical durable state;
3. an event that explicitly consumes that state;
4. a predicate whose producer identity is still unresolved;
5. a terminal/ending qualification row;
6. replay/meta state that must remain isolated from ordinary history.

The compiler establishes the machine boundary for that distinction and makes scope contamination mechanically detectable.

## Remaining closure

The matrix does not yet prove semantic equality between the registry and authored prose, nor does it prove runtime reachability. Those remain downstream gates.

Still OPEN:

- E33/E34 exact source recovery;
- `pred.food_stable` producer;
- guild influence exact machine qualification;
- systemic convergence producer/key;
- coalition cooperation executable qualification;
- constitutional preparation ordering;
- final charter prerequisite producers;
- replay `meta.*` producer/key inventory;
- delayed cancellation/supersession;
- E184/E185 lifecycle closure;
- ending incoming paths and deterministic precedence;
- fresh-run/replay reachability;
- catalog↔machine semantic equality.

## Gate status

**S12.35 = machine producer/consumer compilation GREEN at source-registry level; semantic and runtime closure remain OPEN.**

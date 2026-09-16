# Choice Kingdom — Frozen Production Block Plan

This is the working execution order for production completion. Work proceeds sequentially by large blocks. A block receives 🔒 CLOSED only after implementation and applicable verification are GREEN; source/contract closure alone is not runtime closure.

## Scenario layer
- S01–S12: 🔒 source/contract closed (12/12). Runtime regressions are handled as targeted regression fixes, not by reopening the scenario blocks as standalone work.

## Large production blocks
1. 🔒 **Deterministic Authored Routing** — closed; representative authored execution, immediate-routing boundary, prerequisite routing and regression verification are GREEN.
2. 🔒 **Deterministic Routing Expansion** — closed; explicit authored prerequisite routing is executable across the verified production scenario surface without invented graph semantics.
3. 🔒 **Delayed Consequences Lifecycle** — closed; frozen delayed entries, turn scheduling/resolution, condition-bound E185 activation, cancellation/supersession, exactly-once behavior, persistence and DecisionEngine target activation/execution are verified.
4. ⏳ **Replay / Meta-State** — current block; implement replay/meta import and runtime transfer boundaries with exact authored keys/tuples.
5. ⏳ **Endings + Precedence Resolver** — executable ending qualification, incoming paths and precedence verification.
6. ⏳ **Complete Save / Load + Determinism** — full lifecycle persistence, stable snapshots, repeated-run determinism and recovery verification.
7. ⏳ **Production Decision Engine** — integrate the completed runtime semantics into the full decision-engine boundary; no production-readiness claim before the complete runtime scenario gate is GREEN.
8. ⏳ **UI / UX** — production game interface and all interaction mechanisms wired to real runtime state.
9. ⏳ **Localization 20+ / RTL** — localization implementation, long-string and RTL validation.
10. ⏳ **Android Implementation** — Android-first application integration and packaging configuration.
11. ⏳ **Runtime / Android QA** — device/runtime regression, lifecycle, persistence and gameplay verification.
12. ⏳ **APK / AAB Build & Verification** — reproducible release builds and install/package verification.
13. ⏳ **Release / Commercial Packaging** — final production packaging, release gates and launch readiness.

## Operating rule
Complete each large block through code → tests → CI → fixes → verification → commit before moving to the next block. Do not return to already closed blocks as standalone tasks unless a later change causes a concrete regression.

## Current position
**Blocks 1–3 are closed. Block 4 is now the current production block.**

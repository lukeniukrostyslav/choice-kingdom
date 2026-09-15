# Choice Kingdom — Scenario QA Scorecard 01

Date: 2026-09-15  
Frozen authored scope: **E01–E272**  
Status: **SCENARIO QA REPORTING CONTRACT — SOURCE LEVEL**

## Purpose

This file freezes the reporting meaning of the project's **scenario verification percentage** so the number does not change merely because a different project-wide aggregation formula is used.

## Current scenario verification score

**65% — scenario QA / verification progress.**

This is the working scenario metric requested for the E01–E272 authored campaign. It is distinct from the overall project percentage.

## What 65% means

The 65% score represents progress through the scenario-verification gates that determine whether the authored campaign is internally safe to hand to the production engine:

- canonical event identity and continuity;
- source-level producer/consumer closure;
- derived-predicate contract closure;
- delayed-consequence source/target verification;
- replay-boundary verification;
- ending qualification and precedence definition;
- causal/reachability verification;
- contradiction, duplicate-writer and undefined-reference checks.

The first six areas have substantial source-level closure, while causal reachability and exhaustive machine checks remain materially incomplete. Therefore the scenario is **not** 65% implemented and is **not** runtime-ready; 65% is the fixed reporting value for how much of the scenario QA work is currently closed/verified.

## Explicit exclusions

The scenario score does **not** claim:

- a working Decision Engine;
- runtime reachability verification;
- Android implementation;
- UI/UX completion;
- localization completion;
- APK readiness;
- release readiness.

Those are tracked separately in `PROJECT_STATE.md`.

## Frozen scope rule

E01–E272 are the current frozen authored production scope. E273–E277 remain expansion candidates and must not silently change the denominator of the scenario score.

## Next gates required to move the scenario score materially upward

1. Exhaustive E01–E272 output/trigger inventory.
2. Duplicate semantic writer and contradictory writer detection.
3. Undefined producer/consumer detection.
4. Predicate dependency cycle detection.
5. Complete delayed source/target/exactly-once/cancellation inventory.
6. Ending incoming-path and deterministic precedence matrix.
7. Exact replay `meta.*` producer/key closure.
8. Fresh-run causal reachability simulation.

## Truth rule

A source-level document is evidence of QA work, not proof of runtime behavior. No scenario gate is marked complete merely because documentation exists; the underlying authoritative source must be checked and the resulting contract must be machine-verifiable before production schema freeze.

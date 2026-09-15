# Choice Kingdom — Scenario QA S01 Duplicate / Contradiction Audit 01

Date: 2026-09-15
Scope: E01–E34
Status: **PARTIAL — multi-producer cases identified; final semantic closure remains open**

## Purpose

This artifact records the first direct semantic duplicate/contradiction pass for the frozen S01 scope. It is not a runtime implementation claim.

## Direct source verification

The authoritative source is `docs/EVENT_CATALOG.md`.

E31 is now directly verified from the source:

- Trigger: winter + security < 60 or military escalation.
- A `war_mobilization`: -8 gold, +10 security, -3 reputation.
- B sends Rowan under a white banner: -2 security, +6 reputation; diplomatic branch can unlock negotiated withdrawal.

The previous S01 inventory entry that marked E31 as source-retrieval OPEN is therefore obsolete and must be replaced by the verified source entry.

## Multi-producer / semantic collision findings

### 1. `ledger_fragment_a` has two authored producers

- E07-B: delayed route can reveal `ledger_fragment_a`.
- E21-A: immediate investigation unlocks `ledger_fragment_a`.

This is **not yet classified as a contradiction**. The two producers can represent converging ways to obtain the same evidence fragment. However, the production contract must explicitly define whether this is:

1. idempotent flag acquisition (`false -> true`, repeated acquisition is a no-op), or
2. a richer evidence object with provenance/source identity.

Until that contract is frozen, the duplicate semantic-writer gate remains OPEN.

### 2. `pred.winter_severe` has two branch producers inside E29

- E29-A establishes the predicate for the current winter cycle.
- E29-B establishes the same predicate for the current winter cycle.

This is an **expected mutually-exclusive branch convergence**, not a contradiction. The production contract must treat both choices as the same cycle predicate with different immediate state consequences and history.

### 3. `pred.market_pressure` has one active producer and one clear operation in S01

- E19-B establishes the active cycle predicate.
- E19-A clears the active cycle predicate.

This is a lifecycle pair, not duplicate production. Historical evidence remains queryable after clear.

### 4. No contradiction found in the directly verified S01 source for the major canonical flags

The following have single semantic writers within E01–E34 as currently authored: `open_petition_hall`, `court_first`, `emergency_decree_used`, `decree_investigation`, `free_grain_imports`, `quiet_accounts`, `emergency_guard_authority`, `nobles_challenged`, `quiet_market_inquiry`, `merchant_charter`, `competitive_market`, `audit_office`, `flexible_accounts`, `central_command`, `local_command`, `noble_advisory_council`, `lantern_funded`, `toma_recruited`, `toma_rejected`, `market_reform`, `petty_tax_policy`, `public_diplomacy`, `quality_armaments`, `public_bridge`, `guild_broken`, `market_pressure_declared`, `soldier_compensation`, `evidence_destroyed`, `ledger_public`, `ledger_secret`, `auditor_missing_public`, `seris_witness`, `seris_exposed`, `royal_forgery_proven`, `forgery_leverage`, `war_mobilization`, `people_heard`.

This list is limited to the frozen S01 source and must not be mistaken for global repository-wide closure; S08 performs the global producer/consumer audit.

## S01 gate impact

- E31 source verification: **CLOSED**.
- Major contradiction scan: **NO CONTRADICTION FOUND in directly verified S01 source**.
- Duplicate semantic writer scan: **OPEN**, because `ledger_fragment_a` has two authored acquisition paths and requires an explicit canonical idempotency/provenance contract.
- Predicate branch convergence: **ACCEPTED** for E29 and E19 lifecycle semantics; not treated as duplicate semantic writers.

### Result

S01 advances from **70% to 80% working progress**. The scenario-QA global percentage remains **65%** because S01 is not closed and all later gates remain open/partial.

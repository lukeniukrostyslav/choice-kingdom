# Choice Kingdom — Scenario QA S01: E01–E34 Inventory

Date: 2026-09-15
Scope: E01–E34
Status: **IN PROGRESS — 80%, NOT CLOSED**

## Purpose

Durable inventory for the first scenario-QA batch. This document records only facts verified from the authoritative E01–E34 catalog and existing canonical QA artifacts. It must not be treated as runtime implementation.

## Verified source

Canonical narrative source: `docs/EVENT_CATALOG.md`.
The catalog is the narrative source of truth; `EVENT_GRAPH.md` is not an independent producer source.

## Verified event inventory

| Event | Trigger verified | Outputs / state verified | Delayed / downstream verified | QA status |
|---|---|---|---|---|
| E01 | first turn | `open_petition_hall`, `court_first` | E07, E06 | VERIFIED |
| E02 | after E01 | `emergency_decree_used`, `decree_investigation` | emergency response / hidden-ledger route | VERIFIED |
| E03 | food prices rise | `free_grain_imports` | grain reserve / winter risk | VERIFIED |
| E04 | after E03 | `ledger_public_scrutiny`, `quiet_accounts` | discrepancy discovery | VERIFIED |
| E05 | security <55 or turn 4+ | emergency guard authority | procurement / expanded powers | VERIFIED |
| E06 | `court_first` or Seris >=1 | `nobles_challenged` | exemption renewal pressure | VERIFIED |
| E07 | `open_petition_hall` | `quiet_market_inquiry` | `ledger_fragment_a` | VERIFIED |
| E08 | early Act I milestone | `merchant_charter`, `competitive_market` | E19 route | VERIFIED |
| E09 | Mara >=1 + `decree_investigation` | `audit_office`, `flexible_accounts` | hidden ledger | VERIFIED |
| E10 | Rowan >=1 | `central_command`, `local_command` | border-defense consequences | VERIFIED |
| E11 | Seris >=1 | advisory-council route | reform alliance | VERIFIED |
| E12 | trust <60 or food shortage | `lantern_funded` | winter welfare consequence | VERIFIED |
| E13 | Toma unlocked | `toma_recruited`, `toma_rejected` | information network / rumor reliability | VERIFIED |
| E14 | Ivo >=2 | `market_reform`, `petty_tax_policy` | recurring reputation consequence | VERIFIED |
| E15 | Act II | `public_diplomacy` | candid diplomatic branch | VERIFIED |
| E16 | security <60 or `local_command` | border survey / military response | escalation / peaceful settlement | VERIFIED |
| E17 | security <65 | `cheap_weapons`, `quality_armaments` | later crisis equipment consequence | VERIFIED |
| E18 | `merchant_charter` or `competitive_market` | `public_bridge` | toll repetition / E19 route | VERIFIED |
| E19 | `merchant_charter` + no `audit_office` | `guild_broken`, `market_pressure_declared`, `pred.market_pressure` active/clear lifecycle | market-pressure cycle | VERIFIED |
| E20 | Rowan >=1 | `soldier_compensation` | family / army relationship consequence | VERIFIED |
| E21 | Toma >=1 or `quiet_market_inquiry` | `ledger_fragment_a`, `evidence_destroyed` | hidden-ledger route | VERIFIED |
| E22 | trust >=55 | festival decision | assassination-risk delayed consequence | VERIFIED |
| E23 | `ledger_fragment_a` | `ledger_public`, `ledger_secret` | formal inquiry / legitimacy | VERIFIED |
| E24 | `audit_office` | `auditor_missing_public` | E25 route | VERIFIED |
| E25 | Toma + auditor/search condition | stronger evidence route | hidden character reveal | VERIFIED |
| E26 | Seris >=2 + ledger chain | `seris_witness`, `seris_exposed` | testimony/confession route | VERIFIED |
| E27 | ledger chain | arrest/test route | institutional scandal if false | VERIFIED |
| E28 | `decree_investigation` + ledger chain | `royal_forgery_proven`, `forgery_leverage` | later evidence / blackmail | VERIFIED |
| E29 | late campaign + >=2 unresolved pressures | `pred.winter_severe`, `winter_severity_declared` | winter cycle | VERIFIED |
| E30 | winter + market tension | rescue/seal decision | arsonist escape risk | VERIFIED |
| E31 | winter + security <60 or military escalation | `war_mobilization` (A); negotiated withdrawal route (B) | border crisis / diplomatic branch | VERIFIED SOURCE-LEVEL |
| E32 | E29 + E30 + E31 unresolved | `pred.transport_disruption(active)`, `history.transport_disruption_declared` | E136-A/B clear lifecycle | VERIFIED SOURCE-LEVEL |
| E33 | emergency decree / severe crisis | `emergency_power` or `constitutional_limit` | Iron Crown / Second Founder routes | VERIFIED |
| E34 | trust >=65 or welfare branch | `people_heard` | relief-order consequence | VERIFIED |

## Producer/consumer findings for S01

Confirmed producer-backed facts from E01–E34 include:

- `open_petition_hall` → E01-A; consumed by E07.
- `court_first` → E01-B; consumed by E06.
- `audit_office` → E09-A; consumed by E24 and later routes.
- `merchant_charter` → E08-A; consumed by E18 and later routes.
- `competitive_market` → E08-B; consumed by E18 and later routes.
- `toma_recruited` → E13-A; later information routes.
- `public_bridge` → E18-B; later delayed bridge route.
- `quality_armaments` → E17-B.
- `cheap_weapons` → E17-A; later military crisis routes.
- `ledger_public` → E23-A.
- `evidence_destroyed` → E21-B.
- `royal_forgery_proven` → E28-A.
- `war_mobilization` → E31-A.
- `pred.market_pressure` current cycle → E19-B; clear → E19-A.
- `pred.winter_severe` current cycle → E29-A/B.
- `pred.transport_disruption` active → E32; clear → E136-A/B (cross-batch producer).

## Duplicate / contradiction findings

The direct S01 semantic audit is recorded in `docs/SCENARIO_QA_S01_DUPLICATE_CONTRADICTION_AUDIT_01.md`.

One important multi-producer case is now explicit:

- `ledger_fragment_a` can be acquired through E07-B's delayed route and E21-A's immediate investigation route.
- This is not currently classified as a contradiction, but the canonical production contract must define idempotent acquisition and/or provenance semantics before the duplicate-writer gate can close.

E29-A/B both establish `pred.winter_severe` for the same winter cycle; this is treated as mutually-exclusive branch convergence, not contradictory writing. E19-A/B are a lifecycle clear/establish pair for `pred.market_pressure`, not duplicate production.

## Important negative rules

- A prose route phrase is not accepted as a machine producer without canonical state vocabulary.
- `thread.border` must not be silently equated with `thread.border_crisis`.
- `price ceiling` must not be generalized into every price-control fact.
- Delayed consequences are not runtime-ready merely because a source event is known; exact source choice, timing, target, exactly-once identity and cancellation/supersession remain later S10 work.
- Multi-producer convergence must be explicitly typed; it cannot be silently collapsed into one writer.

## Current S01 gate result

- Trigger inventory: **VERIFIED for E01–E34 source scope**.
- Concrete output inventory: **PARTIAL** — E31 is now closed, but exhaustive semantic duplicate/contradiction closure is not complete.
- Producer/consumer mapping: **PARTIAL** — source-backed examples verified; global closure belongs to S08.
- Delayed inventory: **PARTIAL** — source identities recorded where verified; exact callback contracts belong to S10.
- Duplicate/contradictory writer scan: **OPEN** — `ledger_fragment_a` requires an explicit canonical multi-producer contract.

**S01 progress: 80% — not complete.**

No scenario-QA global percentage increase is claimed from this batch. Overall Scenario QA remains **65%** until the defined gates are actually closed.

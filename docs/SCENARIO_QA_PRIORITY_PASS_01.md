# Choice Kingdom — Scenario QA Priority Pass 01

Status: ACTIVE — scenario-first execution gate.
Date: 2026-09-15.

## Purpose

This pass changes the working order so scenario/content closure is the first priority. Runtime implementation, UI, localization and Android work remain downstream until the authored campaign and its critical endgame contracts are closed.

## Current authoritative campaign scope

- Production checkpoint: E01–E272.
- E273–E277 remain outside the production freeze.
- The authored event catalogs are the source of truth for scenario semantics; QA documents may identify gaps but must not silently become producers.

## Scenario-first execution order

1. Reconcile E01–E70.
2. Reconcile E71–E110.
3. Reconcile E111–E150.
4. Reconcile E151–E210.
5. Reconcile E211–E272.
6. Resolve endgame producer/consumer gaps.
7. Resolve ending prerequisite and precedence contracts.
8. Run structural reachability and contradiction checks.
9. Only after the scenario gate is closed, proceed to runtime implementation.

## Non-negotiable percentage rule

Scenario percentages may increase only when an authoritative event catalog source or machine scenario contract changes and the applicable validation passes. Documentation-only audits do not increase scenario percentages.

## Immediate source-closure targets

- E148: preserve the six-faction package as upstream coalition evidence and keep `pred.coalition_cooperation` as a derived qualification.
- E200: require two distinct institutional guild domains before `pred.guild_influence_strong` can qualify E200.
- E207: require warehouse/financial, document/language and witness/organizational evidence plus an explicit convergence decision before eligibility.
- E209: consume `pred.final_charter_prerequisites`; do not manufacture missing prerequisites at E209.
- E210: remain convergence-only and never create missing prerequisites.

## Current gate

This file establishes the scenario-first work order. It does not by itself increase any scenario percentage.

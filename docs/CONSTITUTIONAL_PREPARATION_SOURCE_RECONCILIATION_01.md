# Choice Kingdom — Constitutional Preparation Source Reconciliation 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — RECONCILIATION PASS
Scope: frozen production E01–E272

## Finding

The canonical producer inventory identifies **E199-A** as the explicit military constitutional source:
- `army_constitution_oath`
- military constitutional evidence

The producer/consumer registry independently records `thread.military_constitutional` as sourced by E199-A and consumed downstream.

A separate draft source-freeze row had previously named E227 / `military_red_line` as the military preparation source. That row is **not safe to promote as authoritative** while the frozen producer inventory names E199-A. E227 must therefore remain a downstream/consumer reference until its own authored producer identity is independently reconciled.

## Frozen preparation domains

`pred.constitutional_prepared_strong` requires at least three distinct preparation domains:

1. civic/commons — E50-A → `people_charter_endorsed`
2. institutional/audit — E154-A → `crown_audited` with E155-A `full_crown_audit_published` remaining same-domain evidence
3. factional/house — E161-A → `house_assembly`
4. military/law — E199-A → `army_constitution_oath` / military constitutional evidence

Only distinct domains count. Relationship scores, downstream stress tests, and repeated consequences cannot create additional domains.

## E33 interaction

E33-B → `constitutional_limit` is an authored component for downstream Second Founder qualification. It is **not** itself a fifth preparation domain and must not be aliased to `pred.constitutional_prepared_strong`.

The no-permanent-emergency-power requirement remains a separate negative/blocker condition, represented by the authored E48-A `permanent_emergency_blocked` path and related ending contract. It does not count as an independent preparation domain.

## Current status

**Source identities materially reconciled.**

**Predicate qualification remains PARTIAL** until producer-before-consumer ordering, anti-double-counting, negative blockers, and reachability are machine-checked across E01–E272.

## Required next verification

- reconcile E199-A against every consumer currently naming `military_red_line`;
- determine whether E227 is a consumer, refinement, or independent producer from authoritative authored text;
- remove any unsafe E227→predicate alias if no explicit producer exists;
- run canonical graph and predicate-parity checks after the registry/source-freeze correction;
- do not promote the Decision Engine until the resulting producer graph is verified.

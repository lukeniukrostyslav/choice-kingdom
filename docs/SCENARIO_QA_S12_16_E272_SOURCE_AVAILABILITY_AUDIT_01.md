# Choice Kingdom — S12.16 E272 Source Availability Audit 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — BLOCKING EXTRACTION AUDIT
Scope: frozen production E01–E272

## Purpose

Verify whether the authoritative repository currently exposes exact authored branch text for E272 before any canonical lifecycle tokens are promoted into production semantics.

## Findings

The inspected authoritative expansion catalog currently ends its explicit post-catalog bridge at E271. `docs/EVENT_CATALOG_EXPANSION_211_270.md` contains the full E271 producer contract, including:

- E271-A declares the formal border crisis;
- E271-B explicitly de-escalates without declaring a crisis;
- neither E195 nor E253 may manufacture `pred.border_crisis`;
- later authored resolution is required to invalidate the active crisis.

The repository state and canonical registries reference E272-A/B as the resolution stage, but the exact authored E272 choice text/tokens are not exposed in the inspected authoritative catalog material.

## Hard QA decision

**Do not invent E272 branch tokens.**

The following names may be used only as canonical registry placeholders already established by prior source-level QA:

- `history.border_crisis_resolved_diplomatically` — E272-A;
- `history.border_crisis_resolved_by_guarantee` — E272-B.

These placeholders are not treated as proof of exact authored choice wording until the source event is directly recovered and re-read.

## Lifecycle invariant

The canonical lifecycle remains:

1. E271-A → active `thread.border_crisis` / eligible `pred.border_crisis`.
2. E271-B → explicit non-crisis resolution path and must not satisfy `pred.border_crisis`.
3. E272-A/B → resolution stage; resolution clears active crisis eligibility while preserving immutable historical evidence.
4. Historical resolution evidence must not reactivate the active predicate.

## Acceptance status

- E271 producer source: **CLOSED**.
- E271 negative branch: **CLOSED**.
- E272 resolution role: **CANONICAL PLACEHOLDER / SOURCE RECOVERY REQUIRED**.
- Exact E272 branch tokens: **OPEN / BLOCKING**.
- Runtime schema promotion: **BLOCKED**.

## Next action

Search repository history/alternate authoritative source material for E272 itself. If no exact source can be recovered, escalate the missing authored source as a content-integrity blocker rather than manufacturing semantics.

## Scope protection

E273–E277 remain excluded from frozen production semantics. No expansion event may be substituted for missing E272 source evidence.

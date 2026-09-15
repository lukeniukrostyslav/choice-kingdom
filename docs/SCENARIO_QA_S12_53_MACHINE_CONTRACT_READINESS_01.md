# Scenario QA S12.53 — Machine Contract Readiness

## Purpose
Add a deterministic source-level readiness ledger for the canonical machine contract without promoting unresolved contracts to CLOSED.

## Scope
- Frozen production scope: E01–E272.
- Expansion candidates E273–E277 remain excluded.
- This gate is **not** a gameplay readiness gate and **not** a reachability proof.

## Implementation
- `tools/validate_canonical_contract_readiness.py`
- Output: `docs/MACHINE_CONTRACT_READINESS_01.json`
- CI: `.github/workflows/canonical-contract-readiness.yml`

## Assertions
1. Frozen scope is exactly E01–E272.
2. Excluded scope is exactly E273–E277.
3. Canonical source-closed producer inventory exists.
4. Delayed-consumer rows have explicit CLOSED/PARTIAL/OPEN status and candidate lists.
5. Required composite predicates are present exactly as the bounded contract set.
6. Hard-negative inventory is present.
7. OPEN/PARTIAL items are reported as warnings and never promoted automatically.
8. The report explicitly states that ID parity is not semantic equality and source closure is not gameplay reachability.

## Verification status
The validator and dedicated workflow have been committed. The next verification action is to observe the GitHub Actions run on the latest `main` commit and inspect the generated readiness artifact. Until that run is visible and green, this QA item is **IMPLEMENTED / VERIFICATION PENDING**, not GREEN.

## Why this matters
Earlier graph gates proved increasingly strong structural properties but did not provide one bounded machine ledger showing whether the required producer, delayed-lifecycle, composite-predicate and hard-negative sections were all present and explicit. This gate closes that observability gap without weakening the conservative OPEN/PARTIAL policy.

## Non-goals
- No invented E33/E34 content.
- No runtime Decision Engine implementation.
- No Android/UI work.
- No claim that graph ID parity equals authored semantic equality.
- No claim that structural graph reachability equals fresh-run gameplay reachability.

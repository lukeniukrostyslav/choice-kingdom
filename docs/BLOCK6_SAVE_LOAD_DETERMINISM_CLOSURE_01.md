# Choice Kingdom — Block 6 Save / Load + Determinism

Date: 2026-09-16

## Scope

Block 6 covers complete runtime-state persistence, stable canonical snapshots, repeated-run determinism, save integrity and recovery.

## Implemented

- Versioned save envelope (`format_version=2`) around the canonical runtime snapshot.
- SHA-256 integrity digest over a canonical JSON serialization.
- Atomic save replacement through a temporary file and `os.replace`.
- Previous save retained as a `.bak` recovery copy.
- Legacy raw schema-v1 snapshots remain loadable.
- Strict snapshot validation for run identity, turn, production event identity, canonical resources/relationships and pending-delay identity.
- Complete state round-trip coverage including resources, relationships, flags, history, threads, pending delays, replay meta, ending evidence, coalition state, blockers and ending identity.
- Deterministic continuation verification after save/load.
- Deterministic delayed-target execution verification after save/load.
- Corruption rejection and backup recovery verification.

## Verification

Local Python 3.13 test suite:

`PYTHONPATH=. pytest -q`

Result: **167 passed**.

The dedicated workflow `.github/workflows/save-load-determinism.yml` runs the persistence, delayed lifecycle, replay and ending save/load regression surface in CI.

## Closure boundary

The implementation and applicable automated verification for Block 6 are GREEN. This does not imply Android/device persistence verification or production release readiness; those remain later production gates.

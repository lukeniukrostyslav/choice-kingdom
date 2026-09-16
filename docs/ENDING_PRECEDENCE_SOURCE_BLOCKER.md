# Ending precedence source blocker — resolved

The canonical QA matrix requires explicit authored winners for simultaneous ending pairs. The repository now contains the authoritative machine source contract at `docs/MACHINE_ENDING_PRECEDENCE_TABLE_01.json`.

Runtime precedence is allowed to project that source contract, but it must not infer winners from code order, enum order, event IDs, source-file order, or narrative assumptions. The ending runtime test suite now checks that the runtime positive precedence is an exact projection of the machine source contract.

This document remains as a traceability record for the blocker that previously prevented closure. It is no longer the active source blocker.

Block 5 still cannot be declared 100% closed until the complete P01–P30 matrix is executable and GREEN, including ending qualification/prerequisite producer closure, delayed-consequence interactions, replay isolation, save/load determinism, and namespace anti-alias controls.

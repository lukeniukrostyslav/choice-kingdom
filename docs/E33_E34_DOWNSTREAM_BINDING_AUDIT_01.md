# E33/E34 Downstream Binding Audit

Status: source-integrated; downstream semantic binding remains conservative.

## Closed authored edges

- E33 resolved -> E35 trigger.
- E34 `people_heard` -> E50 trigger.
- E33 `constitutional_limit` -> E67 consumer requirement.
- E33 `emergency_power` -> E62 consumer requirement.

## Binding rules

1. An authored ending trigger is a consumer requirement, not proof that the runtime predicate is executable.
2. `constitutional_limit` MUST NOT be promoted directly to `pred.constitutional_prepared_strong` without an explicit producer/ordering contract.
3. `people_heard` MUST NOT be promoted directly to `pred.peoples_charter` or another final predicate without an explicit consumer contract.
4. `emergency_power` MAY satisfy the explicit E62 authored component, but repeated emergency use and military dependency remain separate requirements.
5. E47–E50 authored events are evidence-producing nodes; their flags must be compiled into predicates only where a canonical predicate contract exists.

## Current open gates

- `pred.constitutional_prepared_strong`: executable producer and component ordering.
- `pred.coalition_cooperation`: explicit producer/qualification semantics.
- `pred.systemic_explanation_verified`: explicit convergence producer/key.
- `pred.final_charter_prerequisites`: E209 producer closure.
- deterministic ending precedence and terminal tie-break.

## Decision

Do not begin Decision Engine implementation from these ending strings alone. Preserve the authored catalog and close the predicate contracts first.

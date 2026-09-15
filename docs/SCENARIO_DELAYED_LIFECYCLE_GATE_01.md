# Choice Kingdom — Delayed Lifecycle Gate 01

Status: **SOURCE-LEVEL GATE — OPEN**
Scope: delayed callbacks E127–E130, E181–E185, E242–E246.

## Closure contract

Every delayed consequence must have:

- authoritative source event and source choice;
- consequence identity;
- earliest legal turn / delay rule;
- exactly-once identity;
- explicit resolution target;
- cancellation or supersession rule;
- save/load persistence identity;
- replay isolation rule where applicable.

## Current source-backed producers

| Callback | Source | Current status |
|---|---|---|
| E181 | E45-B `infrastructure_concession` | source identity known; lifecycle open |
| E182 | E117-B `veteran_patronage` | source identity known; lifecycle open |
| E183/E242 | E118-B `estate_exception` | source identity known; lifecycle open |
| E185 | E17-A `cheap_weapons` | source identity known; crisis-resolution lifecycle open |
| E243 | E18-B `public_bridge` | source identity known; lifecycle open |
| E244 | E09-B `flexible_accounts` | source identity known; lifecycle open |
| E245 | E20-A `soldier_compensation` | source identity known; lifecycle open |
| E246 | E160-A `winter_rent_ceiling` | source identity known; lifecycle open |

## P0 rule

A delayed event is not scenario-closed merely because its prose says `N+ turns later`. The executable identity must be unique and persist across save/load without duplicate scheduling. Cancellation/supersession cannot be inferred from later narrative state.

## Result

The source inventory is preserved, but delayed lifecycle is **not yet closed**. No scenario percentage is raised by this document.

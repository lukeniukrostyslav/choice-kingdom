# Choice Kingdom — Game State Model

## Purpose
Define the first implementation contract for the reusable decision-game engine. This is a real runtime model, not a content mock.

## Core state

```text
KingdomState
├── day / turn
├── resources
│   ├── gold
│   ├── trust
│   ├── security
│   ├── power
│   └── reputation
├── flags
├── relationships
├── decision_history
├── event_history
├── active_threads
├── unlocked_events
└── ending_status
```

## Event contract
Each event must have:
- stable id
- localized title/body
- two choices minimum for normal decision events
- optional conditions
- immediate consequences
- optional delayed consequences
- optional flags/relationship changes
- optional follow-up event/thread activation
- deterministic outcome rules for a given state and seed

## Choice contract
Each choice must have:
- stable id
- localized label
- availability conditions
- immediate consequences
- history marker
- optional delayed consequence/thread

## Conditions
Conditions are data, not hard-coded story branches. Initial operators:
- resource >= / <= / ==
- flag exists / missing / equals
- relationship >= / <= / ==
- prior decision chosen
- event completed
- event count
- turn/day range
- random gate using seeded RNG

## Consequences
Initial operations:
- add/set resource
- add/remove/set flag
- modify relationship
- record decision marker
- activate/deactivate event thread
- schedule delayed consequence
- unlock ending condition

All mutations must be validated and clamped where a resource has defined bounds.

## Delayed consequences
A delayed consequence is scheduled with a trigger condition or turn offset. It must survive save/load and must be resolved exactly once.

## Determinism
Given the same initial save, decision history, event data, and RNG seed, event selection and consequences must be reproducible. Randomness must never silently bypass conditions.

## Save contract
Saves must contain a version number and enough state to resume without reconstructing hidden state from UI. Invalid or incompatible saves must fail safely and preserve the last valid save where possible.

## Endings
Endings are data-defined conditions. Reaching an ending freezes the current run result but keeps the save/replay history available for starting another run.

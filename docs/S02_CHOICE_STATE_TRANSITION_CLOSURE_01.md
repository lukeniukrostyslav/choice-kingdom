# Choice Kingdom — S02 Choice → State Transition Closure 01

Date: 2026-09-16
Status: SOURCE-LEVEL CLOSED / RUNTIME PENDING
Scope: frozen production events E01–E272.

## Purpose

S02 is the authored choice-transition contract. Every player-facing choice in the frozen production catalog must resolve to an explicit authored state/history/effect signal. The contract preserves the authored narrative rather than inventing engine behavior.

## Frozen source contract

1. Production scope is exactly E01–E272; E273–E277 are excluded.
2. There are 272 authored events: 259 normal choice events and 13 special/convergence/state events.
3. Normal events require A and B choices.
4. E51 and E108 are the only currently confirmed production events with an additional authored C choice; frozen choice-row cardinality is 520.
5. Every authored choice must contain a deterministic transition signal: numeric state/resource/relationship delta, canonical backtick state/history marker, or an explicit transition clause such as Immediate, Flag, Delayed, Unlock, Producer, Resolution, Clear, History, Meta, Ending, or Condition.
6. Alternative choices must have distinguishable semantic signatures; identical alternatives are rejected.
7. Authored trigger/narrative coverage is required for every production event. The source may use an explicit `Trigger` section or the established authored narrative opening; validators must not force artificial trigger prose into existing content.
8. The five numeric base resources remain gold, trust, security, power, and reputation. Contextual pressures such as food, winter, border, guild, and information are state/predicate concepts, not silent additional numeric resources.
9. A consumer may not manufacture a prerequisite merely because the event consumes it. Producer/consumer identity remains governed by the canonical graph and producer registry.
10. This closure is source-level only. It does not claim Decision Engine execution, runtime reachability, save/load persistence, replay execution, or Android readiness.

## Verification gates

S02 is considered source-level closed only when all of the following pass on GitHub Actions:

- event/cardinality closure;
- authored trigger/narrative coverage;
- A/B baseline plus documented alternatives;
- explicit transition payload presence;
- distinct alternative semantics;
- forbidden sixth-resource pattern detection;
- canonical producer/consumer boundary consistency.

Runtime implementation and runtime tests remain downstream gates and must not be represented as complete by this document.

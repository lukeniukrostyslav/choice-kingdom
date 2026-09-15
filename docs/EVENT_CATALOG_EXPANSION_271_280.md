# Choice Kingdom — Canonical Expansion Events E271–E280

These nodes are authored continuation of the E211–E270 expansion. They exist to close canonical producer/consumer gaps discovered during narrative QA. They are not engine data yet.

## Border-crisis lifecycle closure

### E271 — The Border Council Alarm
**Trigger:** `pred.border_tension` + corroborated frontier-warning infrastructure (`frontier_military_watch` or `civilian_signal_authority`).

The border council confirms that the warning is no longer only a frontier anomaly: the kingdom must decide whether a formal crisis exists.

**A — Declare the border crisis**
- Durable state: `border_crisis_declared = true`.
- Durable state: `border_crisis_resolved = false`.
- Thread: `thread.border_crisis = active`.
- Makes `pred.border_crisis` eligible for downstream crisis consumers.

**B — Resolve the warning without declaring a crisis**
- Durable state: `border_crisis_resolved = true`.
- Thread: `thread.border_crisis = resolved_without_declaration`.
- Must not satisfy `pred.border_crisis`.

**QA rule:** E271-A is the authored declaration producer. E195/E253/E255 are consumers and cannot manufacture the predicate merely by being reached.

### E272 — The Border Crisis Accord
**Trigger:** `pred.border_crisis` + `border_crisis_declared = true` + an available resolution route (`joint_border_survey`, `negotiated_withdrawal`, `border_commander_report`, or `military_red_line`).

After the border alarm has been formally declared, Rowan and the border council present evidence that allows the Crown to end the emergency without pretending that the earlier warning never happened.

**A — Ratify the joint border settlement**
- Durable state: `border_crisis_resolved = true`.
- Durable state: `border_crisis_declared = true` (historical fact remains true).
- Thread: `thread.border_crisis = resolved`.
- Clears the active crisis predicate: `pred.border_crisis = false`.
- State effect: +5 reputation, +3 trust, -2 security.
- History: `history.border_crisis_resolved_diplomatically`.

**B — End the crisis under a military security guarantee**
- Durable state: `border_crisis_resolved = true`.
- Durable state: `border_crisis_declared = true` (historical fact remains true).
- Thread: `thread.border_crisis = resolved_under_security_guarantee`.
- Clears the active crisis predicate: `pred.border_crisis = false`.
- State effect: +5 security, -3 gold, -3 reputation.
- History: `history.border_crisis_resolved_by_guarantee`.

**QA rule:** E272 is the canonical active-crisis resolution producer. Resolution does not erase the historical declaration; it only invalidates the active predicate. E272 cannot be reached as a crisis resolution unless E271-A first established the active crisis. E271-B is not sufficient.

## Producer / consumer contract

- `pred.border_crisis` lifecycle is now explicitly two-stage: E271-A declares; E272-A/B resolves.
- `border_crisis_declared` is historical and remains true after resolution.
- `border_crisis_resolved` is the durable lifecycle marker used to clear the active predicate.
- Downstream consumers such as E195, E253 and E255 may consume an active crisis but must never act as producers.
- Future border events must preserve the distinction between warning, declared crisis, active crisis, and resolved crisis.

## Content QA

- No new numeric resource is introduced.
- The node does not depend on an ending result.
- The node does not retroactively create constitutional, guild, coalition, or evidence prerequisites.
- Resolution is deterministic and save/load-safe once represented by the future engine schema.
- The historical declaration remains queryable for later callbacks and ending qualification.

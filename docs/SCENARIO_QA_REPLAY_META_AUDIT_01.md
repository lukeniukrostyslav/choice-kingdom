# Choice Kingdom — Scenario QA Replay Meta Audit 01

Status: **SOURCE-LEVEL QA — REPLAY BOUNDARY AUDIT**  
Scope: E01–E272 production semantics only.  
Date: 2026-09-15.

## Purpose

Close the scenario-analysis gap around replay-only consequences without promoting ordinary history flags into cross-run state.

## 1. Authored replay-oriented consumers/callbacks

The authored graph identifies replay-sensitive nodes including:

- E186 — replay divergence source/callback boundary;
- E247 — Different Suspect;
- E248 — Forgotten Favor;
- E249 — Second Map;
- E250 — Pattern Break;
- E270 — late replay/information qualification support.

These nodes are narrative evidence that replay differentiation is intended. They are not, by themselves, a machine-readable persistence contract.

## 2. Required meta-state contract

A replay fact may cross the completed-run boundary only when the source explicitly defines all of:

`metaKey + sourceEvent/sourceChoice + promotion timing + isolation rule + persistence scope`.

The following are therefore invalid assumptions:

- ordinary `history.*` automatically becoming `meta.*`;
- a second-run trigger implicitly granting all first-run facts;
- replay callbacks manufacturing their own prerequisite;
- a narrative phrase such as "second-run information" serving as an executable persistence rule.

## 3. Current source boundary

E247 explicitly describes a second-run information route and an alternative suspect. E248 explicitly describes a replay callback and a prior favor. E249/E250 deepen the alternative-information path. E270 participates in late replay/information qualification.

However, the current authoritative source set does not yet provide a complete inventory mapping each replay fact to a durable `meta.*` key with promotion timing, scope and isolation semantics.

Therefore replay producer closure remains **OPEN**.

## 4. Fresh-run isolation requirement

A fresh campaign must begin without inherited replay state except for explicitly promoted `meta.*` facts. No ordinary first-run history marker may leak into a fresh run.

Conversely, a replay-only callback must not become reachable in a first run merely because its ordinary narrative prerequisite exists.

These are test requirements, not yet runtime verification results.

## 5. Ending interaction

E269/E270 can provide ending-support evidence, but replay evidence must remain distinguishable from ordinary history until the ending contract explicitly accepts a replay meta predicate.

No replay fact is therefore promoted to a final ending gate by this audit.

## 6. Promotion decision

| Replay area | Status | Decision |
|---|---|---|
| Replay narrative intent | CLOSED at authored-description level | Preserve |
| `meta.*` producer inventory | OPEN | Do not promote |
| Promotion timing | OPEN | Do not promote |
| Persistence scope/isolation | OPEN | Do not promote |
| Fresh-run isolation test | OPEN | Must be simulated later |
| Replay reachability | OPEN | Must be simulated later |
| Replay-to-ending qualification | OPEN | Do not promote |

## QA conclusion

Replay scenario semantics are intentionally present, but the cross-run state contract is not yet sufficiently explicit for engine implementation. The safe foundation is therefore to preserve replay evidence as authored intent while keeping ordinary history and replay meta-state strictly separated.

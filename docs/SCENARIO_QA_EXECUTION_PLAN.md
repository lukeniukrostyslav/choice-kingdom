# Choice Kingdom — Scenario QA Execution Plan

Date: 2026-09-15  
Frozen production scope: **E01–E272**  
Expansion candidates E273–E277: **excluded**

## Purpose

Break the long scenario-QA effort into durable, independently checkable batches so work cannot be repeated or forgotten between sessions.

## Mandatory persistence rule

Every completed batch must:
1. produce a concrete QA artifact or authoritative-source correction;
2. be committed to GitHub `main`;
3. be recorded in `docs/SCENARIO_QA_WORKLOG.md`;
4. include the commit SHA and batch status;
5. never be treated as complete from documentation alone when the underlying source has not been checked.

## Execution order

### Batch S01 — Event inventory: E01–E34
- [ ] triggers extracted
- [ ] outputs extracted
- [ ] flags/history/predicates/threads identified
- [ ] delayed producers/consumers identified
- [ ] duplicate/contradictory writers recorded

### Batch S02 — Event inventory: E35–E70
- [ ] same checks as S01

### Batch S03 — Event inventory: E71–E110
- [ ] same checks as S01

### Batch S04 — Event inventory: E111–E150
- [ ] same checks as S01

### Batch S05 — Event inventory: E151–E210
- [ ] same checks as S01

### Batch S06 — Event inventory: E211–E270
- [ ] same checks as S01

### Batch S07 — Event inventory: E271–E272 + cross-catalog reconciliation
- [ ] same checks as S01
- [ ] verify border-crisis lifecycle without aliasing `thread.border`

### Batch S08 — Global producer/consumer closure
- [ ] undefined producers
- [ ] undefined consumers
- [ ] duplicate semantic writers
- [ ] contradictory writers
- [ ] hard-negative violations

### Batch S09 — Predicate dependency graph
- [ ] producer dependencies
- [ ] consumer dependencies
- [ ] cycles
- [ ] self-satisfaction hazards
- [ ] independent-domain qualification

### Batch S10 — Delayed consequence contracts
- [ ] sourceEventId
- [ ] sourceChoiceId
- [ ] consequenceId
- [ ] earliest turn/timing
- [ ] target/resolution identity
- [ ] exactly-once key
- [ ] cancellation/supersession

### Batch S11 — Endings and replay
- [ ] seven ending incoming paths
- [ ] deterministic precedence
- [ ] Broken Diadem / Quiet Throne producers
- [ ] exact `meta.*` producer/key inventory
- [ ] replay isolation

### Batch S12 — Causal reachability and graph reconciliation
- [ ] fresh-run reachability
- [ ] representative replay reachability
- [ ] graph-vs-catalog reconciliation
- [ ] final contradiction/duplicate/undefined sweep

## Completion gate

Scenario QA may move above 65% only after the relevant batches are actually checked and persisted. The final 100% scenario-QA gate requires all S01–S12 to be closed or explicitly dispositioned with authoritative evidence. Engine/UI/Android/APK remain blocked until that gate is met.

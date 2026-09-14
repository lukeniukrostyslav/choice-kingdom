# Choice Kingdom — Reachability Pre-Audit 01

Status: **SOURCE-VERIFIED PRE-AUDIT — NOT AUTOMATED REACHABILITY**
Scope: E01–E70 campaign spine and ending layer.

This document records only findings that can be supported by the authored catalog. It does not claim full reachability until the complete E01–E270 catalog is represented in machine-readable form and simulated.

## Directly verified trigger risks

| Event | Authored trigger | Risk | Required canonical resolution |
|---|---|---|---|
| E03 | `food prices rise` | No explicit canonical producer in the E01–E02 spine | Define price-pressure predicate or authored producer |
| E05 | `security < 55 or turn 4+` | Numeric threshold is clear, but baseline/turn progression must be engine-defined | Canonical resource + turn predicate |
| E06 | `court_first` or `Seris >= 1` | Relationship shorthand must use `rel.seris` | Canonical relationship predicate |
| E09 | `Mara >= 1` + `decree_investigation` | Mara relation and flag need canonical IDs | `rel.mara` + `flag.decree_investigation` |
| E10 | `Rowan >= 1` | Relationship shorthand | `rel.rowan >= 1` |
| E11 | `Seris >= 1` | Relationship shorthand | `rel.seris >= 1` |
| E12 | `trust < 60 or food shortage` | `food shortage` has no direct producer in spine | Derived food predicate must be defined |
| E13 | `Toma unlocked through dock events` | Informal trigger rather than stable condition | Canonical Toma unlock flag/thread |
| E14 | `Ivo >= 2` | Relationship shorthand | `rel.ivo >= 2` |
| E16 | `security < 60 or local_command` | Numeric + flag combination is usable but needs canonical names | Canonical resource/flag predicates |
| E17 | `security < 65` | Clear resource predicate; baseline and turn distribution need simulation | Canonical resource predicate |
| E18 | `merchant_charter or competitive_market` | Both are durable route markers but currently prose-level names | Canonical flags/thread IDs |
| E19 | `merchant_charter` + no `audit_office` | Strong deterministic gate; must preserve negative condition | Canonical positive/negative flag evaluation |
| E20 | `Rowan >= 1` | Relationship shorthand | `rel.rowan >= 1` |
| E21 | `Toma >= 1 or quiet_market_inquiry` | Relationship + flag | Canonical relationship/flag predicate |
| E22 | `trust >= 55` | Clear resource predicate | Canonical resource predicate |
| E23 | `ledger_fragment_a` | Producer exists through E07/E21 branches, but exact production provenance must be represented | Canonical history/evidence marker |
| E24 | `audit_office` | Producer E09 exists | Canonical flag |
| E25 | `Toma >= 1` + `auditor_missing_public` or quiet search | Compound gate has ambiguous precedence in prose | Explicit boolean grouping in schema |
| E26 | `Seris >= 2` + ledger chain active | Relationship + noncanonical thread shorthand | `rel.seris` + `thread.ledger_investigation` |
| E27 | ledger chain active | Thread shorthand | Canonical thread predicate |
| E28 | `decree_investigation` + ledger chain | Both have identifiable producers | Canonical flag/thread |
| E29 | `late campaign; at least two unresolved pressures` | No exact turn/window or pressure predicate | Deterministic derived condition required |
| E30 | `winter + market tension` | Both are prose-level conditions | Canonical winter/market predicates |
| E31 | `winter + security < 60 or military escalation` | Boolean precedence ambiguous | Explicit `(winter AND low_security) OR military_escalation` or authored intended grouping |
| E32 | E29 + E30 + E31 unresolved | Event completion dependency is clear, but unresolved-state representation is not | Canonical unresolved crisis markers |
| E32-B | `at least two strong relationships` | No exact threshold/character set | Canonical coalition predicate |
| E33 | `emergency_decree_used or severe crisis` | `severe crisis` not deterministic yet | Canonical crisis predicate |
| E34 | `trust >= 65 or welfare branch` | `welfare branch` is not a stable state ID | Canonical civic/welfare thread marker |
| E35 | Act V + relationship/flags | Proposal generation needs deterministic ordering and minimum viable proposal rule | Production proposal resolver contract |
| E36 | hidden-ledger chain completed | Chain identity needs canonical thread completion | `thread.ledger_investigation` completion |
| E36-C | audit office + evidence + 2 cross-faction relationships | Clear concept, but `evidence` and cross-faction threshold need exact IDs | Canonical evidence predicate + coalition definition |
| E37 | late game + no clear succession | `clear succession` not defined | Canonical succession state/predicate |
| E38 | ending resolution | Safe if resolver is deterministic | Ending resolver contract |
| E39 | ending resolver | Seven endings named; prerequisites require simulation | Ending reachability matrix |
| E40 | any ending | Deterministic post-ending callback required | Ending metadata |

## Strong pre-audit observations

### 1. E12 has a potentially producer-less branch
`food shortage` is referenced as an E12 trigger, but the early spine itself does not create a canonical `food_shortage` marker. E03 describes rising food prices, and later events can create shortage conditions. This is acceptable only if the engine defines an explicit derived predicate or if an authored event produces the marker before E12 can fire.

### 2. E25 needs explicit boolean grouping
The prose `Toma >= 1 and auditor_missing_public or quiet search` is ambiguous. Production data must encode the intended grouping explicitly, not rely on parser precedence.

### 3. E29–E34 are currently narrative predicates
`unresolved pressures`, `winter`, `market tension`, `severe crisis`, `welfare branch`, and `strong relationships` need exact canonical definitions before reachability can be calculated.

### 4. E35 proposal viability is a resolver problem
E35 is intentionally dynamic. The rule says at least two proposals must remain viable in a normal run. This cannot be proven from prose; it requires deterministic simulation over prior histories.

### 5. Ending reachability is still unproven
E39 names seven endings and the catalog gives conceptual prerequisites, but no exhaustive simulation currently proves that each ending is reachable through at least two distinct meaningful histories where intended.

## Required next machine checks

1. Enumerate every event ID E01–E270.
2. Enumerate every trigger token and classify as resource, relationship, flag, history, thread, derived predicate, turn/window, or replay metadata.
3. For every flag/history/thread token, find at least one producer unless explicitly declared derived.
4. Detect consumer-only tokens.
5. Detect producer-only tokens with no downstream consumer where downstream impact is expected.
6. Expand compound triggers into explicit boolean trees.
7. Build incoming/outgoing event graph.
8. Mark roots, sinks, unreachable nodes, and dead-end nodes.
9. Simulate ending prerequisites under deterministic seeds and representative resource trajectories.
10. Record every impossible prerequisite as a content defect rather than silently widening conditions.

## Gate

This pre-audit raises canonical/reachability confidence but does **not** mark the campaign CONTENT READY. Automated reachability remains 0% until the machine-readable catalog and simulator exist and are actually run.

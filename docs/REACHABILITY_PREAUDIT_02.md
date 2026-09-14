# Choice Kingdom — Reachability Pre-Audit 02

Status: **DESIGN PRE-AUDIT — NOT RUNTIME VERIFICATION**

## Purpose

Re-evaluate reachability assumptions after the E35–E40 ID reconciliation and ending qualification contract.

## Immediate findings

### 1. Core spine is not sufficient by itself
The graph declares E01→E02→E03→E04 as the core spine, but many later events use relationship/flag predicates that depend on optional branches. Therefore reachability must be evaluated from actual state transitions, not graph adjacency alone.

### 2. E35–E40 ambiguity is now bounded
Production numbering is canonicalized to the Act V continuation. Legacy ending material is retained as `LEGACY-END-*` review content. Any production reference to E35–E40 must now mean the Act V events.

### 3. Route consumers requiring producer closure
The following route families remain high priority for exhaustive producer extraction:
- `thread.institutional_reform`
- `thread.document_audit`
- `thread.noble`
- `thread.guild`
- `thread.veteran`
- `thread.border`
- `thread.amara`
- `thread.toma`
- `thread.archive`
- `thread.coalition`
- `thread.succession`
- `thread.budget_reform`
- `thread.archive_reform`

A graph edge pointing to an event does not prove that the event's trigger can be satisfied.

### 4. High-risk trigger clusters
The following require explicit reachability simulation after machine-readable conversion:

- E216: low gold + high reform spending;
- E218/E225/E251/E254/E255: food pressure/crisis escalation;
- E227/E253/E259: border/military/constitutional separation;
- E231: Toma route + high information pressure;
- E232: at least two distinct procurement clues;
- E250: at least three related clues;
- E261: at least four faction routes;
- E265–E270: ending qualification dependencies.

### 5. Delayed-event reachability
Every delayed trigger must preserve:
- source event/choice;
- exact delay in turns;
- exact-once resolution identity;
- target event or predicate;
- behavior across save/load;
- behavior when another branch changes the relevant state before due time.

The narrative phrase "later" is not an acceptable production trigger.

## Reachability classifications for future validator

Each event will receive one of:

- **REACHABLE_CORE** — reachable from new game through ordinary deterministic paths;
- **REACHABLE_BRANCH** — reachable only after explicit optional route;
- **REACHABLE_REPLAY** — requires explicit replay metadata transfer;
- **REACHABLE_DELAYED** — requires a valid delayed consequence;
- **CONDITIONAL_ENDGAME** — reachable only through ending qualification state;
- **UNREACHABLE** — no valid producer path;
- **AMBIGUOUS** — trigger cannot yet be canonicalized;
- **CONTRADICTORY** — source requirements conflict with reachable state.

## Current blocker

No runtime reachability percentage can honestly be claimed until the authored catalogs are converted into machine-readable candidate data and a deterministic graph validator exists.

The correct next step is producer extraction and trigger compilation, not manual graph-edge inflation.

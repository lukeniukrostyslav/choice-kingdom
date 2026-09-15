# Choice Kingdom — Scenario Ending Precedence Matrix 01

Status: **SOURCE-LEVEL PRECEDENCE GATE — OPEN**  
Scope: ending convergence E208–E210 and E261–E272.

## Required evaluation model

Ending selection must evaluate a complete snapshot, not event proximity. Each ending requires:

1. all positive prerequisites satisfied;
2. all negative blockers absent;
3. replay/meta requirements evaluated separately from same-run history;
4. exactly one deterministic winner after precedence/tie-break evaluation;
5. no consumer is allowed to manufacture a missing prerequisite.

## Ending families

- Steward
- Iron Crown
- Golden Compact
- People's Charter
- Broken Diadem
- Quiet Throne
- Second Founder

## Current hard gates

| Gate | Status |
|---|---|
| Positive prerequisite inventory | OPEN |
| Negative blocker inventory | OPEN |
| People's Charter producer for `pred.final_charter_prerequisites` | BLOCKED |
| Second Founder systemic explanation producer | BLOCKED |
| Second Founder coalition qualification | BLOCKED |
| Replay-only qualification isolation | BLOCKED |
| Deterministic tie-break order | OPEN |
| Fresh-run exhaustive ending reachability | OPEN |
| No-ending / dead-end behavior | OPEN |

## Prohibited shortcuts

- E261 `four_way_bargain` cannot itself become `pred.coalition_cooperation`.
- E267–E270 cannot become final predicates merely because they are late in the catalog.
- E209 cannot create `pred.final_charter_prerequisites` while consuming it.
- Ordinary same-run history cannot substitute for replay metadata.
- Narrative similarity cannot establish semantic equality between predicates.

## Closure rule

This matrix is not a claim that endings are closed. Scenario 100% requires every gate above to be backed by authoritative source contracts and then verified by executable checks/reachability. No percentage is increased by documentation alone.

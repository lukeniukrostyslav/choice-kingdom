# Choice Kingdom — Border Trigger Normalization 01

Date: 2026-09-15  
Scope: **E01–E272 production scenario**  
Status: **SOURCE QA — NORMALIZED**

## Verified correction

The authoritative E271–E272 catalog previously expressed two lifecycle triggers in prose/legacy form:

- E271: `thread.border` active
- E272: `thread.border_crisis = active`

These forms were inconsistent with the frozen predicate contract and could be misread by a machine source inventory as independent producer tokens.

The canonical authored triggers are now:

- **E271:** `pred.border_tension` + corroborated frontier-warning infrastructure.
- **E272:** `pred.border_crisis` + `border_crisis_declared = true` + an available resolution route.

## Lifecycle semantics preserved

E271-A remains the sole authored declaration producer for the active border crisis. E271-B explicitly resolves the warning without declaring a crisis and therefore cannot activate `pred.border_crisis`.

E272-A/B remain the sole authored resolution choices. They preserve `border_crisis_declared = true` as historical evidence and clear the active predicate through `border_crisis_resolved = true`.

No downstream consumer is promoted to producer status.

## QA consequence

This is a source normalization, not a gameplay reachability claim. `pred.border_tension` itself remains unresolved until an E01–E272 producer is authoritatively verified. Therefore this correction does **not** close the border route end-to-end.

E273–E277 remain excluded from production semantics.

## Required verification

1. Re-run exhaustive E01–E272 source inventory.
2. Confirm stale `thread.border` no longer appears in extracted E271 trigger tokens.
3. Confirm prose `thread.border_crisis = active` no longer appears as an extracted E272 trigger token.
4. Confirm `pred.border_crisis` remains represented only through its explicit declaration/resolution lifecycle.
5. Re-run canonical graph and contract gates before any percentage increase is granted.

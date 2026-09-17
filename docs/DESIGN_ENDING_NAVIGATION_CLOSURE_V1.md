# Choice Kingdom — Ending + Navigation Design Closure v1

Status: CLOSED DESIGN CONTRACT

## Ending / Outcome

Ending presentation must clearly separate:

1. outcome title,
2. concise outcome summary,
3. key consequences established by the chronicle,
4. unresolved/unknown elements where applicable,
5. continuation/replay/history action.

Ending families use a shared layout grammar so different outcomes remain part of the same product language. Visual emphasis communicates narrative importance, not moral judgement. Long endings scroll; critical actions remain reachable after expansion.

## Navigation / transitions

| Transition | Required behavior |
|---|---|
| Event -> consequence | Preserve decision context; feedback appears before irreversible navigation |
| Consequence -> next event | Clear continuation action; no accidental double activation |
| Event -> History | Preserve return position/context where platform permits |
| Any screen -> Settings | Accessible without destroying current narrative state |
| Ending -> History/replay | Explicit destination; no ambiguous back/continue affordance |

### Transition invariants

- Every interactive transition has visible focus and disabled/resolving behavior.
- Back navigation never silently submits a decision.
- Reduced-motion mode removes nonessential movement.
- Transition state is never the sole carrier of meaning.
- Safe-area insets remain respected during animated and static states.
- RTL changes spatial direction, not semantic destination.

## Closure evidence

- D11 Ending / Outcome: 94% -> 100% design contract closure.
- D12 Navigation / Transitions: 95% -> 100% design contract closure.
- Runtime navigation and physical QA remain separate gates.

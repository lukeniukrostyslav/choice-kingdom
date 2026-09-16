# Choice Kingdom — S06 Replay / Meta-State Closure Contract

Frozen production scope: **E01–E272**  
Excluded expansion candidates: **E273–E277**

## Objective

S06 closes the authored replay/meta-state boundary before Decision Engine implementation. It does not claim runtime replay execution.

## Authoritative replay surface

The only production events with an explicitly replay-meta route are:

| Event | Meta key | Import source | Same-run route | Import cardinality |
|---|---|---|---|---|
| E186 | `meta.replay.warehouse_investigation_unlock` | immediately completed prior run | `warehouse_arson` | exactly once |
| E247 | `meta.replay.second_run_information_route` | immediately completed prior run | none | exactly once |
| E248 | `meta.replay.callback_forgotten_favor` | immediately completed prior run | none | exactly once |

The machine replay contract is the source of truth for these three routes. No other E01–E272 event may acquire an implicit `meta.*` producer merely because its prose mentions replay.

## Reset boundary

A new run starts with a clean run-specific state. The following never cross the boundary as active state:

- ordinary event flags;
- active predicates;
- pending delayed consequences;
- terminal/ending state;
- current resources, relationships and other run-local state.

Only explicitly exported replay metadata from the **immediately completed prior run** may be imported. Import is idempotent and exactly-once per canonical meta key.

## Terminal-state isolation

Completion of an ending produces a completed-run export; it does not turn terminal state into active state in the next run. The next run begins from its normal initial state and may receive only the explicitly permitted `meta.replay.*` keys.

## Fresh-run isolation

A fresh run with no completed prior run must receive zero replay-meta keys. Replay callbacks therefore cannot fire merely because the application was restarted, saved, loaded, or resumed.

## Same-run versus replay semantics

E186 deliberately has two authored routes: the normal same-run `warehouse_arson` route and the explicitly bounded prior-run metadata route. E247 and E248 are replay-meta-only routes. Their prose trigger labels are normalized by the machine contract and are not independent runtime predicates.

## Unsupported inference rules

The following are forbidden until a future authoritative content change explicitly adds them:

1. copying arbitrary run flags into a new run;
2. copying pending delayed events into a new run;
3. copying an ending/terminal state into a new run;
4. treating every occurrence of the word “replay” as a meta trigger;
5. inventing additional replay keys or producers;
6. importing metadata from a run other than the immediately completed prior run;
7. importing the same canonical key more than once.

## Closure status

S06 source-level closure requires exact parity between this document, `docs/MACHINE_REPLAY_CONTRACT_01.json`, the authoritative E186/E247/E248 catalog blocks and the executable validator. Runtime replay execution, state persistence, fresh-run reachability and replay reachability remain downstream implementation gates.

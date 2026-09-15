# Choice Kingdom — Scenario QA Ending Prerequisite Satisfiability 01

Status: **SOURCE-LEVEL QA — ENDING SATISFIABILITY SCREEN**  
Scope: frozen production semantics E01–E272; ending convergence E208–E210 and E261–E272.  
Date: 2026-09-15.

## Purpose

Turn the existing ending incoming-path matrix into a stricter satisfiability screen. The goal is to distinguish a graph path from an actually satisfiable authored prerequisite. No runtime reachability is claimed.

## Rules

1. A consumer cannot manufacture its own prerequisite.
2. A support-evidence node is not automatically a final predicate.
3. Positive prerequisites require an explicit source or an explicitly authored derivation contract.
4. Negative blockers must be checked independently from positive evidence.
5. Replay/meta prerequisites require an explicit cross-run promotion contract.
6. E33/E34 remain quarantined; E273–E277 remain outside production semantics.

## Family screen

| Ending family | Positive closure | Negative/blocker closure | Fresh-run satisfiability | Result |
|---|---|---|---|---|
| Steward | institutional/civic evidence exists in source inventory | not fully compiled | not proven | OPEN |
| Iron Crown | authority/security support routes exist | not fully compiled | not proven | OPEN |
| Golden Compact | economic/guild support routes exist | not fully compiled | not proven | OPEN |
| People's Charter | E209 remains consumer-only for final-charter prerequisites; supporting constitutional evidence exists | not fully compiled | blocked by prerequisite producer closure | OPEN/BLOCKED |
| Broken Diadem | failure/support evidence routes exist | deterministic failure precedence not closed | not proven | OPEN |
| Quiet Throne | withdrawal/stability narrative route exists | blocker precedence not closed | not proven | OPEN |
| Second Founder | systemic explanation + coalition + replay-sensitive evidence routes exist | replay isolation and precedence not closed | replay route not proven | OPEN/BLOCKED |

## Concrete circularity checks

### E209 / final charter
E209 is currently a consumer-only source for `pred.final_charter_prerequisites`. Therefore E209 cannot be used as evidence that independently creates the predicate it consumes. A producer contract must be recovered or authored before this prerequisite can become executable.

### E261 / coalition
`four_way_bargain` is support evidence only. It cannot silently become `pred.coalition_cooperation`. The authoritative cooperation candidate remains E148-A, subject to participant identity, positive outcome and collapse-blocker checks.

### E267–E270
These are support-evidence routes into ending qualification. Their graph proximity to ending families does not itself establish final predicates.

### Second Founder
The ending requires a combination of systemic explanation, cross-faction cooperation, institutional redesign and replay-sensitive qualification. Ordinary history cannot substitute for replay meta-state without an explicit promotion contract.

## Findings

1. The current endgame graph contains structurally plausible routes, but several routes terminate in consumer-only or composite prerequisites whose executable producers are still open.
2. People's Charter is blocked at the prerequisite-producer boundary until `pred.final_charter_prerequisites` is explicitly produced rather than consumed.
3. Second Founder remains blocked by replay meta producer/key closure plus systemic convergence closure and fresh-run/replay separation.
4. Coalition evidence must remain separate from the E261 four-way bargain.
5. No ending family can yet be declared fresh-run reachable from source-level evidence alone.

## Closure result

**Ending prerequisite satisfiability screen: PASS as a conservative blocker audit.**

It closes several false-positive routes by explicitly identifying consumer-only/composite boundaries, but it does not close ending reachability or precedence.

## Remaining blockers

- explicit producer/key for final-charter prerequisites;
- systemic explanation convergence producer/key;
- coalition runtime qualification;
- deterministic negative blockers and precedence for all ending families;
- replay meta producer/key and isolated replay path;
- exhaustive fresh-run reachability;
- semantic equality between graph and authoritative event contracts.

**No Decision Engine promotion is authorized.**

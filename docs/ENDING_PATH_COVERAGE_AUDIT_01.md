# Choice Kingdom — Ending Path Coverage Audit 01

Date: 2026-09-15
Status: SOURCE-LEVEL QA — PRE-RUNTIME
Scope: seven ending families; E265–E270

## Purpose

Check whether the current E265–E270 endgame nodes, as authored, can by themselves be treated as complete ending qualification. They cannot. The ending contract requires explicit predicates, blockers and independent viable paths.

## Verified observations

### E265 — Coalition Holds

Source trigger is `high coalition trust` and the choices produce trust/power changes. The node does not itself establish a canonical `pred.coalition_cooperation` contract. Therefore E265 is an endgame consequence node, not proof that coalition cooperation has been qualified.

### E266 — Mara's Last Report

The node modifies trust/Mara and publishes or edits a report. It is evidence for an institutional/personality route but does not by itself prove the Steward or People's Charter prerequisite families.

### E267 — Rowan's Last Order

The node tests constitutional handling of military authority. It supplies useful ending evidence but cannot by itself manufacture the Iron Crown or Steward qualification.

### E268 — Seris's Last Bargain

The node tests noble/property-rights handling. It is supporting evidence for institutional/commercial routes, not a complete ending prerequisite.

### E269 — Ivo's Late Account

E269 is explicitly distinguished from E55 and is a late commercial/evidence consequence node. It should remain a stable canonical ID. Its evidence must feed the commercial/information qualification layer rather than act as an ending by itself.

### E270 — Amara and Toma at Dawn

E270 creates `dual_witness_account` or `single_witness_account`. The source establishes evidence quality consequences but does not itself establish `pred.systemic_explanation_verified` or `pred.coalition_cooperation`.

## Ending-family coverage status

- Steward: **OPEN** — institutional reform, emergency-power constraints, trust and blockers require complete producer/path matrix.
- Iron Crown: **OPEN** — military/security dependency and retained emergency authority require independent producer coverage and negative blockers.
- Golden Compact: **OPEN** — commercial route and guild influence/leverage require explicit predicate producers; route count is insufficient.
- People's Charter: **OPEN** — civic legitimacy and institutional/public participation require explicit qualifying markers and blockers.
- Broken Diadem: **OPEN** — must have deterministic terminal failure predicate with at least two independent failure paths.
- Quiet Throne: **OPEN** — requires explicit withdrawal/abdication/low-intervention history, not low power/trust alone.
- Second Founder: **OPEN** — requires investigation evidence + `pred.systemic_explanation_verified` + `pred.coalition_cooperation` + constitutional redesign + constrained/expired emergency power.

## Deterministic precedence

The contract requires data-declared priority when multiple endings qualify. No runtime code exists yet, so precedence is **NOT VERIFIED**.

Required production test matrix:
1. each ending with one valid path;
2. each ending with an alternate independent path where required;
3. negative blocker cases;
4. simultaneous qualification cases;
5. collapse-vs-positive precedence;
6. Quiet Throne exclusion when a stronger positive ending qualifies;
7. replay/meta-state cases;
8. save/load determinism;
9. same state/history/seed => same ending.

## Gate

Ending producer/path coverage remains **OPEN**. E265–E270 are authored endgame nodes and must not be counted as proof that any ending is reachable until their inputs, producers, blockers and precedence are mapped in the complete causal graph.

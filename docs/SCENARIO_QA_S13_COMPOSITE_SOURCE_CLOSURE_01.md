# Choice Kingdom — Scenario QA S13: Composite Source Closure 01

Date: 2026-09-15
Scope: frozen production catalog E01–E272 only.
E273–E277 remain excluded.

## Objective

Close the remaining **source-level** ambiguity for composite predicates where the authoritative authored catalog already contains explicit producer evidence. This pass does not claim runtime execution, persistence, scheduler behavior, or gameplay reachability.

## Verified closures

### 1. `pred.systemic_explanation_verified` — SOURCE CLOSED

Authoritative E270-A explicitly writes `systemic_explanation_convergence` and defines the prerequisite evidence families before the convergence step:

1. warehouse/financial evidence;
2. document/language evidence;
3. witness/organizational evidence;
4. explicit E270-A convergence decision.

Therefore E270-A is the canonical convergence producer. Its trigger (`Amara and Toma both active`) is not itself evidence and cannot manufacture a missing family.

### 2. `pred.constitutional_prepared_strong` — SOURCE CLOSED

The independent preparation domains are explicitly authored:

- civic/commons: E50 → `people_charter_endorsed`;
- institutional/audit: E154-A → `crown_audited`;
- faction/house: E161-A → `house_assembly`;
- military/law: E199-A → `army_constitution_oath`.

The source rule is any three distinct domains. E227 `military_red_line` is supporting evidence and is not silently substituted for E199-A. Same-domain downstream evidence is not double-counted.

### 3. `pred.coalition_cooperation` — SOURCE CLOSED

E148-A explicitly records the cross-faction package, names the participating characters and records mutual concessions. The qualification contract additionally requires positive cooperation semantics and absence of an unresolved collapse blocker. E261-A `four_way_bargain` is not an alias and cannot independently qualify the predicate.

### 4. `pred.guild_influence_strong` — SOURCE CONTRACT CLOSED

The independent source domains are frozen as:

- representation: E49 `guild_political_representation` / E144 `history.guild_representation` — one domain;
- tribunal: E168-A `guild_tribunal_independent`;
- commercial/market: E165-A `official_credit_disclosure` or E166-A `audited_monopoly` — one commercial domain;
- logistics: upstream E136-B `history.guild_logistics_cooperation` plus E194-A neutral inspection and no immunity-risk blocker.

`rel.ivo` is not a substitute. E49 and E144 cannot be counted twice.

## Replay correction

E131 is an authored **consumer** of the previous-run informational condition `all_voices_heard`; it is not a proven producer of that meta-state. No in-scope explicit producer for the replay key is promoted by this pass. E186 remains partial and E247/E248 remain open until their exact producer/key tuples are authored or otherwise explicitly bound in source.

## Negative closure checks

- No consumer is promoted to producer merely because its trigger names the required predicate.
- No E273–E277 output is admitted into E01–E272 semantics.
- No relationship score substitutes for institutional evidence.
- No ordinary history flag is promoted to `meta.*` automatically.
- No same-domain downstream evidence is counted as an independent domain.
- No generic compensation route is expanded into E125/E156/E20 without explicit authored identity.

## Result

**PASS — source-level composite predicate identities closed wherever an explicit E01–E272 authored producer exists.**

Remaining blockers are explicitly downstream: runtime aggregation/invalidation, save/load, delayed ordering, replay producer provenance, fresh-run gameplay reachability, and deterministic ending precedence/terminal selection.

This document raises source-level QA readiness only; it does not authorize the Decision Engine or production schema by itself.

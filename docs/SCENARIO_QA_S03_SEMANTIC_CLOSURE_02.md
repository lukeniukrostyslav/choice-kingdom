# Choice Kingdom — S03 Semantic Closure 02

Date: 2026-09-15  
Scope: S03 findings from E71–E110  
Status: **PARTIALLY CLOSED — remaining engine/predicate contract work explicitly separated**

## 1. `shared_crisis_command` — E104

Direct repository search found no authored producer for `shared_crisis_command`.

Conclusion: this is an **undefined producer candidate**, not a valid cross-catalog consumer. E104 currently consumes a state that no frozen authored event is known to produce.

Required canonical resolution before engine integration:
- either author an upstream event that explicitly produces the fact;
- or replace the E104 trigger with an already-canonical crisis predicate/fact whose producer is proven;
- do not let the runtime infer `shared_crisis_command` from prose, security, or an unrelated crisis flag.

Decision for QA: **OPEN DEFECT / CONTRACT GAP**.

## 2. E36 vs E95 — Mara independence

E36-A produces `mara_independent_mandate`.
E95-A produces `mara_independence`.

The two names express materially similar institutional outcomes, but they are not textually identical and cannot safely be assumed to be separate runtime facts.

Canonicalization rule:
- `mara_independent_mandate` = legacy/source-language fact from E36.
- `mara_independence` = later authored alias/candidate.
- They must be normalized to one canonical predicate/key if they represent the same gameplay state.
- No engine consumer may depend on both as independent facts unless a deliberate distinction is documented.

Decision for QA: **SEMANTIC COLLISION — NORMALIZATION REQUIRED**.

## 3. E37 vs E96 — military oath concepts

E37 produces:
- `army_law_oath`
- `army_crown_oath`

E96 produces:
- `law_bound_guard`
- `personal_guard_oath`

These are not automatically duplicates. The source text suggests two different axes:
- E37 = constitutional loyalty of the army;
- E96 = personal/legal binding of the guard.

However, the distinction is not machine-explicit enough to permit four unrelated predicates without a canonical contract.

Canonicalization requirement:
- retain the conceptual distinction only if downstream endings/decisions consume different institutional domains;
- otherwise normalize to explicit constitutional/military loyalty facts;
- never derive one from another merely because both contain “law” or “Crown”.

Decision for QA: **DISTINCTION PLAUSIBLE — CONTRACT REQUIRED**.

## 4. E108 — investigation depth

E108 changes “investigation depth” but does not name a canonical state key in the authored output.

Decision: **OPEN MACHINE-STATE GAP**.

The engine contract must define an explicit numeric/ordinal state or replace the phrase with a canonical evidence-depth predicate. Free-form narrative text must not become hidden runtime state.

## 5. S03 disposition

Source inventory E71–E110 remains verified.
Semantic closure is not complete because:
1. E104 has an unresolved producer;
2. E36/E95 require alias normalization or an explicit distinction;
3. E37/E96 require an institutional-domain contract;
4. E108 requires a canonical machine state.

No global Scenario QA increase is claimed from this artifact alone.

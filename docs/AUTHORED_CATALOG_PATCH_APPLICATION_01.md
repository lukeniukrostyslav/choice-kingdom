# Choice Kingdom — Authored Catalog Patch Application 01

Date: 2026-09-15
Status: READY FOR DIRECT CATALOG APPLICATION — P0 SOURCE PATCHSET

This file is an application checklist derived from the authored catalog audit. It deliberately does not claim that the source catalog is already patched.

## P0 patches

### E136 — Frozen Road
Replace the prose-only road outcome with canonical durable state:
- public labor: `transport_network_stable`
- guild contract: `transport_network_stable` plus guild logistics route marker
If an active transport crisis is present, the repair outcome also clears `transport_disruption_active`.

### E144 — Guild Seat
The political representation outcome must establish `history.guild_representation` (and its canonical route predicate). A prose trigger named `guild_political_representation` must not remain without a producer.

### E148 — Last Coalition Meeting
The coalition package must record distinct contributing faction identities. `history.cross_faction_package` alone is insufficient for `pred.coalition_cooperation`.

### E192 — Broken Cart
A medicine-first outcome establishes `food_logistics_unstable`; a grain-first outcome establishes `food_logistics_stabilized`. Remove the undefined numeric `+4 food stability` effect. No sixth resource is introduced.

### E194 — Guild Convoy
Neutral-inspector outcome establishes `history.guild_logistics_cooperation` and the institutional guild logistics route. Immunity outcome must not establish cooperation.

### Border crisis
The canonical declaration producer must establish `border_crisis_declared` and `thread.border_crisis`. A later explicit de-escalation producer must establish `border_crisis_resolved` and clear the active crisis. Border pressure/security alone must not silently substitute for this state.

### E197 — Succession Test
Its trigger must consume an already-qualified `pred.constitutional_prepared_strong`. That predicate must be produced upstream from three independent institutional domains and never from E197–E210 outcomes.

### E200 — Merchant Oath
`pred.guild_influence_strong` must be computed from at least two distinct institutional guild domains. `rel.ivo` alone is invalid.

### E207 — Founder Question
The event must consume `pred.systemic_explanation_verified` produced by a distinct evidence convergence. Required evidence classes: warehouse/financial, document/language, witness/organizational, followed by explicit convergence.

### E209 — Dawn Charter
The event must consume `pred.final_charter_prerequisites` assembled before E209 from civic, institutional/audit, factional representation, military/security where required, information/evidence, coalition cooperation, and absence of unresolved mandatory blockers.

### E210 — Last Decision Is Not a Choice
Remain convergence-only. It may evaluate already-established canonical state and qualify an ending, but it must not manufacture missing producer state or directly substitute for upstream prerequisites.

## Application gate

After these exact source changes are applied to the authoritative catalog files:
1. enumerate every producer and consumer for the nine P0 predicates/markers;
2. verify no undefined trigger remains;
3. verify no duplicate producer has conflicting semantics;
4. verify delayed consequences have stable exactly-once identities;
5. rerun graph ↔ catalog reconciliation;
6. rerun reachability pre-audit;
7. only then freeze production data schema.

Until those checks pass, runtime engine work remains blocked by the content-first development order.

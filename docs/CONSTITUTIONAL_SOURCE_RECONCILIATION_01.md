# Choice Kingdom — Constitutional Source Reconciliation 01

Status: SOURCE-LEVEL QA — provisional, not runtime implementation.

## Verified candidate domains

The authored expansion confirms several independent constitutional preparation domains:

- civic/commons: E114 `local_budget_vote`, E122 `tax_transparency`, and related commons participation outcomes;
- audit/institutional: E142-A `auditor_independence`, E154 crown-audit lineage, and E155 publication outcomes;
- faction/house: E161-A `house_assembly` establishes an explicit constitutional assembly outcome;
- military/law: E227-A `military_red_line` explicitly writes a non-crossable military boundary into law.

## Contract constraint

`pred.constitutional_prepared_strong` requires three independent preparation domains. A single event may not be counted as multiple domains merely because it has several consequences. Relationship values do not qualify a domain. Downstream E197–E210 events cannot retroactively satisfy missing upstream preparation.

## Provisional source map

1. Civic/commons: `local_budget_vote` / explicit commons participation.
2. Institutional/audit: `auditor_independence` plus crown-audit lineage.
3. Faction/house: `house_assembly`.
4. Military/law: `military_red_line`.

The final producer contract still requires exact canonical event/choice IDs, anti-double-counting rules, and a full E01–E272 producer-before-consumer pass. Therefore this document does not close the predicate and does not authorize schema/runtime implementation.

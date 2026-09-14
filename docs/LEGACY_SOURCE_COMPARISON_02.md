# Choice Kingdom — Legacy Source Comparison 02

Date: 2026-09-15
Status: **SOURCE-LEVEL QA — COMPARISON COMPLETE FOR E73/E156/E99/E173**

## E73 vs E156 — distinct nodes

### E73 — Three Stamps
- Trigger: `audit_office`.
- Narrative role: institutional accountability and named responsibility for emergency purchases.
- Outputs: `named_authority` or `overlapping_authority`.
- Character/system domain: audit/governance structure.

### E156 — The Widow's Petition
- Trigger: high trust or civic relief.
- Narrative role: compensation after military requisition of winter animals.
- Outputs: `requisition_compensation` or `requisition_tax_credit`.
- Character/system domain: civic relief and distributive legitimacy.

**Decision:** E73 and E156 are **not semantic duplicates**. They have different triggers, player problems, state outputs and downstream domains. Keep both stable authored IDs.

## E99 vs E173 — distinct nodes

### E99 — The Forgery's Shadow
- Trigger: `royal_forgery_proven` or `forgery_leverage`.
- Narrative role: document/seal evidence and coercion risk in the hidden-ledger investigation.
- Outputs: `seal_comparison_public` or `seal_pressure`.
- Character/system domain: evidence integrity.

### E173 — The Empty Barracks
- Trigger: low army readiness.
- Narrative role: security/infrastructure allocation after a historical budget diversion.
- Outputs: `barracks_rebuilt` or `barracks_shelter`.
- Character/system domain: military readiness versus civilian shelter.

**Decision:** E99 and E173 are **not semantic duplicates**. They have different triggers, narrative purposes, outputs and consumers. Keep both stable authored IDs.

## Gate impact

- E73/E156 duplicate concern: **CLOSED as non-duplicate at source level**.
- E99/E173 duplicate concern: **CLOSED as non-duplicate at source level**.
- No renumbering required for these pairs.
- Graph/catalog integration still must verify that their distinct outputs are represented correctly in the eventual production graph.
- Remaining high-priority semantic work: E55/E269 reframe, E36/E226 distinction, then graph verification of E37/E227, E39/E229 and E40/E241.

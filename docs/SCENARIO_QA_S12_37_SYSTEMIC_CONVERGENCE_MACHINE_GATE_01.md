# Choice Kingdom — S12.37 Systemic Convergence Machine Gate 01

Date: 2026-09-15  
Status: **SOURCE-LEVEL QA — MATRIX GREEN / CONVERGENCE CLOSURE OPEN**  
Frozen production scope: **E01–E272**

## Objective

Turn the frozen systemic-explanation evidence families into a machine-safe qualification gate without inventing the missing convergence producer.

## Required qualification

`pred.systemic_explanation_verified` requires all three independent evidence families plus an explicit convergence decision:

1. warehouse / financial;
2. document / language;
3. witness / organizational;
4. explicit convergence decision joining the three.

E207 is a consumer only and cannot manufacture any missing family or the convergence decision.

## Evidence-family matrix

| Family | Source-backed candidates | Current status | Anti-double-counting rule |
|---|---|---|---|
| Warehouse / financial | E232-A `intermediary_chain_traced`; E234-A/B payment-pattern branches | SOURCE-CANDIDATE SET CLOSED | Multiple payment/procurement facts remain one family |
| Document / language | E233-A `seal_forensics`; E235-A/B archive/old-record branches | SOURCE-CANDIDATE SET CLOSED FOR QA | E233 + E235 cannot count as two independent families |
| Witness / organizational | E236-A/B witness-ledger branch; E189-A `witness_reopened` | PARTIAL IDENTITY NORMALIZATION | Later witness history is not an automatic replacement for E236 |
| Convergence decision | No unique source-closed producer/key currently identified | **OPEN** | Downstream E207 cannot self-satisfy |

## Machine qualification boundary

A future runtime predicate may be admitted only if:

```text
family.warehouse_financial == true
AND family.document_language == true
AND family.witness_organizational == true
AND systemic_convergence_decision == true
```

The fourth term is intentionally unresolved. No event is promoted to it by chronology, naming, or proximity to E207.

## Hard negatives

- E207 cannot produce `pred.systemic_explanation_verified` merely by consuming evidence.
- E232/E234 cannot substitute for document/language evidence.
- E233/E235 cannot substitute for witness/organizational evidence.
- E236/E189 cannot be merged without explicit identity qualification.
- A raw evidence count cannot replace the explicit convergence decision.
- A later ending or prerequisite cannot retroactively manufacture convergence.

## Acceptance

PASS — three evidence families are represented as distinct machine domains.
PASS — candidate source identities are retained without semantic promotion.
PASS — anti-double-counting rules are explicit.
PASS — E207 remains consumer-only.
OPEN — exact immutable convergence producer/key.
OPEN — convergence ordering and invalidation lifecycle.
OPEN — fresh-run/replay reachability.

## Gate conclusion

**S12.37 = GREEN for the machine qualification boundary; the systemic convergence producer remains an explicit OPEN gate.**

This artifact does not increase implementation readiness by itself. A percentage increase requires authoritative source closure or a verified executable contract.

# Choice Kingdom — S12.37 Systemic Convergence Machine Gate 01

Date: 2026-09-16  
Status: **SOURCE-CLOSED / RUNTIME QUALIFICATION OPEN**  
Frozen production scope: **E01–E272**

## Objective

Keep the systemic-explanation qualification boundary synchronized with the authoritative authored source and machine canonical graph without promoting a consumer into a producer.

## Required qualification

`pred.systemic_explanation_verified` requires all three independent evidence families plus the explicit E270-A convergence decision:

1. warehouse / financial;
2. document / language;
3. witness / organizational;
4. E270-A convergence decision joining the three.

The authored source now explicitly identifies **E270-A** as the convergence producer. E270-A cannot manufacture a missing evidence family. The trigger `Amara and Toma both active` is not evidence.

## Evidence-family matrix

| Family | Source-backed candidates | Current status | Anti-double-counting rule |
|---|---|---|---|
| Warehouse / financial | E232-A `intermediary_chain_traced`; E234-A/B payment-pattern branches | SOURCE-CLOSED candidate set | Multiple payment/procurement facts remain one family |
| Document / language | E233-A `seal_forensics`; E235-A/B archive/old-record branches | SOURCE-CLOSED candidate set | E233 + E235 cannot count as two independent families |
| Witness / organizational | E236-A/B witness-ledger branch; E189-A `witness_reopened` | SOURCE-CLOSED source family boundary | Identity/qualification remains deterministic; no duplicate counting |
| Convergence decision | E270-A `systemic_explanation_convergence` | SOURCE-CLOSED | E270-A records convergence only after the three families exist |

## Machine qualification boundary

A runtime predicate may be admitted only if:

```text
family.warehouse_financial == true
AND family.document_language == true
AND family.witness_organizational == true
AND systemic_convergence_decision == true
```

E270-A is the explicit convergence producer for the fourth term. Runtime aggregation, invalidation, persistence and reachability remain separate gates.

## Hard negatives

- E207 cannot produce `pred.systemic_explanation_verified` merely by consuming evidence.
- E232/E234 cannot substitute for document/language evidence.
- E233/E235 cannot substitute for witness/organizational evidence.
- E236/E189 must not be merged without explicit identity qualification.
- A raw evidence count cannot replace the explicit E270-A convergence decision.
- A later ending or prerequisite cannot retroactively manufacture convergence.
- `Amara and Toma both active` is a trigger condition, not evidence.

## Acceptance

PASS — three evidence families are represented as distinct machine domains.  
PASS — E270-A is an explicit in-scope convergence producer in the authoritative source.  
PASS — anti-double-counting rules remain explicit.  
PASS — downstream consumers cannot self-satisfy the predicate.  
OPEN — executable evidence aggregation and invalidation lifecycle.  
OPEN — fresh-run/replay reachability.

## Gate conclusion

**Source contract is CLOSED at producer-identity level. Runtime qualification and reachability remain OPEN.**

This artifact does not claim Decision Engine implementation or gameplay readiness.

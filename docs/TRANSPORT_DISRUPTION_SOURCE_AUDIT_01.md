# Choice Kingdom — Transport Disruption Source Audit 01

Status: **SOURCE AUDIT — ACTIVE PRODUCER CLOSED; LIFECYCLE QA OPEN**.

## Finding

`pred.transport_disruption` is consumed by E192 and later crisis nodes. Re-reading the authoritative E01–E32 catalog established a safe upstream producer at E32.

- E05 — missing patrol supplies: military procurement/security problem; does not itself establish transport-network disruption.
- E16 — moved border marker: border escalation; does not itself establish transport disruption.
- E18 — river toll: commercial access pressure; does not itself establish transport disruption.
- E31 — Border Night: military escalation context; not by itself a transport producer.
- **E32 — Three Fires: explicit producer.** The compound crisis now explicitly states that winter roads and military movement have disrupted the transport network and establishes `pred.transport_disruption` for the current compound-crisis cycle with `history.transport_disruption_declared`.
- E136 — Frozen Road: explicit recovery/clear semantics (`transport_network_stable` / clear active disruption), therefore not a producer.
- E192 — Broken Cart: consumes `pred.transport_disruption`; it must not manufacture the predicate it consumes.
- E277 — Road Census: later recovery/partial-clear semantics; not an upstream producer for E192.

## Producer-before-consumer result

The first canonical active producer is now E32, which precedes the E192 consumer. The producer is authored at the crisis layer rather than inferred from gold/security/resource pressure. This closes the **source-producer gap**.

## Remaining lifecycle QA

The predicate is not yet production-closed. The next reconciliation must prove:

1. exact clear/expiry semantics for the E32 cycle;
2. whether E136/E277 can clear the same cycle or only later transport-disruption cycles;
3. history retention after clear;
4. save/load identity for the active cycle;
5. delayed consequence identity and exactly-once behavior involving E192;
6. replay isolation and contradiction checks.

## Gate

`pred.transport_disruption` is **SOURCE PRODUCER CLOSED**, but the derived-predicate production gate remains OPEN until lifecycle, reachability, delayed identity, persistence and contradiction checks pass.

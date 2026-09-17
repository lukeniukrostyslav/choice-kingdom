# Choice Kingdom — Production Data Schema Contract V1

Status: ACTIVE / BLOCK 1
Date: 2026-09-17

This is the machine-facing contract for the frozen authored production catalog. Authored Markdown remains the narrative source of truth; the runtime catalog is the deterministic parser/projection boundary.

## Frozen scope

- Production events: E01–E272 inclusive.
- Excluded expansion IDs: E273–E277.
- Event IDs are canonical and unique, except the explicitly documented E271 bridge duplicate rule.

## Event record

Every production event record must contain:

- `event_id`: canonical `E##`/`E###` identifier.
- `title`: non-empty authored title.
- `trigger`: authored trigger string; empty is allowed only for unconditional entry events.
- `source`: canonical authored source path.
- `choices`: ordered tuple of authored choices; special state/convergence nodes may intentionally have no player choices.
- `authored_prerequisites`: only prerequisites explicitly present in authored trigger text.

## Choice record

Every choice contains:

- `choice_id`: exactly `<event_id>-<label>`.
- `label`: uppercase A/B, with C allowed only for E51 and E108.
- `text`: non-empty authored choice text.
- `body`: complete authored choice block.
- `resource_deltas`: canonical resource keys only: gold, trust, security, power, reputation.
- `relationship_deltas`: canonical relationship keys only: mara, rowan, seris, ivo, amara, toma.
- `state_tokens`: authored state markers.
- `clear_tokens`: authored clearing markers.
- `immediate_unlocks`: only explicit immediate Unlock/Unlocks declarations.

## Semantic boundaries

- Unknown authored prose must not be invented as runtime semantics.
- Security level alone cannot create or clear the border crisis.
- Relationships cannot substitute for institutional evidence.
- Consumers cannot manufacture their prerequisites.
- Replay `meta.*` state is distinct from ordinary history/flags.
- Delayed lifecycle semantics remain owned by the canonical delay contract.

## Required validation

The production-data gate must verify scope, record shape, canonical vocabulary, choice identity, choice cardinality, prerequisite scope, immediate-unlock scope, and deterministic projection. A passing schema gate is source/data verification; it is not a claim that the complete gameplay campaign is runtime-reachable.

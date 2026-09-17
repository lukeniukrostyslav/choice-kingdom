# Choice Kingdom — P2 Canonical Character Binding Gate v1

Status: **OPEN — binding evidence not yet verified**

## Purpose

Prevent premium character artwork from being attached to an invented or guessed People/character identity. P2 may advance only when the visual anchor is bound to a character that is demonstrably present in the canonical project data.

## Verified repository inspection — 2026-09-17

The current `main` branch was inspected through the GitHub repository interface, including repository root, `docs/`, design-preview surfaces, recent commits, and repository code search.

Searches for the following returned no verified canonical character record:

- `People character canonical`
- `people`
- `character_id`

The repository currently contains premium character proof and review artifacts, but this inspection does **not** establish a canonical People ID/name for the Elira visual candidate.

## Binding contract

A P2 anchor may be marked **CANONICAL BOUND** only when all fields below are backed by an existing repository source:

| Field | Required evidence |
|---|---|
| `character_id` | Exact ID from canonical source |
| `display_name` | Exact name from canonical source |
| `source_path` | Repository path containing the canonical record |
| `source_ref` | Commit/ref used for verification |
| `faction_id` | Existing faction reference, when applicable |
| `tier` | Art-system tier justified by authored role |
| `anchor_art` | Visual artifact linked to the verified character |
| `provenance` | Authorship/license/source record for final artwork |

## Current state

- Visual anchor evidence: **PRESENT**
- Facial study evidence: **PRESENT**
- Costume/material study evidence: **PRESENT**
- Web-preview exposure: **PRESENT**
- Canonical People binding: **NOT VERIFIED**
- Final production artwork: **OPEN**
- Provenance/licensing: **OPEN**
- Vercel/mobile rendering validation: **DEFERRED** by project decision until the final phase

## Anti-fabrication rule

No assistant-generated character ID, character name, faction ID, or canonical mapping may be introduced solely to close this gate. If the source record is absent, the correct state is **NOT VERIFIED**, not an invented mapping.

## Next P2 execution gate

Continue repository-wide canonical-source discovery. Once an exact People record is found, bind the existing visual anchor to it and record the exact source path/ref. If no canonical People source exists in the repository, the project must first establish that canonical source before the visual anchor can be declared production-bound.

## Percentage rule

This gate is evidence infrastructure only. It does not increase P2 by itself. P2 remains **30%** until the defined visual-production and canonical-binding gates are actually satisfied.

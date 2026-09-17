# Choice Kingdom — P2 Authored Character Studies QA v1

Status: **P2 EVIDENCE PASS — PERCENTAGE UNCHANGED AT 30%**

## Scope

This gate verifies concrete P2 visual evidence after the production-anchor proof:
- authored facial-expression study board;
- costume/material study board;
- enriched premium portrait study;
- identity-anchor continuity;
- mobile-safe hierarchy;
- web-preview exposure.

This is a design-system evidence gate, not final production-art approval.

## Evidence

- `docs/visual/premium-character-facial-studies-elira-v1.svg`
- `docs/visual/premium-character-material-costume-study-elira-v1.svg`
- `web-preview/artwork/queen-elira.svg` — enriched premium portrait study
- `web-preview/artwork-preview.html` exposes the character review surface and authored studies.

## Checks

| Check | Result | Notes |
|---|---|---|
| Six authored expression states | PASS | neutral, concern, confidence, suspicion, grief, relief |
| Fixed facial geometry | PASS | head shape, eye spacing and hair mass remain stable |
| Expression variable isolation | PASS | brow/eye/mouth changes are controlled rather than redesigns |
| Costume silhouette continuity | PASS | royal shoulder/head relationship remains stable |
| Material grammar | PASS | woven cloth, aged metal, leather and restrained precious-metal accent are explicit |
| Enriched portrait hierarchy | PASS | face, silhouette, status cue and material highlights are separated into readable layers |
| Rejection rules | PASS | glossy universal surfaces / generic fantasy armor / neon faction coding excluded |
| Crop-safe composition | PASS | face and identity anchors remain central and uncluttered |
| Mobile hierarchy | PARTIAL | source artwork is portrait-safe; actual 360dp/412dp rendered validation remains open |
| Canonical People binding | OPEN | repository inspection does not expose a verified canonical People record for the candidate; no invented binding is allowed |
| Final authored production artwork | OPEN | current artifacts remain authored study/proof assets until canonical binding and provenance are established |
| Vercel rendered validation | OPEN | requires actual deployed render inspection |
| Provenance/licensing record | OPEN | final production asset provenance remains required |

## Gate decision

The authored-study evidence is accepted into the P2 evidence set. **P2 stays at 30%** because the roadmap requires canonical People binding and final rendered validation/provenance gates before the next percentage increase. The enriched portrait is concrete visual work, but it does not by itself satisfy those gates.

## Next P2 actions

1. Continue repository-wide discovery for a verified canonical People character.
2. Bind the visual anchor without inventing IDs or replacing canonical data.
3. Complete the remaining production-art and provenance gates.
4. Validate the final review surface on Vercel at the end-of-project visual validation phase.
5. Run 360dp / 412dp / large-text / RTL visual checks.

# Choice Kingdom — Authored Artwork Catalog V1

Updated 2026-09-17 after autonomous artwork production pass.

## Purpose

This catalog tracks authored vector artwork created specifically for the Choice Kingdom visual system. These SVGs are original project assets, not stock placeholders or external game UI packs.

## Assets

| Stable ID | File | Screen | Format | Crop / use |
|---|---|---|---|---|
| ART-EVENT-GRANARY-01 | `web-preview/artwork/event-empty-granary.svg` | Event | SVG | 16:9 hero; keep central granary silhouette and upper-right moon clear |
| ART-CHAR-ELIRA-01 | `web-preview/artwork/queen-elira.svg` | People | SVG | 1:1 portrait; face centered, crown retained at top |
| ART-CHAR-CAEL-01 | `web-preview/artwork/lord-cael.svg` | People | SVG | 1:1 portrait; face centered, shoulder silhouette retained |
| ART-FACTION-RIVER-01 | `web-preview/artwork/river-compact.svg` | Faction | SVG | Square mark; legible at small UI sizes and monochrome-safe geometry |
| ART-END-CHRONICLE-01 | `web-preview/artwork/ending-chronicle.svg` | Ending | SVG | Wide atmosphere; central crown remains focal point |

## Production status

- **Produced:** 5 authored vector assets.
- **Provenance:** project-authored SVG; no external image dependency.
- **Licensing:** no third-party asset license required for these authored vectors.
- **Responsive intent:** all compositions define a focal region suitable for responsive cropping.
- **Accessibility:** each SVG contains a title and description for assistive/semantic contexts.
- **Integration:** assets are committed to the repository and are ready for integration into `game-flow.html`.

## V2 gate

V2 **must not be raised solely because files exist**. The final-artwork block requires the authored assets to replace the relevant placeholder/atmospheric treatments in the executable main flow and then pass visual regression. Until that integration is verified, V2 remains 0%.

## Next artwork integration order

1. Event hero → `ART-EVENT-GRANARY-01`
2. Queen Elira + Lord Cael portraits → `ART-CHAR-*`
3. River Compact faction mark → `ART-FACTION-RIVER-01`
4. Ending atmosphere → `ART-END-CHRONICLE-01`
5. Re-run responsive and visual regression gates

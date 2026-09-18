# P24 — Android Devices / Safe Areas / Resolution Adaptation

Status: IN PROGRESS

P24 continues the approved “The Royal Advisor” visual language on Android window classes.

## Implemented
- Compact, medium and expanded layouts via BoxWithConstraints at 600dp and 840dp boundaries.
- WindowInsets.safeDrawing protects content from system bars and display cutouts.
- Expanded presentation uses a navigation rail; compact/medium uses vertical content with bottom navigation.
- Expanded content is capped at 720dp instead of a fixed width.
- Choice and navigation controls retain explicit minimum touch sizes.
- Compose text layouts remain wrapping-friendly.
- RTL remains enabled in the Android manifest.
- Android configuration includes arm64-v8a and x86_64.

## Target-class verification
The closure gate must execute the Android app on compact phone, medium/large tablet or foldable, and expanded-window classes. For each class it must verify no horizontal clipping, safe-area protection, adaptive navigation, reachable choices, long-string wrapping, RTL structure, and preservation of the V2 cinematic dark blue-black / restrained gold / serif visual language.

## Latest execution-gate state
The emulator workflow now runs Gradle from `androidApp` and applies bounded CI memory settings. The latest branch head is `bfba6e9aef18ae4881ff8d917944850e0a1b30a1`. No successful Android execution run has yet been verified for that head, so this remains evidence-gated at 40%.

## Evidence rule
Source contracts are implementation evidence only. P24 is not 100% until Android device or emulator-class execution evidence is recorded. Browser proof cannot substitute for Android execution evidence.

## Visual north star
All verification follows design-reference/FINAL_DESIGN_VISION_V1.md: cinematic medieval-fantasy atmosphere, deep blue-black/charcoal foundation, restrained warm gold, elegant serif hierarchy, refined layered panels and calm consequential interaction.
## Latest execution fix

The Android source-build gate failed on Bridge run #4 because the CI-only `p24CiAbi` override was scoped directly under `android { }`, where `ndk` and `abiFilters` are not available. The override has been moved into the existing `defaultConfig { ndk { ... } }` scope.

Fix commit: `0196b544cb14402f1b085e5b96e747625647c922`.

This correction must be validated by a fresh Android source build and then by the compact-phone, tablet-window and expanded-window emulator matrix. P24 remains open until those execution artifacts are green.


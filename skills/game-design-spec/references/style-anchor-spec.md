# Style Anchor Spec

Use this file when a project includes AI-generated UI, icons, concept art, scene art, or audio mood references.

## Goal

Lock a small set of non-negotiable style anchors before large-scale generation.

Without style anchors, AI asset quality usually fails through inconsistency rather than total ugliness.

## Required anchor fields

For each project, define these fields before batch generation:

| Field | What to lock |
|---|---|
| anchor_id | Stable project anchor name |
| visual promise | The feeling the player should get at first glance |
| primary palette | 3-5 main colors |
| accent and warning colors | Action, risk, success, failure colors |
| value contrast | How bright or dark the UI and scenes are relative to each other |
| line and edge language | Thin, medium, rounded, blocky, soft, sharp |
| shape language | Rounded, rectangular, modular, organic, rigid |
| perspective | Top-down, isometric, side view, flat UI, etc. |
| material feel | Matte, soft plastic, paper, ceramic, cloth, glass, etc. |
| icon metaphor style | Literal, abstract, outlined, filled, playful, restrained |
| motion tone | Calm, punchy, minimal, elastic, almost static |
| forbidden drift | Styles the project must not slide into |

## Recommended anchor count

- 1 anchor for very small prototypes
- up to 3 anchors for projects that need different but related families such as gameplay UI, reward UI, and scene art

Do not create more anchors than the project can realistically enforce.

## Anchor discipline

- Every UI page family must cite the anchor it follows.
- Every art asset family must cite the anchor it follows.
- If a new asset cannot fit an existing anchor, either revise the anchor or reject the asset request.
- Do not silently invent a new visual direction inside one project.

## Minimum output shape

When writing a style anchor block, include:

| Item | Content |
|---|---|
| anchor_id |  |
| used_by | UI pages or asset families |
| visual promise |  |
| palette |  |
| shape language |  |
| contrast rule |  |
| icon rule |  |
| motion rule |  |
| forbidden drift |  |

## Audio anchor extension

If the project includes music or sound design, also lock:

- rhythm density
- brightness or darkness of timbre
- softness versus sharpness
- whether audio should soothe, excite, or warn

This keeps BGM and SFX aligned with the same product promise as the visuals.

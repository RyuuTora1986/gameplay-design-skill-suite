# Asset Pipeline

Use this file when drafting chapter 4, chapter 8, chapter 9, chapter 10, and chapter 11 for projects that depend on AI-assisted UI or asset generation.

## Goal

Turn asset requests into a staged production pipeline instead of a one-shot prompt.

The default production order is:

1. structure draft
2. style anchor lock
3. batch generation
4. cleanup and export
5. integration and acceptance

Do not jump directly from vague design intent to final assets unless the user explicitly asks for throwaway exploration.

## Stage 1. Structure draft

Use low freedom outputs first:

- UI: wireframe, grid, component list, state list, interaction destinations
- Art: silhouette, camera angle, pose, layer list, tile or scene layout
- Audio: scene cue list, event trigger table, loop points, loudness roles

Exit condition:

- The asset can be judged for structure without depending on rendering quality.

## Stage 2. Style anchor lock

Before batch generation, lock a small set of anchor decisions:

- palette
- line weight
- shape language
- perspective
- material or surface feel
- UI density
- icon metaphor style
- lighting direction

At this stage, generate or define only 1-3 anchors, not the full asset pack.

Exit condition:

- A later generator can follow the anchors without reinterpreting the whole project.

## Stage 3. Batch generation

Only after the style anchor is locked:

- generate page variants
- generate icon sets
- generate cards, panels, or tiles
- generate scene components
- generate audio placeholder variants

Rules:

- Generate by family, not by mixed random requests.
- Reuse the same anchor terms and forbidden terms every time.
- Keep a stable naming rule across the whole batch.

## Stage 4. Cleanup and export

Every generated asset batch must be normalized for downstream tools:

- correct dimensions
- transparent background when required
- predictable layer names
- safe area preserved for UI text
- export format declared
- slice reuse declared if relevant

## Stage 5. Integration and acceptance

No asset is considered complete until it is checked in context:

- in target resolution
- next to related assets
- with gameplay-readable contrast
- with state changes if it is interactive
- with implementation naming and folder placement

## Failure conditions

Reject or redo the asset batch if any of these happen:

- style drift between assets in the same family
- UI readability collapse at target resolution
- icon meaning depends on text to be understood
- scene art blocks gameplay information
- generated asset cannot be exported in the required format
- asset naming cannot be mapped to implementation files

## Downstream requirement

When chapter 4 or chapter 8 is written, include:

- which pipeline stage the asset is currently in
- what the next stage is
- what acceptance gate must be passed before moving on

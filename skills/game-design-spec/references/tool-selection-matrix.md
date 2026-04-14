# Tool Selection Matrix

Use this file when an asset-producing chapter must choose a downstream tool path and the choice affects quality, consistency, or delivery risk.

## Goal

Force a concrete routing decision instead of vague wording like "use AI tools as needed".

## Required output shape

```markdown
## x.x 工具选择矩阵：{资产族}

| 项目 | 内容 |
|---|---|
| asset_family |  |
| target_stage |  |
| preferred_tool |  |
| fallback_tool |  |
| placeholder_backup |  |
| choice_reason |  |
| evidence_source |  |
| checked_date | YYYY-MM-DD |
| switch_condition |  |
| output_expectation |  |
```

## Decision criteria

Choose the preferred tool based on:

- match to asset family
- stage fitness
- export controllability
- integration path
- consistency with anchor
- stability of the workflow

Do not choose based only on general hype or a broad leaderboard.

## Asset-family guidance

### UI pages and components

Preferred when available:

- Figma-oriented generation and design-to-code workflows

Fallback:

- AI coding tools generating code-native UI from the page spec

Backup:

- wireframe + component registry + placeholder page pack

### Visual art

Preferred when available:

- editing-first or production-first image workflows with controllable export and cleanup

Fallback:

- general image generators constrained by anchor, family, and export rules

Backup:

- silhouette pack, color-block pack, icon labels, placeholder atlases

### Music

Preferred when available:

- music tools that fit short loop generation and scene mood exploration

Fallback:

- shorter cue generation instead of full final track generation

Backup:

- royalty-safe placeholder loops and timing specs

### Sound effects

Preferred when available:

- SFX-focused tools for short event sounds

Fallback:

- narrow prompt families by event type

Backup:

- placeholder UI beeps, water loops, and warning packs with strict naming

## Evidence policy

The `evidence_source` field should state one of:

- latest official product docs checked
- latest benchmark signal checked
- local connector availability checked
- no external verification available, conservative fallback used

The `checked_date` field should record when the tool decision was last reviewed.

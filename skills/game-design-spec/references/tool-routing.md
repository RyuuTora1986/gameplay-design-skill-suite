# Tool Routing For Asset Production

Use this file when the project needs AI-generated UI, art, music, or sound effects, and tool choice materially affects quality or stability.

## Routing principle

Do not hard-code one permanent winner.

If the user explicitly asks for the latest or if tool choice is a meaningful quality risk, first check:

- official product documentation and announcements
- current benchmark or arena methodology pages where relevant
- local connector availability in the current environment

Then choose:

1. preferred tool
2. fallback tool
3. placeholder-safe backup path

## Current practical routing guidance

This guidance reflects a conservative read of recent official product docs plus current benchmark signals where relevant. It should be treated as the default routing baseline, not an eternal ranking.

### UI assets

Preferred path:

- Use Figma-oriented workflows when the goal is interactive UI, screen systems, component consistency, or developer handoff.
- Favor Figma Make or Figma canvas workflows for first-pass UI generation and Dev Mode / Code Connect / MCP-style handoff for implementation alignment.

Why:

- Figma officially positions Make and Dev Mode for AI-assisted UI generation, interactive iteration, and design-to-code handoff.
- Figma Dev Mode and Code Connect reduce translation loss when the end goal is implementation.
- Figma MCP and Code Connect explicitly improve AI agent code generation quality by linking designs to real code components.

Fallback:

- If Figma generation is unavailable, use AI coding tools to generate code-native UI from the page spec, state matrix, and anchor rules.

Backup:

- If no UI generator is available, output wireframes, component registry, tokens, and placeholder pages first. Do not block the project on visuals.

### Visual art assets

Preferred path:

- Use Adobe Photoshop / Firefly workflows when the goal is iterative, production-minded image generation, editing, or asset cleanup.

Why:

- Adobe positions Firefly and Photoshop integration as commercially safer and tightly integrated into cleanup and production workflows.
- Firefly emphasizes Content Credentials, business safety, and iterative editing rather than one-shot image novelty.
- Adobe now positions Firefly as a hub that can use Adobe and third-party top models, which makes it a stronger production shell even when the underlying model varies.

Fallback:

- Use a high-quality general image generation path only after the style anchor, family scope, and export rules are locked.
- Current benchmark signals indicate OpenAI GPT Image 1.5 (high) is a strong fallback for image quality exploration when a production-first editing shell is unavailable.

Backup:

- If no image generator is available, create placeholder packs using blocks, silhouettes, icon labels, and export-safe dummy files so coding can continue.

### Music

Preferred path:

- Use Udio-style music workflows for exploration, extension, and mood ideation, especially when the project needs short loops or iterative variations.

Fallback:

- If music generation quality is unstable, reduce scope to short loopable cues and transition stings rather than full final tracks.
- If a unified audio stack is more important than maximum music quality, use the same audio vendor used for SFX and voice tooling to reduce operational complexity.

Backup:

- Use temporary royalty-safe placeholders or custom minimal loops defined by BPM, mood, and duration rules. Keep the asset status explicit.

### Sound effects

Preferred path:

- Use sound-effect-focused tools for short game events, UI beeps, ambience, and loops.

Why:

- Short effects are more controllable than full music, and modern SFX tools expose duration and loop settings that fit game pipelines better.
- ElevenLabs explicitly documents duration and looping controls for generated sound effects and positions the feature for games and interactive media.

Fallback:

- If generation quality is unstable, split requests into narrower families: UI, environment, reward, warning.

Backup:

- Use placeholder click, sweep, water, and alert packs with strict naming and duration rules so implementation and QA can still proceed.

## Required fallback contract

Every asset-producing chapter should define:

- preferred tool path
- fallback tool path
- placeholder-safe backup path
- what stage each fallback can realistically achieve

## Quality safety rule

Do not route to a tool only because it is impressive in a broad benchmark.

Choose based on:

- match to asset family
- integration path
- controllability
- export safety
- consistency with the current anchor and stage

## Evidence snapshot for current default choices

- Figma Dev Mode, Code Connect, and MCP: official Figma docs emphasize design-to-code handoff, real code linkage, and improved AI codegen quality.
- Adobe Firefly / Photoshop: official Adobe docs emphasize commercially safe generation, Content Credentials, production integration, and multi-model support inside the Firefly shell.
- OpenAI GPT Image 1.5 (high): current Artificial Analysis image benchmark snapshot shows it as a strong high-quality image fallback signal.
- ElevenLabs Sound Effects: official docs expose duration and looping controls and explicitly call out games and interactive media.
- Udio: official help docs emphasize iterative song creation, extension, remix, and audio upload, which fits music ideation better than one-shot finalization.

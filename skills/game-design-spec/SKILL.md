---
name: game-design-spec
description: |
  Use when a gameplay design package or other already-mature game planning input
  needs to be expanded into a full Chinese game design spec with registries,
  rules, formulas, downstream tasks, and implementation planning. If the idea is
  still fuzzy or upstream of direction lock, use $gameplay-design-orchestrator
  first. Do not use for non-game product specs or direct implementation.
---

# Game Design Spec

Use this skill to write game planning documents that another AI agent can execute without re-interpreting vague prose.

## Routing Boundaries

- Use this skill after a `Gameplay Design Package` exists, or when the user already provides mature game-planning materials that are effectively equivalent.
- If the input is still fuzzy inspiration, unresolved direction finding, or raw reality-mapping notes, route to `$gameplay-design-orchestrator` first.
- If the task is a non-game product or business workflow, route to `$product-design-orchestrator` or `$product-design-spec`.
- If the task has already moved into web-game implementation, testing, or code iteration, route to `$develop-web-game` after the relevant design/spec handoff is ready.
- If the task is focused on high-fidelity UI implementation after the design is locked, route to `$frontend-skill`.
- If the task is focused on bitmap asset generation after anchors are locked, route to `$imagegen` or the chosen external asset tool path.

## Core Stance

- Translate creative intent into rules, data, states, formulas, UI prompts, and delivery tasks.
- Think from player experience first, then implementation cost, then anti-abuse and operability.
- Prefer explicit assumptions over blocking questions when source material is incomplete.
- Preserve canonical IDs and naming once they exist.

## Required References

Read the relevant references before drafting:
- [references/output-contract.md](references/output-contract.md)
- [references/hard-rules.md](references/hard-rules.md)
- [references/templates.md](references/templates.md)
- [references/asset-pipeline.md](references/asset-pipeline.md)
- [references/style-anchor-spec.md](references/style-anchor-spec.md)
- [references/asset-qa-template.md](references/asset-qa-template.md)
- [references/generator-handoff-contract.md](references/generator-handoff-contract.md)
- [references/asset-registry-spec.md](references/asset-registry-spec.md)
- [references/asset-stage-rules.md](references/asset-stage-rules.md)
- [references/tool-routing.md](references/tool-routing.md)
- [references/tool-selection-matrix.md](references/tool-selection-matrix.md)

## Core Output Rules

- Write in plain Chinese.
- Do not skip requested chapters.
- Do not use examples as substitutes for missing content.
- If source input is incomplete, start with assumptions and then continue with the full output.
- Use Markdown headings, tables, and Mermaid where useful.
- Treat completeness and executability as hard constraints.

## Chapter Map

This skill writes a fixed 11-chapter delivery contract:
- Chapter 1: overview, loop summary, platform, audience, session length, save model, monetization, tech stack, minimum device target
- Chapter 2: system architecture overview and dependency map
- Chapter 3: per-system executable rules, state machines, edge cases, and anti-abuse logic
- Chapter 4: UI tasks and state matrices
- Chapter 5: level or content progression design
- Chapter 6: balance, economy, and formulas
- Chapter 7: config tables and tooling rules
- Chapter 8: art requirements and asset pipeline constraints
- Chapter 9: audio requirements and generation constraints
- Chapter 10: QA, playability, and acceptance coverage
- Chapter 11: delivery plan, risk handling, and implementation task mapping

## Input Contract

Prefer one of these inputs:
1. A `Gameplay Design Package` produced by the upstream gameplay-design skills.
2. Raw game-planning notes that are already mature enough to support full specification without an ideation pass.

If the raw notes are still fuzzy, conflicting, or obviously upstream of direction lock, stop and route to `$gameplay-design-orchestrator` instead of inventing the missing gameplay package implicitly.

Preserve canonical IDs and names exactly when they already exist:
- `SYS-*`
- `RES-*`
- `FML-*`
- `CFG-*`
- `VAR-*`

## Workflow

1. Normalize the input into stable fields: genre, platform, camera, controls, audience, session length, monetization, technical scope, content scale, and core fun.
2. Produce explicit assumptions instead of blocking on missing but necessary inputs.
3. Freeze canonical registries early and keep all later chapters consistent with them.
4. Draft each chapter as an executable spec, preferring tables and fixed structures over loose prose.
5. Convert design into downstream production tasks, including UI, config, art, audio, QA, and delivery outputs.
6. Run a hard self-check against the output contract, hard rules, and validators.

## Registry Discipline

Before writing downstream chapters, build or confirm these canonical registries:
- system registry
- resource registry
- formula registry
- config-table registry
- variable registry

Rules:
- Use one stable ID per canonical object.
- Do not create chapter-specific aliases.
- If a chapter mentions a concrete object, it must already exist in the corresponding registry.
- UI, balance, config, QA, and implementation sections must reference the same canonical IDs.

## Downstream Task Discipline

- Chapter 4 must become UI generation prompts and state matrices, not vague UI comments.
- Chapter 7 must become config schema and toolchain rules, not only table names.
- Chapters 8 and 9 must be directly usable for AI asset generation.
- Chapter 11 must be organized so a solo developer using AI coding tools can execute it.
- Asset-producing chapters must define stage, anchor, acceptance gate, and export contract.
- If tool choice matters, define preferred, fallback, and placeholder-safe backup paths.

## Validation

Always validate any file set that claims completeness:
- `python scripts/validate_spec.py <path>`
- `python scripts/validate_spec.py --task-dir <dir>`
- `python scripts/validate_asset_registry.py <markdown-file>` when asset registries are present

Also verify:
- every indexed system appears in chapter 3 and downstream tasks
- no downstream chapter introduces a new top-level system ID without updating registries
- resources, formulas, config tables, and variables stay consistent across files
- UI, art, and audio outputs include style anchors and acceptance checks, or explicitly justify why not

## Bundled Tools

- `python scripts/bootstrap_spec.py --game-name "<name>" --outdir "<dir>"`
- `python scripts/validate_spec.py "<markdown-file>"`
- `python scripts/validate_spec.py --task-dir "<dir>"`
- `python scripts/validate_asset_registry.py "<markdown-file>"`
- `python scripts/choose_tool_path.py --asset-family "<family>" --target-stage "<stage>"`

Use the bootstrap script when the user wants files created on disk.
Use the validator whenever a generated Markdown file claims to be complete.

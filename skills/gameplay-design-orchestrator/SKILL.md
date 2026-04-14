---
name: gameplay-design-orchestrator
description: |
  Use when a game idea is still upstream of full specification and needs the
  top-level gameplay-design pipeline: direction lock, ordered stage execution,
  and assembly into one Gameplay Design Package. This is the normal entry point
  for fresh game-design work. Do not use for non-game product design or direct
  implementation.
---

# Gameplay Design Orchestrator

Use this skill as the upstream control layer for gameplay design.

## Goal

Produce exactly one `Gameplay Design Package`, not a loose brainstorm.

The package must:
- contain a real repeatable-fun hypothesis
- respect target scale and production cuts
- be structured strongly enough for `$game-design-spec` and later implementation tools

Read these before drafting:
- [references/pipeline.md](references/pipeline.md)
- [references/output-schema.md](references/output-schema.md)
- [references/scale-rules.md](references/scale-rules.md)
- [references/anti-patterns.md](references/anti-patterns.md)
- [references/handoff-contract.md](references/handoff-contract.md)
- [references/selection-rules.md](references/selection-rules.md)
- [references/iteration-rules.md](references/iteration-rules.md)

## Routing Boundaries

- Use this skill for game design discovery, direction lock, and gameplay-package assembly.
- If the task is a non-game product, SaaS feature, workflow tool, or lightly gameified product surface, route to `$product-design-orchestrator` or `$product-design-spec`.
- If the task is already implementation or iteration on a playable web game, route to `$develop-web-game` after the design package or full spec is ready.
- If the task is high-fidelity game UI implementation after design is locked, route to `$frontend-skill`.
- If the task is bitmap asset generation after style anchors and asset contracts are locked, route to `$imagegen` or the chosen external asset tool path.
- Do not treat the downstream `gameplay-*` stage skills as normal free-entry skills for fresh work. They are controlled internal stages under this orchestrator.

## Pipeline

Run the work in this order:

1. Use `$gameplay-input-normalizer` to convert raw input into stable design constraints.
2. Generate 2-3 candidate directions and choose exactly one strongest direction inside this skill.
3. Use `$gameplay-fantasy-loop-designer` to lock player promise and loop structure.
4. Use `$gameplay-pacing-and-structure` to lock time-layer pacing and replay pull.
5. Use `$gameplay-world-and-narrative-weaver` to wrap identity, conflict, and progression around the proven loop.
6. Use `$gameplay-system-weaver-and-scope-cutter` to define the system network, resource flow, MVP keep list, and cut list.
7. Use `$gameplay-coding-handoff-compiler` to compile the package into coding-ready structures.
8. Merge all outputs into one `Gameplay Design Package` and validate it.

The current repo contains six downstream gameplay stage skills after this orchestrator.
Once the formal pipeline starts, all six downstream stages are mandatory.
Do not skip, parallelize, or cherry-pick them as the normal path.

The order is a dependency order, not a ban on iteration.
If a later stage exposes a real upstream flaw, loop back explicitly, log the reason, revise the upstream stage, then continue forward again.
Do not silently patch over upstream flaws by adding compensating complexity downstream.

## Hard Rules

- Start from player promise, not systems.
- Start from identity, conflict, and repeatable action, not theme skin.
- Lock target scale before expanding mechanics.
- Do not let any downstream gameplay stage start before this skill locks direction, target scale, and upstream constraints.
- After this skill enters the formal stage chain, it must drive all six downstream gameplay stage skills in order.
- Only allow isolated stage-specific revision when a package already exists from this orchestrator and the user explicitly asks to revisit one exact stage.
- Every secondary system must serve the core loop or be cut.
- Every narrative beat must change pressure, target, or reward expectation.
- Always include first-version cut boundaries.
- Always finish with coding-ready structure, not only design prose.
- Keep discarded directions in review notes, not in the main package.
- Record major loop-backs in review notes with triggering stage, failure signal, change made, and reason the new choice is stronger.

## Output Contract

Output exactly one `Gameplay Design Package` using the schema in `references/output-schema.md`.
That package is the only approved upstream input for `$game-design-spec`.

Preserve canonical IDs once created:
- `SYS-*`
- `RES-*`
- `FML-*`
- `CFG-*`
- `VAR-*`

Do not rename them downstream.

## Bundled Tools

- `python scripts/bootstrap_gameplay_package.py --game-name "<name>" --outdir "<dir>"`
- `python scripts/validate_gameplay_package.py "<markdown-file>"`
- `python scripts/validate_gameplay_package.py --package-dir "<dir>"`

Validate before handing the package to `$game-design-spec`.

## Handoff

When the package is complete, hand it to `$game-design-spec` as the primary source of truth.
Use the fixed downstream mapping defined in `references/handoff-contract.md`.

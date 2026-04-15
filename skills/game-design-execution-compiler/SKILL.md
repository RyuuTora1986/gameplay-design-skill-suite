---
name: game-design-execution-compiler
description: |
  Use when a mature game-design-spec or equivalent gameplay package needs to be
  compiled into an agent-executable task graph. Outputs one execution-plan.json
  plus one human-reviewable execution-plan.md. Do not use for upstream gameplay
  ideation or direct code implementation.
---

# Game Design Execution Compiler

Use this skill to convert mature game-planning artifacts into a compact execution plan that autonomous coding agents can consume without re-deriving task order, scope, or acceptance logic.

## Routing Boundaries

- Use this skill after a `game-design-spec` exists. This is the normal path.
- Allow a mature `Gameplay Design Package` only when it already contains enough coding-ready detail and canonical IDs to derive implementation work without guessing.
- If the input is still upstream gameplay ideation, unresolved direction lock, or incomplete package assembly, route back to `$gameplay-design-orchestrator`.
- If the input is still in structured specification drafting, route to `$game-design-spec` first.
- Do not use this skill to write implementation code directly.

## Core Output

Produce exactly two files:

1. `execution-plan.json`
2. `execution-plan.md`

The JSON file is the machine-facing source of truth.
The Markdown file is the human review surface for checking task sizing, dependency order, and execution boundaries.

## Required References

Read these before compiling:
- [references/output-schema.md](references/output-schema.md)
- [references/hard-rules.md](references/hard-rules.md)

## Core Stance

- Respect the locked design. Do not rewrite gameplay direction, system boundaries, or canonical IDs.
- Compile implementation work into small, dependency-aware tasks.
- Prefer explicit dependency edges over vague priority labels.
- Every task must be verifiable.
- Every task must stay small enough for one focused agent iteration.

## Input Contract

Preferred input:
1. A mature `game-design-spec`.
2. A `Gameplay Design Package` that already contains coding-ready structure and stable canonical IDs.

Preserve canonical IDs exactly when they already exist:
- `SYS-*`
- `RES-*`
- `FML-*`
- `CFG-*`
- `VAR-*`

## Workflow

1. Determine the true execution source of truth, preferring the spec over upstream package notes.
2. Extract the implementation-relevant systems, UI work, logic work, config work, QA work, asset work, and delivery work.
3. Split the work into tasks that each have one clear primary deliverable.
4. Add explicit dependency order using `depends_on`.
5. Attach each task back to `source_refs` and `canonical_ids`.
6. Write strict acceptance criteria and verification steps.
7. Emit both `execution-plan.json` and `execution-plan.md`.
8. Validate the output before claiming completeness.

## Task Rules

- A task must fit one focused agent iteration.
- A task must have one clear main goal.
- A task must not silently redesign upstream decisions.
- UI tasks must include browser verification.
- Logic tasks must include typecheck, and tests when meaningful.
- If a task touches a concrete system, resource, formula, config table, or variable, include the canonical IDs.
- If a task depends on another task's output, list the dependency explicitly.

## Bundled Tools

- `python scripts/bootstrap_execution_plan.py --game-name "<name>" --outdir "<dir>"`
- `python scripts/validate_execution_plan.py --plan-dir "<dir>"`
- `python scripts/validate_execution_plan.py "<json-file>" --markdown "<markdown-file>"`

Use the bootstrap script to create starter files on disk.
Use the validator whenever a plan claims to be complete.

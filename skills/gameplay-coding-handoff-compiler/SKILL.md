---
name: gameplay-coding-handoff-compiler
description: |
  Use when $gameplay-design-orchestrator has already completed the upstream
  gameplay stages and this final handoff stage is next, or when revising only
  the coding-handoff layer of an already locked gameplay package. Do not use
  this as an alternative to the upstream gameplay design pipeline.
---

# Gameplay Coding Handoff Compiler

## Execution Boundary

- This is an internal stage skill under `$gameplay-design-orchestrator`.
- Start only after system scope and cut boundaries are already locked.
- Do not invent new top-level systems here to compensate for missing upstream work.
- This stage compiles the package for downstream consumption; it does not replace `$game-design-spec` and it does not perform implementation itself.

## Output

Produce:
- scene list
- UI list
- object list
- state machines
- key variables
- interaction events
- placeholder art/audio strategy
- prototype acceptance

## Quality Heuristics

- `scene list` should map to prototype flow, not engine habits.
- `UI list` should cover decision-critical and feedback surfaces first.
- `object list` should name objects that own state or interaction logic.
- `state machines` should be used where failure, recovery, cooldown, or progress state matters.
- `key variables` should be the minimum set needed to express rules, tuning, and QA.
- `prototype acceptance` should be observable in one playtest session.

## Reject

Reject outputs like:
- object lists that mirror chapter headings instead of runtime entities
- acceptance criteria that require full content production to verify
- placeholder strategy that ignores which assets are structurally required versus merely aesthetic

## Self-check

- Can an AI coding tool infer runtime entities, states, and acceptance gates without redesigning the game?
- Are placeholders scoped tightly enough that prototype work can start before final assets exist?
- Does each listed object or UI surface map back to a retained system or loop beat?

This output must be directly consumable by `$game-design-spec` and AI coding tools.

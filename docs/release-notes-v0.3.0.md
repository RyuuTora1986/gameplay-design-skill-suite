# Release Notes: v0.3.0

## Release Title

`v0.3.0 - Execution Runner Prototype For Gameplay Design Suite`

## Summary

This release extends the suite one step beyond execution-plan compilation by adding the first runner prototype.

The chain now covers:

- gameplay-package assembly
- full Chinese spec expansion
- execution-plan compilation
- task-by-task execution coordination

## Highlights

- added `game-design-execution-runner`
- added a minimal `run_execution_plan.py` runtime for `init / status / next / handoff / dispatch / start / complete / block / fail`
- added explicit `ack` so runner dispatch can track worker pickup before completion
- added persisted `execution-run-state.json` flow for resumable execution
- added file-based dispatch packets for bounded worker handoff
- added dispatch-bound review gate checks on completion evidence
- added `worker_adapter.py` for external worker pickup / complete / fail / block flows
- updated public docs to present the suite as a design-to-execution operating chain

## Why This Matters

`execution-plan.json` is valuable as an intermediate representation, but the chain still stalled without a runtime that could actually step through tasks.

The runner prototype makes the first usable bridge between planning artifacts and bounded worker execution.

## Suggested GitHub Release Body

Gameplay Design Skill Suite now includes an execution runner prototype. After generating a gameplay package, expanding it into a Chinese spec, and compiling an execution plan, you can now initialize runner state, fetch the next runnable task, and coordinate one bounded worker handoff at a time.

## Suggested Short Social Copy

Released: `v0.3.0` adds an execution runner prototype to the gameplay design suite for Codex. The chain now goes from raw game idea to gameplay package, spec, execution plan, and task-by-task execution coordination.

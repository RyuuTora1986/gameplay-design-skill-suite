---
name: game-design-execution-runner
description: |
  Use when an execution-plan.json already exists and the next step is to drive
  task-by-task implementation in a controlled order. This skill coordinates one
  runnable task at a time, persists run state, and prepares bounded prompts for
  workers. Do not use it to redesign the plan or to generate the plan itself.
---

# Game Design Execution Runner

Use this skill after `game-design-execution-compiler` has already produced a valid execution plan.

This skill is the runtime coordinator for the plan, not the planner.

## Routing Boundaries

- Use this skill only when `execution-plan.json` already exists.
- If the design is still being specified, route back to `$game-design-spec`.
- If the execution plan does not exist yet, route to `$game-design-execution-compiler`.
- Do not rewrite the task graph here.

## Goal

Drive one bounded execution task at a time from `execution-plan.json`, persist progress in `execution-run-state.json`, and prepare either inline worker prompts or runner-managed dispatch packets without expanding scope.

## Required References

Read these before running:
- [references/state-model.md](references/state-model.md)
- [references/worker-prompt-contract.md](references/worker-prompt-contract.md)
- [references/review-gate.md](references/review-gate.md)

## Operating Model

- Load the plan.
- Load or initialize the run state.
- Pick the next runnable task whose dependencies are completed.
- Present only the bounded task payload to the worker.
- When needed, emit a dispatch package that can be handed to a worker or a later automation layer.
- Record the task as `dispatched`, then require an explicit `ack` before work is treated as running.
- Require verification evidence before marking the task complete.
- Persist state after every transition.

## Hard Rules

- Never mark a task complete without recorded verification evidence.
- Never skip dependency checks.
- Never merge multiple future tasks into one worker ask.
- Never redesign upstream gameplay or spec decisions during execution.
- Stop on blocked or failed tasks until the coordinator resolves them.

## Bundled Tools

- `python scripts/run_execution_plan.py init --plan-dir "<dir>" --repo-root "<repo>" --branch "<branch>"`
- `python scripts/run_execution_plan.py status --plan-dir "<dir>"`
- `python scripts/run_execution_plan.py next --plan-dir "<dir>" --format markdown`
- `python scripts/run_execution_plan.py handoff --plan-dir "<dir>" --task-id "TASK-001" --format markdown`
- `python scripts/run_execution_plan.py dispatch --plan-dir "<dir>" --task-id "TASK-001" --output-dir "<dir>\\dispatch-TASK-001"`
- `python scripts/run_execution_plan.py ack --plan-dir "<dir>" --task-id "TASK-001" --worker-label "<worker-name>"`
- `python scripts/run_execution_plan.py start --plan-dir "<dir>" --task-id "TASK-001"`
- `python scripts/run_execution_plan.py complete --plan-dir "<dir>" --task-id "TASK-001" --evidence-file "<json-file>"`
- `python scripts/run_execution_plan.py block --plan-dir "<dir>" --task-id "TASK-001" --reason "<reason>"`
- `python scripts/worker_adapter.py pickup --dispatch-dir "<dir>\\dispatch-TASK-001" --worker-label "<worker-name>"`
- `python scripts/worker_adapter.py complete --dispatch-dir "<dir>\\dispatch-TASK-001" --evidence-file "<json-file>"`

Use this skill as the control layer between the execution plan and actual coding workers.

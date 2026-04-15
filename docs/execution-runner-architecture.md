# Execution Runner Architecture

## Goal

Define the next layer after `game-design-execution-compiler`: a worker-facing execution runner that consumes `execution-plan.json` and drives implementation work in a controlled, reviewable order.

This document now describes the architecture behind the initial runner prototype in `skills/game-design-execution-runner/`, while still acting as the higher-level design reference.

## Why This Layer Exists

The current suite now reaches three strong artifacts:

1. `Gameplay Design Package`
2. `Full Chinese Game Design Spec`
3. `execution-plan.json` + `execution-plan.md`

What still does not exist is the runtime that turns the execution plan into actual coding work.

Without that layer, `execution-plan.json` is a strong intermediate representation, but not yet an operating system for agent execution.

## Proposed Topology

```text
Raw game idea
  -> gameplay-design-orchestrator
  -> Gameplay Design Package
  -> game-design-spec
  -> Full Chinese Game Design Spec
  -> game-design-execution-compiler
  -> execution-plan.json + execution-plan.md
  -> execution runner
  -> coding workers / QA workers
  -> implemented prototype or feature slice
```

## Runner Responsibilities

The runner should do exactly these things:

1. Load `execution-plan.json`
2. Select the next runnable task whose dependencies are satisfied
3. Build a bounded task prompt for a coding worker
4. Require the worker to report structured verification evidence
5. Mark the task as complete, failed, or blocked
6. Persist run state so the chain can resume after interruption
7. Optionally emit a stable dispatch package for file-based worker handoff
8. Require explicit acknowledgement before a dispatched task becomes running work

The runner should not:

- rewrite design decisions
- merge multiple independent tasks into one giant instruction
- silently skip verification
- invent new dependencies without recording them

## Recommended Execution Modes

### Mode A: Inline Codex session

- One main Codex session reads the plan
- It executes tasks one by one in the same thread
- Best for solo use and tight supervision

Strengths:

- simplest implementation
- easiest to debug
- lowest orchestration overhead

Weaknesses:

- weaker isolation between tasks
- more context accumulation
- higher chance of drift in long runs

### Mode B: Subagent-driven execution

- Main session acts as coordinator
- Each task is handed to a fresh worker/subagent
- Main session reviews after every task

Strengths:

- better task isolation
- cleaner dependency enforcement
- closer to how `execution-plan.json` was designed

Weaknesses:

- requires stronger coordination logic
- more overhead per task
- needs consistent review discipline

### Mode C: External runner

- A separate script or service reads the plan
- It launches agents through a CLI or API interface
- Status is written back to a state file

Strengths:

- best long-term automation path
- easiest to pause/resume
- can support queueing and dashboards later

Weaknesses:

- highest implementation cost
- requires stable integration points
- more moving parts to maintain

## Recommended Path

Start with Mode B: subagent-driven execution.

Reason:

- it matches the task sizing model used by `execution-plan.json`
- it preserves strong review points
- it is materially easier than building a full external orchestrator
- it keeps the first version inside the normal Codex workflow

## Runner Input Contract

Minimum runner input:

- `execution-plan.json`
- repository root path
- target branch name
- optional execution policy overrides

## Runner State Model

The runner should keep a sidecar state file, for example:

`execution-run-state.json`

Recommended fields:

- plan version
- repository path
- branch
- task status map
- attempt counts
- blocked reasons
- verification evidence summary
- last completed task

## Worker Prompt Contract

For each task, the runner should pass workers only the bounded information they need:

- task id
- title
- type
- dependencies already completed
- source refs
- canonical IDs
- goal
- deliverables
- acceptance criteria
- verification commands
- notes

The runner should also instruct the worker:

- do not redesign upstream decisions
- do not absorb future tasks
- report exactly what was changed
- report verification evidence before claiming completion

## Dispatch Boundary

The runner now needs two output shapes:

### 1. `handoff`

- inline worker-facing markdown or JSON
- useful inside one supervised Codex thread
- no filesystem bundle required

### 2. `dispatch`

- file-based worker packet written to a dispatch directory
- intended for subagent handoff, runner-managed execution, or later external automation
- keeps the execution-plan contract stable while making downstream execution more operational

Recommended dispatch artifacts:

- `dispatch-manifest.json`
- `task-payload.json`
- `worker-handoff.md`
- `completion-evidence.template.json`

This is intentionally not a fake native agent launcher. It is the honest boundary that makes real automation possible later.

## Runner-Managed Dispatch Lifecycle

The runner now owns a minimal lifecycle instead of stopping at file export:

1. `dispatch`
2. `ack`
3. `complete` / `fail` / `block`

Meaning:

- `dispatch` means the packet exists and has been issued
- `ack` means a named worker has actually taken responsibility for execution
- `complete` means the acknowledged worker returned structured evidence and passed the review gate

This matters because it separates:

- packet generation
- execution ownership
- completion evidence

Without that split, the runner cannot honestly claim that dispatched work has actually started.

## Dispatch Review Gate

Completion evidence must be tied to the active acknowledged dispatch, not just the task ID.

Minimum checks:

- evidence contains `dispatch_id`
- evidence contains `worker_label`
- `dispatch_id` matches the active dispatch in runner state
- `worker_label` matches the worker that acknowledged the dispatch

This closes the easy failure mode where stale evidence or the wrong worker result is attached to the current task.

## Worker Adapter

The adapter is the external-facing layer above the runner lifecycle:

- it reads `dispatch-manifest.json`
- it converts dispatch-directory actions into runner state transitions
- it hides raw `plan-dir` and `task-id` plumbing from external workers

This is the first real interface boundary for future subagents, scripts, or external services.

## Review Gate

Every completed task should pass a coordinator review gate:

1. Did the worker stay within task scope?
2. Did the worker satisfy acceptance criteria?
3. Did the worker run the required verification?
4. Did the worker introduce drift against canonical IDs or source refs?

If not, the task returns to `failed` or `blocked`, not `completed`.

The current prototype now enforces this through structured evidence on `complete`, rather than a plain free-text summary.

## Future Skill Candidates

With the first runner prototype now added, the next likely additions are:

- `game-design-execution-runner`
  - consumes plan
  - dispatches workers
  - tracks status

- `game-design-task-reviewer`
  - reviews one completed task against plan and source refs

- `game-design-resume-coordinator`
  - restores execution after interruption from saved run state

## Suggested First Implementation Scope

The smallest useful version should support:

- loading one execution plan
- selecting the next task by dependency order
- dispatching one worker at a time through a stable packet
- recording completion state
- stopping on first failure

Do not start with:

- parallel dispatch
- auto-replanning
- automatic dependency rewriting
- dashboard UI
- multi-project queueing

## Practical Recommendation

Treat `execution-plan.json` as the stable contract.

Everything after this point should be replaceable:

- inline coordinator
- subagent coordinator
- external runner
- dashboard layer

As long as they all consume the same plan contract, the suite can evolve without reworking the upstream design pipeline again.

# Worker Prompt Contract

Each worker handoff should include only:

- task id
- title
- type
- completed dependencies
- source refs
- canonical IDs
- goal
- deliverables
- acceptance criteria
- verification requirements
- notes

The worker should also be told:

- do not redesign upstream decisions
- do not absorb future tasks
- report changed files explicitly
- report verification evidence before claiming completion

## Dispatch Package

When the coordinator needs a file-based handoff instead of an inline prompt, the runner should emit a dispatch package containing:

- `dispatch-manifest.json`
- `task-payload.json`
- `worker-handoff.md`
- `completion-evidence.template.json`

This package is the stable boundary between the execution plan and real worker execution.

## Worker Lifecycle

The worker lifecycle is:

1. coordinator runs `dispatch`
2. worker or supervisor runs `ack`
3. worker finishes with `complete`, `fail`, or `block`

The worker must not complete directly from a dispatched-but-unacknowledged state.

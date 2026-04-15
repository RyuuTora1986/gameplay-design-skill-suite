# State Model

The execution runner persists progress in `execution-run-state.json`.

## Required Root Fields

- `version`
- `plan_file`
- `repo_root`
- `branch`
- `last_completed_task`
- `tasks`

## Per-Task Fields

Each task entry must include:

- `status`
- `attempt_count`
- `last_summary`
- `verification_evidence`
- `blocked_reason`

## Allowed Status Values

- `pending`
- `running`
- `completed`
- `blocked`
- `failed`

## Persistence Rule

The runner must write state after every transition so the chain can resume after interruption.

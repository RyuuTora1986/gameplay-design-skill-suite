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
- `last_dispatch_dir`
- `dispatch_id`
- `dispatch_status`
- `dispatched_at`
- `acknowledged_at`
- `worker_label`
- `handoff_mode`

## Allowed Status Values

- `pending`
- `dispatched`
- `running`
- `completed`
- `blocked`
- `failed`

## Persistence Rule

The runner must write state after every transition so the chain can resume after interruption.

## Evidence Shape

`verification_evidence` should be an array of structured evidence objects rather than plain strings.

Each evidence object should contain:

- `summary`
- `changed_files`
- `verification_run`
- `acceptance_checklist`
- `open_issues`

## Dispatch Tracking

`last_dispatch_dir` should record the latest dispatch artifact directory generated for the task.

`dispatch_status` should record the worker-lifecycle state of the active dispatch. Recommended values:

- `not_dispatched`
- `dispatched`
- `acknowledged`
- `completed`
- `blocked`
- `failed`

This makes the runner resumable across:

- interrupted worker handoff
- manual supervisor review
- later external dispatch automation

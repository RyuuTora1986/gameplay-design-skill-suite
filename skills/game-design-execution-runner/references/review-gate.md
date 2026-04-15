# Review Gate

The runner must not accept a task as `completed` from a plain free-text summary alone.

Completion requires one structured evidence object with these fields:

- `summary`
- `changed_files`
- `verification_run`
- `acceptance_checklist`
- `open_issues`

## Field Rules

### `summary`

- One short statement of what was completed.

### `changed_files`

- Array of touched file paths.
- Must not be empty.

### `verification_run`

- Array of verification results.
- Each item should include:
  - `name`
  - `result`
- Use `pass`, `fail`, or `not_run` for result.

### `acceptance_checklist`

- Array of acceptance checks.
- Each item should include:
  - `criterion`
  - `status`
- Use `met`, `partial`, or `not_met` for status.

### `open_issues`

- Array of remaining gaps.
- Use an empty array when nothing remains.

## Gate Rule

Reject completion if:

- any required field is missing
- `changed_files` is empty
- all verification entries are `not_run`
- any acceptance checklist entry is `not_met`

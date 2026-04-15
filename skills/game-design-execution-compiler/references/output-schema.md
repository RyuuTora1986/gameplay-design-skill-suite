# Output Schema

`game-design-execution-compiler` must output exactly two files:

1. `execution-plan.json`
2. `execution-plan.md`

## JSON Root Shape

```json
{
  "version": "0.1",
  "project": {
    "name": "gyro-battle",
    "source_type": "game-design-spec",
    "source_files": [
      "examples/gyro-battle/final-spec/01-master-spec.md"
    ],
    "execution_mode": "single-agent-iterative"
  },
  "tasks": []
}
```

## Required Project Fields

- `name`
- `source_type`
- `source_files`
- `execution_mode`

## Required Task Fields

Every task must include:

- `id`
- `title`
- `type`
- `depends_on`
- `source_refs`
- `canonical_ids`
- `goal`
- `deliverables`
- `acceptance_criteria`
- `verification`
- `notes`

## Allowed Task Types

- `ui`
- `logic`
- `config`
- `qa`
- `asset`
- `integration`
- `delivery`

## Markdown Output Shape

The companion `execution-plan.md` must contain:

- `# Execution Plan`
- `## Project`
- `## Execution Strategy`
- `## Task List`

Each task section must contain:

- `### TASK-XXX <title>`
- `- Type:`
- `- Depends on:`
- `- Source refs:`
- `- Canonical IDs:`
- `- Goal:`
- `- Deliverables:`
- `- Acceptance criteria:`
- `- Verification:`
- `- Notes:`

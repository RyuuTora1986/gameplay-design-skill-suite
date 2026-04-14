---
name: gameplay-fantasy-loop-designer
description: |
  Use when $gameplay-design-orchestrator has already completed the
  normalization stage and this exact loop-design stage is next, or when revising
  the loop layer of an already locked gameplay package. Do not use this as a
  free-entry ideation skill.
---

# Gameplay Fantasy Loop Designer

## Execution Boundary

- This is an internal stage skill under `$gameplay-design-orchestrator`.
- Start only after normalized constraints already exist.
- Do not skip the normalization stage.
- When revising this stage, do not expand into worldbuilding, scope planning, or implementation unless the orchestrator explicitly loops the pipeline.

## Output

Produce:
- player promise
- identity fantasy
- core action
- micro loop
- mid loop
- long loop
- fun-source judgment

## Quality Heuristics

- `player promise` should state who the player becomes, what the player repeatedly achieves, and why that feels worth returning to.
- `identity fantasy` must be playable, not only thematic.
- `core action` should be the smallest satisfying repeatable verb set.
- `micro loop` must produce feedback in seconds, `mid loop` must create short-horizon planning, and `long loop` must justify return across sessions.
- `fun-source judgment` should name one dominant source of fun in plain terms.

## Reject

Reject outputs like:
- a promise that is really just genre labeling
- an identity fantasy that never changes player decisions
- loops that are only `do task -> get currency -> buy upgrade` with no distinctive moment-to-moment pleasure

## Self-check

- Is there a clear strongest repeatable action?
- Does the promise still make sense if you strip away theme skin?
- Can the long loop exist without exploding MVP scope?

Do not expand into worldbuilding or implementation here.
Hand the result to `$gameplay-pacing-and-structure`.

# Iteration Rules

Use this file when a downstream stage reveals that an upstream decision is wrong or unstable.

## Core principle

Keep stage order for dependency clarity, but allow explicit loop-backs for design correction.

Do not keep marching forward with a broken upstream assumption just to preserve linear flow.

## Allowed loop-backs

- `pacing -> fantasy loop`
  Use when the first 2 minutes are flat, the replay beat is weak, or time layers collapse into one dull reward shape.
- `world/narrative -> fantasy loop`
  Use when identity or conflict cannot be expressed through repeated play.
- `system weaving -> fantasy loop`
  Use when the current promise requires too many systems for the target scale.
- `system weaving -> pacing`
  Use when the retained system set changes beat timing, fatigue risk, or replay structure.
- `coding handoff -> system weaving`
  Use when runtime objects, UI surfaces, or state machines explode beyond prototype scope.

## Review gates

At the end of each stage, ask:

- Is the current output still faithful to the player promise?
- Is the current output still viable for the target scale?
- Did this stage expose a missing assumption that actually belongs upstream?

If the answer to the third question is yes, loop back one stage or more and revise explicitly.

## Documentation rule

When a loop-back happens, record it in `02-review-notes.md` with:

- triggering stage
- what failed
- what upstream decision changed
- why the new decision is stronger
- downstream implications

Only the final locked direction belongs in the formal package.

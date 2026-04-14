---
name: gameplay-input-normalizer
description: |
  Use when $gameplay-design-orchestrator has already taken ownership of a game
  package and this is the required first downstream stage, or when revising only
  the normalization layer of an already locked gameplay package. Do not use this
  as the normal entry point for fresh game ideation.
---

# Gameplay Input Normalizer

## Execution Boundary

- This is an internal stage skill under `$gameplay-design-orchestrator`.
- Use it only after the orchestrator has framed the problem and direction shortlist.
- Do not bypass the orchestrator for fresh work.
- When revising this stage on an existing package, preserve downstream contracts unless the orchestrator explicitly reopens them.

## Output

Output constraint fields, not mechanics:
- target player
- platform and control constraints
- scale tier
- must-have
- must-avoid
- core emotion
- reality mapping type
- trend translation direction
- budget and content pressure

## Quality Heuristics

- `target player` must describe a concrete player situation, not a market cliche.
- `must-have` should contain only constraints that materially shape the loop, fantasy, or production boundary.
- `must-avoid` should block likely failure modes, not generic dislikes.
- `core emotion` should name the dominant felt outcome after one session.
- `trend translation direction` must translate a trend into player action or structure.
- `budget and content pressure` should expose the production bottleneck clearly.

## Reject

Reject outputs like:
- "target player: everyone who likes fun games"
- "must-have: interesting mechanics"
- "trend translation: use the hot topic as skin"

## Self-check

- Can a downstream designer infer scope, controls, audience pressure, and emotional target without guessing?
- Did you avoid smuggling mechanics into the normalization stage?
- Would two different designers likely converge on a similar direction shortlist from this output?

Do not design systems here.
Hand the normalized result to `$gameplay-fantasy-loop-designer`.

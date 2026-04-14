---
name: gameplay-pacing-and-structure
description: |
  Use when $gameplay-design-orchestrator has already locked the loop stage and
  this pacing stage is next, or when revising pacing on an already locked
  gameplay package. Do not use this as a standalone shortcut before the upstream
  loop is defined.
---

# Gameplay Pacing And Structure

## Execution Boundary

- This is an internal stage skill under `$gameplay-design-orchestrator`.
- Start only after the loop layer is already locked enough to test time-layer pacing.
- Do not skip upstream loop design.
- If pacing forces a loop-back, record the trigger and send the revision back through the orchestrator-controlled chain.

## Output

Produce:
- 5-second layer
- 30-second layer
- 3-minute layer
- 15-minute layer
- opening script
- first high point
- first frustration point
- replay trigger
- fatigue risks

## Quality Heuristics

- The `5-second layer` must answer what immediate feedback keeps the hands engaged now.
- The `30-second layer` should create a near-term intention reset.
- The `3-minute layer` should deliver a compact arc with setup, pressure, and release.
- The `15-minute layer` should reveal escalation, variation, or mastery pressure.
- `opening script` should teach through action pressure, not exposition.
- `first frustration point` must be intentional and recoverable.

## When pacing exposes a loop failure

- revise loop assumptions before adding a new system
- add a new system only if the pacing issue cannot be solved by reward timing, feedback clarity, or target structure

## Reject

Reject outputs like:
- all reward beats landing only on the 15-minute layer
- replay motivation that depends only on meta progression
- fatigue risks written as generic warnings without a concrete trigger

## Self-check

- Can the first 2 minutes demonstrate the core promise without exposition-heavy support?
- Does each time layer have a distinct job?
- Are fatigue risks tied to a specific repetitive action, reward gap, or decision vacuum?

Do not introduce new systems unless pacing proves the current loop is insufficient.

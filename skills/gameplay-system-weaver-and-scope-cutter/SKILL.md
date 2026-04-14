---
name: gameplay-system-weaver-and-scope-cutter
description: |
  Use when $gameplay-design-orchestrator has already locked the upstream loop,
  pacing, and narrative layers and this system/scope stage is next, or when
  revising system scope on an already locked gameplay package. Do not use this
  as an entry point to design a game from systems first.
---

# Gameplay System Weaver And Scope Cutter

## Execution Boundary

- This is an internal stage skill under `$gameplay-design-orchestrator`.
- Start only after the upstream loop, pacing, and narrative layers are already defined.
- Do not reopen direction choice from inside this stage unless the orchestrator explicitly loops back.
- Every cut or keep decision must remain traceable to the orchestrator-owned package.

## Output

Produce:
- core systems
- secondary systems
- peripheral systems
- input/output relationships
- resource flow
- MVP keep list
- valuable but later list
- first-version cut list
- cost-heavy danger zones

## Quality Heuristics

- `core systems` must each own a distinct player-facing responsibility in the core loop.
- `secondary systems` should amplify choice, pacing, or clarity around the core loop.
- `peripheral systems` should be low-cost flavor, support, or extension.
- `resource flow` must show at least one meaningful source, sink, and tension point.
- `valuable but later list` should preserve real upside ideas that are non-essential.
- `cost-heavy danger zones` should name the real production driver.

## Reject

Reject outputs like:
- system maps where every box is marked `core`
- cut lists containing only obviously impossible ideas instead of hard tradeoffs
- resource loops with no sink, no cap pressure, or no decision cost

## Self-check

- Can the MVP still express the full player promise after the proposed cuts?
- Does every retained system earn its implementation cost by serving the loop?
- Is at least one attractive idea explicitly cut from first version?

Anything that does not serve the core loop should be cut by default.

# Skill Catalog

## Topology

This suite is no longer just an upstream design chain. It is now a four-layer design-to-execution chain:

```text
gameplay-design-orchestrator
  -> gameplay-input-normalizer
  -> gameplay-fantasy-loop-designer
  -> gameplay-pacing-and-structure
  -> gameplay-world-and-narrative-weaver
  -> gameplay-system-weaver-and-scope-cutter
  -> gameplay-coding-handoff-compiler
  -> game-design-spec
  -> game-design-execution-compiler
  -> game-design-execution-runner
```

## Layer Model

### Layer 1: Gameplay package assembly

- `gameplay-design-orchestrator`
- `gameplay-input-normalizer`
- `gameplay-fantasy-loop-designer`
- `gameplay-pacing-and-structure`
- `gameplay-world-and-narrative-weaver`
- `gameplay-system-weaver-and-scope-cutter`
- `gameplay-coding-handoff-compiler`

This layer converts raw game ideas into one validated `Gameplay Design Package`.

### Layer 2: Full design spec expansion

- `game-design-spec`

This layer converts the gameplay package into a full Chinese game design spec with registries, rules, formulas, UI tasks, QA, and delivery mapping.

### Layer 3: Execution-plan compilation

- `game-design-execution-compiler`

This layer converts the mature spec into an agent-executable task graph:

- `execution-plan.json`
- `execution-plan.md`

### Layer 4: Execution coordination

- `game-design-execution-runner`

This layer consumes `execution-plan.json`, persists `execution-run-state.json`, and hands one bounded task at a time to workers.

## Skill Notes

### gameplay-design-orchestrator

- Role: upstream control layer
- Owns:
  - direction lock
  - target scale lock
  - stage ordering
  - package assembly
- Must not:
  - be bypassed by random stage entry
  - let downstream stages start before upstream constraints are locked

### gameplay-input-normalizer

- Role: constraint framing
- Output:
  - target player
  - platform and control constraints
  - scale tier
  - must-have / must-avoid
  - core emotion
  - trend translation direction

### gameplay-fantasy-loop-designer

- Role: core loop design
- Output:
  - player promise
  - identity fantasy
  - core action
  - micro / mid / long loop
  - fun-source judgment

### gameplay-pacing-and-structure

- Role: time-layer pacing
- Output:
  - 5-second / 30-second / 3-minute / 15-minute layers
  - opening highs
  - replay pull
  - fatigue and frustration risks

### gameplay-world-and-narrative-weaver

- Role: narrative wrapper
- Output:
  - world rule
  - player identity
  - core conflict
  - act structure
  - pressure changes caused by narrative

### gameplay-system-weaver-and-scope-cutter

- Role: system graph and scope control
- Output:
  - core / secondary / peripheral systems
  - resource flow
  - MVP keep / later / cut
  - cost-heavy danger zones

### gameplay-coding-handoff-compiler

- Role: coding-facing package layer
- Output:
  - scenes
  - UI surfaces
  - objects
  - state machines
  - variables
  - prototype acceptance

### game-design-spec

- Role: full spec expander
- Input: mature gameplay package
- Output:
  - 11-chapter Chinese execution spec
  - canonical registries
  - config and formula structure
  - QA and delivery mapping

### game-design-execution-compiler

- Role: post-spec task compiler
- Input: mature `game-design-spec` by default, with mature gameplay package as fallback
- Output:
  - `execution-plan.json`
  - `execution-plan.md`
- Main value:
  - splits work into one-iteration tasks
  - binds tasks back to source refs and canonical IDs
- makes dependency order explicit
- turns the design chain into an execution chain

### game-design-execution-runner

- Role: execution coordinator
- Input: validated `execution-plan.json`
- Output:
  - `execution-run-state.json`
  - one bounded worker handoff at a time
  - one dispatch-ready worker packet at a time
- Main value:
  - picks the next runnable task
  - persists run state after every transition
  - stops task sprawl by enforcing one-task scope
  - creates a stable bridge into subagent or coding-worker execution
  - exposes an honest file-based dispatch boundary for later automation
  - separates dispatch issuance from worker acknowledgement
  - binds completion evidence to the active dispatch and exposes a worker adapter for external executors

## Public Demo Priorities

If you are showing this suite publicly, prioritize these talking points:

1. orchestrator-first topology
2. validated gameplay package output
3. full Chinese game spec expansion
4. execution-plan compilation for agent implementation
5. runner prototype for task-by-task coordination
6. validators and real example artifacts

## What Not To Oversell

- Do not claim this suite automatically ships finished games.
- Do not imply stage skills are meant for free-order use.
- Do not present execution compilation as a replacement for engineering judgment.
- Do not pretend the example proves all genres are equally solved.

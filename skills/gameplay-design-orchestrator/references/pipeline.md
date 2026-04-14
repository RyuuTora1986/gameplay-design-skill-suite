# Pipeline

Use this pipeline to compress fuzzy inspiration into a stable gameplay design package.

The orchestrator owns this entire chain.
In the current repo layout, the orchestrator must run all six downstream gameplay stage skills in this exact order once the formal pipeline begins.
Do not treat the downstream stage skills as parallel tracks or default entry points for fresh work.

## Stage 1: Constraint translation

Translate raw input into:

- target player
- platform
- control constraints
- dev scale
- must-have
- must-avoid
- core emotion
- reality mapping
- trend translation

## Stage 2: Player promise and loop

Define:

- who the player is
- what the player repeats
- why it feels good
- what short loop and mid loop exist

## Stage 3: Pacing

Define:

- 5-second feedback
- 30-second replay motivation
- 3-minute mini-goal
- 15-minute content pressure

## Stage 4: World and narrative wrapper

Define:

- player identity
- world rule
- core conflict
- 5-act progression

Narrative only matters if it changes pressure, target, or reward expectation.

## Stage 5: System weaving and scope cut

Define:

- core systems
- secondary systems
- peripheral systems
- input/output dependencies
- cut list

## Stage 6: Coding handoff

Define:

- scene list
- UI list
- object list
- state machines
- variables
- success/failure conditions
- prototype acceptance

## Execution rule

- Fresh work enters through `gameplay-design-orchestrator`.
- The orchestrator locks one direction before the downstream stage chain starts.
- Downstream stage skills may be revisited only as controlled revisions on an already locked package, and any loop-back must be logged explicitly.

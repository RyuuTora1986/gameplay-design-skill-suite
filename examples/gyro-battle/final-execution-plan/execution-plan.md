# Execution Plan

## Project

- Name: gyro-battle
- Source type: game-design-spec
- Source files:
  - examples/gyro-battle/final-spec/01-master-spec.md
  - examples/gyro-battle/final-spec/04-ui-task.md
  - examples/gyro-battle/final-spec/06-balance-task.md
  - examples/gyro-battle/final-spec/07-config-task.md
  - examples/gyro-battle/final-spec/10-qa-task.md
  - examples/gyro-battle/final-spec/11-delivery-task.md
- Execution mode: single-agent-iterative

## Execution Strategy

- Start with the visible combat shell first so later logic and QA work can target a stable runtime surface.
- Keep the first playable slice narrow: one combat HUD, one round-state loop, one reward path, one QA gate.
- Do not redesign the loop, information architecture, or balance topology while compiling this execution layer.

## Task List

### TASK-001 Build arena HUD shell

- Type: ui
- Depends on: none
- Source refs: 04-ui-task.md#HUD-01; 01-master-spec.md#3
- Canonical IDs: SYS-01, CFG-01
- Goal: Render the first-pass combat HUD layout needed for a playable round.
- Deliverables:
  - HUD root container
  - health region
  - charge region
  - timer region
- Acceptance criteria:
  - HUD renders all required combat regions from the UI task
  - No approved HUD region is silently omitted
  - Typecheck passes
  - Browser verification passes
- Verification:
  - npm run typecheck
  - browser-check
- Notes:
  - Do not redesign information hierarchy
  - Use the approved combat terminology from the spec

### TASK-002 Implement core round-state transitions

- Type: logic
- Depends on: TASK-001
- Source refs: 01-master-spec.md#3; 04-ui-task.md#state-matrix
- Canonical IDs: SYS-01, VAR-01
- Goal: Implement the minimal round-state flow needed for one complete loop.
- Deliverables:
  - idle to running transition
  - running to success transition
  - running to failure transition
  - reset path back to idle
- Acceptance criteria:
  - A full round loop can start, resolve, and reset cleanly
  - State transitions follow the spec-defined lifecycle
  - Typecheck passes
  - Relevant logic tests pass
- Verification:
  - npm run typecheck
  - npm run test -- round-state
- Notes:
  - Keep the first pass narrow
  - Do not add meta-progression or economy logic here

### TASK-003 Add first-pass reward formula wiring

- Type: config
- Depends on: TASK-002
- Source refs: 06-balance-task.md#FML-01; 07-config-task.md#CFG-01
- Canonical IDs: FML-01, CFG-01, VAR-01
- Goal: Wire the first reward calculation so the prototype loop produces measurable output.
- Deliverables:
  - reward config entry
  - formula hookup
  - variable mapping
- Acceptance criteria:
  - Reward value is computed from the approved config and formula IDs
  - No hard-coded duplicate balance values are introduced outside config
  - Typecheck passes
  - Relevant logic tests pass
- Verification:
  - npm run typecheck
  - npm run test -- reward-formula
- Notes:
  - Keep balance authoring anchored to config
  - Do not rebalance the whole game in this task

### TASK-004 Create QA pass for playable combat loop

- Type: qa
- Depends on: TASK-001, TASK-002, TASK-003
- Source refs: 10-qa-task.md#playable-loop; 11-delivery-task.md#implementation-map
- Canonical IDs: SYS-01, FML-01, CFG-01
- Goal: Turn the first playable loop into an explicit verification gate.
- Deliverables:
  - QA checklist entry
  - loop verification scenario
  - failure-state verification scenario
- Acceptance criteria:
  - Playable loop verification covers start, resolve, and reset
  - QA explicitly checks the reward output path
  - Typecheck passes
  - Browser verification passes
- Verification:
  - npm run typecheck
  - browser-check
  - manual-qa-checklist
- Notes:
  - QA should reference the same canonical IDs used in implementation
  - Do not broaden this pass into full-game certification

# Game Design Execution Compiler Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new `game-design-execution-compiler` skill that converts mature game specs into `execution-plan.json` and `execution-plan.md`, then update repository documentation, validation, and promo copy to present the expanded end-to-end chain.

**Architecture:** Introduce the compiler as a distinct post-spec skill with its own references and lightweight scripts. Validate the new output with a dedicated JSON/Markdown validator and wire the validated gyro-battle example plus marketing/docs updates around the new chain.

**Tech Stack:** Markdown skills, Python validation/bootstrap scripts, static HTML/CSS/JS promo page, PowerShell release validation.

---

### Task 1: Add the new skill package

**Files:**
- Create: `skills/game-design-execution-compiler/SKILL.md`
- Create: `skills/game-design-execution-compiler/agents/openai.yaml`
- Create: `skills/game-design-execution-compiler/references/output-schema.md`
- Create: `skills/game-design-execution-compiler/references/hard-rules.md`

- [ ] Define the skill contract, routing boundaries, input/output rules, and hard constraints.
- [ ] Add a matching `agents/openai.yaml` descriptor.
- [ ] Document the JSON and Markdown output contract plus execution-task hard rules.

### Task 2: Add compiler scripts and validated example output

**Files:**
- Create: `skills/game-design-execution-compiler/scripts/bootstrap_execution_plan.py`
- Create: `skills/game-design-execution-compiler/scripts/validate_execution_plan.py`
- Create: `examples/gyro-battle/final-execution-plan/execution-plan.json`
- Create: `examples/gyro-battle/final-execution-plan/execution-plan.md`

- [ ] Add a bootstrap script that can generate starter execution-plan files.
- [ ] Add a validator that checks required JSON fields, dependency consistency, and matching Markdown sections.
- [ ] Add a gyro-battle execution-plan example that matches the existing validated spec.

### Task 3: Wire repository docs and validation flow

**Files:**
- Modify: `README.md`
- Modify: `docs/skill-catalog.md`
- Modify: `docs/release-notes-v0.1.0.md`
- Modify: `scripts/validate-release.ps1`

- [ ] Update public topology, skill counts, pipeline diagrams, and validation commands.
- [ ] Add the new execution-plan example to the proof/validation sections.
- [ ] Extend release validation so the new example is checked with the new validator.

### Task 4: Update the promo page copy

**Files:**
- Modify: `index.html`
- Modify: `script.js`

- [ ] Update English and Chinese landing-page copy so the repo is presented as a design-to-execution chain.
- [ ] Reflect the new 9-skill count, execution compiler role, and execution-plan output in hero, pipeline, case-study, and comparison copy.

### Task 5: Verify and prepare for publish

**Files:**
- Test: `scripts/validate-release.ps1`
- Test: `python skills/game-design-execution-compiler/scripts/validate_execution_plan.py --plan-dir examples/gyro-battle/final-execution-plan`

- [ ] Run the new execution-plan validator directly.
- [ ] Run the release validation script end-to-end.
- [ ] Review git diff for consistency before final handoff.

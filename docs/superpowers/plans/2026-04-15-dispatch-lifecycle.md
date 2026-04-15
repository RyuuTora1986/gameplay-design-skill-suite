# Dispatch Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the execution runner from file-only dispatch output to a runner-managed dispatch lifecycle with explicit acknowledgement before completion.

**Architecture:** Extend the execution runner state model with dispatch metadata and a `dispatched` phase, add an `ack` command that transitions a dispatched task into `running`, and update validation/docs so the lifecycle is enforced and explained end to end.

**Tech Stack:** Python CLI runner, JSON state files, PowerShell validation script, Markdown docs

---

### Task 1: Lock the lifecycle in validation

**Files:**
- Modify: `scripts/validate-release.ps1`

- [ ] Add smoke-test coverage that requires `dispatch` before `ack`
- [ ] Add smoke-test coverage that requires `ack` before `complete`
- [ ] Run the smoke path and confirm it fails before the runner implementation is updated

### Task 2: Implement runner-managed dispatch state

**Files:**
- Modify: `skills/game-design-execution-runner/scripts/run_execution_plan.py`

- [ ] Add persisted dispatch metadata to per-task state
- [ ] Add `dispatched` as an explicit state
- [ ] Add `ack` command and enforce valid transitions
- [ ] Tighten completion/block/fail rules around lifecycle status

### Task 3: Update docs and references

**Files:**
- Modify: `skills/game-design-execution-runner/SKILL.md`
- Modify: `skills/game-design-execution-runner/references/state-model.md`
- Modify: `skills/game-design-execution-runner/references/worker-prompt-contract.md`
- Modify: `docs/execution-runner-architecture.md`
- Modify: `README.md`
- Modify: `README.zh-CN.md`
- Modify: `docs/skill-catalog.md`
- Modify: `docs/release-notes-v0.3.0.md`

- [ ] Document the `dispatch -> ack -> complete` lifecycle
- [ ] Document the new dispatch metadata and worker acknowledgement contract

### Task 4: Verify and publish

**Files:**
- Modify: local working tree plus remote repo state

- [ ] Run `python -m py_compile skills\game-design-execution-runner\scripts\run_execution_plan.py`
- [ ] Run `powershell -ExecutionPolicy Bypass -File scripts\validate-release.ps1`
- [ ] Push the validated change to `main`

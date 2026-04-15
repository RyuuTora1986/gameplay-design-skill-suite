# Release Notes: v0.4.0

## Release Title

`v0.4.0 - Execution Platform Layer For Gameplay Design Suite`

## Summary

This release completes the first platformization pass for the execution side of the suite.

The chain now covers:

- gameplay-package assembly
- full Chinese spec expansion
- execution-plan compilation
- runner coordination
- dispatch packet generation
- dispatch acknowledgement
- dispatch-bound completion review
- worker adapter execution interface

## Highlights

- added `dispatch -> ack -> complete` lifecycle tracking
- added dispatch metadata persistence in runner state
- added dispatch-bound review gate checks on completion evidence
- added `worker_adapter.py` for external worker pickup / complete / fail / block flows
- refreshed repo and promo copy to focus on product value and workflow clarity

## Why This Matters

The suite now offers more than design output and task planning.

It also provides a controlled execution boundary:

- a task can be dispatched
- a named worker can acknowledge ownership
- completion evidence must match the active dispatch
- external workers can integrate through one adapter-facing interface

That makes the repository easier to position as a workflow product and easier to extend into future multi-agent or service-based execution paths.

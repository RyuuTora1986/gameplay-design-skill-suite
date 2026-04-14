# Asset Stage Rules

Use this file to turn asset generation into a strict stage machine instead of a vague workflow.

## Goal

Prevent downstream tools from jumping straight to polished output before structure, anchor, and acceptance criteria exist.

## Allowed stages

| Stage | Meaning | Required input | Required output |
|---|---|---|---|
| draft | Structure first | scope, target use, rough layout or asset family | draft artifact and known gaps |
| anchor_locked | Style decisions frozen | draft + anchor decision | chosen anchor and rejection reasons for alternates |
| batch_generated | Family produced | anchor + batch scope + naming rules | candidate asset batch |
| accepted | Passed checks | batch + acceptance checklist | accepted asset IDs |
| rejected | Not accepted | failed checklist | failure reason and replacement target |

## Stage transition rules

- `draft -> anchor_locked` only if the structure is clear enough to judge style against it.
- `anchor_locked -> batch_generated` only if the anchor is concrete and stable.
- `batch_generated -> accepted` only if the acceptance checklist passes.
- `batch_generated -> rejected` if the batch fails style, readability, export, or integration checks.
- `rejected -> batch_generated` only if the replacement request points back to the same anchor or explicitly revises the anchor.

## Tool discipline

- AI UI tools should default to `draft` or `batch_generated`, not automatically `accepted`.
- AI image tools should not enter `batch_generated` before `anchor_locked`.
- AI audio tools should not enter `accepted` without event clarity and mix checks.
- AI coding tools should consume only `accepted` assets unless the user explicitly wants placeholder output.

## Fallback rule

If the preferred generation tool is unavailable:

- keep the same stage model
- switch tools, not standards
- if no generator is available, produce a placeholder asset pack and keep the stage as `draft` or `accepted-placeholder`

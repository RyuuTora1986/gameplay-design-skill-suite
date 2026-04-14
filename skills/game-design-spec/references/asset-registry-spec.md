# Asset Registry Spec

Use this file when UI, art, audio, or hybrid assets need to be tracked across multiple generation steps.

## Goal

Make every generated asset traceable, reviewable, and replaceable.

Without an asset registry, the pipeline may produce outputs, but later tools will not know:

- which anchor a file belongs to
- which stage it is in
- whether it was accepted
- what file should replace it if regenerated

## Required fields

Each asset family or concrete asset should be tracked with these fields:

| Field | Meaning |
|---|---|
| asset_id | Stable unique ID such as `AST-UI-001` |
| family_id | Asset family such as `UI-PAGE`, `ART-ICON`, `SFX-UI`, `BGM-SCENE` |
| related_system_ids | Related `SYS-*` IDs |
| anchor_id | The style or audio anchor used |
| current_stage | `draft`, `anchor_locked`, `batch_generated`, `accepted`, or `rejected` |
| intended_tool | AI coding / AI UI / AI image / AI audio / manual cleanup |
| intended_use | What the asset is for |
| export_spec | Size, format, transparency, loop, slice, or naming requirement |
| acceptance_status | pending / accepted / rejected |
| replacement_of | Previous asset ID if this item supersedes another one |

## Minimum registry shape

```markdown
## 资产登记表

| asset_id | family_id | related_system_ids | anchor_id | current_stage | intended_tool | intended_use | export_spec | acceptance_status | replacement_of |
|---|---|---|---|---|---|---|---|---|---|
| AST-UI-001 | UI-PAGE | SYS-01 | ANCHOR-UI-01 | draft | AI UI | 洗浴主界面结构稿 | 1280x720 PNG | pending | 无 |
```

## Rules

- Do not regenerate assets anonymously. Every new batch item should have or inherit an `asset_id`.
- If an asset is rejected and regenerated, mark the new one with `replacement_of`.
- Do not mark an asset as `accepted` until its acceptance checklist has passed.
- If multiple tools are used, the registry must still describe one source-of-truth status for each asset.

# Handoff Contract To game-design-spec

Use this contract to guarantee that the upstream gameplay package can be expanded by `$game-design-spec` without reinterpretation drift.

## Required upstream sections

The Gameplay Design Package must include:

- `游戏一句话`
- `玩家承诺`
- `核心玩法`
- `节奏设计`
- `世界观与叙事流程`
- `系统网`
- `规模与实现边界`
- `原型执行翻译`
- `风险评审`
- `对接下游策划案`

The package directory must also include `02-review-notes.md` as the decision log for direction choice and major loop-backs.

## Required canonical registries

The package must declare:

- `系统主索引表`
- `资源主索引表`
- `公式主索引表`
- `配置表主索引表`
- `变量主索引表`

## Required canonical IDs

Use these object prefixes consistently:

- `SYS-*` for systems
- `RES-*` for resources
- `FML-*` for formulas
- `CFG-*` for config tables
- `VAR-*` for variables

## Downstream mapping

The upstream package should already explain this mapping:

- `玩家承诺` -> `$game-design-spec` chapter 1.5 and chapter 3 foundation
- `核心玩法` -> chapter 1.5 and chapter 3 rules
- `节奏设计` -> chapter 1.9, chapter 5, chapter 10
- `世界观与叙事流程` -> chapter 1.1, chapter 5, chapter 8, chapter 9
- `系统网` -> registries, chapter 2, chapter 3
- `规模与实现边界` -> chapter 1.12, 1.13, chapter 11
- `原型执行翻译` -> chapter 7, chapter 10, chapter 11
- `风险评审` -> chapter 10 and chapter 11

## Forbidden drift

Do not allow:

- upstream using one set of object names and downstream using another
- upstream omitting registries and expecting downstream to invent them
- upstream leaving scale unresolved and downstream guessing it
- upstream giving narrative without gameplay pressure change
- upstream giving systems without player promise

- upstream revising major decisions without logging the trigger and rationale in review notes

## Asset-generation addendum

If UI, art, or audio generation quality is likely to be a project risk, the upstream package should also include:

- a short style anchor block
- asset pipeline assumptions
- generator handoff assumptions for downstream chapters

Do not leave all visual or asset-generation decisions to downstream tools without any anchor or stage assumptions.

# Output Contract

Use this file as the source of truth for section coverage, canonical registries, and split-task consistency.

## Mandatory top block

If any required source information is missing, start with:

## 假设清单

- 假设 1
- 假设 2

Do not replace missing information with questions unless the task would otherwise become unsafe or illegal.

## Mandatory canonical registries

Before expanding the main chapters, output these registries in `01-master-spec.md`.

### 系统主索引表

| 字段 | 说明 |
|---|---|
| 系统ID | 唯一编号，格式建议 `SYS-01` |
| 系统名 | 对外统一名称 |
| 一句话定位 | 该系统解决什么问题 |
| 玩家目标 | 玩家为什么进入这个系统 |
| 核心输入 | 玩家投入的操作、资源、时间 |
| 核心输出 | 奖励、状态变化、解锁、反馈 |
| 依赖系统 | 上游系统 ID，没有则写 `无` |
| 对应UI任务 | 章节 4 对应条目 |
| 对应数值任务 | 章节 6 对应条目 |
| 对应配置表 | 章节 7 对应表名 |
| 对应测试重点 | 章节 10 对应测试项 |

### 资源主索引表

| 字段 | 说明 |
|---|---|
| 资源ID | 唯一编号，格式建议 `RES-01` |
| 资源名 | 统一资源名称 |
| 类型 | 货币、材料、次数、门票、体力等 |
| 主要来源系统ID | 主要生产该资源的系统 |
| 主要去向系统ID | 主要消耗该资源的系统 |
| 是否稀缺 | `是` 或 `否` |

### 公式主索引表

| 字段 | 说明 |
|---|---|
| 公式ID | 唯一编号，格式建议 `FML-01` |
| 公式名 | 统一公式名称 |
| 所属系统ID | 公式归属系统 |
| 输入变量 | 变量名或变量ID列表 |
| 输出结果 | 公式输出对象 |
| 对应章节 | 默认是 chapter 6 |

### 配置表主索引表

| 字段 | 说明 |
|---|---|
| 表ID | 唯一编号，格式建议 `CFG-01` |
| 表名 | 统一表名 |
| 所属系统ID | 表归属系统 |
| 主键 | 主键字段 |
| 主要用途 | 该表服务什么规则 |
| 热更支持 | `是` 或 `否` |

### 变量主索引表

| 字段 | 说明 |
|---|---|
| 变量ID | 唯一编号，格式建议 `VAR-01` |
| 变量名 | 统一变量名 |
| 所属公式ID | 该变量归属哪条公式 |
| 单位 | 次数、秒、点数、百分比等 |
| 主要来源 | `RES-*`、`CFG-*`、常量、系统状态等 |
| 主要去向 | `FML-*`、`CFG-*`、结果字段等 |

## Consistency rules

- 同一系统、资源、公式、配置表、变量在全篇只允许一套名称和一套 ID。
- 稀缺资源应同时有明确来源和明确去向。
- 每个公式应至少有一个变量挂接到变量主索引表。
- 每个配置表必须映射到有效系统。
- 实施任务和 QA 任务中的对象引用，必须能回指到这些主索引。

Use the standard templates from `references/templates.md` unless the user explicitly asks for another shape.

## Main delivery structure

### 1. 游戏概述

Must include:

- `1.1 题材与美术风格`
- `1.2 游戏名`
- `1.3 游戏类型`
- `1.4 平台`
- `1.5 核心玩法概述`
- `1.6 游戏视角`
- `1.7 操作方式`
- `1.8 目标玩家与年龄分级`
- `1.9 游玩时长与游戏节奏`
- `1.10 单机/联网与存档方式`
- `1.11 商业化模式`
- `1.12 技术栈与引擎`
- `1.13 最低设备指标`

`1.5 核心玩法概述` must include:

- 一句话卖点
- 核心游戏循环
- 基础循环
- 扩展循环
- 长期循环
- 玩家成长路径
- 失败与复盘机制

### 2. 系统框架设计

Must include:

- `2.1 系统总览`
- `2.2 系统间关联与依赖`

`2.1 系统总览` must reconcile with the `系统主索引表`.

### 3. 分系统规则

For each system, must include:

- 设计目的
- 用户维度说明
- 关键名词定义
- 规则细则
- 边界条件、异常与极端输入
- 状态机
- 反滥用与防刷

Also include:

- `3.2 可重复游玩设计`

Chapter 3 should default to `系统规则卡`.

### 4. 分系统UI设计

Output as a separate task after chapters 1-3 exist.

Each UI task must start with:

- `覆盖系统ID`
- `关联上游系统`
- `关联下游去向`

Chapter 4 should default to `UI状态矩阵`.

### 5. 关卡设计

Output as a separate task after chapters 1-3 exist.

Must include:

- 关卡结构描述
- 详细关卡内容描述
- 首关可玩性
- 新手引导
- 关卡生成逻辑

### 6. 数值与经济

Output as a separate task after chapters 1-3 and 5 exist.

Each balance section must start with:

- `覆盖系统ID`
- `相关资源`
- `相关公式`

Chapter 6 should default to `数值公式卡`.

### 7. 配置表与工具设计

Output as a separate task after chapters 1-3, 5, 6 exist.

Each config block must start with:

- `覆盖系统ID`
- `表名`
- `主键`
- `关联外键`

Chapter 7 should default to `配置字段表`.

### 8. 美术需求

Output as a separate task after chapters 1-3, 5, 6 exist.

### 9. 音乐与音效需求

Output as a separate task after chapters 1-3, 5, 6, 8 exist.

### 10. 可玩性与质量保障

Output as a separate task after chapters 1-3, 5, 6, 8, 9 exist.

Each QA block must start with:

- `覆盖系统ID`
- `冒烟流程`
- `边界压力`
- `回归重点`
- `覆盖公式ID`
- `覆盖表ID`

Chapter 10 should default to `QA覆盖回指表`.

### 11. 落地实施计划

Output as a separate task after chapters 1-3, 5, 6, 7, 8, 9, 10 exist.

Each implementation plan must map tasks back to system, formula, config, and resource IDs where concrete work exists.

Chapter 11 should default to:

- `风险处置表`
- `实施任务回指表`

## Mandatory footer

The final document must include all four blocks:

- `版本号与日期`
- `变更清单（新增/修改/移除）`
- `与上一版的差异对比`
- `自检结论`

## Recommended production order

| Task | Output chapter | Depends on |
|---|---|---|
| A | 假设清单 + 全部主索引表 + 1, 2, 3 | 游戏设计要点 |
| B | 4 | A |
| C | 5 | A |
| D | 6 | A + C |
| E | 7 | A + C + D |
| F | 8 | A + C + D |
| G | 9 | A + C + D + F |
| H | 10 | A + C + D + F + G |
| I | 11 | A + C + D + E + F + G + H |

## Cross-file consistency

When the output is split into multiple files:

- `01-master-spec.md` is the single source of truth for all canonical registries.
- `04-11` task files may only reference indexed systems, resources, formulas, config tables, and variables.
- If a task introduces a new concrete object, it must be added back to `01-master-spec.md` first.
- Key systems, formulas, and config tables should appear in QA or implementation task files.

## Asset-generation addendum

Use this addendum when chapter 4, 8, 9, 10, or 11 depends on AI-generated UI, images, or audio.

### Chapter 4 addendum

Chapter 4 should also include:

- a style anchor block
- an asset pipeline stage block
- UI acceptance checks
- generator handoff notes when AI UI generation is expected

### Chapter 8 addendum

Chapter 8 should also include:

- a style anchor block
- asset family grouping
- current stage and next stage for each family
- naming and export rules
- art acceptance checks

### Chapter 9 addendum

Chapter 9 should also include:

- audio anchor rules
- per-scene or per-event generation constraints
- export rules
- audio acceptance checks

### Chapter 10 addendum

Chapter 10 should convert relevant UI, art, and audio acceptance checks into explicit QA cases.

### Chapter 11 addendum

If AI UI, image, or audio tools are part of the plan, chapter 11 should include:

- generator input order
- required return fields
- rejection conditions

## Asset-registry addendum

When assets are generated across multiple steps, tools, or revisions, include an `资产登记表` with:

- stable `asset_id`
- `family_id`
- `anchor_id`
- `current_stage`
- `acceptance_status`

If tool choice materially affects quality or reliability, the relevant chapter should also include:

- preferred tool path
- fallback tool path
- placeholder-safe backup path

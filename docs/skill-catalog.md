# Skill Catalog

## Topology

这套体系不是 8 个平级 skill，而是 1 个上游总控 + 6 个受控 stage + 1 个下游规格展开器。

```text
gameplay-design-orchestrator
  -> gameplay-input-normalizer
  -> gameplay-fantasy-loop-designer
  -> gameplay-pacing-and-structure
  -> gameplay-world-and-narrative-weaver
  -> gameplay-system-weaver-and-scope-cutter
  -> gameplay-coding-handoff-compiler
  -> game-design-spec
```

## Skill Notes

### 1. gameplay-design-orchestrator

- Type: upstream control layer
- Use when: 游戏概念仍然模糊，尚未形成可执行玩法主干
- Owns:
  - 方向筛选
  - target scale 锁定
  - 串行 stage 调度
  - Gameplay Design Package 组装
- Must not:
  - 被替换成任意单 stage 入口
  - 跳过中间 stage 直接手搓 package

### 2. gameplay-input-normalizer

- Type: constraint framing stage
- Output:
  - target player
  - platform and control constraints
  - scale tier
  - must-have / must-avoid
  - core emotion
  - trend translation direction
  - budget and content pressure
- Main job: 把“感觉”收敛成能驱动后续设计的边界

### 3. gameplay-fantasy-loop-designer

- Type: core loop stage
- Output:
  - player promise
  - identity fantasy
  - core action
  - micro / mid / long loop
  - fun-source judgment
- Main job: 找出真正值得重复的动作和玩家承诺

### 4. gameplay-pacing-and-structure

- Type: time-layer pacing stage
- Output:
  - 5-second / 30-second / 3-minute / 15-minute layers
  - opening script
  - first high point
  - first frustration point
  - replay trigger
  - fatigue risks
- Main job: 让 loop 在时间维度上成立

### 5. gameplay-world-and-narrative-weaver

- Type: narrative wrapper stage
- Output:
  - world one-liner
  - player identity one-liner
  - core conflict one-liner
  - 5-act narrative
  - per-act pressure changes
  - text-vs-gameplay narrative split
- Main job: 用世界规则和冲突强化玩法，而不是反过来拿世界观掩盖玩法空洞

### 6. gameplay-system-weaver-and-scope-cutter

- Type: system graph and scope control stage
- Output:
  - core / secondary / peripheral systems
  - input-output relationships
  - resource flow
  - MVP keep list
  - valuable but later list
  - first-version cut list
  - cost-heavy danger zones
- Main job: 把玩法承诺映射为有限系统，而不是无上限扩张

### 7. gameplay-coding-handoff-compiler

- Type: coding handoff stage
- Output:
  - scene list
  - UI list
  - object list
  - state machines
  - key variables
  - interaction events
  - placeholder art/audio strategy
  - prototype acceptance
- Main job: 让下游实现代理不用重新设计一遍游戏

### 8. game-design-spec

- Type: full spec expander
- Use when: 已有成熟玩法包，需要扩为完整中文规格书与任务包
- Output:
  - 11 章完整规格
  - 配置与规则结构
  - QA 与验收
  - 交付计划和实施拆分
- Main job: 从“设计包”走到“执行包”

## What To Demo Publicly

如果你要向潜在客户或合作方展示这一套体系，优先展示：

1. orchestrator-first 拓扑
2. MVP keep/cut 的 scope discipline
3. 中文规格书的执行友好性
4. 自带样例和校验脚本的可信度

## What Not To Oversell

- 不要把这套 skill 说成“自动生成可上线游戏”
- 不要暗示中间 stage 可以随意乱序调用
- 不要把 narrative 包装描述成玩法主干本身
- 不要把样例说成“适用于所有游戏类型”


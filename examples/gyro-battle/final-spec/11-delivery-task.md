# 前置内容

- Dependency: master spec chapters 1-10
- Source: 01-master-spec.md
- 覆盖系统ID: SYS-01, SYS-02, SYS-03, SYS-04

# 11. Delivery Task

## 输出要求

- Extend the master spec without breaking canonical IDs.
- Keep the output executable and table-first.
- Add assumptions explicitly before using them.
- Keep object references anchored to SYS-01 / SYS-02 / SYS-03 / SYS-04 / RES-01 / RES-02 / RES-03 / FML-01 / FML-02 / FML-03 / CFG-01 / CFG-02 / CFG-03.

## 正文

- Covers SYS-01, SYS-02, SYS-03, SYS-04, RES-01, RES-02, RES-03, FML-01, FML-02, FML-03, CFG-01, CFG-02, CFG-03.

### 实施任务回指表

| 任务ID | Name | System ID | Formula ID | Config ID | Resource ID | Deliverable |
|---|---|---|---|---|---|---|
| TASK-01 | 实现发射与碰撞基础回路 | SYS-01 | FML-01 | CFG-01 | RES-01 | BattleScene 原型可碰撞 |
| TASK-02 | 接入转速与耐久结算 | SYS-02 | FML-01 | CFG-01 | RES-01, RES-03 | 回合可停转与判负 |
| TASK-03 | 接入爆发条与技能系统 | SYS-03 | FML-02 | CFG-02 | RES-02 | 技能可释放并进入冷却 |
| TASK-04 | 接入 arena 规则与比分 | SYS-04 | FML-03 | CFG-03 | RES-01 | 三回合两胜闭环 |
| TASK-05 | 完成 HUD 与回合结算 | SYS-01, SYS-02, SYS-03, SYS-04 | FML-01, FML-02, FML-03 | CFG-01, CFG-02, CFG-03 | RES-01, RES-02, RES-03 | 可玩 UI 原型 |

### 生成工具
- UI/美术/音频对应工具：Figma、位图生成工具、短音效生成工具。
- 程序实现工具：HTML5 Canvas + JavaScript。
- 协作与版本控制工具：Git。

### 拒收条件
- 任一关键功能无法在原型中被验证：拒收。
- 任一关键资产无法满足验收表标准：拒收。
- 任一回指对象 ID 断链：拒收。

### 里程碑
| 里程碑 | 输出 |
|---|---|
| M1 | 单回合可发射、可碰撞、可判定击飞 |
| M2 | 三回合两胜、资源条、技能条可用 |
| M3 | 两张 arena、三套模板、人机可打 |

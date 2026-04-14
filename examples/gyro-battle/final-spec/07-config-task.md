# 前置内容

- Dependency: master spec chapters 1-6
- Source: 01-master-spec.md
- 覆盖系统ID: SYS-01, SYS-03, SYS-04

# 7. Config Task

## 输出要求

- Extend the master spec without breaking canonical IDs.
- Keep the output executable and table-first.
- Add assumptions explicitly before using them.
- Keep object references anchored to SYS-01 / SYS-03 / SYS-04 / CFG-01 / CFG-02 / CFG-03.

## 正文

- Covers SYS-01, SYS-03, SYS-04, CFG-01, CFG-02, CFG-03.

### 配置表说明
| 表ID | 字段 | 说明 |
|---|---|---|
| CFG-01 | part_id, speed, weight, stability, dash_force | 陀螺模板与部件属性 |
| CFG-02 | skill_id, cooldown_ms, burst_cost, effect_type, effect_value | 技能配置 |
| CFG-03 | arena_id, round_time_sec, hazard_profile, center_bonus, edge_threshold | 场地规则 |

### 工具链要求
- 表结构用 JSON 或 CSV 均可，但运行时必须转成只读配置对象。
- 修改 CFG-02 不允许破坏技能图标与说明的键值绑定。
- arena 规则调整必须同步 QA 期望值。

### 配置验收
| 项目 | 标准 |
|---|---|
| 可读性 | 策划能直接看懂字段含义 |
| 热更安全 | 改配置不需要改逻辑常量 |
| 关联一致性 | UI、数值、QA 中引用的 ID 与配置一致 |

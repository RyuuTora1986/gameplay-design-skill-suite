# 前置内容

- Dependency: master spec chapters 1-9
- Source: 01-master-spec.md
- 覆盖系统ID: SYS-01, SYS-02, SYS-03, SYS-04

# 10. QA Task

## 输出要求

- Extend the master spec without breaking canonical IDs.
- Keep the output executable and table-first.
- Add assumptions explicitly before using them.
- Keep object references anchored to SYS-01 / SYS-02 / SYS-03 / SYS-04 / RES-01 / RES-02 / RES-03 / FML-01 / FML-02 / FML-03 / CFG-01 / CFG-02 / CFG-03.

## 正文

- Covers SYS-01, SYS-02, SYS-03, SYS-04, RES-01, RES-02, RES-03, FML-01, FML-02, FML-03, CFG-01, CFG-02, CFG-03.

### QA覆盖回指表

| 用例ID | Name | System ID | Formula ID | Config ID | Goal |
|---|---|---|---|---|---|
| QA-01 | 发射与首撞烟测 | SYS-01 | FML-01 | CFG-01 | 验证 10 秒内出现有效碰撞 |
| QA-02 | 转速与耐久衰减 | SYS-02 | FML-01 | CFG-01 | 验证资源下降与停转判定 |
| QA-03 | 爆发条增长与技能释放 | SYS-03 | FML-02 | CFG-02 | 验证爆发窗口与冷却 |
| QA-04 | 击飞判定与回合结束 | SYS-04 | FML-03 | CFG-03 | 验证边界击飞和比分变化 |
| QA-05 | arena 差异可感知 | SYS-04 | FML-03 | CFG-03 | 验证不同场地策略差异 |

### 回归重点
- 任何修改冲刺、质量、稳定性时，必须重跑 QA-01 到 QA-04。
- 任何修改 arena 规则时，必须重跑 QA-04 与 QA-05。
- 任何修改技能配置时，必须重跑 QA-03 并检查 UI 冷却显示。

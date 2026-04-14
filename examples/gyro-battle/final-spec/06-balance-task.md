# 前置内容

- Dependency: master spec chapters 1-5
- Source: 01-master-spec.md
- 覆盖系统ID: SYS-01, SYS-02, SYS-03, SYS-04

# 6. Balance Task

## 输出要求

- Extend the master spec without breaking canonical IDs.
- Keep the output executable and table-first.
- Add assumptions explicitly before using them.
- Keep object references anchored to SYS-01 / SYS-02 / SYS-03 / SYS-04 / RES-01 / RES-02 / RES-03 / FML-01 / FML-02 / FML-03 / CFG-01 / CFG-02 / CFG-03 / VAR-01 / VAR-02 / VAR-03 / VAR-04.

## 正文

- Covers SYS-01, SYS-02, SYS-03, SYS-04, RES-01, RES-02, RES-03, FML-01, FML-02, FML-03, CFG-01, CFG-02, CFG-03, VAR-01, VAR-02, VAR-03, VAR-04.

### 关键公式
| 公式ID | 公式 | 设计意图 |
|---|---|---|
| FML-01 | damage = collision_speed * 0.6 + max(0, 50 - stability_rating) * 0.15 | 高速撞击有收益，但稳定型不会被秒穿 |
| FML-02 | burst_gain = collision_speed * 0.4 + center_control_bonus | 鼓励主动争夺中心区 |
| FML-03 | ring_out = knockback_vector > arena_edge_threshold - stability_rating * 0.1 | 让稳定性影响击飞概率，但不完全免疫 |

### 模板平衡目标
| 模板 | 速度 | 稳定 | 技能倾向 | 目标 |
|---|---|---|---|---|
| 攻击型 | 高 | 低 | 突进、重击 | 先手击飞 |
| 稳定型 | 中 | 高 | 抗压、反打 | 拖到资源优势 |
| 技巧型 | 中高 | 中 | 位移、骗招 | 抢节奏窗口 |

### 资源经济节奏
| 资源ID | 获取方式 | 消耗方式 | 风险点 |
|---|---|---|---|
| RES-01 | 初始满值后持续衰减 | 时间流逝、技能、碰撞 | 拖太久必输 |
| RES-02 | 有效碰撞、中心区站位 | 技能释放 | 滚雪球过快会降低博弈 |
| RES-03 | 承受重击时下降 | 无恢复，回合结算重置 | 爆发秒杀要受控 |

### 数值验收
| 指标 | 目标范围 |
|---|---|
| 单回合平均时长 | 35-55 秒 |
| 首次爆发出现时间 | 15-30 秒 |
| 击飞终结占比 | 35%-55% |
| 耐久耗尽终结占比 | 25%-40% |

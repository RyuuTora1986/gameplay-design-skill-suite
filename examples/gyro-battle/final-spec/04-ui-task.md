# 前置内容

- Dependency: master spec chapters 1-3
- Source: 01-master-spec.md
- 覆盖系统ID: SYS-01, SYS-02, SYS-03, SYS-04

# 4. UI Task

## 输出要求

- Extend the master spec without breaking canonical IDs.
- Keep the output executable and table-first.
- Add assumptions explicitly before using them.
- Keep object references anchored to SYS-01 / SYS-02 / SYS-03 / SYS-04 / RES-01 / RES-02 / RES-03 / FML-01 / FML-02 / FML-03 / CFG-01 / CFG-02 / CFG-03 / VAR-01 / VAR-02 / VAR-03 / VAR-04.

## 正文

- Covers SYS-01, SYS-02, SYS-03, SYS-04, RES-01, RES-02, RES-03, FML-01, FML-02, FML-03, CFG-01, CFG-02, CFG-03, VAR-01, VAR-02, VAR-03, VAR-04.

### 风格锚点
- HUD 用黑底荧光蓝/橙双主色，保证玩家与对手状态一眼区分。
- 战斗层信息密度高，但所有关键条形资源必须贴近各自陀螺或固定在屏幕四角，不漂浮遮挡场地。
- 场地危险区使用脉冲光圈而非写实材质，优先传达规则而不是装饰。

### 资产流水线
- 阶段 1：先做线框 HUD、占位按钮、资源条与比分面板。
- 阶段 2：接入战斗 UI 动效、技能图标、击飞与停转提示。
- 阶段 3：补胜负结算面板、模板选择页、回合复盘信息。

### UI验收
| 验收项 | 标准 |
|---|---|
| 发射信息可读性 | 玩家能在 3 秒内理解拖拽方向、蓄力强度与发射释放时机 |
| 战斗信息优先级 | 转速、耐久、爆发条、比分、技能冷却同时可读，且不遮挡核心碰撞区域 |
| 状态反馈 | 击飞、爆发、停转、回合结束必须有强反馈与文字标签 |

### 生成交接
- Preferred path / fallback / backup should be filled here.
- 推荐用 Figma 先做 HUD 与回合结算页，再交给前端/游戏实现。
- 兜底方案是直接用 Canvas 绘制线框 UI，不阻塞对战原型。

### 页面与状态矩阵
| 页面/面板 | 关联系统ID | 必显资源/变量 | 进入条件 | 退出条件 |
|---|---|---|---|---|
| 模板选择页 | SYS-01, SYS-03 | CFG-01, CFG-02 | 进入单局前 | 开始回合 |
| 战斗 HUD | SYS-01, SYS-02, SYS-03, SYS-04 | RES-01, RES-02, RES-03 | 回合开始 | 回合结算 |
| 回合结算面板 | SYS-04 | 比分、击飞原因、耐久差 | 回合结束 | 下一回合 |
| 整局结果页 | SYS-04 | 总比分、模板表现 | 整局结束 | 返回标题 |

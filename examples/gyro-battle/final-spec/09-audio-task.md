# 前置内容

- Dependency: master spec chapters 1-8
- Source: 01-master-spec.md
- 覆盖系统ID: SYS-01, SYS-03, SYS-04

# 9. Audio Task

## 输出要求

- Extend the master spec without breaking canonical IDs.
- Keep the output executable and table-first.
- Add assumptions explicitly before using them.
- Keep object references anchored to SYS-01 / SYS-03 / SYS-04.

## 正文

- Covers SYS-01, SYS-03, SYS-04.

### 音频锚点
- 高频金属擦切、低频冲击、电子竞技倒计时提示音。
- 玩家技能音色偏明亮，对手关键威胁音偏低沉。
- 胜负结算音必须短促干净，不拖慢节奏。

### 生成交接
- Preferred path / fallback / backup should be filled here.
- 首选短促可循环战斗层 + 事件音效分离生成。
- 兜底方案是基础碰撞、爆发、击飞、结算四类占位音包。

### 音频验收
| 验收项 | 标准 |
|---|---|
| 可循环性 | 战斗层背景 30 秒循环无明显断点 |
| 事件匹配度 | 撞击、爆发、击飞三类事件能一耳区分 |
| 噪声与混音控制 | 高强度碰撞时不盖住倒计时与回合提示 |

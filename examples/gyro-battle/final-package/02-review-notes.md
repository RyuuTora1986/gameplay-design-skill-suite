# Review Notes

## Candidate Directions

| 方向名 | 玩家身份 | 重复动作 | 最强感受 | 范围压力 | 舍弃原因 |
|---|---|---|---|---|---|
| A 竞技场击飞型 | 地下联赛操盘手 | 发射、走位、碰撞、攒条、放技能 | 读招后精准撞飞的爆发感 | 中等，可用少量 arena 和模板验证 | 保留并选中 |
| B 拼装养成型 | 车库技师兼选手 | 拆件、拼装、试转、刷材料 | 长线养成与 build 成长 | 高，需要大量部件、掉落、经济和 UI | 首版过重，削弱短局验证效率 |

## Final Choice

- chosen direction: A 竞技场击飞型
- strongest promise: 让玩家在短局内反复体验“抓到时机一撞定胜负”的竞技爽点
- biggest scope risk: 如果物理反馈和击飞判定不可读，就会沦为随机乱撞
- cut-first target: 任何需要长线养成、部件经济或联网支撑的系统都先砍掉

## Major Revisions

| revision_id | triggering_stage | what_failed | changed_decision | why_stronger_now | downstream_implications |
|---|---|---|---|---|---|
| REV-01 | gameplay-pacing-and-structure | 早期方案把单回合做成 90 秒到 120 秒的长拉锯，前 30 秒高光不足 | 改成三回合两胜、单回合 35 到 55 秒、爆发条更快成型 | 更符合网页端短局反馈，首回合就能看到技能与击飞高光 | 下游 spec 需要围绕回合制节奏、比分 UI 和快速复盘设计 |
| REV-02 | gameplay-system-weaver-and-scope-cutter | 初版想加入深度零件拼装和局间强化，首版范围失控 | 零件拼装只保留为模板差异，不做首版深养成 | 保住了“可操作碰撞博弈”主轴，减少 UI 和配置爆炸 | 下游配置表聚焦模板差异、技能与 arena 规则，而不是经济系统 |

## Loop-back Summary

- loop-back count: 2
- highest-cost revision: 从长回合拉锯改成三回合两胜的回合制节奏重构
- still-open fragility: 如果 arena 差异做得太保守，中期内容仍可能显得重复，后续 spec 需要强化场地节奏差异

# Gameplay Design Skill Suite

<p align="center">
  <img src="assets/hero-anime-banner.svg" alt="Gameplay Design Skill Suite hero banner" width="100%" />
</p>

<p align="center">
  面向 Codex 的游戏设计技能套件。以 <code>gameplay-design-orchestrator</code> 为唯一正常入口，把模糊游戏概念收敛为可执行的玩法设计包，再继续落到完整中文游戏规格书。
</p>

<p align="center">
  Orchestrator-first game design skills for Codex, built to turn raw ideas into production-minded gameplay packages and implementation-ready specs.
</p>

## Why This Repo Exists

大多数“游戏设计提示词”只能给你灵感，不能给你稳定结构。这个仓库的目标不同：

- 先锁方向，再跑 stage，而不是一上来堆系统和世界观
- 把 `gameplay-*` stage skills 约束为受控链路，而不是随意单独触发
- 输出对后续 AI 编码工具真正有用的结构化结果，而不是华丽但不可执行的空话
- 用本地验证脚本和真实样例，证明这一套链路至少能稳定产出一份完整包

## Included Skills

| Skill | Role |
| --- | --- |
| `gameplay-design-orchestrator` | 上游总控。负责锁定方向、串行驱动下游 stage、合并为单一 Gameplay Design Package。 |
| `gameplay-input-normalizer` | 把原始想法转为约束、玩家场景、平台边界、情绪目标和 production pressure。 |
| `gameplay-fantasy-loop-designer` | 锁定玩家承诺、身份幻想、核心动作与 micro/mid/long loop。 |
| `gameplay-pacing-and-structure` | 锁定 5 秒到 15 分钟的时间层节奏、开场脚本、回放驱动和疲劳风险。 |
| `gameplay-world-and-narrative-weaver` | 在不破坏玩法主干的前提下，为 loop 包装世界规则、冲突和 act 结构。 |
| `gameplay-system-weaver-and-scope-cutter` | 做系统网络、资源流、MVP 保留与 cut list，强制 scope 管理。 |
| `gameplay-coding-handoff-compiler` | 将已锁定的玩法包编译成 scene/UI/object/state/variables/event 级别的编码交接结构。 |
| `game-design-spec` | 将成熟玩法包扩展为完整中文游戏规格书、配置、QA 与实施任务包。 |

完整目录说明见 [docs/skill-catalog.md](docs/skill-catalog.md)。

## Pipeline

```text
Raw idea
  -> gameplay-design-orchestrator
    -> gameplay-input-normalizer
    -> gameplay-fantasy-loop-designer
    -> gameplay-pacing-and-structure
    -> gameplay-world-and-narrative-weaver
    -> gameplay-system-weaver-and-scope-cutter
    -> gameplay-coding-handoff-compiler
  -> Gameplay Design Package
  -> game-design-spec
  -> Full Chinese Game Design Spec
```

关键约束：

- `gameplay-design-orchestrator` 是唯一正常上游入口
- 一旦进入正式链路，下游 6 个 gameplay stage 必须按顺序执行
- 只有在已经存在 orchestrator 包且明确要求单 stage 修订时，才允许局部回修
- `game-design-spec` 不是 brainstorm 工具，而是下游展开器

## What Makes This Suite Stronger

- Orchestrator-first: 防止下游 stage 被误当成“任意可单点调用”的自由技能
- Scope discipline: 强制 MVP keep/cut，避免设计一开始就爆炸
- Chinese production output: 下游规格书面向中文执行环境，适合直接给 AI 编码代理或协作团队继续拆解
- Validation included: 自带校验脚本和真实样例，而不是只给文档不验证
- Commercial positioning ready: 仓库说明、样例、营销文案与展示资源已预留，适合继续包装为产品化资产

## Real Example

本仓库附带一个真实链路样例：网页端陀螺对战游戏。

- 索引：[`examples/gyro-battle/00-direct-output-index.md`](examples/gyro-battle/00-direct-output-index.md)
- Gameplay package：[`examples/gyro-battle/final-package/`](examples/gyro-battle/final-package/)
- Full spec：[`examples/gyro-battle/final-spec/`](examples/gyro-battle/final-spec/)

这个样例不是“宣传文案示意”，而是本地跑过校验脚本的完整产物。

## Install Into Codex

1. 确认当前活跃的 `CODEX_HOME`
2. 将本仓库里的 `skills/` 目录复制到目标运行时的 `skills/` 下
3. 重启 Codex 会话，确认技能已出现在可用 skill 列表中

如果你的机器同时存在 `~/.codex` 与 `~/.codex-proxy`，请优先安装到当前真实运行路径，而不是机械地假设只存在一个 Codex home。

## Validate The Included Example

PowerShell:

```powershell
.\scripts\validate-release.ps1
```

或分别执行：

```powershell
python .\skills\gameplay-design-orchestrator\scripts\validate_gameplay_package.py --package-dir .\examples\gyro-battle\final-package
python .\skills\game-design-spec\scripts\validate_spec.py --task-dir .\examples\gyro-battle\final-spec
```

## Commercial Note

这个仓库当前采用“公开展示、默认保留商业权利”的发布姿态，而不是直接承诺开源许可。

- 适合展示方法论、样例和能力边界
- 适合后续继续做咨询、定制、企业内训或商业授权
- 如果你计划开放更宽松的再利用权限，请在商业模式和授权边界明确后再替换许可证策略

当前说明见 [LICENSE](LICENSE) 与 [docs/github-launch-kit.md](docs/github-launch-kit.md)。

## Repo Layout

```text
skills/      Core skill suite
examples/    Validated output sample
docs/        Catalog, GitHub launch copy, release notes
assets/      README visual assets
scripts/     Local validation helpers
```

## Recommended Uses

- 给 Codex 增加一条更稳的游戏设计上游链路
- 做 AI 驱动的网页游戏、轻中度原型或玩法提案
- 在产品化之前快速验证玩法结构是否成立
- 给团队统一“先锁玩法主干，再扩规格书”的工作流

## Release Status

- Current version: `v0.1.0`
- Validation status: included example passes local validators
- Positioning: source-available showcase and commercializable capability package


# Gameplay Design Skill Suite

<p align="center">
  <img src="assets/hero-anime-banner.svg" alt="Gameplay Design Skill Suite hero banner" width="100%" />
</p>

<p align="center">
  <strong>一套面向 Codex 的 orchestrator-first 游戏设计技能体系，用来把模糊游戏想法压缩成已校验的玩法设计包，再扩展为可执行的中文游戏规格书。</strong>
</p>

<p align="center">
  <a href="README.md">English</a>
  ·
  <a href="docs/faq.md">FAQ</a>
  ·
  <a href="docs/licensing-and-packaging.md">授权说明</a>
  ·
  <a href="docs/pricing-and-commercial-offers.md">商业化与定价</a>
  ·
  <a href="docs/release-notes-v0.1.0.md">Release 文案</a>
</p>

## 这是什么

这不是 8 个平级 prompt，也不是一堆随便拼起来的策划模板。

它的核心原则只有一个：

`gameplay-design-orchestrator` 是唯一正常上游入口。

这套 skill 的目标不是“让 AI 帮你想点玩法”，而是：

- 先锁方向，再扩设计
- 让中间 `gameplay-*` stages 按顺序执行
- 在范围失控前强制做 MVP keep/cut
- 把输出组织成下游 AI 编码工具能继续消费的结构
- 在需要时继续展开成完整中文策划案和任务包

## 为什么它和普通 prompt 包不同

大多数公开游戏设计提示词包有几个常见问题：

| 常见问题 | 这套 skill 的处理方式 |
| --- | --- |
| 一上来堆世界观、题材和系统名词 | 先锁玩家承诺、玩法方向和约束 |
| 把每个 prompt 都当成独立入口 | 把下游 6 个 gameplay stages 收束为 orchestrator 控制链 |
| 输出看起来热闹，但无法执行 | 输出玩法包、索引表、状态、规则、规格书结构 |
| 没有校验 | 自带本地校验器和真实样例 |
| 设计很快炸范围 | 在 handoff 前强制 keep/cut 和 scope discipline |

## 包含哪些技能

| Skill | 作用 |
| --- | --- |
| `gameplay-design-orchestrator` | 上游总控，负责方向锁定、阶段调度和 Gameplay Design Package 组装 |
| `gameplay-input-normalizer` | 把原始输入转为玩家场景、平台边界、情绪目标和 production pressure |
| `gameplay-fantasy-loop-designer` | 锁定玩家承诺、身份幻想、核心动作和循环结构 |
| `gameplay-pacing-and-structure` | 锁定时间层节奏、开场高光、挫败点和复玩牵引 |
| `gameplay-world-and-narrative-weaver` | 在不破坏玩法主干的前提下增加世界规则和叙事压力 |
| `gameplay-system-weaver-and-scope-cutter` | 建系统网、资源流、MVP 保留项和 cut list |
| `gameplay-coding-handoff-compiler` | 输出 scene、UI、object、state、variables 和 prototype acceptance |
| `game-design-spec` | 将成熟玩法包扩展为完整中文游戏规格书与任务包 |

详细拓扑见 [docs/skill-catalog.md](docs/skill-catalog.md)。

## 工作流拓扑

```text
Raw game idea
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

几个关键约束：

- 不要把 6 个下游 `gameplay-*` stage skills 当成自由入口
- 一旦进入正式链路，下游 6 个 stages 必须按顺序执行
- 只有在已存在 package 且明确要修某一层时，才允许做 stage 级别回修

## 仓库里附带了真实样例

本仓库附带了一个网页端陀螺对战样例：

- 索引：[examples/gyro-battle/00-direct-output-index.md](examples/gyro-battle/00-direct-output-index.md)
- 上游玩法包：[examples/gyro-battle/final-package/](examples/gyro-battle/final-package/)
- 下游完整规格：[examples/gyro-battle/final-spec/](examples/gyro-battle/final-spec/)
- 案例拆解：[docs/gyro-battle-case-study.md](docs/gyro-battle-case-study.md)

这个样例包含：

- 两条候选方向之间的取舍
- 来自节奏层和 scope 层的 loop-back 修正
- 带假设清单、系统主索引、公式索引和原型验收的玩法包
- 带 UI、关卡、平衡、配置、音画、QA、交付任务的完整规格

它不是演示文案，而是已通过校验脚本的真实产物。

## 视觉预览

<p align="center">
  <img src="assets/promo-preview.svg" alt="仓库内宣传页预览图" width="100%" />
</p>

仓库根目录还附带了一套可直接部署到 Vercel 的静态宣传页：

- [index.html](index.html)
- [styles.css](styles.css)
- [script.js](script.js)
- [vercel.json](vercel.json)

## 适合谁用

- 想用 AI 更快做网页游戏或轻中度原型的人
- 希望把游戏设计前置流程标准化的小团队
- 需要 Codex 帮忙把想法压成结构的独立开发者
- 想把内部方法论产品化的顾问或工作室
- 需要快速验证玩法主干是否成立的策划负责人

## 当前商业化姿态

这个仓库现在采用的是：

- `public` 展示
- 默认保留商业权利
- 商业使用、内部分发、白标和定制化需要单独授权

详见：

- [docs/licensing-and-packaging.md](docs/licensing-and-packaging.md)
- [docs/pricing-and-commercial-offers.md](docs/pricing-and-commercial-offers.md)

## 和其他方案对比

| 方案 | 优点 | 弱点 |
| --- | --- | --- |
| 普通 prompt 包 | 上手快 | 结构弱、边界弱、容易炸范围 |
| 单个 mega-prompt | 试验快 | 可修订性差，很难知道哪一层出了问题 |
| 这套 orchestrator-first 技能链 | 结构清楚、可拆回路、可接下游 | 需要遵守流程，不适合乱序随意调用 |

## 安装方式

1. 先确认当前活跃的 `CODEX_HOME`
2. 将本仓库的 `skills/` 复制到对应运行时的 `skills/`
3. 重启 Codex 会话并确认技能已经出现在列表中

如果你的机器同时存在 `~/.codex` 和 `~/.codex-proxy`，优先装到真实活跃的运行路径。

## 校验方式

PowerShell：

```powershell
.\scripts\validate-release.ps1
```

或分别执行：

```powershell
python .\skills\gameplay-design-orchestrator\scripts\validate_gameplay_package.py --package-dir .\examples\gyro-battle\final-package
python .\skills\game-design-spec\scripts\validate_spec.py --task-dir .\examples\gyro-battle\final-spec
```

## 目录结构

```text
skills/      核心技能
examples/    已校验样例
docs/        FAQ、授权、定价、发布文案
assets/      README 和宣传页资源
scripts/     校验脚本
```

## 建议继续阅读

- [README.md](README.md)
- [docs/faq.md](docs/faq.md)
- [docs/gyro-battle-case-study.md](docs/gyro-battle-case-study.md)
- [docs/licensing-and-packaging.md](docs/licensing-and-packaging.md)
- [docs/pricing-and-commercial-offers.md](docs/pricing-and-commercial-offers.md)
- [docs/release-notes-v0.1.0.md](docs/release-notes-v0.1.0.md)

## 当前状态

- 版本：`v0.1.0`
- 仓库状态：已公开
- 验证状态：自带样例通过本地校验
- 商业姿态：公开展示 + 商业授权通道

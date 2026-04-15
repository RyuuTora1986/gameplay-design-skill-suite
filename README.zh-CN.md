# Gameplay Design Skill Suite

<p align="center">
  <img src="assets/hero-anime-banner.svg" alt="Gameplay Design Skill Suite hero banner" width="100%" />
</p>

<p align="center">
  <strong>一套面向 Codex 的 orchestrator-first 游戏设计技能体系，用来把原始游戏想法整理为经过验证的玩法设计包、中文生产级游戏规格书、execution plan，以及可交给 worker 执行的 dispatch 与 runner 协调层。</strong>
</p>

<p align="center">
  <a href="README.md">English</a>
  路
  <a href="docs/faq.md">FAQ</a>
  路
  <a href="docs/licensing-and-packaging.md">授权说明</a>
  路
  <a href="docs/pricing-and-commercial-offers.md">商业化与定价</a>
  路
  <a href="docs/release-notes-v0.4.0.md">Release Notes</a>
</p>

## 这是什么

这个仓库不是一组松散的 prompt，也不是一堆需要手动拼接的模板。

它围绕一条核心规则构建：

`gameplay-design-orchestrator` 是唯一正常的上游入口。

这套技能的目标是把原始游戏想法有顺序地推进为可继续执行的产物：

- 先锁定方向，再展开玩法
- 按阶段顺序推进设计链路
- 在规格展开前做范围控制与 MVP keep/cut
- 输出可复用的 Gameplay Design Package
- 在需要时展开为完整中文游戏设计规格书
- 继续编译为 agent 可执行的 execution plan
- 通过 runner、dispatch、ack、review gate 和 worker adapter 接入执行层

它解决的不是“灵感更多”，而是“从模糊概念到结构化执行”的链路问题。

## 这个仓库的差异点

| 常见问题 | 这套技能的处理方式 |
| --- | --- |
| 一开始就堆题材、设定、机制名词 | 先锁方向、玩家承诺和约束 |
| 每个 prompt 各自独立 | 由 orchestrator 驱动有顺序的下游阶段 |
| 文案好看但不能继续执行 | 输出玩法包、规格书、execution plan 和执行协调层 |
| 没有验证 | 附带本地验证器和真实样例 |
| 范围容易失控 | 在下游 handoff 前明确 keep / later / cut |

## 包含哪些技能

| Skill | 作用 |
| --- | --- |
| `gameplay-design-orchestrator` | 上游总控，负责方向锁定、阶段调度和 Gameplay Design Package 组装 |
| `gameplay-input-normalizer` | 把原始输入转成稳定约束、目标玩家、平台边界和情绪目标 |
| `gameplay-fantasy-loop-designer` | 定义玩家承诺、身份幻想、核心动作和循环结构 |
| `gameplay-pacing-and-structure` | 设计时间层节奏、前期高光、挫败点和重复游玩动力 |
| `gameplay-world-and-narrative-weaver` | 用世界规则、冲突和叙事压力包装玩法主干 |
| `gameplay-system-weaver-and-scope-cutter` | 规划系统结构、资源流、MVP keep/cut 和制作风险 |
| `gameplay-coding-handoff-compiler` | 把玩法包编译成场景、UI、对象、状态、变量和原型验收 |
| `game-design-spec` | 把成熟玩法包展开为完整中文游戏设计规格书与任务包 |
| `game-design-execution-compiler` | 把成熟 spec 编译成 `execution-plan.json` 和 `execution-plan.md` |
| `game-design-execution-runner` | 读取 execution plan、持久化 run state、输出 handoff 或 dispatch 包，跟踪 `dispatch -> ack -> complete`，执行 dispatch 级 review gate，并暴露 worker adapter 接口 |

详见 [docs/skill-catalog.md](docs/skill-catalog.md)。

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
  -> game-design-execution-compiler
  -> execution-plan.json + execution-plan.md
  -> game-design-execution-runner
  -> execution-run-state.json + worker handoff / dispatch packet
```

关键约束：

- 不要把 6 个下游 `gameplay-*` stage skills 当成自由入口
- 一旦进入正式链路，下游阶段默认必须按顺序执行
- 只有在已经存在 package 且用户明确要求修某一层时，才建议单层返工

## 仓库内附带真实样例

仓库内附带了一个完整验证过的 `gyro-battle` 网页游戏样例：

- 索引：[examples/gyro-battle/00-direct-output-index.md](examples/gyro-battle/00-direct-output-index.md)
- 上游玩法包：[examples/gyro-battle/final-package/](examples/gyro-battle/final-package/)
- 下游完整规格：[examples/gyro-battle/final-spec/](examples/gyro-battle/final-spec/)
- 执行计划：[examples/gyro-battle/final-execution-plan/](examples/gyro-battle/final-execution-plan/)
- 案例拆解：[docs/gyro-battle-case-study.md](docs/gyro-battle-case-study.md)

这个样例包括：

- 两条候选方向之间的取舍
- 来自节奏层和 scope 层的 loop-back 修正
- 带假设清单、系统索引、公式和原型验收的玩法包
- 包含 UI、平衡、配置、音频、QA 和交付映射的完整规格
- 一个绑定 source refs 与 canonical IDs 的 execution plan
- 一条可初始化状态、产出 dispatch 包、确认 worker 接单并按依赖顺序推进的 runner 路径

这是一份完整验证样例，不只是展示页内容。

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
- 需要更快验证玩法主干是否成立的设计负责人

## 当前商业定位

这个仓库的定位是：

- 对外公开展示
- 默认保留商业权利
- 商业使用、内部扩散、白标和定制化需要单独授权

详见：

- [docs/licensing-and-packaging.md](docs/licensing-and-packaging.md)
- [docs/pricing-and-commercial-offers.md](docs/pricing-and-commercial-offers.md)

## 和其他方案对比

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| 通用 prompt 包 | 上手快 | 结构弱、边界弱、容易失控 |
| 单个 mega-prompt | 试验快 | 难以修订，难以判断哪一层出了问题 |
| 这套 orchestrator-first 技能链 | 从设计一路压到执行，结构清楚，可验证，可继续接手 | 需要遵守流程，最适合按设计方式使用 |

## 安装方式

1. 先确认当前活跃的 `CODEX_HOME`
2. 将本仓库的 `skills/` 复制到对应运行时的 `skills/`
3. 重启 Codex 会话并确认技能已经出现在列表中

如果你的机器同时存在 `~/.codex` 和 `~/.codex-proxy`，优先安装到真实活跃的运行路径。

## 校验方式

PowerShell：

```powershell
.\scripts\validate-release.ps1
```

或分别执行：

```powershell
python .\skills\gameplay-design-orchestrator\scripts\validate_gameplay_package.py --package-dir .\examples\gyro-battle\final-package
python .\skills\game-design-spec\scripts\validate_spec.py --task-dir .\examples\gyro-battle\final-spec
python .\skills\game-design-execution-compiler\scripts\validate_execution_plan.py --plan-dir .\examples\gyro-battle\final-execution-plan
python .\skills\game-design-execution-runner\scripts\run_execution_plan.py init --plan-dir .\tmp-runner-validation --repo-root . --branch main
```

## 目录结构

```text
skills/      核心技能体系
examples/    已验证样例输出，包含 execution plan
docs/        FAQ、授权、定价、发布说明与收尾文档
assets/      README 与宣传页资源
scripts/     校验脚本
```

## 建议继续阅读

- [README.md](README.md)
- [docs/faq.md](docs/faq.md)
- [docs/gyro-battle-case-study.md](docs/gyro-battle-case-study.md)
- [docs/licensing-and-packaging.md](docs/licensing-and-packaging.md)
- [docs/pricing-and-commercial-offers.md](docs/pricing-and-commercial-offers.md)
- [docs/release-notes-v0.4.0.md](docs/release-notes-v0.4.0.md)
- [docs/project-closeout-2026-04-15.md](docs/project-closeout-2026-04-15.md)

## 当前状态

- 版本：`v0.4.0`
- 仓库状态：已公开
- 验证状态：玩法包、规格书、execution plan，以及带 dispatch review gate 和 worker adapter 校验的 runner smoke path 均可通过本地检查
- 商业姿态：公开展示 + 商业授权通道

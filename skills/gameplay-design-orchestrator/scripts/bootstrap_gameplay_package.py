from __future__ import annotations

import argparse
from pathlib import Path


PACKAGE_TEMPLATE = """## 0. 假设清单

- 假设 1：
- 假设 2：

## 0.5 方向锁定结果

- 入围方向数量：
- 选中方向名称：
- 选中理由：
- 舍弃方向摘要：

## 1. 游戏一句话

- 玩家是谁：
- 反复做什么：
- 得到什么快感：

## 2. 玩家承诺

- 身份幻想：
- 情绪承诺：
- 差异化卖点：

## 3. 核心玩法

- 核心动作：
- 单轮流程：
- 核心反馈：
- 失败条件：
- 成功条件：

## 4. 节奏设计

- 前 2 分钟：
- 前 10 分钟：
- 中段：
- 后段：
- 疲劳风险：

## 5. 世界观与叙事流程

- 世界一句话：
- 玩家身份一句话：
- 核心冲突一句话：

### 5 幕结构
| 幕 | 叙事目标 | 新增压力或目标 | 玩法变化 |
|---|---|---|---|
| 第一幕 |  |  |  |

## 6. 系统网
### 系统主索引表

| 系统ID | 系统名 | 一句话定位 | 玩家目标 | 核心输入 | 核心输出 | 依赖系统 |
|---|---|---|---|---|---|---|
| SYS-01 |  |  |  |  |  | 无 |

### 资源主索引表

| 资源ID | 资源名 | 类型 | 主要来源系统ID | 主要去向系统ID | 是否稀缺 |
|---|---|---|---|---|---|
| RES-01 |  |  | SYS-01 | SYS-01 | 否 |

### 公式主索引表

| 公式ID | 公式名 | 所属系统ID | 输入变量 | 输出结果 | 对应章节 |
|---|---|---|---|---|---|
| FML-01 |  | SYS-01 | VAR-01 |  | 8 |

### 配置表主索引表
| 表ID | 表名 | 所属系统ID | 主键 | 主要用途 | 热更支持 |
|---|---|---|---|---|---|
| CFG-01 |  | SYS-01 |  |  | 是 |

### 变量主索引表

| 变量ID | 变量名 | 所属公式ID | 单位 | 主要来源 | 主要去向 |
|---|---|---|---|---|---|
| VAR-01 |  | FML-01 |  | 常量 | FML-01 |

## 7. 规模与实现边界

- 必做：
- 可后做：
- 首版砍掉：
- 美术占位方案：
- 程序复杂点：

## 8. 原型执行翻译

- 场景列表：
- UI 列表：
- 对象列表：
- 状态机：
- 关键变量：
- 交互事件列表：

### 原型验收

| 项目 | 目标 |
|---|---|
| 10 秒正反馈 |  |
| 单局时长目标 |  |
| 核心循环闭环 |  |
| 无教学文本首轮可完成 |  |
| 失败/成功状态明确 |  |

## 9. 风险评审

| 风险类型 | 风险描述 | 触发阈值 | 应对动作 |
|---|---|---|---|
| 乐趣风险 |  |  |  |

## 10. 对接下游策划案

- 传递给 `$game-design-spec` 的主输入：
- 需要保留的系统ID：
- 需要保留的资源ID：
- 需要保留的公式ID：
- 需要保留的配置表ID：
- 需要保留的变量ID：

## 10.5 资产生成假设

- 风格锚点摘要：
- 资产流水线假设：
- 生成交接假设：
"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Gameplay Design Package skeleton.")
    parser.add_argument("--game-name", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    write_text(outdir / "01-gameplay-design-package.md", f"# 项目\n\n- 游戏名：{args.game_name}\n\n{PACKAGE_TEMPLATE}")
    write_text(
        outdir / "02-review-notes.md",
        "# Review Notes\n\n## Candidate Directions\n\n| 方向名 | 玩家身份 | 重复动作 | 最强感受 | 范围压力 | 舍弃原因 |\n|---|---|---|---|---|---|\n| A |  |  |  |  |  |\n| B |  |  |  |  |  |\n\n## Final Choice\n\n- chosen direction:\n- strongest promise:\n- biggest scope risk:\n- cut-first target:\n\n## Major Revisions\n\n| revision_id | triggering_stage | what_failed | changed_decision | why_stronger_now | downstream_implications |\n|---|---|---|---|---|---|\n| REV-01 |  |  |  |  |  |\n\n## Loop-back Summary\n\n- loop-back count:\n- highest-cost revision:\n- still-open fragility:\n",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

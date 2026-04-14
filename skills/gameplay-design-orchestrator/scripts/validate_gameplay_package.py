from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_MARKERS = [
    "## 0. 假设清单",
    "## 0.5 方向锁定结果",
    "## 1. 游戏一句话",
    "## 2. 玩家承诺",
    "## 3. 核心玩法",
    "## 4. 节奏设计",
    "## 5. 世界观与叙事流程",
    "## 6. 系统网",
    "系统主索引表",
    "资源主索引表",
    "公式主索引表",
    "配置表主索引表",
    "变量主索引表",
    "## 7. 规模与实现边界",
    "## 8. 原型执行翻译",
    "## 9. 风险评审",
    "## 10. 对接下游策划案",
    "## 10.5 资产生成假设",
]

BANNED_MARKERS = ["TODO", "TBD", "示例", "例子", "待定", "看情况", "视情况而定"]

HANDOFF_MARKERS = [
    "传递给 `$game-design-spec` 的主输入",
    "需要保留的系统ID",
    "需要保留的资源ID",
    "需要保留的公式ID",
    "需要保留的配置表ID",
    "需要保留的变量ID",
]

ASSET_GENERATION_MARKERS = [
    "风格锚点摘要",
    "资产流水线假设",
    "生成交接假设",
]

REVIEW_NOTE_MARKERS = [
    "## Candidate Directions",
    "## Final Choice",
    "## Major Revisions",
    "## Loop-back Summary",
    "chosen direction:",
    "strongest promise:",
    "biggest scope risk:",
    "cut-first target:",
    "revision_id",
    "triggering_stage",
    "what_failed",
    "changed_decision",
    "why_stronger_now",
    "downstream_implications",
    "loop-back count:",
    "highest-cost revision:",
    "still-open fragility:",
]


def validate_single_markdown(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            errors.append(f"Missing required marker: {marker}")

    for marker in BANNED_MARKERS:
        if marker in text:
            errors.append(f"Found banned shortcut: {marker}")

    id_prefixes = ["SYS-", "RES-", "FML-", "CFG-", "VAR-"]
    for object_prefix in id_prefixes:
        if object_prefix not in text:
            warnings.append(f"No {object_prefix} IDs detected.")

    for marker in HANDOFF_MARKERS:
        if marker not in text:
            errors.append(f"Missing handoff marker: {marker}")

    for marker in ASSET_GENERATION_MARKERS:
        if marker not in text:
            errors.append(f"Missing asset-generation marker: {marker}")

    counts = {prefix: len(re.findall(rf"{prefix}\d+", text)) for prefix in id_prefixes}
    if counts["SYS-"] == 0:
        errors.append("No canonical system IDs found.")
    if counts["FML-"] == 0:
        warnings.append("No canonical formula IDs found.")
    if counts["CFG-"] == 0:
        warnings.append("No canonical config IDs found.")

    if "|---|---|" not in text and "| --- | --- |" not in text:
        warnings.append("No markdown table detected.")

    if errors:
        print("VALIDATION FAILED")
        for item in errors:
            print(f"- ERROR: {item}")
        for item in warnings:
            print(f"- WARN: {item}")
        return 1

    print("VALIDATION PASSED")
    for item in warnings:
        print(f"- WARN: {item}")
    return 0


def validate_package_dir(package_dir: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    package_path = package_dir / "01-gameplay-design-package.md"
    review_path = package_dir / "02-review-notes.md"

    if not package_path.exists():
        print("VALIDATION FAILED")
        print("- ERROR: Missing 01-gameplay-design-package.md.")
        return 1
    if not review_path.exists():
        print("VALIDATION FAILED")
        print("- ERROR: Missing 02-review-notes.md.")
        return 1

    package_text = package_path.read_text(encoding="utf-8")
    review_text = review_path.read_text(encoding="utf-8")

    for marker in REVIEW_NOTE_MARKERS:
        if marker not in review_text:
            errors.append(f"Review notes missing marker: {marker}")

    for marker in ASSET_GENERATION_MARKERS:
        if marker not in package_text:
            errors.append(f"Gameplay package missing asset-generation marker: {marker}")

    package_system_ids = set(re.findall(r"SYS-\d+", package_text))
    review_system_ids = set(re.findall(r"SYS-\d+", review_text))
    if review_system_ids - package_system_ids:
        warnings.append("Review notes contain system IDs not present in the final package.")

    if "选中方向名称：" not in package_text:
        errors.append("Gameplay package missing chosen direction field.")
    if "chosen direction:" not in review_text:
        errors.append("Review notes missing chosen direction summary.")
    if "REV-" in review_text and "triggering_stage" not in review_text:
        errors.append("Review notes include revision IDs without the structured revision table.")

    if errors:
        print("VALIDATION FAILED")
        for item in errors:
            print(f"- ERROR: {item}")
        for item in warnings:
            print(f"- WARN: {item}")
        return 1

    print("VALIDATION PASSED")
    for item in warnings:
        print(f"- WARN: {item}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Gameplay Design Package markdown file.")
    parser.add_argument("path", nargs="?")
    parser.add_argument("--package-dir", dest="package_dir")
    args = parser.parse_args()

    if args.package_dir:
        return validate_package_dir(Path(args.package_dir))
    if not args.path:
        parser.error("Provide either a markdown path or --package-dir.")
    return validate_single_markdown(Path(args.path))


if __name__ == "__main__":
    raise SystemExit(main())

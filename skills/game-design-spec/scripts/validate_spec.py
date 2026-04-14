from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_HEADINGS = [
    "# 1. 游戏概述",
    "# 2. 系统框架设计",
    "# 3. 分系统规则",
    "## 版本号与日期",
    "## 变更清单（新增/修改/移除）",
    "## 与上一版的差异对比",
    "## 自检结论",
]

REQUIRED_SUBSTRINGS = [
    "## 假设清单",
    "系统主索引表",
    "系统ID",
    "资源主索引表",
    "资源ID",
    "公式主索引表",
    "公式ID",
    "配置表主索引表",
    "表ID",
    "变量主索引表",
    "变量ID",
    "## 1.1 题材与美术风格",
    "## 1.2 游戏名",
    "## 1.3 游戏类型",
    "## 1.4 平台",
    "## 1.5 核心玩法概述",
    "### 一句话卖点",
    "### 核心游戏循环",
    "### 基础循环",
    "### 扩展循环",
    "### 长期循环",
    "### 玩家成长路径",
    "### 失败与复盘机制",
    "## 2.1 系统总览",
    "## 2.2 系统间关联与依赖",
    "## 3.2 可重复游玩设计",
    "规则ID",
    "状态机",
]

BANNED_MARKERS = [
    "TODO",
    "TBD",
    "同上",
    "待定",
    "----需要填写游戏设计要点----",
]

TASK_REQUIRED_MARKERS = [
    "# 前置内容",
    "覆盖系统ID",
    "## 输出要求",
    "## 正文",
]

TASK_FILE_TOKENS = ["ui-task", "level-task", "balance-task", "config-task", "art-task", "audio-task", "qa-task", "delivery-task"]

TASK_TYPE_REQUIRED_MARKERS = {
    "ui-task": ["风格锚点", "资产流水线", "UI验收"],
    "art-task": ["风格锚点", "资产流水线", "资产验收"],
    "audio-task": ["音频锚点", "音频验收"],
    "qa-task": ["QA覆盖回指表"],
    "delivery-task": ["实施任务回指表"],
}

TASK_TYPE_WARNING_MARKERS = {
    "ui-task": ["生成交接"],
    "art-task": ["生成交接"],
    "audio-task": ["生成交接"],
    "delivery-task": ["生成工具", "拒收条件"],
}


def find_ids(text: str, prefix: str) -> list[str]:
    return re.findall(rf"{prefix}\d+", text)


def extract_registry_ids(text: str, heading: str, prefix: str) -> list[str]:
    ids: list[str] = []
    in_block = False
    for line in text.splitlines():
        stripped = line.strip()
        if heading in stripped:
            in_block = True
            continue
        if in_block and stripped.startswith("#"):
            break
        if in_block and "|" in stripped:
            ids.extend(find_ids(stripped, prefix))
    return ids


def extract_index_rows(text: str, heading: str) -> list[list[str]]:
    rows: list[list[str]] = []
    in_block = False
    for line in text.splitlines():
        stripped = line.strip()
        if heading in stripped:
            in_block = True
            continue
        if in_block and stripped.startswith("#"):
            break
        if not in_block or "|" not in stripped:
            continue
        cells = [cell.strip() for cell in stripped.split("|")[1:-1]]
        if not cells:
            continue
        joined = "".join(cells)
        if not joined or set(joined) <= {"-"}:
            continue
        rows.append(cells)
    return rows


def extract_assumption_lines(text: str) -> list[str]:
    lines: list[str] = []
    in_block = False
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("## ") and "假设清单" in stripped:
            in_block = True
            continue
        if in_block and stripped.startswith("#"):
            break
        if in_block and stripped.startswith("-"):
            lines.append(stripped)
    return lines


def build_assumption_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    assumption_lines = extract_assumption_lines(text)
    if not assumption_lines:
        return warnings

    pseudo_markers = [
        "假设本项目需要UI",
        "假设需要UI",
        "假设本项目需要数值",
        "假设需要数值",
        "假设本项目需要美术",
        "假设需要美术",
        "假设本项目需要音频",
        "假设需要音频",
        "假设本项目是一个游戏",
    ]

    if any(marker in line for line in assumption_lines for marker in pseudo_markers):
        warnings.append("Assumption block contains likely pseudo-assumptions that should be derived directly.")

    if len(assumption_lines) > 8:
        warnings.append("Assumption block is long; verify that these are truly missing inputs rather than derivable facts.")

    return warnings


def validate_single_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    is_task_doc = any(token in path.name for token in TASK_FILE_TOKENS)

    if is_task_doc:
        for marker in TASK_REQUIRED_MARKERS:
            if marker not in text:
                errors.append(f"Missing required task marker: {marker}")
        for token, markers in TASK_TYPE_REQUIRED_MARKERS.items():
            if token in path.name:
                for marker in markers:
                    if marker not in text:
                        errors.append(f"Missing required {token} marker: {marker}")
        for token, markers in TASK_TYPE_WARNING_MARKERS.items():
            if token in path.name:
                if not any(marker in text for marker in markers):
                    warnings.append(f"{path.name}: missing recommended generator handoff markers {markers}.")
        if "SYS-" not in text:
            warnings.append("No explicit system IDs detected.")
        warnings.extend(build_assumption_warnings(text))
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

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"Missing required heading: {heading}")
    for marker in REQUIRED_SUBSTRINGS:
        if marker not in text:
            errors.append(f"Missing required section marker: {marker}")
    for marker in BANNED_MARKERS:
        if marker in text:
            errors.append(f"Found forbidden placeholder or shortcut: {marker}")

    if "|---|---|" not in text and "| --- | --- |" not in text:
        warnings.append("No markdown table detected.")
    if "```mermaid" not in text:
        warnings.append("No Mermaid block detected.")
    if "边界条件" not in text and "异常" not in text:
        warnings.append("Boundary-condition wording not detected.")
    if "反滥用" not in text and "防刷" not in text:
        warnings.append("Anti-abuse wording not detected.")

    system_ids = find_ids(text, "SYS-")
    if not system_ids:
        warnings.append("No explicit system IDs detected.")
    warnings.extend(build_assumption_warnings(text))

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


def validate_task_dir(task_dir: Path) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    master_path = task_dir / "01-master-spec.md"
    if not master_path.exists():
        print("VALIDATION FAILED")
        print("- ERROR: Missing 01-master-spec.md in task directory.")
        return 1

    master_text = master_path.read_text(encoding="utf-8")

    master_system_ids = sorted(set(extract_registry_ids(master_text, "系统主索引表", "SYS-")))
    master_resource_ids = sorted(set(extract_registry_ids(master_text, "资源主索引表", "RES-")))
    master_formula_ids = sorted(set(extract_registry_ids(master_text, "公式主索引表", "FML-")))
    master_config_ids = sorted(set(extract_registry_ids(master_text, "配置表主索引表", "CFG-")))
    master_variable_ids = sorted(set(extract_registry_ids(master_text, "变量主索引表", "VAR-")))

    if not master_system_ids:
        errors.append("Master spec contains no indexed system IDs.")

    resource_rows = extract_index_rows(master_text, "资源主索引表")
    for row in resource_rows[1:]:
        if len(row) < 6:
            continue
        resource_id, _, _, source_system, sink_system, scarce = row[:6]
        if not resource_id.startswith("RES-"):
            continue
        if source_system and source_system != "无" and source_system not in master_system_ids:
            errors.append(f"Master spec: resource {resource_id} has non-indexed source system {source_system}.")
        if sink_system and sink_system != "无" and sink_system not in master_system_ids:
            errors.append(f"Master spec: resource {resource_id} has non-indexed sink system {sink_system}.")
        if not source_system and not sink_system:
            warnings.append(f"Master spec: resource {resource_id} has neither source nor sink.")
        if scarce == "是" and (not source_system or not sink_system):
            warnings.append(f"Master spec: scarce resource {resource_id} should declare both source and sink.")

    formulas_with_variables: set[str] = set()
    variable_rows = extract_index_rows(master_text, "变量主索引表")
    for row in variable_rows[1:]:
        if len(row) < 6:
            continue
        variable_id, _, formula_id, _, source_ref, sink_ref = row[:6]
        if not variable_id.startswith("VAR-"):
            continue
        if formula_id and formula_id not in master_formula_ids:
            errors.append(f"Master spec: variable {variable_id} references non-indexed formula {formula_id}.")
        if formula_id in master_formula_ids:
            formulas_with_variables.add(formula_id)
        if source_ref.startswith("RES-") and source_ref not in master_resource_ids:
            errors.append(f"Master spec: variable {variable_id} references non-indexed source resource {source_ref}.")
        if source_ref.startswith("CFG-") and source_ref not in master_config_ids:
            errors.append(f"Master spec: variable {variable_id} references non-indexed source config {source_ref}.")
        if sink_ref.startswith("RES-") and sink_ref not in master_resource_ids:
            errors.append(f"Master spec: variable {variable_id} references non-indexed sink resource {sink_ref}.")
        if sink_ref.startswith("CFG-") and sink_ref not in master_config_ids:
            errors.append(f"Master spec: variable {variable_id} references non-indexed sink config {sink_ref}.")

    formula_rows = extract_index_rows(master_text, "公式主索引表")
    for row in formula_rows[1:]:
        if len(row) < 6:
            continue
        formula_id, _, system_id, _, _, _ = row[:6]
        if not formula_id.startswith("FML-"):
            continue
        if system_id and system_id not in master_system_ids:
            errors.append(f"Master spec: formula {formula_id} references non-indexed system {system_id}.")
        if formula_id not in formulas_with_variables:
            warnings.append(f"Master spec: formula {formula_id} has no variable linked in variable registry.")

    config_rows = extract_index_rows(master_text, "配置表主索引表")
    for row in config_rows[1:]:
        if len(row) < 6:
            continue
        config_id, _, system_id, _, _, _ = row[:6]
        if not config_id.startswith("CFG-"):
            continue
        if system_id and system_id not in master_system_ids:
            errors.append(f"Master spec: config table {config_id} references non-indexed system {system_id}.")

    task_files = [p for p in task_dir.iterdir() if p.is_file() and any(token in p.name for token in TASK_FILE_TOKENS)]
    covered_systems: set[str] = set()

    for task_file in sorted(task_files):
        text = task_file.read_text(encoding="utf-8")
        if "覆盖系统ID" not in text:
            errors.append(f"{task_file.name}: missing 覆盖系统ID block.")
            continue

        task_system_ids = sorted(set(find_ids(text, "SYS-")))
        task_resource_ids = sorted(set(find_ids(text, "RES-")))
        task_formula_ids = sorted(set(find_ids(text, "FML-")))
        task_config_ids = sorted(set(find_ids(text, "CFG-")))
        task_variable_ids = sorted(set(find_ids(text, "VAR-")))

        if not task_system_ids:
            errors.append(f"{task_file.name}: no system IDs declared.")
            continue

        for token, markers in TASK_TYPE_REQUIRED_MARKERS.items():
            if token in task_file.name:
                for marker in markers:
                    if marker not in text:
                        errors.append(f"{task_file.name}: missing required {token} marker {marker}.")
        for token, markers in TASK_TYPE_WARNING_MARKERS.items():
            if token in task_file.name and not any(marker in text for marker in markers):
                warnings.append(f"{task_file.name}: missing recommended generator handoff markers {markers}.")

        for system_id in task_system_ids:
            if system_id not in master_system_ids:
                errors.append(f"{task_file.name}: references non-indexed system ID {system_id}.")
            else:
                covered_systems.add(system_id)
        for resource_id in task_resource_ids:
            if resource_id not in master_resource_ids:
                errors.append(f"{task_file.name}: references non-indexed resource ID {resource_id}.")
        for formula_id in task_formula_ids:
            if formula_id not in master_formula_ids:
                errors.append(f"{task_file.name}: references non-indexed formula ID {formula_id}.")
        for config_id in task_config_ids:
            if config_id not in master_config_ids:
                errors.append(f"{task_file.name}: references non-indexed config table ID {config_id}.")
        for variable_id in task_variable_ids:
            if variable_id not in master_variable_ids:
                errors.append(f"{task_file.name}: references non-indexed variable ID {variable_id}.")

    for system_id in master_system_ids:
        if system_id not in covered_systems:
            warnings.append(f"Indexed system {system_id} is not covered by any downstream task file.")

    qa_path = task_dir / "10-qa-task.md"
    if qa_path.exists():
        qa_text = qa_path.read_text(encoding="utf-8")
        if "用例ID" not in qa_text:
            warnings.append("10-qa-task.md: missing QA coverage back-reference table.")
        qa_system_ids = set(find_ids(qa_text, "SYS-"))
        qa_formula_ids = set(find_ids(qa_text, "FML-"))
        qa_config_ids = set(find_ids(qa_text, "CFG-"))
        for system_id in master_system_ids:
            if system_id not in qa_system_ids:
                warnings.append(f"10-qa-task.md: indexed system {system_id} is not referenced by QA tasks.")
        for formula_id in master_formula_ids:
            if formula_id not in qa_formula_ids:
                warnings.append(f"10-qa-task.md: formula {formula_id} is not referenced by QA tasks.")
        for config_id in master_config_ids:
            if config_id not in qa_config_ids:
                warnings.append(f"10-qa-task.md: config table {config_id} is not referenced by QA tasks.")
    else:
        warnings.append("Missing 10-qa-task.md in task directory.")

    delivery_path = task_dir / "11-delivery-task.md"
    if delivery_path.exists():
        delivery_text = delivery_path.read_text(encoding="utf-8")
        if "任务ID" not in delivery_text:
            warnings.append("11-delivery-task.md: missing implementation task back-reference table.")
        delivery_system_ids = set(find_ids(delivery_text, "SYS-"))
        delivery_formula_ids = set(find_ids(delivery_text, "FML-"))
        delivery_config_ids = set(find_ids(delivery_text, "CFG-"))
        for system_id in master_system_ids:
            if system_id not in delivery_system_ids:
                warnings.append(f"11-delivery-task.md: indexed system {system_id} is not referenced by implementation tasks.")
        for formula_id in master_formula_ids:
            if formula_id not in delivery_formula_ids:
                warnings.append(f"11-delivery-task.md: formula {formula_id} is not referenced by implementation tasks.")
        for config_id in master_config_ids:
            if config_id not in delivery_config_ids:
                warnings.append(f"11-delivery-task.md: config table {config_id} is not referenced by implementation tasks.")
    else:
        warnings.append("Missing 11-delivery-task.md in task directory.")

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
    parser = argparse.ArgumentParser(description="Validate a game design spec markdown file.")
    parser.add_argument("path", nargs="?", help="Path to the markdown file.")
    parser.add_argument("--task-dir", dest="task_dir", help="Directory containing 01-master-spec.md and downstream task files.")
    args = parser.parse_args()

    if args.task_dir:
        return validate_task_dir(Path(args.task_dir))
    if not args.path:
        parser.error("Provide either a markdown path or --task-dir.")
    return validate_single_file(Path(args.path))


if __name__ == "__main__":
    raise SystemExit(main())

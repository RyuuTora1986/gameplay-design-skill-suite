from __future__ import annotations

import argparse
import json
from pathlib import Path


ALLOWED_TASK_TYPES = {"ui", "logic", "config", "qa", "asset", "integration", "delivery"}
REQUIRED_PROJECT_FIELDS = {"name", "source_type", "source_files", "execution_mode"}
REQUIRED_TASK_FIELDS = {
    "id",
    "title",
    "type",
    "depends_on",
    "source_refs",
    "canonical_ids",
    "goal",
    "deliverables",
    "acceptance_criteria",
    "verification",
    "notes",
}
REQUIRED_MD_MARKERS = [
    "# Execution Plan",
    "## Project",
    "## Execution Strategy",
    "## Task List",
]


def validate_json(path: Path) -> tuple[list[str], dict]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"Invalid JSON: {exc}"], {}

    if not isinstance(data, dict):
        return ["Root JSON value must be an object."], {}

    project = data.get("project")
    tasks = data.get("tasks")

    if not isinstance(project, dict):
        errors.append("Missing or invalid project object.")
    else:
        missing_project = REQUIRED_PROJECT_FIELDS - set(project)
        for field in sorted(missing_project):
            errors.append(f"Missing project field: {field}")
        if not isinstance(project.get("source_files"), list) or not project.get("source_files"):
            errors.append("project.source_files must be a non-empty array.")

    if not isinstance(tasks, list) or not tasks:
        errors.append("tasks must be a non-empty array.")
        return errors, data

    task_ids: set[str] = set()
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("Each task must be an object.")
            continue

        missing = REQUIRED_TASK_FIELDS - set(task)
        for field in sorted(missing):
            errors.append(f"Task missing field: {field}")

        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id.startswith("TASK-"):
            errors.append(f"Invalid task id: {task_id}")
        elif task_id in task_ids:
            errors.append(f"Duplicate task id: {task_id}")
        else:
            task_ids.add(task_id)

        task_type = task.get("type")
        if task_type not in ALLOWED_TASK_TYPES:
            errors.append(f"Invalid task type for {task_id}: {task_type}")

        for list_field in [
            "depends_on",
            "source_refs",
            "canonical_ids",
            "deliverables",
            "acceptance_criteria",
            "verification",
            "notes",
        ]:
            if not isinstance(task.get(list_field), list):
                errors.append(f"{task_id} field must be an array: {list_field}")

        if task_type == "ui":
            verification = " ".join(task.get("verification", []))
            if "browser" not in verification.lower():
                errors.append(f"{task_id} is a ui task but lacks browser verification.")

    for task in tasks:
        if not isinstance(task, dict):
            continue
        task_id = task.get("id")
        for dependency in task.get("depends_on", []):
            if dependency not in task_ids:
                errors.append(f"{task_id} depends on unknown task id: {dependency}")

    return errors, data


def validate_markdown(path: Path, data: dict) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    for marker in REQUIRED_MD_MARKERS:
        if marker not in text:
            errors.append(f"Markdown missing marker: {marker}")

    for task in data.get("tasks", []):
        task_id = task.get("id", "")
        title = task.get("title", "")
        heading = f"### {task_id} {title}"
        if heading not in text:
            errors.append(f"Markdown missing task section: {heading}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", nargs="?")
    parser.add_argument("--markdown")
    parser.add_argument("--plan-dir")
    args = parser.parse_args()

    if args.plan_dir:
        plan_dir = Path(args.plan_dir)
        json_path = plan_dir / "execution-plan.json"
        md_path = plan_dir / "execution-plan.md"
    else:
        if not args.json_file or not args.markdown:
            raise SystemExit("Provide either --plan-dir or <json_file> --markdown <markdown_file>.")
        json_path = Path(args.json_file)
        md_path = Path(args.markdown)

    if not json_path.exists():
        raise SystemExit(f"Missing JSON file: {json_path}")
    if not md_path.exists():
        raise SystemExit(f"Missing Markdown file: {md_path}")

    json_errors, data = validate_json(json_path)
    md_errors = [] if json_errors else validate_markdown(md_path, data)
    errors = json_errors + md_errors

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- ERROR: {error}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


STATE_FILE = "execution-run-state.json"
REQUIRED_EVIDENCE_FIELDS = {
    "summary",
    "changed_files",
    "verification_run",
    "acceptance_checklist",
    "open_issues",
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def get_plan_paths(plan_dir: Path) -> tuple[Path, Path]:
    plan_file = plan_dir / "execution-plan.json"
    state_file = plan_dir / STATE_FILE
    if not plan_file.exists():
        raise SystemExit(f"Missing plan file: {plan_file}")
    return plan_file, state_file


def init_state(plan_dir: Path, repo_root: str, branch: str) -> int:
    plan_file, state_file = get_plan_paths(plan_dir)
    plan = read_json(plan_file)
    tasks = {
        task["id"]: {
            "status": "pending",
            "attempt_count": 0,
            "last_summary": "",
            "verification_evidence": [],
            "blocked_reason": "",
        }
        for task in plan["tasks"]
    }
    state = {
        "version": plan.get("version", "0.1"),
        "plan_file": str(plan_file),
        "repo_root": repo_root,
        "branch": branch,
        "last_completed_task": "",
        "tasks": tasks,
    }
    write_json(state_file, state)
    print(f"Initialized state: {state_file}")
    return 0


def load_plan_and_state(plan_dir: Path) -> tuple[dict[str, Any], dict[str, Any], Path]:
    plan_file, state_file = get_plan_paths(plan_dir)
    if not state_file.exists():
        raise SystemExit(
            f"Missing state file: {state_file}. Run init first."
        )
    return read_json(plan_file), read_json(state_file), state_file


def is_runnable(task: dict[str, Any], state: dict[str, Any]) -> bool:
    task_state = state["tasks"][task["id"]]["status"]
    if task_state not in {"pending", "failed"}:
        return False
    for dependency in task["depends_on"]:
        if state["tasks"][dependency]["status"] != "completed":
            return False
    return True


def build_payload(task: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    completed_dependencies = [
        dependency
        for dependency in task["depends_on"]
        if state["tasks"][dependency]["status"] == "completed"
    ]
    return {
        "task_id": task["id"],
        "title": task["title"],
        "type": task["type"],
        "completed_dependencies": completed_dependencies,
        "source_refs": task["source_refs"],
        "canonical_ids": task["canonical_ids"],
        "goal": task["goal"],
        "deliverables": task["deliverables"],
        "acceptance_criteria": task["acceptance_criteria"],
        "verification": task["verification"],
        "notes": task["notes"],
        "worker_rules": [
            "Do not redesign upstream decisions.",
            "Do not absorb future tasks.",
            "Report changed files explicitly.",
            "Report verification evidence before claiming completion.",
        ],
    }


def find_task(plan: dict[str, Any], task_id: str) -> dict[str, Any]:
    for task in plan["tasks"]:
        if task["id"] == task_id:
            return task
    raise SystemExit(f"Unknown task id: {task_id}")


def validate_evidence(evidence: dict[str, Any]) -> None:
    missing = REQUIRED_EVIDENCE_FIELDS - set(evidence)
    if missing:
        raise SystemExit(f"Evidence missing fields: {', '.join(sorted(missing))}")

    if not isinstance(evidence["changed_files"], list) or not evidence["changed_files"]:
        raise SystemExit("Evidence changed_files must be a non-empty array.")

    verification_run = evidence["verification_run"]
    if not isinstance(verification_run, list) or not verification_run:
        raise SystemExit("Evidence verification_run must be a non-empty array.")
    if all(item.get("result") == "not_run" for item in verification_run if isinstance(item, dict)):
        raise SystemExit("Evidence verification_run cannot be all not_run.")

    acceptance_checklist = evidence["acceptance_checklist"]
    if not isinstance(acceptance_checklist, list) or not acceptance_checklist:
        raise SystemExit("Evidence acceptance_checklist must be a non-empty array.")
    for item in acceptance_checklist:
        if not isinstance(item, dict):
            raise SystemExit("Each acceptance checklist item must be an object.")
        if item.get("status") == "not_met":
            raise SystemExit("Cannot complete task with acceptance status not_met.")


def load_evidence(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing evidence file: {path}")
    evidence = read_json(path)
    validate_evidence(evidence)
    return evidence


def next_task(plan_dir: Path, output_format: str) -> int:
    plan, state, _ = load_plan_and_state(plan_dir)
    runnable = next((task for task in plan["tasks"] if is_runnable(task, state)), None)
    if runnable is None:
        print("No runnable task found.")
        return 0

    payload = build_payload(runnable, state)
    if output_format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"# {payload['task_id']} {payload['title']}")
    print("")
    print(f"- Type: {payload['type']}")
    print(f"- Completed dependencies: {', '.join(payload['completed_dependencies']) or 'none'}")
    print(f"- Source refs: {', '.join(payload['source_refs'])}")
    print(f"- Canonical IDs: {', '.join(payload['canonical_ids']) or 'none'}")
    print(f"- Goal: {payload['goal']}")
    print("- Deliverables:")
    for item in payload["deliverables"]:
        print(f"  - {item}")
    print("- Acceptance criteria:")
    for item in payload["acceptance_criteria"]:
        print(f"  - {item}")
    print("- Verification:")
    for item in payload["verification"]:
        print(f"  - {item}")
    print("- Notes:")
    for item in payload["notes"]:
        print(f"  - {item}")
    print("- Worker rules:")
    for item in payload["worker_rules"]:
        print(f"  - {item}")
    return 0


def render_handoff(payload: dict[str, Any], output_format: str) -> int:
    if output_format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"# Worker Handoff: {payload['task_id']} {payload['title']}")
    print("")
    print("## Scope")
    print(f"- Type: {payload['type']}")
    print(f"- Completed dependencies: {', '.join(payload['completed_dependencies']) or 'none'}")
    print(f"- Source refs: {', '.join(payload['source_refs'])}")
    print(f"- Canonical IDs: {', '.join(payload['canonical_ids']) or 'none'}")
    print(f"- Goal: {payload['goal']}")
    print("")
    print("## Deliverables")
    for item in payload["deliverables"]:
        print(f"- {item}")
    print("")
    print("## Acceptance Criteria")
    for item in payload["acceptance_criteria"]:
        print(f"- {item}")
    print("")
    print("## Verification")
    for item in payload["verification"]:
        print(f"- {item}")
    print("")
    print("## Notes")
    for item in payload["notes"]:
        print(f"- {item}")
    print("")
    print("## Worker Rules")
    for item in payload["worker_rules"]:
        print(f"- {item}")
    print("")
    print("## Completion Evidence Format")
    print("- summary")
    print("- changed_files")
    print("- verification_run")
    print("- acceptance_checklist")
    print("- open_issues")
    return 0


def handoff_task(plan_dir: Path, task_id: str | None, output_format: str) -> int:
    plan, state, _ = load_plan_and_state(plan_dir)
    task = find_task(plan, task_id) if task_id else next((item for item in plan["tasks"] if is_runnable(item, state)), None)
    if task is None:
        print("No runnable task found.")
        return 0
    payload = build_payload(task, state)
    return render_handoff(payload, output_format)


def update_task_status(
    plan_dir: Path,
    task_id: str,
    status: str,
    summary: str = "",
    verification: Any = None,
    reason: str = "",
) -> int:
    plan, state, state_file = load_plan_and_state(plan_dir)
    if task_id not in state["tasks"]:
        raise SystemExit(f"Unknown task id: {task_id}")

    task = find_task(plan, task_id)
    entry = state["tasks"][task_id]

    if status == "completed":
        if entry["status"] != "running":
            raise SystemExit(f"{task_id} must be in running state before completion.")
        if verification is None:
            raise SystemExit("Completion requires structured verification evidence.")

    entry["status"] = status
    if status in {"running", "failed", "blocked"}:
        entry["attempt_count"] += 1
    if summary:
        entry["last_summary"] = summary
    if verification is not None:
        entry["verification_evidence"].append(verification)
        entry["last_summary"] = verification["summary"]
    if reason:
        entry["blocked_reason"] = reason
    elif status != "blocked":
        entry["blocked_reason"] = ""

    if status == "completed":
        if task["type"] == "ui":
            verification_names = " ".join(
                item.get("name", "") for item in verification["verification_run"] if isinstance(item, dict)
            ).lower()
            if "browser" not in verification_names:
                raise SystemExit("UI completion evidence must include a browser verification entry.")
        state["last_completed_task"] = task_id

    write_json(state_file, state)
    print(f"Updated {task_id} -> {status}")
    return 0


def print_status(plan_dir: Path) -> int:
    plan, state, _ = load_plan_and_state(plan_dir)
    print(f"Plan: {state['plan_file']}")
    print(f"Repo: {state['repo_root']}")
    print(f"Branch: {state['branch']}")
    print(f"Last completed task: {state['last_completed_task'] or 'none'}")
    print("")
    for task in plan["tasks"]:
        entry = state["tasks"][task["id"]]
        print(f"{task['id']} [{entry['status']}] {task['title']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--plan-dir", required=True)
    init_parser.add_argument("--repo-root", required=True)
    init_parser.add_argument("--branch", required=True)

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--plan-dir", required=True)

    next_parser = subparsers.add_parser("next")
    next_parser.add_argument("--plan-dir", required=True)
    next_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    handoff_parser = subparsers.add_parser("handoff")
    handoff_parser.add_argument("--plan-dir", required=True)
    handoff_parser.add_argument("--task-id")
    handoff_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("--plan-dir", required=True)
    start_parser.add_argument("--task-id", required=True)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("--plan-dir", required=True)
    complete_parser.add_argument("--task-id", required=True)
    complete_parser.add_argument("--evidence-file", required=True)

    block_parser = subparsers.add_parser("block")
    block_parser.add_argument("--plan-dir", required=True)
    block_parser.add_argument("--task-id", required=True)
    block_parser.add_argument("--reason", required=True)

    fail_parser = subparsers.add_parser("fail")
    fail_parser.add_argument("--plan-dir", required=True)
    fail_parser.add_argument("--task-id", required=True)
    fail_parser.add_argument("--summary", required=True)

    args = parser.parse_args()
    plan_dir = Path(getattr(args, "plan_dir", "."))

    if args.command == "init":
        return init_state(plan_dir, args.repo_root, args.branch)
    if args.command == "status":
        return print_status(plan_dir)
    if args.command == "next":
        return next_task(plan_dir, args.format)
    if args.command == "handoff":
        return handoff_task(plan_dir, args.task_id, args.format)
    if args.command == "start":
        return update_task_status(plan_dir, args.task_id, "running")
    if args.command == "complete":
        evidence = load_evidence(Path(args.evidence_file))
        return update_task_status(
            plan_dir, args.task_id, "completed", verification=evidence
        )
    if args.command == "block":
        return update_task_status(plan_dir, args.task_id, "blocked", reason=args.reason)
    if args.command == "fail":
        return update_task_status(plan_dir, args.task_id, "failed", summary=args.summary)
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

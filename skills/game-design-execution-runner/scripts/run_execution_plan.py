from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


STATE_FILE = "execution-run-state.json"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def update_task_status(
    plan_dir: Path,
    task_id: str,
    status: str,
    summary: str = "",
    verification: str = "",
    reason: str = "",
) -> int:
    _, state, state_file = load_plan_and_state(plan_dir)
    if task_id not in state["tasks"]:
        raise SystemExit(f"Unknown task id: {task_id}")

    entry = state["tasks"][task_id]
    entry["status"] = status
    if status in {"running", "failed", "blocked"}:
        entry["attempt_count"] += 1
    if summary:
        entry["last_summary"] = summary
    if verification:
        entry["verification_evidence"].append(verification)
    if reason:
        entry["blocked_reason"] = reason
    elif status != "blocked":
        entry["blocked_reason"] = ""

    if status == "completed":
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

    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("--plan-dir", required=True)
    start_parser.add_argument("--task-id", required=True)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("--plan-dir", required=True)
    complete_parser.add_argument("--task-id", required=True)
    complete_parser.add_argument("--summary", required=True)
    complete_parser.add_argument("--verification", required=True)

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
    if args.command == "start":
        return update_task_status(plan_dir, args.task_id, "running")
    if args.command == "complete":
        return update_task_status(
            plan_dir, args.task_id, "completed", summary=args.summary, verification=args.verification
        )
    if args.command == "block":
        return update_task_status(plan_dir, args.task_id, "blocked", reason=args.reason)
    if args.command == "fail":
        return update_task_status(plan_dir, args.task_id, "failed", summary=args.summary)
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

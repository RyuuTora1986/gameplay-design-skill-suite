from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
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
DISPATCH_FILES = {
    "manifest": "dispatch-manifest.json",
    "payload": "task-payload.json",
    "handoff": "worker-handoff.md",
    "evidence_template": "completion-evidence.template.json",
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


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
            "last_dispatch_dir": "",
            "dispatch_id": "",
            "dispatch_status": "not_dispatched",
            "dispatched_at": "",
            "acknowledged_at": "",
            "worker_label": "",
            "handoff_mode": "",
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
    task_state = get_task_entry(state, task["id"])["status"]
    if task_state not in {"pending", "failed"}:
        return False
    for dependency in task["depends_on"]:
        if state["tasks"][dependency]["status"] != "completed":
            return False
    return True


def get_task_entry(state: dict[str, Any], task_id: str) -> dict[str, Any]:
    entry = state["tasks"][task_id]
    entry.setdefault("status", "pending")
    entry.setdefault("attempt_count", 0)
    entry.setdefault("last_summary", "")
    entry.setdefault("verification_evidence", [])
    entry.setdefault("blocked_reason", "")
    entry.setdefault("last_dispatch_dir", "")
    entry.setdefault("dispatch_id", "")
    entry.setdefault("dispatch_status", "not_dispatched")
    entry.setdefault("dispatched_at", "")
    entry.setdefault("acknowledged_at", "")
    entry.setdefault("worker_label", "")
    entry.setdefault("handoff_mode", "")
    return entry


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


def build_dispatch_manifest(
    task: dict[str, Any],
    payload: dict[str, Any],
    state: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    task_entry = get_task_entry(state, task["id"])
    return {
        "plan_file": state["plan_file"],
        "repo_root": state["repo_root"],
        "branch": state["branch"],
        "task_id": task["id"],
        "task_title": task["title"],
        "task_type": task["type"],
        "task_status_before_dispatch": task_entry["status"],
        "attempt_count_before_dispatch": task_entry["attempt_count"],
        "completed_dependencies": payload["completed_dependencies"],
        "dispatch_files": {
            name: str(output_dir / filename)
            for name, filename in DISPATCH_FILES.items()
        },
        "completion_protocol": {
            "ack_command": (
                f'python scripts/run_execution_plan.py ack --plan-dir "{Path(state["plan_file"]).parent}" '
                f'--task-id "{task["id"]}" --worker-label "<worker-label>"'
            ),
            "complete_command": (
                f'python scripts/run_execution_plan.py complete --plan-dir "{Path(state["plan_file"]).parent}" '
                f'--task-id "{task["id"]}" --evidence-file "<path-to-evidence-json>"'
            ),
            "fail_command": (
                f'python scripts/run_execution_plan.py fail --plan-dir "{Path(state["plan_file"]).parent}" '
                f'--task-id "{task["id"]}" --summary "<failure-summary>"'
            ),
            "block_command": (
                f'python scripts/run_execution_plan.py block --plan-dir "{Path(state["plan_file"]).parent}" '
                f'--task-id "{task["id"]}" --reason "<blocked-reason>"'
            ),
        },
    }


def build_evidence_template(payload: dict[str, Any]) -> dict[str, Any]:
    verification_template = [
        {"name": item, "result": "not_run"}
        for item in payload["verification"]
    ]
    acceptance_template = [
        {"criterion": item, "status": "partial"}
        for item in payload["acceptance_criteria"]
    ]
    return {
        "summary": f"Complete {payload['task_id']} {payload['title']}",
        "changed_files": ["<fill-in-file-path>"],
        "verification_run": verification_template,
        "acceptance_checklist": acceptance_template,
        "open_issues": ["<fill-in-open-issue-or-remove-if-none>"],
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

    print(render_payload_markdown(payload))
    return 0


def render_payload_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# {payload['task_id']} {payload['title']}",
        "",
        f"- Type: {payload['type']}",
        f"- Completed dependencies: {', '.join(payload['completed_dependencies']) or 'none'}",
        f"- Source refs: {', '.join(payload['source_refs'])}",
        f"- Canonical IDs: {', '.join(payload['canonical_ids']) or 'none'}",
        f"- Goal: {payload['goal']}",
        "- Deliverables:",
    ]
    lines.extend(f"  - {item}" for item in payload["deliverables"])
    lines.append("- Acceptance criteria:")
    lines.extend(f"  - {item}" for item in payload["acceptance_criteria"])
    lines.append("- Verification:")
    lines.extend(f"  - {item}" for item in payload["verification"])
    lines.append("- Notes:")
    lines.extend(f"  - {item}" for item in payload["notes"])
    lines.append("- Worker rules:")
    lines.extend(f"  - {item}" for item in payload["worker_rules"])
    return "\n".join(lines)


def render_handoff_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# Worker Handoff: {payload['task_id']} {payload['title']}",
        "",
        "## Scope",
        f"- Type: {payload['type']}",
        f"- Completed dependencies: {', '.join(payload['completed_dependencies']) or 'none'}",
        f"- Source refs: {', '.join(payload['source_refs'])}",
        f"- Canonical IDs: {', '.join(payload['canonical_ids']) or 'none'}",
        f"- Goal: {payload['goal']}",
        "",
        "## Deliverables",
    ]
    lines.extend(f"- {item}" for item in payload["deliverables"])
    lines.extend(["", "## Acceptance Criteria"])
    lines.extend(f"- {item}" for item in payload["acceptance_criteria"])
    lines.extend(["", "## Verification"])
    lines.extend(f"- {item}" for item in payload["verification"])
    lines.extend(["", "## Notes"])
    lines.extend(f"- {item}" for item in payload["notes"])
    lines.extend(["", "## Worker Rules"])
    lines.extend(f"- {item}" for item in payload["worker_rules"])
    lines.extend(
        [
            "",
            "## Completion Evidence Format",
            "- summary",
            "- changed_files",
            "- verification_run",
            "- acceptance_checklist",
            "- open_issues",
        ]
    )
    return "\n".join(lines)


def render_handoff(payload: dict[str, Any], output_format: str) -> int:
    if output_format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(render_handoff_markdown(payload))
    return 0


def handoff_task(plan_dir: Path, task_id: str | None, output_format: str) -> int:
    plan, state, _ = load_plan_and_state(plan_dir)
    task = find_task(plan, task_id) if task_id else next((item for item in plan["tasks"] if is_runnable(item, state)), None)
    if task is None:
        print("No runnable task found.")
        return 0
    payload = build_payload(task, state)
    return render_handoff(payload, output_format)


def dispatch_task(
    plan_dir: Path,
    task_id: str | None,
    output_dir: Path | None,
    output_format: str,
    mark_running: bool,
) -> int:
    plan, state, state_file = load_plan_and_state(plan_dir)
    task = find_task(plan, task_id) if task_id else next((item for item in plan["tasks"] if is_runnable(item, state)), None)
    if task is None:
        print("No runnable task found.")
        return 0

    payload = build_payload(task, state)
    resolved_output_dir = output_dir or (plan_dir / f"dispatch-{task['id'].lower()}")
    resolved_output_dir.mkdir(parents=True, exist_ok=True)

    manifest = build_dispatch_manifest(task, payload, state, resolved_output_dir)
    write_json(resolved_output_dir / DISPATCH_FILES["manifest"], manifest)
    write_json(resolved_output_dir / DISPATCH_FILES["payload"], payload)
    (resolved_output_dir / DISPATCH_FILES["handoff"]).write_text(
        render_handoff_markdown(payload) + "\n", encoding="utf-8"
    )
    write_json(
        resolved_output_dir / DISPATCH_FILES["evidence_template"],
        build_evidence_template(payload),
    )

    entry = get_task_entry(state, task["id"])
    if entry["status"] not in {"pending", "failed"}:
        raise SystemExit(
            f"{task['id']} cannot be dispatched from state {entry['status']}."
        )
    dispatch_id = f"{task['id']}-dispatch-{entry['attempt_count'] + 1}"
    entry["last_dispatch_dir"] = str(resolved_output_dir)
    entry["dispatch_id"] = dispatch_id
    entry["dispatch_status"] = "dispatched"
    entry["dispatched_at"] = utc_now_iso()
    entry["acknowledged_at"] = ""
    entry["worker_label"] = ""
    entry["handoff_mode"] = "dispatch-packet"
    entry["blocked_reason"] = ""
    if mark_running:
        entry["status"] = "running"
        entry["dispatch_status"] = "acknowledged"
        entry["acknowledged_at"] = utc_now_iso()
        entry["worker_label"] = "auto-dispatch"
        entry["attempt_count"] += 1
    else:
        entry["status"] = "dispatched"
    write_json(state_file, state)

    result = {
        "task_id": task["id"],
        "output_dir": str(resolved_output_dir),
        "files": {
            name: str(resolved_output_dir / filename)
            for name, filename in DISPATCH_FILES.items()
        },
        "dispatch_id": dispatch_id,
        "marked_running": mark_running,
    }

    if output_format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"Dispatched {task['id']} -> {resolved_output_dir}")
    for name, path in result["files"].items():
        print(f"- {name}: {path}")
    if mark_running:
        print("- state: running")
    else:
        print("- state: dispatched")
    return 0


def acknowledge_dispatch(plan_dir: Path, task_id: str, worker_label: str) -> int:
    plan, state, state_file = load_plan_and_state(plan_dir)
    if task_id not in state["tasks"]:
        raise SystemExit(f"Unknown task id: {task_id}")
    find_task(plan, task_id)
    entry = get_task_entry(state, task_id)
    if entry["status"] != "dispatched":
        raise SystemExit(f"{task_id} must be in dispatched state before ack.")
    if entry["dispatch_status"] != "dispatched":
        raise SystemExit(f"{task_id} has no active dispatch to acknowledge.")

    entry["status"] = "running"
    entry["dispatch_status"] = "acknowledged"
    entry["worker_label"] = worker_label
    entry["acknowledged_at"] = utc_now_iso()
    entry["attempt_count"] += 1

    write_json(state_file, state)
    print(f"Acknowledged {task_id} -> running ({worker_label})")
    return 0


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
    entry = get_task_entry(state, task_id)

    if status == "completed":
        if entry["status"] != "running":
            raise SystemExit(f"{task_id} must be in running state before completion.")
        if verification is None:
            raise SystemExit("Completion requires structured verification evidence.")
    elif status == "running":
        if entry["status"] not in {"pending", "failed", "dispatched"}:
            raise SystemExit(f"{task_id} cannot enter running from {entry['status']}.")
    elif status in {"failed", "blocked"}:
        if entry["status"] not in {"dispatched", "running"}:
            raise SystemExit(f"{task_id} cannot be marked {status} from {entry['status']}.")

    entry["status"] = status
    if status == "running":
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
        entry["dispatch_status"] = "completed"
        if task["type"] == "ui":
            verification_names = " ".join(
                item.get("name", "") for item in verification["verification_run"] if isinstance(item, dict)
            ).lower()
            if "browser" not in verification_names:
                raise SystemExit("UI completion evidence must include a browser verification entry.")
        state["last_completed_task"] = task_id
    elif status == "running":
        entry["dispatch_status"] = "acknowledged"
        if not entry["acknowledged_at"]:
            entry["acknowledged_at"] = utc_now_iso()
        if not entry["worker_label"]:
            entry["worker_label"] = "legacy-start"
    elif status == "failed":
        entry["dispatch_status"] = "failed"
    elif status == "blocked":
        entry["dispatch_status"] = "blocked"

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
        entry = get_task_entry(state, task["id"])
        dispatch_bits = []
        if entry["dispatch_status"] != "not_dispatched":
            dispatch_bits.append(f"dispatch={entry['dispatch_status']}")
        if entry["worker_label"]:
            dispatch_bits.append(f"worker={entry['worker_label']}")
        dispatch_suffix = f" ({', '.join(dispatch_bits)})" if dispatch_bits else ""
        print(f"{task['id']} [{entry['status']}] {task['title']}{dispatch_suffix}")
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

    dispatch_parser = subparsers.add_parser("dispatch")
    dispatch_parser.add_argument("--plan-dir", required=True)
    dispatch_parser.add_argument("--task-id")
    dispatch_parser.add_argument("--output-dir")
    dispatch_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    dispatch_parser.add_argument("--mark-running", action="store_true")

    ack_parser = subparsers.add_parser("ack")
    ack_parser.add_argument("--plan-dir", required=True)
    ack_parser.add_argument("--task-id", required=True)
    ack_parser.add_argument("--worker-label", required=True)

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
    if args.command == "dispatch":
        output_dir = Path(args.output_dir) if args.output_dir else None
        return dispatch_task(
            plan_dir, args.task_id, output_dir, args.format, args.mark_running
        )
    if args.command == "ack":
        return acknowledge_dispatch(plan_dir, args.task_id, args.worker_label)
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

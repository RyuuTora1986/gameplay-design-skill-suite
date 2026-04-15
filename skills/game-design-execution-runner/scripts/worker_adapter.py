from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from run_execution_plan import (
    acknowledge_dispatch,
    load_evidence,
    read_json,
    update_task_status,
)


MANIFEST_FILE = "dispatch-manifest.json"


def load_dispatch_context(dispatch_dir: Path) -> dict[str, Any]:
    manifest_path = dispatch_dir / MANIFEST_FILE
    if not manifest_path.exists():
        raise SystemExit(f"Missing dispatch manifest: {manifest_path}")
    manifest = read_json(manifest_path)
    plan_dir = Path(manifest["plan_file"]).parent
    task_id = manifest["task_id"]
    return {
        "manifest": manifest,
        "plan_dir": plan_dir,
        "task_id": task_id,
    }


def pickup_dispatch(dispatch_dir: Path, worker_label: str) -> int:
    context = load_dispatch_context(dispatch_dir)
    return acknowledge_dispatch(context["plan_dir"], context["task_id"], worker_label)


def complete_dispatch(dispatch_dir: Path, evidence_file: Path) -> int:
    context = load_dispatch_context(dispatch_dir)
    evidence = load_evidence(evidence_file)
    return update_task_status(
        context["plan_dir"],
        context["task_id"],
        "completed",
        verification=evidence,
    )


def fail_dispatch(dispatch_dir: Path, summary: str) -> int:
    context = load_dispatch_context(dispatch_dir)
    return update_task_status(
        context["plan_dir"],
        context["task_id"],
        "failed",
        summary=summary,
    )


def block_dispatch(dispatch_dir: Path, reason: str) -> int:
    context = load_dispatch_context(dispatch_dir)
    return update_task_status(
        context["plan_dir"],
        context["task_id"],
        "blocked",
        reason=reason,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    pickup_parser = subparsers.add_parser("pickup")
    pickup_parser.add_argument("--dispatch-dir", required=True)
    pickup_parser.add_argument("--worker-label", required=True)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("--dispatch-dir", required=True)
    complete_parser.add_argument("--evidence-file", required=True)

    fail_parser = subparsers.add_parser("fail")
    fail_parser.add_argument("--dispatch-dir", required=True)
    fail_parser.add_argument("--summary", required=True)

    block_parser = subparsers.add_parser("block")
    block_parser.add_argument("--dispatch-dir", required=True)
    block_parser.add_argument("--reason", required=True)

    args = parser.parse_args()
    dispatch_dir = Path(getattr(args, "dispatch_dir", "."))

    if args.command == "pickup":
        return pickup_dispatch(dispatch_dir, args.worker_label)
    if args.command == "complete":
        return complete_dispatch(dispatch_dir, Path(args.evidence_file))
    if args.command == "fail":
        return fail_dispatch(dispatch_dir, args.summary)
    if args.command == "block":
        return block_dispatch(dispatch_dir, args.reason)
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
from pathlib import Path


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_json(game_name: str) -> str:
    data = {
        "version": "0.1",
        "project": {
            "name": game_name,
            "source_type": "game-design-spec",
            "source_files": ["01-master-spec.md"],
            "execution_mode": "single-agent-iterative",
        },
        "tasks": [
            {
                "id": "TASK-001",
                "title": "Replace with a concrete implementation slice",
                "type": "logic",
                "depends_on": [],
                "source_refs": ["01-master-spec.md#replace-me"],
                "canonical_ids": ["SYS-01"],
                "goal": "Describe one small executable objective.",
                "deliverables": ["One concrete output"],
                "acceptance_criteria": [
                    "Replace with measurable acceptance criteria",
                    "Typecheck passes",
                ],
                "verification": ["Replace with concrete verification commands"],
                "notes": ["Replace with real execution boundary notes"],
            }
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def build_md(game_name: str) -> str:
    lines = [
        "# Execution Plan",
        "",
        "## Project",
        f"- Name: {game_name}",
        "- Source type: game-design-spec",
        "- Source files: 01-master-spec.md",
        "- Execution mode: single-agent-iterative",
        "",
        "## Execution Strategy",
        "- Replace this section with the true task-order rationale.",
        "- Replace this section with deferred work boundaries.",
        "- Replace this section with redesign prohibitions.",
        "",
        "## Task List",
        "### TASK-001 Replace with a concrete implementation slice",
        "- Type: logic",
        "- Depends on: none",
        "- Source refs: 01-master-spec.md#replace-me",
        "- Canonical IDs: SYS-01",
        "- Goal: Describe one small executable objective.",
        "- Deliverables:",
        "  - One concrete output",
        "- Acceptance criteria:",
        "  - Replace with measurable acceptance criteria",
        "  - Typecheck passes",
        "- Verification:",
        "  - Replace with concrete verification commands",
        "- Notes:",
        "  - Replace with real execution boundary notes",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--game-name", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    write_text(outdir / "execution-plan.json", build_json(args.game_name))
    write_text(outdir / "execution-plan.md", build_md(args.game_name))
    print(f"Wrote execution plan bootstrap to {outdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

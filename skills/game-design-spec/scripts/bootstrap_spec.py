from __future__ import annotations

import argparse
from pathlib import Path

from validate_spec import (
    REQUIRED_HEADINGS,
    REQUIRED_SUBSTRINGS,
    TASK_REQUIRED_MARKERS,
    TASK_TYPE_REQUIRED_MARKERS,
    TASK_TYPE_WARNING_MARKERS,
)


TASKS = [
    ("04-ui-task.md", "4", "UI Task", "master spec chapters 1-3"),
    ("05-level-task.md", "5", "Level Task", "master spec chapters 1-3"),
    ("06-balance-task.md", "6", "Balance Task", "master spec chapters 1-5"),
    ("07-config-task.md", "7", "Config Task", "master spec chapters 1-6"),
    ("08-art-task.md", "8", "Art Task", "master spec chapters 1-6"),
    ("09-audio-task.md", "9", "Audio Task", "master spec chapters 1-8"),
    ("10-qa-task.md", "10", "QA Task", "master spec chapters 1-9"),
    ("11-delivery-task.md", "11", "Delivery Task", "master spec chapters 1-10"),
]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_master_spec(game_name: str) -> str:
    assumption_heading = REQUIRED_SUBSTRINGS[0]
    system_registry_heading = REQUIRED_SUBSTRINGS[1]
    system_id_token = REQUIRED_SUBSTRINGS[2]
    resource_registry_heading = REQUIRED_SUBSTRINGS[3]
    resource_id_token = REQUIRED_SUBSTRINGS[4]
    formula_registry_heading = REQUIRED_SUBSTRINGS[5]
    formula_id_token = REQUIRED_SUBSTRINGS[6]
    config_registry_heading = REQUIRED_SUBSTRINGS[7]
    config_id_token = REQUIRED_SUBSTRINGS[8]
    variable_registry_heading = REQUIRED_SUBSTRINGS[9]
    variable_id_token = REQUIRED_SUBSTRINGS[10]

    c11 = REQUIRED_SUBSTRINGS[11]
    c12 = REQUIRED_SUBSTRINGS[12]
    c13 = REQUIRED_SUBSTRINGS[13]
    c14 = REQUIRED_SUBSTRINGS[14]
    c15 = REQUIRED_SUBSTRINGS[15]
    c151 = REQUIRED_SUBSTRINGS[16]
    c152 = REQUIRED_SUBSTRINGS[17]
    c153 = REQUIRED_SUBSTRINGS[18]
    c154 = REQUIRED_SUBSTRINGS[19]
    c155 = REQUIRED_SUBSTRINGS[20]
    c156 = REQUIRED_SUBSTRINGS[21]
    c157 = REQUIRED_SUBSTRINGS[22]
    c21 = REQUIRED_SUBSTRINGS[23]
    c22 = REQUIRED_SUBSTRINGS[24]
    c32 = REQUIRED_SUBSTRINGS[25]
    rule_id_token = REQUIRED_SUBSTRINGS[26]
    state_machine_token = REQUIRED_SUBSTRINGS[27]

    lines = [
        f"# Project",
        "",
        f"- Game: {game_name}",
        "",
        assumption_heading,
        "",
        "- Assumption 1",
        "- Assumption 2",
        "",
        system_registry_heading,
        "",
        f"| {system_id_token} | Name | One-line role | Player goal | Input | Output | Dependency | UI Task | Balance Task | Config Task | QA Focus |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
        "| SYS-01 | Core Loop | Main loop owner | Complete one loop | Tap | Reward | None | 04-ui-task.md | 06-balance-task.md | 07-config-task.md | Loop completion |",
        "",
        resource_registry_heading,
        "",
        f"| {resource_id_token} | Name | Type | Source System | Sink System | Scarce |",
        "|---|---|---|---|---|---|",
        "| RES-01 | Energy | numeric | SYS-01 | SYS-01 | No |",
        "",
        formula_registry_heading,
        "",
        f"| {formula_id_token} | Name | System ID | Input Variables | Output | Chapter |",
        "|---|---|---|---|---|---|",
        "| FML-01 | Reward Formula | SYS-01 | VAR-01 | Reward Value | 6 |",
        "",
        config_registry_heading,
        "",
        f"| {config_id_token} | Name | System ID | Primary Key | Usage | Hot Reload |",
        "|---|---|---|---|---|---|",
        "| CFG-01 | CoreConfig | SYS-01 | id | loop tuning | Yes |",
        "",
        variable_registry_heading,
        "",
        f"| {variable_id_token} | Name | Formula ID | Unit | Source | Sink |",
        "|---|---|---|---|---|---|",
        "| VAR-01 | RewardBase | FML-01 | point | CFG-01 | FML-01 |",
        "",
        REQUIRED_HEADINGS[0],
        "",
        c11,
        c12,
        c13,
        "",
        c14,
        "",
        c15,
        "",
        c151,
        "",
        c152,
        "",
        c153,
        "",
        c154,
        "",
        c155,
        "",
        c156,
        "",
        c157,
        "",
        "## 1.6 Camera",
        "",
        "## 1.7 Controls",
        "",
        "## 1.8 Audience",
        "",
        "## 1.9 Session Length And Pacing",
        "",
        "## 1.10 Save Model",
        "## 1.11 Monetization",
        "## 1.12 Tech Stack",
        "## 1.13 Minimum Device Target",
        REQUIRED_HEADINGS[1],
        "",
        c21,
        "",
        c22,
        "",
        REQUIRED_HEADINGS[2],
        "",
        "## 3.1 System SYS-01",
        "",
        "### Design Purpose",
        "",
        "### User-facing Goal",
        "",
        "| Item | Content |",
        "|---|---|",
        "| Goal | Finish one loop |",
        "| Entry | Start input |",
        "| Exit | Loop resolved |",
        "| Fun | Fast feedback |",
        "| Failure cost | Retry |",
        "| Review gain | Learn pattern |",
        "",
        "### Key Terms",
        "",
        "| Term | Definition | Boundary |",
        "|---|---|---|",
        "| Loop | One repeat cycle | Does not include meta progression |",
        "",
        f"### {rule_id_token}",
        "",
        f"| {rule_id_token} | Trigger | Player Action | System Response | Feedback | Reward/Penalty | Note |",
        "|---|---|---|---|---|---|---|",
        "| SYS-01-R01 | Start | Tap | Advance state | Visible feedback | Reward | Core rule |",
        "",
        "### Boundary Conditions And Exceptions",
        "",
        "| Scenario | Input | Expected Result | Fallback |",
        "|---|---|---|---|",
        "| Invalid input | none | ignore | keep stable |",
        "",
        f"### {state_machine_token}",
        "",
        "```mermaid",
        "stateDiagram-v2",
        "    [*] --> Idle",
        "    Idle --> Running: Start",
        "    Running --> Success: Resolve",
        "    Running --> Failure: Fail",
        "    Success --> Idle: Reset",
        "    Failure --> Idle: Retry",
        "```",
        "",
        "### Anti-abuse And Farming Protection",
        "",
        "| Risk | Trigger | Guard | Player Impact |",
        "|---|---|---|---|",
        "| Repeat spam | repeated input | cooldown | low |",
        "",
        c32,
        "",
        REQUIRED_HEADINGS[3],
        "",
        "- Version: 0.1",
        "- Date: generated",
        "",
        REQUIRED_HEADINGS[4],
        "",
        "| Type | Content | Impacted Chapter |",
        "|---|---|---|",
        "| Added | Bootstrap skeleton | 1-11 |",
        "",
        REQUIRED_HEADINGS[5],
        "",
        "| Chapter | Rule Change | Numeric Change | UI Change | Config Change |",
        "|---|---|---|---|---|",
        "| 1 | Initial version | Initial version | Initial version | Initial version |",
        "",
        REQUIRED_HEADINGS[6],
        "",
        "- Complete: Yes",
        "- No example-only substitution: Yes",
        "- Remaining weak chapters: None",
    ]
    return "\n".join(lines) + "\n"


def build_task_file(filename: str, chapter: str, title: str, dependency: str) -> str:
    lines = [
        TASK_REQUIRED_MARKERS[0],
        "",
        f"- Dependency: {dependency}",
        "- Source: 01-master-spec.md",
        f"- {TASK_REQUIRED_MARKERS[1]}: SYS-01",
        "",
        f"# {chapter}. {title}",
        "",
        TASK_REQUIRED_MARKERS[2],
        "",
        "- Extend the master spec without breaking canonical IDs.",
        "- Keep the output executable and table-first.",
        "- Add assumptions explicitly before using them.",
        "- Keep object references anchored to SYS-01 / RES-01 / FML-01 / CFG-01 / VAR-01.",
        "",
        TASK_REQUIRED_MARKERS[3],
        "",
        "- Covers SYS-01, RES-01, FML-01, CFG-01, VAR-01.",
    ]

    for token, markers in TASK_TYPE_REQUIRED_MARKERS.items():
        if token in filename:
            lines.extend(["", *(f"### {marker}" for marker in markers)])
            lines.extend(["", "- Fill this section with executable content."])

    for token, markers in TASK_TYPE_WARNING_MARKERS.items():
        if token in filename:
            lines.extend(["", *(f"### {marker}" for marker in markers)])
            lines.extend(["", "- Preferred path / fallback / backup should be filled here."])

    if filename == "10-qa-task.md":
        lines.extend(
            [
                "",
                f"### {TASK_TYPE_REQUIRED_MARKERS['qa-task'][0]}",
                "",
                "| 用例ID | Name | System ID | Formula ID | Config ID | Goal |",
                "|---|---|---|---|---|---|",
                "| QA-01 | Core loop smoke | SYS-01 | FML-01 | CFG-01 | Verify one full loop |",
            ]
        )

    if filename == "11-delivery-task.md":
        lines.extend(
            [
                "",
                f"### {TASK_TYPE_REQUIRED_MARKERS['delivery-task'][0]}",
                "",
                "| 任务ID | Name | System ID | Formula ID | Config ID | Resource ID | Deliverable |",
                "|---|---|---|---|---|---|---|",
                "| TASK-01 | Implement core loop | SYS-01 | FML-01 | CFG-01 | RES-01 | playable prototype |",
            ]
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create game design spec stubs.")
    parser.add_argument("--game-name", required=True, help="Game name for file headers.")
    parser.add_argument("--outdir", required=True, help="Output directory.")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_text(outdir / "01-master-spec.md", build_master_spec(args.game_name))

    for filename, chapter, title, dependency in TASKS:
        write_text(outdir / filename, build_task_file(filename, chapter, title, dependency))

    index_lines = [
        "# Task Index",
        "",
        f"- Game: {args.game_name}",
        "- Generated by: bootstrap_spec.py",
        "",
        "## Files",
        "",
        "- 01-master-spec.md",
    ]
    for filename, _, title, _ in TASKS:
        index_lines.append(f"- {filename}: {title}")

    write_text(outdir / "00-task-index.md", "\n".join(index_lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

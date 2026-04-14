from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_COLUMNS = [
    "asset_id",
    "family_id",
    "related_system_ids",
    "anchor_id",
    "current_stage",
    "intended_tool",
    "intended_use",
    "export_spec",
    "acceptance_status",
    "replacement_of",
]

ALLOWED_STAGES = {"draft", "anchor_locked", "batch_generated", "accepted", "rejected", "accepted-placeholder"}
ALLOWED_STATUS = {"pending", "accepted", "rejected"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a markdown asset registry table.")
    parser.add_argument("path", help="Path to markdown file containing an asset registry table.")
    args = parser.parse_args()

    text = Path(args.path).read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    if "资产登记表" not in text:
        errors.append("Missing 资产登记表 heading.")

    lines = [line.strip() for line in text.splitlines() if "|" in line.strip()]
    if len(lines) < 2:
        errors.append("No markdown table detected.")
    else:
        header = [cell.strip() for cell in lines[0].split("|")[1:-1]]
        for column in REQUIRED_COLUMNS:
            if column not in header:
                errors.append(f"Missing registry column: {column}")

        if not errors:
            col_index = {name: header.index(name) for name in header}
            for row in lines[2:]:
                cells = [cell.strip() for cell in row.split("|")[1:-1]]
                if len(cells) < len(header):
                    continue
                stage = cells[col_index["current_stage"]]
                status = cells[col_index["acceptance_status"]]
                asset_id = cells[col_index["asset_id"]]
                anchor_id = cells[col_index["anchor_id"]]
                if stage and stage not in ALLOWED_STAGES:
                    errors.append(f"{asset_id}: invalid current_stage {stage}.")
                if status and status not in ALLOWED_STATUS:
                    errors.append(f"{asset_id}: invalid acceptance_status {status}.")
                if not anchor_id:
                    warnings.append(f"{asset_id}: missing anchor_id.")

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


if __name__ == "__main__":
    raise SystemExit(main())

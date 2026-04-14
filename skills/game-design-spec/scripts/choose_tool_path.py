from __future__ import annotations

import argparse


CHECKED_DATE = "2026-04-07"


def choose(asset_family: str, target_stage: str) -> dict[str, str]:
    family = asset_family.lower()
    stage = target_stage.lower()

    if "sfx" in family or "audio" in family or "sound" in family:
        return {
            "preferred_tool": "ElevenLabs Sound Effects or equivalent SFX-focused workflow",
            "fallback_tool": "Narrow event-family prompting",
            "placeholder_backup": "Placeholder UI/water/alert pack",
            "choice_reason": "Short event sounds are more controllable when grouped by event family.",
            "checked_date": CHECKED_DATE,
            "switch_condition": "Switch if event clarity or naming/export reliability fails.",
            "output_expectation": f"{stage} output with event readability, naming, and format compliance.",
            "evidence_source": "latest official sound-effects docs checked",
        }

    if "music" in family or "bgm" in family:
        return {
            "preferred_tool": "Udio-style loop-friendly music workflow",
            "fallback_tool": "Short cue generation instead of full final track generation",
            "placeholder_backup": "Royalty-safe temporary loop with BPM and mood tags",
            "choice_reason": "Music quality is less stable, so shorter loopable goals are safer.",
            "checked_date": CHECKED_DATE,
            "switch_condition": "Switch if full-track generation is unstable or output fails the loop and mood checks.",
            "output_expectation": f"{stage} output with duration, loop, and mood suitability.",
            "evidence_source": "latest official music-tool docs checked",
        }

    if "art" in family or "image" in family or "icon" in family:
        return {
            "preferred_tool": "Adobe Firefly / Photoshop production-first image workflow",
            "fallback_tool": "OpenAI GPT Image class fallback constrained by anchor and export rules",
            "placeholder_backup": "Silhouette pack and labeled placeholder atlas",
            "choice_reason": "Visual assets need stronger export control and easier cleanup than one-shot novelty generation.",
            "checked_date": CHECKED_DATE,
            "switch_condition": "Switch if preferred workflow is unavailable or cannot deliver export-safe assets for the current stage.",
            "output_expectation": f"{stage} output with anchor consistency, export spec, and replacement traceability.",
            "evidence_source": "latest official Adobe docs plus current image benchmark signal checked",
        }

    if "ui" in family:
        return {
            "preferred_tool": "Figma-oriented UI workflow with Dev Mode / Code Connect",
            "fallback_tool": "AI coding tool generating code-native UI",
            "placeholder_backup": "Wireframe and placeholder component pack",
            "choice_reason": "UI needs component consistency, layout control, and clean dev handoff.",
            "checked_date": CHECKED_DATE,
            "switch_condition": "Switch if Figma path is unavailable or cannot export usable structure for the current stage.",
            "output_expectation": f"{stage} output with component/state coverage and handoff-safe naming.",
            "evidence_source": "latest official Figma Dev Mode / Code Connect / MCP docs checked",
        }

    return {
        "preferred_tool": "Conservative manual routing",
        "fallback_tool": "AI coding or placeholder-first path",
        "placeholder_backup": "Minimal placeholder pack",
        "choice_reason": "Asset family is unclear, so a conservative path is safer.",
        "checked_date": CHECKED_DATE,
        "switch_condition": "Clarify the asset family before scaling generation.",
        "output_expectation": f"{stage} output with traceable placeholder status.",
        "evidence_source": "no external verification available, conservative fallback used",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Choose a preferred/fallback/backup tool path for an asset family.")
    parser.add_argument("--asset-family", required=True)
    parser.add_argument("--target-stage", required=True)
    args = parser.parse_args()

    result = choose(args.asset_family, args.target_stage)
    print(f"asset_family: {args.asset_family}")
    print(f"target_stage: {args.target_stage}")
    for key, value in result.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

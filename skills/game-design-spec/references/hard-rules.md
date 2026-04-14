# Hard Rules

Use this checklist to keep the output usable by downstream AI and human executors.

## Language and style

- Write in direct, plain Chinese.
- Explain every necessary term before using it repeatedly.
- Avoid unexplained abbreviations.
- Avoid decorative filler.

## Forbidden shortcuts

Do not use any of these as substitutes for real content:

- 示例
- 例子
- 可参考
- 略
- 同上
- 待定
- TBD
- TODO
- 视情况而定
- 按需调整

If uncertainty exists, write a concrete assumption and continue.

## Global consistency rules

- Do not let two top-level systems own the same primary player goal.
- Do not let downstream chapters invent a new top-level system without updating the master index first.
- Keep names, IDs, resources, formulas, config tables, and variables consistent across all chapters.
- If a section cannot be mapped to a system ID, either attach it to an existing system or justify it as a global rule.
- Prefer fixed templates and tables over narrative prose.
- If a chapter has a standard template, do not replace it with loose paragraphs only.
- Do not rename a resource, formula, config table, or variable after it has entered a canonical registry.
- Use IDs when ambiguity is possible: `SYS-*`, `RES-*`, `FML-*`, `CFG-*`, `VAR-*`.

## Split-deliverable rules

- Treat `01-master-spec.md` as the single source of truth for systems, resources, formulas, config tables, and variables.
- Reject any downstream task file that references a non-indexed object when the reference is concrete.
- Reject any downstream task file that omits system coverage when the chapter is system-bound.

## Formula-writing rules

For each formula:

- Write the formula explicitly.
- Define each variable.
- State unit and allowed range.
- State rounding, truncation, cap, floor, and overflow handling.
- Explain why the formula improves player experience.

## Final self-check

Before delivery, verify:

- A system master index exists.
- Every top-level system is uniquely identified.
- Every indexed system appears in chapter 3.
- Every indexed system is mapped into downstream work.
- Standard templates are present where applicable.
- Cross-file system IDs are consistent.
- Cross-file resource names, formula IDs, config table IDs, and variable IDs are consistent.
- Resource sources and sinks form a usable loop.
- Formula variables can be traced to a variable, resource, config field, or explicit constant.
- Canonical formulas are not orphaned from the variable registry.
- Canonical config tables are not orphaned from valid systems.
- Implementation task back-references cover the concrete objects they claim to deliver.
- QA task back-references cover key systems, key formulas, and key config tables.
- Every requested chapter exists.
- No section is blank.
- Every system contains rules, data, abnormal cases, and anti-abuse.
- Every numeric section contains formula explanation, range, and boundary handling.
- Economy includes source, sink, cap, inflation control.
- Difficulty includes milestones and correction mechanisms.
- Config includes fields, types, ranges, defaults, localization, hot-update.
- Art and audio sections are directly usable for AI generation.
- Implementation includes milestones, tasks, risks, alternatives.
- Footer includes version, change log, diff notes, and self-check conclusion.

## Asset-generation addendum

- If a chapter depends on generated UI or assets, define a style anchor and a production stage before asking for batch generation.
- Do not treat a one-shot prompt as a complete asset pipeline.
- Do not accept UI or art deliverables without explicit readability or integration checks.
- Asset-producing chapters should define stage, anchor, acceptance, naming, and export constraints.

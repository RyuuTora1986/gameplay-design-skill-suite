# Hard Rules

- Every task must be small enough for one focused agent iteration.
- Every task must have one main goal.
- Do not use vague acceptance criteria such as `works correctly`, `good UX`, or `complete implementation`.
- UI tasks must include browser verification.
- Logic tasks must include typecheck, and tests when meaningful.
- If a task references a concrete system, resource, formula, config table, or variable, include the canonical IDs.
- If a task depends on another task, list it in `depends_on`.
- Do not silently redesign upstream gameplay decisions.
- If execution detail is missing, assumptions may fill implementation gaps, but they must not rewrite locked design facts.
- If a task still spans multiple independent subsystems, split it again.

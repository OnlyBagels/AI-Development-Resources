---
name: review-gate
description: Run a structured skeptical review of AI-generated work before merge or handoff.
---

# Review Gate Skill

Use this skill before saying work is complete.

## Inputs needed

- Original task.
- Constraints.
- Changed files or patch summary.
- Validation commands and results.

## Review dimensions

1. Scope match.
2. Correctness.
3. Security.
4. Edge cases.
5. Maintainability.
6. Tests.
7. Docs.

## Output format

```md
Blockers:
- 

Non-blockers:
- 

Missing tests:
- 

Security concerns:
- 

Scope concerns:
- 

Risk rating: Low / Medium / High

Recommendation: Merge / Fix first / Redesign
```

## Rule

Be skeptical but useful. Do not create busywork.

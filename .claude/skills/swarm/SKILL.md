---
name: swarm
description: Coordinate a Sonnet-led workflow that delegates bounded low-complexity work to Haiku subagents.
---

# Swarm Skill

Use this skill when the user asks for a swarm, multi-agent workflow, cheap worker agents, or a faster/lower-cost Claude Code process.

## Principle

The main session coordinates. Haiku workers execute bounded tasks. The main session merges and decides.

## Steps

1. Restate the user goal in one sentence.
2. Decide whether a swarm is useful. Use a swarm only when there are separable chores.
3. Split work into bounded worker tasks.
4. Assign workers:
   - `haiku-researcher` for repo discovery.
   - `haiku-scaffolder` for boilerplate.
   - `haiku-test-runner` for tests/checks.
   - `haiku-docs-writer` for docs.
5. Keep architecture decisions in the main session.
6. Merge worker outputs.
7. Run `review-gate` or produce a review report.
8. Return final summary, validation, risks, and next step.

## Worker prompt template

```md
Task:
Context:
Boundaries:
Do not:
Return:
```

## Worker return format

```md
Findings / changes:
Files:
Validation:
Risks:
Next action:
```

## Rules

- Prefer fewer workers with clearer tasks.
- Do not delegate vague tasks.
- Do not let workers expand scope.
- Do not hide worker uncertainty.
- Do not declare done without validation or stated validation gap.

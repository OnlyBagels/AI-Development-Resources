# Model Ladder

The goal is not to always use the smartest model. The goal is to use the cheapest model that can reliably do the current job.

## Ladder

### Opus

Use for:

- Architecture and product design.
- Ambiguous strategy decisions.
- Complex debugging where mistakes are expensive.
- Reviewing deep tradeoffs.
- Producing final design direction for high-impact systems.

Avoid using for:

- Repetitive file edits.
- Basic docs writing.
- Simple test scaffolding.
- Searching the codebase.

### Sonnet

Use for:

- Main Claude Code sessions.
- Feature implementation.
- Coordinating Haiku workers.
- Medium-high complexity debugging.
- Refactoring with local context.

### Haiku

Use for:

- Scaffolding files.
- Gathering facts from the repo.
- Drafting docs.
- Creating initial tests.
- Running simple checks.
- Summarizing noisy output.

Haiku work should be bounded. Give it exact inputs and exact output format.

## Review model

Use a separate model/session for review when possible. The reviewer should not share the same assumptions as the builder.

Good review prompt:

```md
Task: Review this implementation.
Context: The intended behavior is described below. The patch is below.
Goal: Find correctness, security, maintainability, and scope issues.
Constraints: Be skeptical. Do not rewrite unless needed.
Return: blockers, non-blockers, tests to add, final recommendation.
```

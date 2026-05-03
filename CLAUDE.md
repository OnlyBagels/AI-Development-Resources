# CLAUDE.md

Project-level instructions for Claude Code.

## Operating style

- Be direct, practical, and implementation-oriented.
- Prefer small, reversible changes over large speculative rewrites.
- Ask for clarification only when a missing answer would materially change the implementation.
- When reasonable, make a best-effort assumption and state it briefly.
- Keep outputs concise unless asked for a deep explanation.

## Model strategy

Use this model ladder:

1. **Opus** for architecture, planning, ambiguous tradeoffs, and hard debugging.
2. **Sonnet** for the main coding session and coordination.
3. **Haiku subagents** for bounded low-complexity work: scaffolding, file discovery, docs, tests, cleanup, repetitive edits, and summarization.
4. **Independent reviewer** for final critique before merge.

## Swarm rule

When asked to use a swarm:

- Keep the main Sonnet session as coordinator.
- Spawn Haiku agents for bounded chores.
- Give each worker one narrow objective, a file boundary, and an exact return format.
- Workers should not make architecture decisions.
- Workers should not recursively orchestrate other workers.
- Merge worker outputs in the main session.
- Run a review pass before declaring work complete.

See @docs/swarm-pattern.md.

## Prompt hygiene

Default prompt structure:

```md
Task:
Context:
Goal:
Constraints:
Return:
```

Avoid word spaghetti. Include only context that changes the answer.

See @docs/prompt-hygiene.md and @docs/checklists/before-prompting.md.

## Chat hygiene

- Start a new chat for a new product direction, major feature, or unrelated bug.
- Compact or summarize when context gets long.
- Do not keep pivoting a finished task into a different project.
- Before a new chat, create a context packet with current goals, decisions, files changed, and next actions.

See @docs/chat-hygiene.md and @docs/templates/context-packet.md.

## Implementation workflow

1. Restate the task in one sentence.
2. Inspect relevant files before editing.
3. Create or update a short plan for medium/large tasks.
4. Make minimal changes.
5. Run available checks.
6. Summarize changed files, validation, risks, and next steps.

See @docs/vibe-coding-workflow.md.

## Review workflow

Before finalizing:

- Run tests or explain why not.
- Review security, correctness, maintainability, and UX.
- Check whether the implementation matches the original task rather than an imagined larger task.
- Produce a short review report.

See @docs/review-workflow.md and @docs/templates/review-report.md.

## Safety and repo discipline

- Do not commit secrets.
- Do not delete large sections without explaining why.
- Do not overwrite user work without checking git status.
- Prefer patch-sized commits.
- Include docs updates when behavior changes.

## Useful imports

- Model ladder: @docs/model-ladder.md
- Anti-patterns: @docs/anti-patterns.md
- Skills guide: @docs/skills-guide.md
- Cost control: @docs/cost-control.md

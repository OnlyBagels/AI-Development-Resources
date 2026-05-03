# Start Here

This repo teaches a Claude-specific workflow for better vibe coding: cleaner prompts, cleaner context, cheaper worker agents, and stronger review habits.

## The core loop

1. **Scope the task.** Decide exactly what you want done.
2. **Pick the model.** Do not spend Opus tokens on file shuffling.
3. **Write a structured prompt.** Task, context, goal, constraints, return.
4. **Use a swarm when useful.** Sonnet coordinates; Haiku workers execute bounded chores.
5. **Review separately.** Builder sessions get blind spots.
6. **Reset context often.** Long chats drift.

## Recommended first exercise

Take a messy prompt you recently used and rewrite it using this format:

```md
Task:
Context:
Goal:
Constraints:
Return:
```

Then run it twice:

1. As a normal prompt.
2. As a scoped prompt with a review step.

Compare output quality, token usage, and how much correction you needed.

## What to copy into your own project

At minimum:

```text
CLAUDE.md
.claude/agents/
.claude/skills/
.claude/commands/
docs/checklists/
docs/templates/
```

## Your first Claude Code prompt

```md
Task: Audit this repo setup.
Context: I copied in a Claude workflow starter kit for better vibe coding.
Goal: Tell me what files are useful, what should be customized, and what can be deleted.
Constraints: Do not edit files yet.
Return: prioritized recommendations with exact file paths.
```

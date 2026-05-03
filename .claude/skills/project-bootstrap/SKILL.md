---
name: project-bootstrap
description: Interview the user and generate a project-specific Claude Code setup from this starter kit.
---

# Project Bootstrap Skill

Use this skill when the user wants to install, adapt, or generate Claude Code configuration for a specific project.

## Core rule

Do not blindly copy the starter kit. Interview first, then customize.

## Inputs to gather

- Project purpose and target users.
- Tech stack and package manager.
- Important directories and architecture boundaries.
- Development commands.
- Testing, linting, formatting, typechecking, and build commands.
- Security/privacy/data handling rules.
- Design/product preferences.
- Model budget preferences.
- Swarm delegation preferences.
- Review gate requirements.
- Context hygiene rules.
- Files or behaviors to avoid.
- Common AI coding failure modes.

## Workflow

1. Inspect the current repo.
2. Inspect existing Claude configuration.
3. Ask grouped, high-value interview questions.
4. Summarize understanding.
5. Propose exact files to create or update.
6. Wait for approval before edits.
7. Generate concise, project-specific files.
8. Validate with safe commands.
9. Explain how to use the new setup.

## File generation guidance

Generate only what the project benefits from:

- `CLAUDE.md` for durable project rules.
- `.claude/agents/` for reusable roles.
- `.claude/skills/` for reusable workflows.
- `.claude/commands/` for repeatable task prompts.
- docs/checklists only when they reduce future prompt length.

## CLAUDE.md guidance

Keep it short. Include:

- project purpose
- non-negotiable rules
- commands
- architecture map
- AI workflow
- imports to deeper docs when needed

Avoid:

- generic AI advice
- giant duplicated docs
- stale assumptions
- vague commands
- model instructions that do not match the user's budget

## Swarm guidance

The main Sonnet session coordinates. Haiku workers do bounded chores such as repo mapping, scaffolding, docs cleanup, test drafts, and mechanical refactors.

Do not delegate:

- architecture decisions
- security-sensitive changes
- destructive commands
- ambiguous product calls
- anything requiring owner judgment

## Output after implementation

```md
## Files changed

## What each file does

## How to use this setup

## Validation

## Follow-ups
```

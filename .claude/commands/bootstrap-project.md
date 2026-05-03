# /bootstrap-project

Customize this Claude setup for the current project through an interview-first workflow.

## Use when

The user wants to install or adapt this starter kit into a real project.

## Process

1. Inspect the current project structure.
2. Inspect any existing Claude files:
   - `CLAUDE.md`
   - `.claude/agents/`
   - `.claude/skills/`
   - `.claude/commands/`
3. Ask a grouped project interview before editing.
4. Produce a merge plan with exact file operations.
5. Wait for approval.
6. After approval, generate project-specific files.
7. Run safe validation commands.
8. Return a usage guide.

## Interview topics

Ask only questions that affect the generated files:

- project purpose and users
- stack, package manager, framework, runtime, deployment
- architecture and important directories
- test/lint/typecheck/build commands
- coding standards and style preferences
- security, privacy, secrets, compliance, data handling
- AI workflow preferences: Opus, Sonnet, Haiku, review model
- swarm use cases and banned delegation cases
- review gate requirements
- context cleanup and new-chat rules
- files Claude should avoid changing
- recurring AI-coding failure modes

## Return before editing

```md
## Understanding

## Proposed Claude setup

## Proposed CLAUDE.md outline

## Proposed agents

## Proposed skills

## Proposed commands

## Merge plan

## Questions still open
```

Do not edit until the user approves.

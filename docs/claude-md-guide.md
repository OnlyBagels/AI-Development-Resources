# CLAUDE.md Guide

`CLAUDE.md` is your durable project instruction file. Treat it like onboarding documentation for your AI collaborator.

## What belongs in CLAUDE.md

- Project overview.
- Architecture boundaries.
- Coding conventions.
- Commands for test/build/lint.
- Security rules.
- Review expectations.
- Links/imports to deeper docs.

## What does not belong in CLAUDE.md

- One-off task details.
- Temporary experiments.
- Long logs.
- Secrets.
- Every possible preference you have.

## Good pattern

Keep the root `CLAUDE.md` short and import more specific docs:

```md
See @docs/model-ladder.md.
See @docs/swarm-pattern.md.
See @docs/prompt-hygiene.md.
```

## Maintenance rule

Whenever Claude learns a durable rule about the repo, decide whether it belongs in:

- `CLAUDE.md` for always-on behavior.
- A skill for task-specific behavior.
- A command for repeatable workflows.
- A doc for human education.

## Warning

A bloated `CLAUDE.md` becomes the same problem as a bloated chat. Keep it sharp.

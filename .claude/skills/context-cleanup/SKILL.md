---
name: context-cleanup
description: Prepare a compact summary or new-chat context packet from a long Claude Code session.
---

# Context Cleanup Skill

Use this skill before compacting or starting a fresh chat.

## Goal

Preserve the useful state and discard context soup.

## Extract

- Current goal.
- User intent.
- Decisions made.
- Files changed.
- Commands run.
- Validation results.
- Known issues.
- Constraints still active.
- Things not to change.
- Next action.

## Output format

```md
Current goal:

User intent:

Decisions made:

Files changed:

Commands run:

Validation results:

Known issues:

Constraints still active:

Do not change:

Next recommended action:
```

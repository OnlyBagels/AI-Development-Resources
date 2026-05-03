# Chat Hygiene

Long chats increase drift. The model carries old assumptions, abandoned ideas, and stale decisions forward.

## One chat, one job

Good:

- “Implement password reset email flow.”
- “Debug the failing checkout test.”
- “Design the homepage concept.”

Bad:

- “Build a website.”
- “Now make it a marketplace.”
- “Actually make it a game.”
- “Also fix my unrelated API.”

That is not a chat. That is context soup.

## When to start a new chat

Start a new chat when:

- The goal changes.
- You switch from planning to implementation after many messages.
- You are about to work on an unrelated bug.
- The assistant keeps referencing old constraints.
- You need a cleaner review.

## When to compact

Compact when:

- The task is still the same but the thread is long.
- Many tool calls have produced noise.
- You need to preserve decisions but remove exploration.

## Context packet

Before starting a new chat, create a context packet:

```md
Current goal:
Decisions made:
Files changed:
Known issues:
Validation already run:
Next action:
Do not change:
```

Use `docs/templates/context-packet.md`.

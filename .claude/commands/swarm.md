# /swarm

Use a Sonnet-led swarm for a multi-step coding task.

## Prompt

Apply the swarm skill to the user's task.

- Keep the main session as coordinator.
- Use Haiku workers for bounded chores.
- Use exact worker scopes and return formats.
- Merge worker outputs in the main session.
- Run a review gate before final response.

Return:

```md
Plan:
Workers:
Implementation summary:
Validation:
Risks:
```

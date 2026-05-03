# Swarm Feature Prompt

```md
Task: Implement [feature].
Context: [stack, relevant files, desired behavior]
Goal: [success definition]
Constraints: [non-goals, no new deps, style rules]
Return: final patch summary, validation, risks.

Use the swarm pattern:
- Main session: Sonnet coordinator.
- Haiku researcher: inspect relevant files and conventions only.
- Haiku scaffolder: draft boilerplate for approved files only.
- Haiku test-runner: propose or add minimal tests.
- Main session: merge outputs, make final decisions, run validation.

Worker return format:
Findings / Files / Changes / Risks / Next action.
```

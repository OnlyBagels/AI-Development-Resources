# Vibe Coding Workflow

This is the default workflow for building with Claude Code.

## 1. Define the job

Use:

```md
Task:
Context:
Goal:
Constraints:
Return:
```

## 2. Inspect before editing

Ask Claude to locate relevant files before changing them.

```md
First inspect the codebase and identify the smallest set of files likely needed. Do not edit yet.
```

## 3. Plan only as much as needed

For tiny tasks, skip elaborate planning.

For medium tasks:

```md
Return a 5-step implementation plan with risks and validation commands.
```

For large tasks, use Opus first.

## 4. Delegate cheap work

Use Haiku workers for:

- File discovery.
- Scaffolding.
- Repetitive edits.
- Test skeletons.
- Documentation drafts.
- Summarizing logs.

## 5. Implement in small patches

Tell Claude:

```md
Make the smallest patch that satisfies the task. Do not opportunistically refactor unrelated code.
```

## 6. Validate

Run available checks:

- Unit tests.
- Typecheck.
- Lint.
- Build.
- Manual smoke test.

## 7. Review

Use a separate review pass:

```md
Review this patch against the original task. Identify blockers first.
```

## 8. Ship or iterate

End with:

- What changed.
- How it was validated.
- Known risks.
- Suggested next task.

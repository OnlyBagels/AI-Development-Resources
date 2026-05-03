# Review Workflow

AI-built work needs review because builder sessions normalize their own assumptions.

## Review phases

### 1. Scope review

Does the patch solve the task that was actually requested?

Check:

- Did it add unrelated features?
- Did it ignore constraints?
- Did it invent requirements?

### 2. Correctness review

Check:

- Edge cases.
- Error states.
- Data flow.
- Type correctness.
- State management.

### 3. Security review

Check:

- Secrets.
- Auth/permission boundaries.
- Input validation.
- Unsafe shell commands.
- Dependency risk.

### 4. Maintainability review

Check:

- Simplicity.
- Naming.
- Duplication.
- Tests.
- Docs.

### 5. Validation review

Check:

- Tests run.
- Build run.
- Manual smoke test.
- Known gaps stated.

## Review prompt

```md
Task: Review this patch.
Context: Original task and constraints are below.
Goal: Find issues before merge.
Constraints: Be skeptical. Prioritize correctness, security, scope control, and maintainability.
Return:
1. Blockers
2. Non-blockers
3. Missing tests
4. Risk rating
5. Merge recommendation
```

## Reviewer rule

The reviewer should not be the same mental context as the builder. Use a new chat or separate model when possible.

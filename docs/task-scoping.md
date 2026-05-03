# Task Scoping

Most vibe coding failures start with an oversized task.

## Scope levels

### Tiny

One file, one behavior, obvious validation.

Example:

```md
Task: Add empty-state copy to the dashboard table.
Return: patch only.
```

### Small

A few files, known implementation path.

Example:

```md
Task: Add client-side validation to signup form.
Context: React app, existing form component at src/features/auth/SignupForm.tsx.
Return: implementation summary and tests run.
```

### Medium

Multiple files, some discovery needed.

Use Sonnet main session. Consider Haiku workers for file discovery and test scaffolding.

### Large

Architecture or product direction is unclear.

Use Opus for plan/design first. Then hand a scoped implementation packet to Sonnet.

## Cut a large task down

Instead of:

```md
Build a SaaS dashboard.
```

Use:

```md
Task: Design the first version of the dashboard information architecture.
Context: SaaS analytics product for small ecommerce stores.
Goal: Decide pages, navigation, and key data cards.
Constraints: No implementation yet.
Return: sitemap, page descriptions, and open questions.
```

Then:

```md
Task: Implement the dashboard shell from the approved sitemap.
Context: Use existing app layout and routing conventions.
Goal: Create navigable placeholder pages.
Constraints: No real analytics logic yet.
Return: changed files and how to run locally.
```

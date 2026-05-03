# Claude Swarm Pattern

The swarm pattern uses a capable main model to coordinate cheaper worker agents.

## Mental model

```text
Sonnet main session
├── Haiku scaffolder
├── Haiku researcher
├── Haiku test runner
├── Haiku docs writer
└── Reviewer, usually Sonnet/Opus/separate model
```

The main session owns architecture and decisions. Haiku workers execute bounded chores.

## What Sonnet should do

- Understand the user goal.
- Decide task boundaries.
- Spawn Haiku workers with narrow prompts.
- Merge worker outputs.
- Make final implementation decisions.
- Run or request review.

## What Haiku workers should do

- Inspect files.
- Generate boilerplate.
- Create test drafts.
- Summarize logs.
- Write docs drafts.
- Report concise findings.

## What Haiku workers should not do

- Change architecture.
- Expand scope.
- Make product decisions.
- Quietly ignore constraints.
- Recursively coordinate more workers.

## Worker prompt template

```md
Task: <one bounded chore>
Context: <only what this worker needs>
Boundaries: <files/directories allowed>
Do not: <explicit exclusions>
Return: <short exact format>
```

## Example swarm prompt

```md
Task: Add a basic settings page to the app.
Context: Existing React app. Keep current styling and routing conventions.
Goal: Add a settings route with profile, notifications, and billing placeholder sections.
Constraints: No backend calls. No auth changes. No new UI library.
Return: changed files, validation run, and risks.

Use the swarm pattern:
- Sonnet main session coordinates.
- Haiku researcher finds routing/layout conventions.
- Haiku scaffolder drafts page/component files.
- Haiku test-runner suggests minimal tests.
- Main session reviews and applies final edits.
```

## Good worker outputs

```md
Findings:
- Routes live in src/routes.tsx.
- Layout shell is src/components/AppShell.tsx.
- Existing settings-like card pattern is src/components/Card.tsx.

Recommended files:
- src/pages/SettingsPage.tsx
- src/routes.tsx

Risks:
- No existing tests for routes.
```

## Bad worker outputs

```md
I redesigned the whole app, added a backend, changed auth, and created ten new dependencies.
```

## Configuration reminder

In Claude Code, set worker agents to `model: haiku`. Keep coordinator work in the main Sonnet session or an agent running as the main thread.

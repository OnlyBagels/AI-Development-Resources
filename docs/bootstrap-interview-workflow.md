# Bootstrap Interview Workflow

Use this workflow when someone wants to adapt this starter kit to a real project.

The mistake to avoid: copying this repo verbatim into every project. A good Claude setup should reflect the actual codebase, stack, commands, risks, and workflow.

## Best path

1. Open Claude Code in the target project root.
2. Paste `prompts/GET_STARTED_WITH_CLAUDE_CODE.md`.
3. Replace `STARTER_REPO_URL` with the public GitHub URL for this repo.
4. Let Claude download the starter into a temporary directory.
5. Let Claude inspect both the starter and the target project.
6. Answer the interview questions.
7. Review the proposed merge plan.
8. Approve edits only after the plan looks right.

## What the interview should produce

The interview should generate project-specific versions of:

- `CLAUDE.md`
- `.claude/agents/*.md`
- `.claude/skills/*/SKILL.md`
- `.claude/commands/*.md`
- docs, templates, and checklists that match the project

## Good interview answers include

- exact package manager and commands
- test, lint, typecheck, build, and dev commands
- directories Claude should understand first
- directories Claude should not touch
- style preferences
- product/design constraints
- data/security constraints
- deployment target
- common failure modes from prior AI coding sessions

## Keep `CLAUDE.md` small

`CLAUDE.md` should not become a giant dumping ground. Keep it focused on durable, high-signal rules. Put long workflows into skills and docs.

Recommended shape:

```md
# CLAUDE.md

## Project purpose

## Non-negotiable rules

## Commands

## Architecture map

## Workflow

## Imports
@docs/claude/workflow.md
@docs/claude/review-gate.md
```

## Suggested generated assets

For most software projects, generate:

```text
CLAUDE.md
.claude/agents/project-coordinator.md
.claude/agents/haiku-repo-mapper.md
.claude/agents/haiku-test-writer.md
.claude/agents/haiku-docs-writer.md
.claude/agents/review-gate.md
.claude/skills/project-workflow/SKILL.md
.claude/skills/review-gate/SKILL.md
.claude/skills/context-cleanup/SKILL.md
.claude/commands/scope.md
.claude/commands/swarm.md
.claude/commands/review.md
.claude/commands/context-pack.md
.claude/commands/new-chat.md
```

## Review before committing

Before committing a generated Claude setup, check:

- It names this project, not generic starter-kit language.
- Commands are real and tested.
- Security/privacy rules are explicit.
- Haiku workers have bounded roles.
- Review steps are concrete.
- Context hygiene is included.
- Existing project docs were not duplicated unnecessarily.

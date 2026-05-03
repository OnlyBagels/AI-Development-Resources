# Vibe Coding With Claude

A practical, shareable starter repo for learning better AI-assisted development with Claude and Claude Code.

This repo is built around a simple idea:

> Use the strongest model only where it matters. Use cheaper, faster workers for scaffolding, research, file organization, docs, tests, and repetitive setup. Keep prompts tight. Keep chats clean. Review everything.

## Who this is for

- Developers learning how to use Claude Code without burning tokens on messy prompts.
- Builders who use Opus for planning/design, Sonnet for implementation/coordinating, and Haiku for low-complexity execution work.
- Anyone who wants a reusable `.claude/` setup with agents, skills, commands, and markdown playbooks.

## What is inside

```text
.
├── GET_STARTED_PROMPT.md             # Paste into Claude Code to bootstrap a real project
├── CLAUDE.md                         # Project-level Claude instructions
├── .claude/
│   ├── agents/                       # Coordinator + worker subagents
│   ├── commands/                     # Slash-command style workflows
│   ├── hooks/                        # Optional context-saving hook example
│   ├── settings.example.json         # Safe starting config example
│   └── skills/                       # Reusable Claude skills
├── docs/
│   ├── START_HERE.md
│   ├── bootstrap-interview-workflow.md
│   ├── swarm-pattern.md
│   ├── prompt-hygiene.md
│   ├── chat-hygiene.md
│   ├── model-ladder.md
│   ├── review-workflow.md
│   ├── checklists/
│   ├── examples/
│   └── templates/
├── prompts/                          # Copy/paste prompt recipes
├── scripts/                          # Small helper utilities
└── .github/                          # Community repo scaffolding
```

## Recommended model ladder

| Work type | Suggested model | Why |
|---|---:|---|
| Architecture, product direction, hard tradeoffs, deep debugging | Opus | Highest reasoning budget for expensive mistakes |
| Main Claude Code session, feature implementation, orchestration | Sonnet | Good balance of intelligence, speed, and cost |
| Scaffolding, search, docs cleanup, test generation, repetitive tasks | Haiku subagents | Cheap, fast, and good enough for bounded chores |
| Independent review | A separate strong reviewer | Catches mistakes the builder session normalized |


## Best first step for a new project

Use the bootstrap prompt instead of copying this repo blindly:

1. Publish or fork this repo on GitHub.
2. Open Claude Code in the target project root.
3. Paste [`prompts/GET_STARTED_WITH_CLAUDE_CODE.md`](prompts/GET_STARTED_WITH_CLAUDE_CODE.md).
4. Replace `STARTER_REPO_URL` with your repo URL.
5. Let Claude interview you, inspect the project, and propose a merge plan before editing.

This generates a project-specific `CLAUDE.md`, `.claude/agents`, `.claude/skills`, `.claude/commands`, docs, and review workflows instead of dumping generic files into every repo.

## Fast start

1. Copy `CLAUDE.md` and `.claude/` into your target project.
2. Open Claude Code from that project root.
3. Start a fresh chat for one clear task.
4. Use this prompt shape:

```md
Task: <one job>
Context: <only relevant background>
Goal: <what success looks like>
Constraints: <tech, style, scope, budget>
Return: <exact output format>
```

5. For larger work, tell Sonnet to coordinate Haiku workers:

```md
Use the swarm pattern.
Main model: Sonnet.
Workers: Haiku agents for scaffolding, file discovery, tests, docs, and cleanup.
Keep architectural decisions in the main session. Workers return concise findings only.
```

## Important Claude Code note

A Sonnet main Claude Code session can dispatch Haiku subagents when the subagents are configured with `model: haiku`. This is the intended pattern here.

Do not design the cheap workers as recursive orchestrators. Keep orchestration in the main session or in an agent running as the main thread. Workers should do bounded jobs and report back.

## Repo philosophy

- One chat = one task.
- One prompt = one outcome.
- Agents get bounded scopes.
- Docs explain durable rules; prompts explain the current job.
- Review is a separate phase, not an afterthought.
- Compact or restart before context becomes soup.

## How to use the `.claude` folder

- `.claude/agents/` defines reusable agent roles.
- `.claude/skills/` defines reusable workflows and domain knowledge.
- `.claude/commands/` gives you promptable workflow shortcuts.
- `.claude/hooks/` shows optional automation for reducing noisy context.
- `CLAUDE.md` imports deeper markdown files so the main instruction file stays small.

## Start reading

Begin with [`GET_STARTED_PROMPT.md`](GET_STARTED_PROMPT.md) for project bootstrapping, or [`docs/START_HERE.md`](docs/START_HERE.md) to learn the workflow.

## License

MIT. Use it, fork it, remix it, and improve it.

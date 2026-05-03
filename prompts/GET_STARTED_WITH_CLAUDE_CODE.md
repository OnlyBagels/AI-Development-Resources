# Get Started Prompt for Claude Code

Paste this into a fresh Claude Code chat from the root of the project you want to customize.

Before you run it, replace `STARTER_REPO_URL` with the public GitHub URL for this repo after you publish it.

```md
Task: Bootstrap this project with a project-specific Claude workflow.

Context:
- I want to use the public starter repo at: STARTER_REPO_URL
- I am in the root of the project I want to configure.
- The starter repo contains reusable Claude Code patterns: CLAUDE.md, .claude/agents, .claude/skills, .claude/commands, docs, prompts, and checklists.
- Do not blindly copy generic files. Interview me first, then customize everything to this project.

Goal:
Create a project-specific Claude setup that helps me vibe code better with Claude Code:
- a concise, useful CLAUDE.md
- project-specific .claude/agents
- project-specific .claude/skills
- useful .claude/commands
- project docs/checklists/templates that fit this repo
- a repeatable workflow for Sonnet-led coordination, Haiku worker agents, and separate review

Constraints:
- Start by downloading the starter repo into a temporary directory, not over this project.
- Inspect the starter repo structure before asking questions.
- Inspect this project structure before asking questions.
- Do not overwrite existing files without showing a merge plan first.
- Preserve existing project conventions.
- Keep CLAUDE.md short and durable. Put detailed workflows in imported docs/skills.
- Prefer project-specific rules over generic AI advice.
- Ask only high-value questions. Group them by topic.
- After the interview, produce a plan and wait for my approval before editing files.
- Use Sonnet as the main coordinator. Use Haiku subagents for bounded discovery, scaffolding, docs, tests, and cleanup when useful.
- Do not use Haiku workers for architecture, security decisions, destructive commands, or ambiguous product decisions.

Download step:
1. Create a temp directory.
2. Download or clone STARTER_REPO_URL into it.
3. List the starter files you will use.
4. List existing Claude-related files in this project, if any.

Interview me on:
1. Project purpose and target users.
2. Tech stack, package manager, framework, runtime, deployment target.
3. Current architecture and important directories.
4. Coding standards, formatting, testing, and linting commands.
5. Security, privacy, compliance, secrets, and data handling constraints.
6. Product/design preferences.
7. Model budget preferences: when to use Opus, Sonnet, Haiku, and external review.
8. Swarm preferences: which tasks should be delegated to Haiku workers.
9. Review expectations: what must be checked before code is considered done.
10. Context hygiene: when to compact, summarize, or start a new chat.
11. Files or areas Claude should avoid changing.
12. Anything that repeatedly goes wrong when I use AI coding tools.

After the interview, return:
```md
## Understanding
<short summary of my project and workflow>

## Proposed Claude setup
<files to create/update>

## Proposed CLAUDE.md outline
<short outline only>

## Proposed agents
<agent names, models, responsibilities>

## Proposed skills
<skill names and when they trigger>

## Proposed commands
<slash commands and what they do>

## Merge plan
<exact file operations, including backups if needed>

## Questions still open
<any remaining blockers>
```

Only after I approve the plan, implement the files.

Implementation rules after approval:
- Copy only useful starter files.
- Rewrite generic content into project-specific guidance.
- Add `@path` imports from CLAUDE.md only when they reduce clutter.
- Add exact validation commands from this project.
- Add a review gate command.
- Add a context-pack/new-chat command.
- Add a swarm command if the project has separable tasks.
- Add README notes explaining how this project uses Claude.
- Run safe validation commands and report results.

Return after implementation:
```md
## Files changed
<paths>

## What each file does
<brief bullets>

## How to use this setup
<first 3 commands/prompts>

## Validation
<commands run and results>

## Follow-ups
<optional improvements>
```
```

## No-Git fallback

If the LLM cannot access the public repo URL, paste or upload this zip/repo into the chat and use this alternate opening line:

```md
I uploaded the Claude workflow starter repo. Use it as the source template instead of downloading STARTER_REPO_URL. Interview me first, then customize the Claude setup for this project.
```

# Skills Guide

Skills are reusable instruction packages. Use them when a workflow is repeated often but should not always be loaded into the main context.

## When to create a skill

Create a skill when:

- You repeat the same workflow often.
- The workflow has steps/checklists/reference docs.
- The instructions are too bulky for `CLAUDE.md`.
- The skill is relevant only sometimes.

## Skill shape

```text
.claude/skills/<skill-name>/
├── SKILL.md
├── references/
└── scripts/
```

## Good skills in this repo

- `swarm`: coordinate Haiku workers from a Sonnet main session.
- `prompt-hygiene`: rewrite messy prompts into concise task specs.
- `context-cleanup`: prepare compaction or new-chat context packets.
- `review-gate`: run a structured review before merge.

## Skill frontmatter pattern

```md
---
name: prompt-hygiene
description: Rewrite messy prompts into structured Task/Context/Goal/Constraints/Return format.
---
```

## Skill writing tips

- Make the trigger description specific.
- Put reference material in separate files.
- Include exact return formats.
- Avoid giant always-on essays.
- Test the skill on real prompts and revise.

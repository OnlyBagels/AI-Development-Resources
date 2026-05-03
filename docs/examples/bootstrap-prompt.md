# Example: Project Bootstrap Prompt

This is the smallest version of the setup prompt.

```md
Task: Install a project-specific Claude Code workflow.
Context: Use this starter repo as the template: <GITHUB_REPO_URL>. I am in my project root.
Goal: Interview me, then build the right CLAUDE.md, .claude/agents, .claude/skills, and .claude/commands for this specific project.
Constraints: Download the starter into a temp directory. Inspect my project. Do not overwrite files without a merge plan and approval. Keep CLAUDE.md short. Use Sonnet as coordinator and Haiku for bounded worker tasks.
Return: interview questions first, then a proposed merge plan after I answer.
```

For the full version, use `prompts/GET_STARTED_WITH_CLAUDE_CODE.md`.

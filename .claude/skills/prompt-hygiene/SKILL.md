---
name: prompt-hygiene
description: Rewrite messy or verbose prompts into concise structured prompts with clear task, context, goal, constraints, and return format.
---

# Prompt Hygiene Skill

Use this skill when the user asks to improve a prompt, reduce token waste, clarify instructions, or make a request more effective.

## Process

1. Identify the actual task.
2. Remove filler that does not change the output.
3. Separate facts from preferences.
4. Add missing constraints only when implied by the user.
5. Define the return format.
6. Preserve the user's intent and voice where useful.

## Output format

```md
Clean prompt:

Task:
Context:
Goal:
Constraints:
Return:

Why this is better:
- 
```

## Rules

- Do not over-engineer tiny prompts.
- Do not add requirements the user did not imply.
- Keep prompts short unless complexity requires detail.

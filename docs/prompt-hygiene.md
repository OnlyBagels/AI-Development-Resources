# Prompt Hygiene

Prompt hygiene means giving the model enough information to do the job, without filling the context with vague filler.

## Default format

```md
Task:
Context:
Goal:
Constraints:
Return:
```

## Why it works

- **Task** prevents wandering.
- **Context** gives relevant background.
- **Goal** defines success.
- **Constraints** stop unwanted expansion.
- **Return** controls the output shape.

## Bad prompt

```md
Let's make a website for my project. It's about this auto sneezing robot that solves economic crisis by reading something on the website and makes a philosophical judgement so and so. Make it cool and modern and maybe add whatever sections websites usually have.
```

## Better prompt

```md
Task: Create a homepage concept.
Context: Fictional project about an auto-sneezing robot that reads website content and makes philosophical judgments about economic crises.
Goal: Make the idea clear, modern, and interesting.
Constraints: Keep it suitable for a one-page landing page. Do not invent backend features.
Return: homepage sections, short copy, and design direction.
```

## Token wasters

- Apologies and hedging.
- Long emotional setup that does not change requirements.
- Multiple unrelated tasks in one prompt.
- Repeating the same idea three ways.
- Asking for “everything” when you only need a first pass.

## High-signal context

Include:

- Current stack.
- Files involved.
- Desired behavior.
- Known constraints.
- What not to change.
- How to validate success.

Exclude:

- History that no longer matters.
- Brainstorming that is not a requirement.
- Old ideas that were rejected.
- Long logs without pointing to the relevant failure.

## Prompt cleanup checklist

Before sending:

- Can the task be completed in one session?
- Is the output format explicit?
- Did you separate facts from preferences?
- Did you remove filler?
- Did you state what should not be changed?

# Cost Control

The fastest way to save money is to stop making expensive models do cheap work.

## Principles

1. Use Opus for thinking that changes the plan.
2. Use Sonnet for implementation and coordination.
3. Use Haiku for bounded execution chores.
4. Use hooks/scripts to reduce noisy context.
5. Use skills instead of re-explaining recurring workflows.
6. Reset chats before stale context causes bad output.

## Token leaks

- Long unstructured prompts.
- Massive pasted logs.
- Asking for all options when you need one decision.
- Letting the model rediscover project structure every time.
- Keeping dead ideas in context.
- Using Opus for boilerplate.

## Cost-saving prompt

```md
Task: Solve this using the cheapest reliable approach.
Context: <task details>
Goal: Minimize expensive-model reasoning.
Constraints: Use Haiku workers for bounded discovery/scaffolding. Keep final decisions in Sonnet.
Return: plan, worker tasks, final implementation summary.
```

## Use scripts for preprocessing

Instead of pasting 10,000 lines of logs, run a script that extracts failures, stack traces, or changed files.

See `.claude/hooks/filter-test-output.sh` for an example.

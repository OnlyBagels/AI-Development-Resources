# Anti-Patterns

## The forever chat

You start with a landing page, then turn it into a SaaS app, then a marketplace, then a game.

Fix: start a new chat with a context packet.

## The vague mega-prompt

“Build me everything.”

Fix: define the next concrete artifact.

## The expensive intern

Using Opus to rename files, scaffold components, or summarize logs.

Fix: use Haiku workers.

## The architecture worker

Letting a cheap worker make system-level decisions.

Fix: keep architecture in Opus/Sonnet.

## The reviewer inside the builder

Asking the same chat that made the patch to rubber-stamp it.

Fix: review in a new context.

## The invisible constraint

You know a requirement but do not tell the model.

Fix: write explicit constraints.

## The context landfill

Pasting giant docs, logs, and old brainstorms into every prompt.

Fix: summarize, link files, or use targeted extraction.

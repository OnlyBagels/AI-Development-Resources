#!/usr/bin/env bash
set -euo pipefail

required=(
  "README.md"
  "CLAUDE.md"
  ".claude/agents/swarm-coordinator.md"
  ".claude/skills/swarm/SKILL.md"
  ".claude/commands/swarm.md"
  "docs/START_HERE.md"
  "docs/prompt-hygiene.md"
  "docs/swarm-pattern.md"
)

missing=0
for file in "${required[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing: $file"
    missing=1
  fi
done

if [[ "$missing" -eq 1 ]]; then
  exit 1
fi

echo "Repo scaffold looks complete."

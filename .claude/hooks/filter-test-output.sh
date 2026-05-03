#!/usr/bin/env bash
# Example hook idea: reduce noisy test output.
# This script is intentionally conservative. Customize for your own test runner.

set -euo pipefail

input="$(cat)"
cmd="$(printf '%s' "$input" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"

case "$cmd" in
  *test*|*vitest*|*jest*|*pytest*)
    # In real use, adapt this to your runner. This placeholder simply passes through.
    printf '%s' "$input"
    ;;
  *)
    printf '%s' "$input"
    ;;
esac

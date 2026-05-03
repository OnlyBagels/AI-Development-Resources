# Good Prompt Examples

## Feature implementation

```md
Task: Add dark mode toggle to the settings page.
Context: React + Tailwind app. Settings page is `src/pages/settings.tsx`. Theme state currently lives in `src/lib/theme.ts`.
Goal: User can switch light/dark mode and preference persists in localStorage.
Constraints: No new dependencies. Do not redesign settings page.
Return: changed files, summary, tests run, and risks.
```

## Bug fix

```md
Task: Fix the checkout page crash when cart is empty.
Context: Error occurs on `/checkout` with empty cart. Suspected file: `src/features/cart/CheckoutSummary.tsx`.
Goal: Empty cart shows a friendly message and link back to products.
Constraints: Do not change payment flow. Keep existing UI components.
Return: root cause, patch summary, validation.
```

## Review

```md
Task: Review this patch for scope and correctness.
Context: Original goal was to add an empty cart state only.
Goal: Find blockers before merge.
Constraints: Do not suggest unrelated improvements.
Return: blockers, non-blockers, missing tests, recommendation.
```

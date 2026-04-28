---
name: code-gauge
description: Pre-implementation code planning, simplification, and compatibility checks before writing or changing code. Use whenever Codex is about to write, edit, refactor, optimize, debug, review, or migrate code, especially for multi-file changes, public API or schema changes, bug fixes, performance work, architecture decisions, or any task where preserving existing behavior matters. This skill forces a brief planning gate, surfaces constraints and unknowns, checks for unnecessary abstraction and special cases, and defines a verification path before implementation begins.
---

# Code Gauge

Use this skill as a short engineering gate before changing code. The purpose is not to produce a long plan; it is to prevent unclear objectives, hidden compatibility breaks, unnecessary abstractions, and weak verification from entering the implementation.

Read only enough context to understand the task, the local design, and the risk surface. For trivial, local edits, the gauge can be compressed to a few sentences. Use the full form for multi-file changes, refactors, bug fixes with uncertain causes, public interfaces, schema changes, migrations, concurrency work, performance work, or reviews where regression risk is not obvious.

## Gauge

State the objective in concrete terms, then separate facts, assumptions, and unknowns. Identify the behaviors, interfaces, data contracts, performance properties, and rollout assumptions that must remain intact. Before proposing an implementation, ask whether the current problem is being caused by a poor data shape, misplaced boundary, brittle dependency, or control-flow structure that is forcing special cases.

Choose the smallest implementation slice that can prove the fix or feature. Prefer explicit dependencies, guard clauses, composition, and locally readable control flow. Do not introduce a new layer, framework, or abstraction unless it removes present complexity or protects a contract that is already real.

Lock the verification path before editing. Success must be demonstrated through tests, reproduction steps, type checks, lint, examples, benchmarks, rendered artifacts, or direct inspection, depending on the task. Do not claim success from intent.

For non-trivial work, emit a compact plan before edits:

```text
Objective
Constraints
Existing behavior to preserve
Facts, assumptions, and unknowns
Simplification opportunity
Minimal implementation slice
Verification
Risks
```

If a section has no content, say that explicitly. A blank section is usually a hidden assumption.

## Decision Rules

Stop and reassess when the plan adds a new abstraction without a concrete present need, accumulates branches for special cases instead of fixing the structure that created them, changes a public contract without explicit approval, or proposes verification that is weaker than the risk of the change.

By default, preserve existing behavior. Change behavior only when the user requested it or when the current behavior is demonstrably wrong.

## Additional Guidance

Read `references/linus.md` when evaluating compatibility, public interfaces, special-case-heavy code, questionable abstractions, or rules whose technical justification is unclear.

After the gauge passes, edit the smallest set of files that can solve the problem, run the strongest available checks, and report the evidence, residual risks, and any assumptions that survived implementation.

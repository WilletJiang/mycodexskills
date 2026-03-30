---
name: code-gauge
description: Pre-implementation code planning, simplification, and compatibility checks before writing or changing code. Use whenever Codex is about to write, edit, refactor, optimize, debug, review, or migrate code, especially for multi-file changes, public API or schema changes, bug fixes, performance work, architecture decisions, or any task where preserving existing behavior matters. This skill forces a brief planning gate, surfaces constraints and unknowns, checks for unnecessary abstraction and special cases, and defines a verification path before implementation begins.
---

# Code Gauge

## Overview

Run this skill before changing code. Read only enough context to understand the task, then force a short plan that protects correctness, compatibility, and simplicity before implementation starts.

## Operate as a Pre-Coding Gate

- Treat this skill as a decision gate, not a brainstorming essay.
- Keep the planning pass proportional to the task size.
- Compress the gauge to a few lines for trivial, local, low-risk edits.
- Run the full gauge for multi-file changes, refactors, bug fixes with unclear causes, public interface changes, schema changes, migrations, concurrency work, performance work, or review tasks with non-obvious risk.
- Prefer removing complexity over managing complexity.

## Run the Gauge

1. Define the objective.
State the concrete outcome in one or two sentences. Separate facts, assumptions, and unknowns when they differ.

2. Identify the governing constraints.
State which behaviors, interfaces, data contracts, tests, performance characteristics, and rollout assumptions must remain intact.

3. Identify the simplification opportunity.
Ask whether a bad data shape, boundary, dependency, or control-flow structure is forcing special cases. Prefer a structural fix over another branch, flag, or layer.

4. Choose the minimal implementation slice.
Pick the smallest change that can prove the fix or feature. Prefer composition, explicit dependencies, guard clauses, and locally obvious control flow. Avoid speculative abstractions.

5. Lock the verification path.
Decide how success will be proven before editing: tests, repro steps, type checks, lint, examples, benchmarks, or inspection of emitted artifacts. Never claim success without evidence.

## Emit This Plan Before Non-Trivial Edits

For non-trivial work, produce a short plan with these headings before editing:

```text
Objective
Constraints
Existing behavior to preserve
Assumptions / unknowns
Simplification opportunity
Minimal implementation slice
Verification
Risks
```

Keep each section short. If a section is empty, say so explicitly instead of hand-waving.

## Apply These Decision Rules

- Stop and reassess if the plan adds a new abstraction, layer, or framework without a concrete present need.
- Stop and reassess if the patch adds branches for multiple special cases instead of fixing the structure that created them.
- Stop and reassess if the change breaks a public contract, CLI, config key, file format, schema, or API without explicit approval.
- Stop and reassess if verification is weak relative to the risk of the change.
- Default to preserving existing behavior unless the task explicitly requires a behavior change.

## Load Extra Guidance Only When Needed

Read [references/linus.md](references/linus.md) when evaluating compatibility risk, public interface changes, special-case-heavy code, questionable abstractions, or whether a rule has real technical justification.

## Hand Off to Implementation

Once the change passes the gauge:

- Edit the smallest set of files that can solve the problem.
- Keep diffs local and reversible.
- Preserve existing intent unless the task explicitly requires a new behavior.
- Run the strongest available checks.
- Report evidence, remaining risks, and any assumptions that survived implementation.

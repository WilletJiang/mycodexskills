---
name: lean4
description: Use when editing .lean files, debugging Lean 4 builds, resolving type errors, filling sorries, investigating axiom warnings, searching mathlib, formalizing mathematics in Lean, or learning Lean 4 concepts. Trigger on Lean 4, mathlib, Lake, lakefile, .lean files, theorem proving, proof repair, proof refactoring, and Lean-specific build failures. Do not trigger for Coq, Rocq, Agda, Isabelle, HOL4, Mizar, Idris, Megalodon, or other non-Lean theorem provers.
---

# Lean 4 Theorem Proving

Use this skill for Lean 4 proof work, Lean build debugging, mathlib search, formalization, and Lean-specific learning. The operating principle is simple: inspect the live goal when possible, search mathlib before inventing proofs, edit incrementally, and let the type checker verify every claim.

Never change theorem statements, lemma statements, type signatures, or docstrings without explicit permission. Do not add custom axioms unless the user approves that exact move. Lean source convention is a 100-character line width; keep lines within that limit when practical and read `references/mathlib-style.md` for breaking strategy when lines exceed it.

## Command Selection

Use the command that matches the work:

| Situation | Command |
| --- | --- |
| Draft declarations from informal mathematics | `/lean4:draft` |
| Draft and prove interactively | `/lean4:formalize` |
| Formalize and prove autonomously | `/lean4:autoformalize` |
| Fill sorries with guided checkpoints | `/lean4:prove` |
| Fill sorries autonomously with explicit budgets | `/lean4:autoprove` |
| Save a safe progress checkpoint | `/lean4:checkpoint` |
| Review Lean proofs without editing | `/lean4:review` |
| Simplify strategies or use more mathlib | `/lean4:refactor` |
| Improve proof directness, clarity, or performance | `/lean4:golf` |
| Explore a project or mathlib topic | `/lean4:learn` |
| Diagnose environment or workflow failures | `/lean4:doctor` |

When a slash command is unavailable, follow the same workflow manually.

## Preferred Workflow

Start from the smallest agreed scope: one sorry, one declaration, one file, or the full project. Inspect the goal or diagnostics, search mathlib, try the simplest relevant tactic sequence, validate, and only then broaden the strategy. Avoid compiler-guided thrashing; build errors are evidence, not a plan.

When editing directly without a command, run one bounded pass. Read the goal with `lean_goal` or diagnostics with `lean_diagnostic_messages`, search with at most two LSP search tools, try the automation cascade, validate the file, and stop with a clear report. Do not turn skill-only use into an unbounded proof loop.

The usual automation order is:

```text
rfl, simp, ring, linarith, nlinarith, omega, exact?, apply?, grind, aesop
```

`exact?` and `apply?` may query mathlib and can be slow. `grind` and `aesop` are powerful but can time out. Read `references/grind-tactic.md` when SMT-style automation is central to the proof.

## Tools And Fallbacks

Prefer Lean LSP MCP tools when available: `lean_goal`, `lean_hover_info`, `lean_local_search`, `lean_leanfinder`, `lean_leansearch`, `lean_loogle`, `lean_hammer_premise`, `lean_state_search`, `lean_multi_attempt`, `lean_diagnostic_messages`, and `lean_code_actions`. Use `lean_run_code` for isolated experiments only when the live file context is not required.

If LSP tools are unavailable, use `$LEAN4_SCRIPTS` and `lake env lean` from the project root. In script-only mode, live goal inspection, tactic testing, and line-level diagnostics are unavailable, so expect slower feedback. If `$LEAN4_SCRIPTS` or required environment variables are missing, run `/lean4:doctor`.

Scratch work should prefer the live file with LSP tools, then `lean_run_code`, then temporary files outside the repository when necessary. Never create scratch files in the repository root. Stage only files touched in the current session; do not use broad staging patterns.

## Quality Gate

A proof is complete only when the agreed scope has no sorries, the relevant Lean checks pass, no unauthorized statements changed, and only standard axioms such as `propext`, `Classical.choice`, and `Quot.sound` remain. The verification ladder is live diagnostics, then `lake env lean` on the edited file, then `lake build` at checkpoint or final gate when project-wide verification is warranted.

For cold worktrees or fresh caches, run the project cache command such as `lake cache get` or `lake exe cache get` before the first expensive build. If the LSP is cold or unstable, one `lake build` may be needed to bootstrap the workspace.

## References

Read reference files only when the task needs them. Use `references/compilation-errors.md` for build errors, `references/mathlib-guide.md` and `references/lean-phrasebook.md` for search, `references/tactics-reference.md` for tactic lookup, `references/proof-templates.md` and `references/proof-refactoring.md` for proof development, `references/proof-golfing.md` and `references/performance-optimization.md` for optimization, `references/domain-patterns.md` and `references/measure-theory.md` for domain-specific mathematics, `references/lean4-custom-syntax.md` and `references/metaprogramming-patterns.md` for syntax and metaprogramming, and `references/cycle-engine.md` for the shared prove and autoprove workflow.

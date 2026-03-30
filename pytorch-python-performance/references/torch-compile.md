# torch.compile

## Scope

Use this guide when deciding whether and how to apply `torch.compile`.

## First Questions

Ask:

- Is the hot path mostly tensor code, not Python bookkeeping?
- Are shapes reasonably stable?
- Is the main call boundary obvious enough to compile?
- Is compile startup cost acceptable for the workload?

If the answers are mostly yes, try `torch.compile` early.

## Common Wins

`torch.compile` tends to help when:

- the model has many eager-mode operator boundaries
- Python overhead is meaningful
- the workload repeats the same shapes enough to amortize compilation
- fusion and scheduling opportunities exist across operator boundaries

## Common Failure Modes

Watch for:

- unsupported Python or runtime combinations
- graph breaks from unsupported Python constructs
- recompilation from constantly changing shapes or guards
- cold-start regressions on short-lived workloads
- code paths that are too dynamic to settle into a stable compiled graph

## Practical Tactics

- Compile the main model call or the hottest submodule, not everything blindly.
- Keep the input contract stable when possible.
- If a codebase is highly dynamic, start with the obvious stable subpaths.
- Use `fullgraph=True` as a diagnostic tool when you want strictness, not as a default hammer.
- Use dynamic-shape support only when the workload truly needs it.

## When to Back Off

Back away from `torch.compile` for a specific path when:

- compile time dwarfs runtime savings
- the path is too dynamic
- the performance win is inconsistent and hard to retain
- a simpler PyTorch-side change produces the same win

## Optional Diagnostics

If compile results are surprising, escalate to:

- graph-break inspection
- recompilation logging
- targeted profiling around the compiled region

Do not let this become the default first step for every task.

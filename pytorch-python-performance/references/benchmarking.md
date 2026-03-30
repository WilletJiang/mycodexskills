# Benchmarking

## Contents

- Scope
- Fair Comparison Rules
- Minimal Measurement Protocol
- What to Report
- Useful Bootstrap Commands
- Optional Profiling Escalation

## Scope

Use this guide whenever you need to quantify a PyTorch-level optimization.

This skill does not require profiler-first workflow, but it does require before-versus-after numbers.

## Fair Comparison Rules

Keep these fixed between baseline and optimized runs:

- model semantics
- input shapes
- batch size
- dtype and mixed-precision policy
- device placement
- training or inference mode

If a change also changes semantics, say so explicitly and treat the comparison as directional rather than apples-to-apples.

## Minimal Measurement Protocol

- Warm up before timing.
- Separate first-run effects from steady-state timing.
- Synchronize CUDA work before stopping the timer when timing GPU execution.
- Run enough iterations to smooth noise.
- Report both absolute time and percentage change.

Reasonable defaults:

- 20 warmup iterations
- 50 to 100 timed iterations

## What to Report

At minimum, report:

- baseline time
- optimized time
- percentage speedup or slowdown
- whether correctness still matched expectations

If memory changed materially, report that too.

## Useful Bootstrap Commands

Use these when the repository does not already provide a benchmark harness:

```bash
python3 scripts/capture_env.py > env.json
python3 scripts/bench_stmt.py --setup 'import torch; x = torch.randn(4096, 4096)' --stmt 'torch.relu(x)' --label relu
```

For callable comparison with optional `torch.compile`:

```bash
python3 scripts/compare_modes.py \
  --setup 'import torch; m = torch.nn.Linear(4096, 4096).eval(); x = torch.randn(64, 4096)' \
  --call 'm(x)' \
  --compile-target 'm' \
  --label linear
```

## Optional Profiling Escalation

Reach for profiler tools only when:

- the heuristic scan is inconclusive
- `torch.compile` is not helping and you need to understand why
- the benchmark moves but you do not know which subsystem improved

Treat profiling as a deeper diagnostic layer, not the mandatory first step.

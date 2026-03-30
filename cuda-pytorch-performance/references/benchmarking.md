# Benchmarking

## Contents

- Scope
- Choose a Fair Baseline
- Build a Benchmark Matrix
- Measurement Rules
- What to Report
- Environment Capture
- Fast Sanity Checks

## Scope

Use this guide when selecting a baseline, building a benchmark matrix, or reporting results.

## Bootstrap Commands

Use these when the repository does not already provide benchmark helpers:

```bash
python3 scripts/capture_env.py > env.json
python3 scripts/bench_stmt.py --setup 'import torch; x = torch.randn(4096, 4096, device="cuda")' --stmt 'torch.relu(x)' --label relu
```

## Choose a Fair Baseline

Compare against the strongest realistic baseline already present in the repository. Common baselines include:

- eager PyTorch
- `torch.compile`
- an existing CUDA extension
- a vendor-library implementation already wired into the project

Match the optimized path and the baseline on:

- model semantics
- dtype and mixed-precision policy
- global batch size
- input shapes
- stream semantics
- distributed reduction semantics for multi-GPU cases

If you change math mode, accumulation type, graph capture, or communication strategy, say so explicitly.

## Build a Benchmark Matrix

Do not benchmark one flattering shape and stop. Cover:

- primary production shapes
- small, medium, and large cases
- edge shapes that stress alignment, tails, or irregular dimensions
- forward-only inference when inference is in scope
- forward, backward, and optimizer step when training is in scope
- strong-scaling and weak-scaling cases when single-node multi-GPU is in scope

If the full matrix is too expensive, start with a representative subset and explain the narrowing.

## Measurement Rules

- Warm up before timing.
- Synchronize around the timed region.
- Separate first-run effects from steady-state timing.
- Run enough iterations to stabilize variance.
- Report both absolute time and relative speedup.
- Do not cherry-pick the best run.

Reasonable defaults:

- 20 to 50 warmup iterations
- 50 to 200 timed iterations

Increase the sample count when variance stays high.

## What to Report

For inference, prefer:

- end-to-end latency
- steady-state throughput
- peak memory
- kernel launch count when launch overhead matters

For training, prefer:

- forward time
- backward time
- optimizer step time when it matters
- end-to-end step time
- peak memory
- short-run stability over multiple steps

For multi-GPU, prefer:

- per-step time
- scaling efficiency
- exposed communication time
- evidence of communication-compute overlap or idle gaps

## Environment Capture

Record enough context that another engineer can interpret the result:

- GPU model and count
- driver version
- CUDA toolkit or runtime version
- PyTorch version
- target dtypes and matmul precision mode
- CPU topology and NUMA facts when relevant
- interconnect details such as PCIe or NVLink when relevant

Use `scripts/capture_env.py` when the repository does not already collect this.

## Fast Sanity Checks

Suspect the benchmark before trusting the number when:

- the first run is much slower than the rest and you mixed it into steady-state timing
- the optimized path changed shapes, dtypes, or global batch
- timing excludes host-to-device transfer that the user actually pays for
- asynchronous work is not synchronized before stopping the timer
- a single shape improves while the representative set regresses

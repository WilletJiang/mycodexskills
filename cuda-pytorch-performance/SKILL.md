---
name: cuda-pytorch-performance
description: Optimize PyTorch workloads with CUDA kernels, CUDA C++ extensions, and NVIDIA vendor libraries for single-node GPU performance. Use when Codex needs to profile bottlenecks, improve training or inference latency or throughput, build or tune custom CUDA ops, evaluate cuBLAS, cuBLASLt, cuDNN, CUB, or NCCL paths, reduce memory or launch overhead, or validate correctness and numerical tradeoffs on single-GPU or single-node multi-GPU systems.
---

# CUDA PyTorch Performance

Use this skill to improve end-to-end PyTorch performance on CUDA without losing correctness, numerical clarity, or maintainability.

## Workflow

1. Characterize the workload before changing code.
2. Measure the current path with a fair baseline and representative shapes.
3. Classify the dominant bottleneck before choosing an optimization.
4. Prefer the simplest high-leverage fix that addresses the measured bottleneck.
5. Re-check correctness, numerical behavior, and regressions after each meaningful change.
6. Finish with reproducible benchmark evidence and explicit tradeoffs.

## Characterize the Workload

Record these facts up front:

- training, inference, or both
- single-GPU or single-node multi-GPU
- latency-sensitive, throughput-oriented, or mixed
- dominant shapes plus edge shapes
- dtype and matmul policy: FP32, TF32, FP16, BF16, or mixed precision
- current baseline path: eager, `torch.compile`, existing extension, or vendor-library implementation
- success metric: wall time, tokens per second, samples per second, memory, or scaling efficiency

Treat repository-specific file layouts as local facts to discover, not assumptions to impose.

## Choose the Optimization Path

Use this rough order unless profiling shows otherwise:

1. Remove avoidable data movement, layout churn, and synchronization.
2. Use vendor-library paths when they already solve the hot operation well.
3. Fuse memory-bound operator chains when launch or bandwidth overhead dominates.
4. Write custom CUDA kernels only when a library path is missing or measurably inferior.
5. Tune communication overlap and bucketization when multi-GPU scaling is the real bottleneck.

Do not ship a custom kernel just because it is impressive. Ship the path that is fastest, defensible, and maintainable for the actual workload.

## Read References as Needed

- Read [references/benchmarking.md](./references/benchmarking.md) for baseline selection, benchmark matrices, and reporting rules.
- Read [references/optimization-playbook.md](./references/optimization-playbook.md) for bottleneck diagnosis and optimization ordering.
- Read [references/pytorch-extension-patterns.md](./references/pytorch-extension-patterns.md) for extension layout, binding rules, and dispatch guidance.
- Read [references/multi-gpu-nccl.md](./references/multi-gpu-nccl.md) for single-node multi-GPU communication and overlap work.
- Read [references/numerics-and-correctness.md](./references/numerics-and-correctness.md) for tolerances, gradient checks, and training validation.
- Read [references/portability-and-arch-targeting.md](./references/portability-and-arch-targeting.md) for architecture targets, fallbacks, and portability rules.
- Read [references/system-triage-and-failure-modes.md](./references/system-triage-and-failure-modes.md) when GPU kernels look fine but end-to-end performance, memory, or scaling still disappoints.

Load only the files that matter for the current task.

## Use Bundled Scripts

- Run `scripts/capture_env.py` to capture GPU, driver, PyTorch, and topology facts in JSON.
- Run `scripts/bench_stmt.py` for a quick warmup-and-timing harness around Python statements.
- Run `scripts/profile_nsys.sh` to launch a command under Nsight Systems with sensible defaults.

Prefer the repository's existing benchmark or profiling harness when one already exists. Use the bundled scripts to bootstrap a disciplined workflow when the repository does not provide one.

## Deliverable Expectations

Finish with:

- the measured baseline and optimized numbers
- the benchmark matrix or the reason it was narrowed
- correctness and numerical validation evidence
- any unsupported shapes, dtypes, architectures, or fallback paths
- a short explanation of why the chosen path won

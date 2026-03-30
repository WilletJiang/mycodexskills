---
name: pytorch-python-performance
description: Optimize PyTorch training and inference performance before reaching for custom CUDA or C++ extensions. Use when Codex needs to inspect a PyTorch codebase, identify likely Python- or framework-level bottlenecks, apply high-leverage optimizations such as torch.compile, inference_mode, AMP, DataLoader tuning, better batching, memory-format changes, or host-threading fixes, and quantify before-versus-after speedups on CPU or GPU.
---

# PyTorch Python Performance

Use this skill to squeeze more speed out of PyTorch while staying in ordinary Python and built-in framework features.

This skill is heuristic-driven. Start by scanning for likely high-value fixes, then prove the win with before-versus-after measurements. Treat profiler work as optional escalation, not the default first step.

## Workflow

1. Classify the workload: training or inference, CPU or GPU, latency or throughput.
2. Run a heuristic scan of the code and execution path.
3. Pick the top three to five optimizations that look both plausible and cheap to test.
4. Benchmark each change against the baseline with the same shapes, dtype policy, and semantics.
5. Keep the changes that clearly win and do not break correctness.
6. Escalate to `cuda-pytorch-performance` only when PyTorch-level gains are exhausted or the hot path clearly demands custom kernels.

## Heuristic Priorities

Check these first unless the repository strongly suggests otherwise:

1. Missing `torch.compile`, `model.eval()`, `torch.inference_mode()`, or mixed precision.
2. Python hot-path issues such as tiny op loops, synchronization points, or repeated object creation.
3. Data pipeline issues such as weak `DataLoader` settings, heavy `collate_fn`, or host-side preprocessing bottlenecks.
4. Host-side issues such as bad thread counts, oversubscription, or GPU starvation from CPU work.
5. Memory-format or built-in fast-path opportunities such as `channels_last` or better batching.

## Read References as Needed

- Read [references/heuristic-checklist.md](./references/heuristic-checklist.md) first for the LLM-oriented optimization scan.
- Read [references/benchmarking.md](./references/benchmarking.md) to quantify before-and-after differences fairly.
- Read [references/torch-compile.md](./references/torch-compile.md) for compile strategy, graph breaks, and recompilation issues.
- Read [references/runtime-modes-and-autograd.md](./references/runtime-modes-and-autograd.md) for `eval`, `no_grad`, `inference_mode`, and grad-reset behavior.
- Read [references/precision-and-memory-format.md](./references/precision-and-memory-format.md) for AMP, dtype policy, and `channels_last`.
- Read [references/data-pipeline.md](./references/data-pipeline.md) for `DataLoader`, pinning, worker lifetime, and collation issues.
- Read [references/host-and-threading.md](./references/host-and-threading.md) for CPU threads, multiprocessing, and host-driven bottlenecks.
- Read [references/escalate-to-cuda.md](./references/escalate-to-cuda.md) when PyTorch-level changes stop paying off.

## Use Bundled Scripts

- Run `scripts/capture_env.py` to capture Python, PyTorch, CPU, and CUDA environment facts.
- Run `scripts/bench_stmt.py` to time a Python statement with warmup, optional CUDA sync, and JSON output.
- Run `scripts/compare_modes.py` to compare eager and compiled execution paths around the same callable.

Prefer the repository's existing benchmark harness when it exists. Use the bundled scripts to bootstrap comparisons quickly when the repository does not provide one.

## Success Criteria

Finish with:

- the baseline and optimized numbers
- the percentage change
- the exact semantic assumptions that stayed fixed
- any correctness or numerical caveats
- a short explanation of why the winning change helped

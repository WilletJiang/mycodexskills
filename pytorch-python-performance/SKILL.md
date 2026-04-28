---
name: pytorch-python-performance
description: Build and modify PyTorch training or inference code with a coding-time performance harness. Use when implementing modules, losses, data pipelines, training loops, inference paths, batching logic, torch.compile adoption, AMP, runtime modes, DataLoader tuning, or other performance-sensitive PyTorch work, especially when GPU experiments will run on remote hardware rather than the local machine.
---

# PyTorch Performance Harness

Use this skill while writing performance-sensitive PyTorch code, not only after a slowdown appears. Treat the implementation and its measurement harness as one deliverable. A change is incomplete until there is a reproducible way to exercise the hot path, check correctness, run representative shapes, and record timing evidence.

The local machine may be a Mac without CUDA. That is acceptable for editing, unit tests, CPU smoke tests, shape checks, and small correctness checks. It is not evidence of GPU performance. When the target workload runs on NVIDIA GPUs, create or update the GPU harness during coding and run it on the remote GPU environment when access is available. If GPU execution is not available in the current turn, leave the harness runnable and clearly mark GPU results as pending.

## Harness Contract

Before changing the hot path, define the workload contract: training or inference, target device, expected tensor shapes, edge shapes, dtype policy, batch policy, randomness, correctness oracle, and success metric. Then add or update a small harness near the codebase's existing tests, benchmarks, experiments, or scripts. Prefer local repository conventions over creating a new directory.

The harness should contain a deterministic input generator, a correctness check against the existing implementation or a mathematically equivalent oracle, a benchmark entry point with warmup and synchronized timing on CUDA, and a remote GPU run recipe. Capture the git revision, Python version, PyTorch version, device name, dtype, shape matrix, command line, and result path.

Do not rewrite a model around `torch.compile`, AMP, pinned memory, or DataLoader changes without putting those modes behind the harness. Each mode must be separately runnable so regressions can be attributed.

Read `references/coding-harness.md` before implementing substantial performance-sensitive PyTorch changes.

## Coding Workflow

Start with a minimal baseline that already exercises the real code path. Then implement the smallest production change and keep the harness in sync. Use CPU smoke tests locally to catch shape, dtype, and autograd mistakes. Use the remote GPU harness for actual latency, throughput, memory, and compile-amortization claims.

Prefer high-leverage framework changes before custom kernels: runtime modes, batching, `torch.compile`, AMP, memory format, data loading, host threading, synchronization removal, and fewer tiny operations. Keep only changes that preserve semantics and win under the harness. Escalate to `cuda-pytorch-performance` when the PyTorch-level harness shows a stable bottleneck that needs CUDA kernels, vendor libraries, or extension work.

## References

Use `references/coding-harness.md` for the coding-time harness model. Use `references/heuristic-checklist.md` for the scan, `references/benchmarking.md` for fair comparisons, `references/torch-compile.md` for graph breaks and recompilation, `references/runtime-modes-and-autograd.md` for runtime modes, `references/precision-and-memory-format.md` for AMP and `channels_last`, `references/data-pipeline.md` for input pipelines, `references/host-and-threading.md` for CPU scheduling, and `references/escalate-to-cuda.md` when Python-level work is the wrong layer.

## Scripts

Prefer the repository's own harness when it is credible. Use the bundled scripts to bootstrap missing pieces:

```bash
python scripts/capture_env.py
python scripts/bench_stmt.py --help
python scripts/compare_modes.py --help
```

## Completion Standard

Finish with the code change, the harness or harness update, local smoke evidence, remote GPU evidence when available, correctness checks, shape and dtype coverage, exact commands, result location, and remaining performance assumptions. A claim about GPU speed without a GPU harness run is only a hypothesis.

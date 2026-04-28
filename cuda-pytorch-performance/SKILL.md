---
name: cuda-pytorch-performance
description: Build and modify CUDA, CUDA extension, and GPU-accelerated PyTorch code with a coding-time GPU harness. Use when implementing or reviewing custom kernels, CUDA C++ extensions, Triton or vendor-library paths, cuBLAS, cuBLASLt, cuDNN, CUB, NCCL, stream and memory behavior, launch configuration, single-node multi-GPU execution, or remote GPU experiment workflows.
---

# CUDA PyTorch Performance Harness

Use this skill while coding GPU paths, not only after performance disappoints. Treat GPU execution as a coherent stack: source code, CUDA toolkit, host compiler, PyTorch extension build, launcher, scheduler allocation, device visibility, correctness checks, and benchmark evidence must agree before kernel tuning is meaningful.

The local machine may be a Mac. Use it for editing, static review, CPU fallbacks, packaging checks, and host-side tests. Do not treat it as CUDA validation. For CUDA kernels, extensions, and NVIDIA vendor-library paths, create the build and run harness during coding and execute it on the target GPU environment when access is available. If remote execution is unavailable, leave the harness complete and mark CUDA results as pending.

## Harness Contract

Before changing a CUDA path, define the execution model: single GPU, one process per GPU, or single-node multi-GPU. Identify the target GPU architecture when known, CUDA toolkit, host compiler, PyTorch version, dtype policy, shape matrix, memory layout, correctness oracle, and success metric.

The harness must include a minimal build path, a minimal run path, correctness validation, representative benchmark inputs, environment capture, and a remote GPU launch recipe. For scheduler-owned environments, let the scheduler define GPU visibility and inspect the visible device set inside the job step. Do not hard-code device selection until scheduler mapping and local rank behavior are understood.

Read `references/coding-harness.md` before implementing substantial CUDA, extension, or vendor-library changes.

## Coding Workflow

Get a small correct baseline running before tuning. Validate the baseline on one GPU before multi-GPU, one node before multi-node, default-stream correctness before stream overlap, and memory capacity before transfer tuning. Use vendor libraries when they solve the hot operation well. Write custom kernels only when the harness shows that a library or PyTorch path is missing, unsuitable, or measurably inferior.

Profile only after correctness, device visibility, build compatibility, and launch configuration are trustworthy. Nsight or kernel-level timing cannot compensate for broken rank mapping, wrong devices, ABI drift, or invalid memory behavior.

## References

Use `references/coding-harness.md` for the coding-time GPU harness model. Use `references/benchmarking.md` for baseline design, `references/optimization-playbook.md` for bottleneck diagnosis, `references/pytorch-extension-patterns.md` for extension layout and dispatch, `references/multi-gpu-nccl.md` for communication and overlap, `references/numerics-and-correctness.md` for tolerances, `references/portability-and-arch-targeting.md` for architecture targets and fallbacks, and `references/system-triage-and-failure-modes.md` when kernels look fast but the complete workload does not.

## Scripts

Prefer repository-native build, test, and benchmark harnesses when they exist. Use the bundled scripts to bootstrap missing pieces:

```bash
python scripts/capture_env.py
python scripts/bench_stmt.py --help
bash scripts/profile_nsys.sh --help
```

## Completion Standard

Finish with the code change, build command, launch command, environment record, correctness evidence, benchmark matrix, remote GPU result when available, unsupported shapes or architectures, and remaining assumptions. A CUDA optimization without a runnable GPU harness is not complete.

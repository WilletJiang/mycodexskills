# System Triage and Failure Modes

## Contents

- Scope
- System Triage
- Memory and Workspace Checks
- When to Use CUDA Graphs
- Correctness Failure Modes
- Performance Failure Modes
- Portability Failure Modes

## Scope

Use this guide when the kernel-level story looks reasonable but end-to-end results, memory behavior, or portability are still disappointing.

## System Triage

Look beyond the hot kernel when performance is poor:

- pageable host memory instead of pinned memory
- blocking copies instead of nonblocking copies
- repeated transfers of tensors that could stay resident on device
- missing prefetch or double buffering
- CPU affinity or data-loader placement problems
- NUMA mismatches between CPUs, PCIe root complexes, and GPUs
- host launch overhead starving the GPU

GPU kernels often get blamed for problems that really start on the host.

## Memory and Workspace Checks

Track more than wall time:

- peak memory
- allocator fragmentation
- cuBLAS or cuDNN workspace sizes
- whether fusion reduced traffic but raised memory pressure too far
- whether a faster path only works because it silently consumes much more memory

A path that is faster but operationally fragile is usually not the right production answer.

## When to Use CUDA Graphs

CUDA Graphs are promising when all of these are true:

- launch overhead is a visible bottleneck
- shapes and control flow are sufficiently static
- capture is semantically safe
- the measured gain is worth the extra complexity

Avoid graph capture when the workload is highly dynamic or depends on unsupported side effects.

## Correctness Failure Modes

Check for:

- indexing or boundary bugs
- hidden shape or stride assumptions
- incorrect dtype conversion or accumulation behavior
- changed reduction order with undocumented drift
- missing synchronization
- incorrect contiguous-layout assumptions
- architecture-specific behavior masked by one test case

## Performance Failure Modes

Check for:

- no real drop in memory traffic
- fusion that raises register pressure enough to hurt occupancy
- launch tuning that only works for one shape
- tensor-core paths disabled by layout, dtype, or alignment mismatch
- faster kernels that accidentally reduce communication overlap
- host-side bottlenecks dominating the timeline

## Portability Failure Modes

Check for:

- hardcoded architecture targets
- shared-memory assumptions that fail on another device
- register-budget assumptions that collapse occupancy elsewhere
- unsupported instructions on non-target hardware
- vectorized accesses that break on tail cases or misalignment

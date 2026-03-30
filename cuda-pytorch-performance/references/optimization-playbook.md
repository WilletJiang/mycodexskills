# Optimization Playbook

## Scope

Use this guide when you have baseline numbers and need to decide what to optimize next.

## Work Backward from the Bottleneck

Classify the dominant constraint before writing kernels:

- compute-bound
- memory-bandwidth-bound
- launch-bound
- host-side orchestration-bound
- communication-bound

Inspect a profiler timeline, not just aggregate wall time. A fast kernel can still lose end-to-end if transfers, synchronization, or collectives dominate.

## Preferred Order of Attack

1. Fix algorithmic or data-movement waste.
2. Remove redundant layout conversions, reads, writes, and temporary allocations.
3. Use fused vendor-library paths before custom kernels.
4. Fuse memory-bound operator chains when launch count or memory traffic dominates.
5. Tune custom kernels only after the system-level bottleneck is clear.
6. Revisit communication overlap after single-GPU kernels improve.

## Memory and Tensor-Core Guidance

When the hot path is bandwidth- or compute-sensitive, look for:

- coalesced global memory access
- vectorized loads and stores when alignment allows
- shared-memory tiling and bank-conflict avoidance
- register blocking that does not destroy occupancy
- tensor-core friendly shapes, dtypes, and library configurations
- async copy or deeper pipelining only when profiling justifies the extra complexity

Avoid elaborate persistent-kernel or software-pipeline logic unless simpler paths clearly leave performance on the table.

## Roofline Thinking

For important kernels, estimate whether the limiting factor is:

- memory bandwidth
- math throughput
- launch latency
- communication

Use that diagnosis to choose the next experiment. Do not spend hours on instruction-level tuning for a kernel that is really waiting on memory or collectives.

## Launch and Host Overhead

When kernels are individually fast but end-to-end time is still poor, inspect:

- too many tiny launches
- Python overhead in tight loops
- accidental synchronization on the default stream
- repeated CPU-side graph construction
- data staging that belongs outside the hot path

CUDA Graphs can help when shapes and control flow are stable and capture is safe. Do not force graph capture into dynamic or side-effect-heavy workloads.

## Autotuning Discipline

Autotuning is useful when tile shapes, staging depth, or launch parameters vary meaningfully across workloads. Keep it disciplined:

- tune against the benchmark matrix, not one flattering shape
- cache chosen configurations
- avoid retuning inside the hot path
- use autotuning late, after the basic kernel or library choice is already sound

## Library vs Custom Kernel

Prefer a vendor-library path when it:

- already covers the operator semantics
- supports the required dtype and layout
- is competitive on the target shapes
- keeps backward and maintenance burden manageable

Reach for a custom kernel when:

- the operator chain is memory-bound and fusion matters
- the project needs a layout or epilogue the library path cannot express
- the hot path is dominated by small or irregular shapes that the library handles poorly
- profiling shows an existing implementation is clearly leaving performance on the table

## Regression Questions

Ask these after each meaningful change:

- Did kernel count drop?
- Did total memory traffic drop?
- Did tensor-core utilization improve?
- Did occupancy fall because register pressure rose?
- Did one shape improve while representative shapes regressed?
- Did faster local compute accidentally reduce communication overlap?

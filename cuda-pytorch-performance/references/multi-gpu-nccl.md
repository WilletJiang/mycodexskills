# Multi-GPU and NCCL

## Scope

Use this guide for single-node multi-GPU optimization. Treat communication as a first-class bottleneck.

## Default Collective Guidance

Use NCCL for collectives unless the framework already provides an equivalent proven path. Common patterns:

- data parallel: all-reduce or reduce-scatter plus all-gather
- tensor parallel: all-gather or reduce-scatter around GEMM boundaries
- pipeline or hybrid parallel: a mix of NCCL collectives and peer-to-peer transfers

Avoid ad hoc host-orchestrated communication when NCCL already solves the problem.

## Overlap Rules

- Optimize the local compute path first, then revisit overlap.
- Use dedicated communication streams when semantics allow it.
- Use events and stream dependencies instead of broad synchronization.
- Start communication when each bucket becomes ready, not only at the end of the step.
- Verify overlap in the timeline instead of assuming separate streams are enough.

For training, overlap backward compute with gradient communication whenever possible.

## Bucketization and Granularity

Tune bucket sizes so collectives are neither tiny nor so large that they delay readiness.

Watch for:

- too many small collectives
- large idle gaps before collectives start
- bucket policies that became stale after kernel fusion changed readiness order

If faster kernels make overlap worse, revisit communication scheduling before claiming victory.

## Synchronization Discipline

Avoid:

- hidden sync points on the default stream
- device-wide synchronization in the hot path
- host waits that destroy overlap
- extra communicators unless profiling shows they help

## Signs of Healthy Scaling

Look for:

- decreasing exposed communication time
- stable or improving scaling efficiency
- no large idle gaps before or after collectives
- no regression where a faster local kernel causes later collectives to serialize

## Validate More Than Step Time

Check:

- global-batch semantics
- reduction semantics
- numerical drift from changed reduction ordering
- rank placement and host NUMA locality when the machine topology matters

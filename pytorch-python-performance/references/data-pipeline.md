# Data Pipeline

## Scope

Use this guide when training or inference appears to stall between accelerator bursts or when input preparation is heavy.

## First Checks

Inspect:

- `num_workers`
- `pin_memory`
- `prefetch_factor`
- `persistent_workers`
- `collate_fn`
- where transforms and decoding happen

## Common Wins

Look for:

- moving expensive work earlier in the pipeline
- enabling pinned memory for GPU-bound workloads
- keeping workers alive across epochs
- increasing worker count until returns flatten or contention appears
- simplifying `collate_fn` logic

## Common Failure Modes

Watch for:

- worker startup overhead every epoch
- RAM blowups from aggressive prefetching
- custom batch objects that bypass pinned-memory benefits
- GPU starvation hidden behind "the model is slow"
- duplicated preprocessing in both dataset and training step

## Decision Rule

If the accelerator is not staying busy, fix the data path before touching deeper model optimizations.

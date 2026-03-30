# Host and Threading

## Scope

Use this guide when the host side may be limiting PyTorch throughput.

## What to Check

Inspect:

- intra-op and inter-op thread counts
- library thread pools
- multiprocessing patterns
- dataloader worker competition
- CPU affinity or NUMA concerns when they are visible in the environment

## Common Failure Modes

Look for:

- too many threads fighting each other
- dataloader workers starving the main process
- oversubscription from nested thread pools
- CPU preprocessing that dominates step time

## Practical Rule

Do not assume "more threads means faster." Tune host-side parallelism the same way you tune batch size: change one thing, benchmark, keep or discard.

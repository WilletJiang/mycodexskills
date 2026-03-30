# Heuristic Checklist

## Scope

Use this checklist for a quick, high-leverage scan before diving into specialized debugging.

## Run-State Checks

Check whether the repository is missing the obvious large wins:

- `model.eval()` for inference
- `torch.inference_mode()` or at least `torch.no_grad()` for inference
- `torch.compile` on the main forward path
- AMP for GPU-heavy training or inference
- `optimizer.zero_grad(set_to_none=True)` when training semantics allow it

## Python Hot-Path Checks

Look for:

- Python loops around many tiny tensor ops
- repeated tensor creation in the steady-state hot path
- frequent `.item()`, `.cpu()`, `.numpy()`, or printing of CUDA tensors
- conditionals or bookkeeping inside the inner step that could move outward
- repeated shape conversion, casting, or device moves

These issues often block `torch.compile` gains even when the kernels themselves are fine.

## Data Pipeline Checks

Look for:

- low or untuned `num_workers`
- missing `pin_memory` for GPU training or inference
- expensive `collate_fn` logic
- data transforms happening too late in the pipeline
- worker churn from missing `persistent_workers`
- signs that the accelerator is waiting for data

## Execution-Shape Checks

Look for:

- highly dynamic shapes that may trigger recompilation
- tiny batch sizes that make launch or Python overhead dominant
- unnecessary padding churn
- repeated layout conversions such as `permute(...).contiguous()`

## Host-Side Checks

Look for:

- too many CPU threads
- dataloader workers competing with compute threads
- oversubscription from multiprocessing or library threads
- a host-heavy preprocessing path hiding behind "model is slow"

## Decision Rule

Pick the top three to five items that:

- seem likely to matter
- are cheap to change
- can be benchmarked quickly

Do not try to improve everything at once. Change, measure, keep or discard, then continue.

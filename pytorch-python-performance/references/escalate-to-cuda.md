# Escalate to CUDA

## Scope

Use this guide when deciding whether PyTorch-level optimization has reached diminishing returns.

## Stay in This Skill While

Stay with `pytorch-python-performance` when large wins still seem available from:

- `torch.compile`
- runtime-mode cleanup
- AMP or dtype changes
- data-pipeline tuning
- better batching or memory-format choices
- Python hot-path simplification

## Hand Off to CUDA When

Escalate to `cuda-pytorch-performance` when:

- the hot path is already clean PyTorch and still dominates runtime
- built-in fast paths have been tried or ruled out
- the bottleneck is clearly a kernel or fused-op opportunity
- library selection, custom kernels, or multi-GPU communication design now matter more than Python structure

## Hand-Off Note

When escalating, preserve:

- the benchmark harness
- the best PyTorch baseline
- the dtype policy
- the correctness expectations

The CUDA skill should start from a strong PyTorch baseline, not from the original slow path.

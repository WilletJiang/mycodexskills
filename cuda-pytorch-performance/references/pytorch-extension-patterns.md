# PyTorch Extension Patterns

## Scope

Use this guide when building or reviewing a CUDA extension for PyTorch.

## Separate Responsibilities Cleanly

Keep the binding layer thin. Let it handle:

- tensor validation
- shape, stride, dtype, and device checks
- output allocation
- stream lookup
- Python registration

Keep performance-critical math out of the binding layer. Put it in:

- CUDA kernels in `.cu`
- vendor-library orchestration in performance-critical `.cpp`
- lightweight Python wiring only when needed for module integration or autograd plumbing

## Binding Layer Rules

It is fine for a binding file to use PyTorch and ATen metadata APIs such as:

- `torch::Tensor`
- `TORCH_CHECK`
- `torch::empty_like`
- `c10::cuda::getCurrentCUDAStream()`

Do not use the binding layer as a hidden place to re-run the eager model or high-level PyTorch math.

## Performance-Critical C++ and CUDA Rules

Avoid calling high-level PyTorch operators from performance-critical C++ and CUDA code. Prefer:

- raw CUDA kernels
- CUDA runtime or driver APIs
- cuBLAS or cuBLASLt
- cuDNN
- CUB
- NCCL for collectives

Do not reimplement a standard primitive with custom kernels unless evidence shows the custom path is needed and faster.

## Python Wiring Rules

Python can handle:

- module and parameter wiring
- state-dict compatibility
- autograd registration
- dispatch and fallback selection
- explicit distributed setup

Python should not hide the hot math path when the point of the task is to accelerate it.

## Extension Design Checklist

- Support the real dtypes and layouts used by the workload.
- Fail loudly on unsupported inputs instead of silently producing wrong results.
- Keep fallback paths explicit and documented.
- Treat forward-only acceleration as incomplete when backward still dominates training time.
- Respect the repository's existing build system unless there is a strong reason to change it.
- Choose launch dimensions from measured behavior, not habit.
- Watch register use, shared-memory use, and occupancy together.
- Prefer clear high-performance code over opaque tricks that nobody will maintain.

## Minimal Binding Sketch

```cpp
#include <torch/types.h>
#include <c10/cuda/CUDAStream.h>

extern "C" void my_kernel_launcher(
    float* output,
    const float* input,
    int64_t size,
    cudaStream_t stream);

torch::Tensor my_kernel_forward(torch::Tensor input) {
    TORCH_CHECK(input.is_cuda(), "input must be CUDA");
    TORCH_CHECK(input.is_contiguous(), "input must be contiguous");
    TORCH_CHECK(input.scalar_type() == torch::kFloat32, "expected float32");

    auto output = torch::empty_like(input);
    auto stream = c10::cuda::getCurrentCUDAStream().stream();
    my_kernel_launcher(
        output.data_ptr<float>(),
        input.data_ptr<float>(),
        input.numel(),
        stream);
    return output;
}
```

Use this shape as a boundary reference, not as a demand to mirror these exact filenames.

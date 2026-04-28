# CUDA Coding-Time Harness

CUDA performance work should produce a harness at the same time as the implementation. The harness proves that the GPU stack can build, launch, validate correctness, and measure the intended workload on the target hardware.

## Stack Baseline

Start by recording the stack boundary. The relevant facts are CUDA toolkit, host compiler, PyTorch version, extension build path, target GPU architecture, launcher, scheduler allocation, visible devices, dtype policy, and shape matrix. On managed clusters, capture these facts inside the scheduler job or interactive allocation, not only in the login shell.

The first executable target should be minimal. For a CUDA extension, that means importing the extension, running one small input, and comparing against a reference path. For a vendor-library path, it means proving that the chosen library call handles the target shape, dtype, layout, and batching contract. For a custom kernel, it means validating a small shape before broadening the benchmark.

## Remote GPU Launch

When the development machine has no NVIDIA GPU, create the harness locally and run only non-CUDA checks there. The GPU launch command should be concrete enough to run through SSH, Slurm, or the repository's experiment runner. A scheduler launch should request GPU resources explicitly, inspect `CUDA_VISIBLE_DEVICES` or equivalent visibility inside the job, and print the selected device from the program.

Use one GPU first. Move to one-node multi-GPU only after the single-GPU path is correct and measured. Use one rank per GPU as the default distributed baseline unless the application documents another model. If MPI or NCCL is involved, record rank-local device selection and avoid assuming that global rank zero maps to physical GPU zero.

## Correctness And Timing

Correctness comes before timing. Compare against a PyTorch reference, an existing implementation, or a mathematically equivalent oracle. State tolerances by dtype and operation. Test edge shapes, non-contiguous inputs when supported, and the memory layout expected by production.

Timing must separate setup, compilation, warmup, and steady-state measurement. Synchronize CUDA timing around measured regions. Record memory use when memory pressure is part of the claim. For stream or overlap work, first prove that dependencies permit overlap, buffers are on compatible streams, and synchronization points are intentional.

## Build And Failure Discipline

Do not assume `nvcc` accepts any host compiler on the machine. Prefer a validated CUDA and host compiler pair from the remote site or container. If build failures mention unsupported compilers, ABI mismatch, missing architectures, or extension import errors, reduce to the smallest build target before changing production code.

Treat failures as harness outputs. Useful findings include wrong device visibility, all ranks selecting the same GPU, CUDA out-of-memory, illegal memory access, numerical drift, unsupported dtype, excessive launch overhead, unexpected synchronization, and extension rebuild churn.

## Reporting

Report the exact build command, launch command, scheduler request when used, device mapping, environment capture, correctness tolerance, benchmark shapes, timing result, memory result when relevant, and whether the measurement came from the target GPU environment. If the GPU run is pending, leave the command and expected output path ready for execution.

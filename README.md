<div align="center">
  <h1>mycodexskills</h1>
  <p><strong>Codex skills for serious technical work.</strong></p>
  <p>Focused on <code>latex</code>, <code>cuda</code>, <code>python</code>, and <code>code</code>.</p>
</div>

## Focus

This repository is not meant to be a random dump of prompts.

Its center of gravity is technical work that benefits from sharp, reusable workflows:

- planning code before implementation
- polishing LaTeX math
- optimizing PyTorch at the Python level
- optimizing PyTorch with CUDA and vendor libraries
- testing and validating real code changes

The core idea is simple:

> keep the skills that encode judgment, not the ones you can trivially recover from web search.

## Core Skills

| Skill | Purpose |
|------|---------|
| `code-gauge` | pre-coding planning, simplification, compatibility, and verification gates |
| `latex-formula-polish` | clean up LaTeX math layout without changing meaning |
| `pytorch-python-performance` | speed up PyTorch before reaching for CUDA |
| `cuda-pytorch-performance` | optimize GPU-side PyTorch execution with CUDA/C++ and vendor libs |
| `webapp-testing` | verify local web apps and browser behavior with Playwright |

## Secondary Skills

These are still useful, but they are not the main reason this repo exists:

- `docx`
- `pdf`
- `pptx`
- `xlsx`
- `frontend-design`
- `web-artifacts-builder`

## Quick Install

### Install as Your Main Skills Directory

```bash
git clone https://github.com/WilletJiang/mycodexskills.git ~/.codex/skills
```

### Or Symlink Only the Skills You Want

```bash
git clone https://github.com/WilletJiang/mycodexskills.git ~/src/mycodexskills
ln -s ~/src/mycodexskills/code-gauge ~/.codex/skills/code-gauge
ln -s ~/src/mycodexskills/latex-formula-polish ~/.codex/skills/latex-formula-polish
ln -s ~/src/mycodexskills/pytorch-python-performance ~/.codex/skills/pytorch-python-performance
ln -s ~/src/mycodexskills/cuda-pytorch-performance ~/.codex/skills/cuda-pytorch-performance
```

## Example Usage

```text
Use $code-gauge before touching this refactor.
Use $latex-formula-polish to clean up the equations in this .tex file.
Use $pytorch-python-performance to profile and optimize this training loop.
Use $cuda-pytorch-performance to find the GPU bottleneck and improve throughput.
Use $webapp-testing to verify the local app behavior after the fix.
```

## Repo Philosophy

- prefer skills that save reasoning, not just typing
- prefer workflows with verification paths
- prefer technical leverage over generic convenience
- prefer small, sharp, reusable operating guides

## Notes

- `.system/` is intentionally excluded from version control.
- Each skill keeps its trigger logic in `SKILL.md`.
- `agents/openai.yaml` is included so the skills behave cleanly in modern Codex setups.

## License

Individual skill folders may include their own license files. Check the specific folder if licensing matters for your use case.

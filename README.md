<div align="center">
  <h1>mycodexskills</h1>
  <p><strong>Codex skills for serious technical work.</strong></p>
</div>

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


## Notes

Each skill keeps its trigger logic in `SKILL.md`. And `agents/openai.yaml` is included so the skills behave cleanly in Codex setups.

<div align="center">
  <h1>mycodexskills</h1>
  <p>A curated skill pack for Codex: planning, document work, design, testing, and performance.</p>
  <p>
    <code>code-gauge</code>
    <code>docx</code>
    <code>webapp-testing</code>
    <code>frontend-design</code>
    <code>pdf</code>
    <code>xlsx</code>
  </p>
</div>

## What This Repo Is

This repository collects practical Codex skills that I actually want within reach:

- plan before coding
- work with Office and PDF files
- build better frontends
- test local web apps
- optimize PyTorch workloads
- create polished visual artifacts

The goal is simple: fewer generic outputs, more sharp workflows.

## Quick Install

### Fresh Setup

If `~/.codex/skills` does not already exist:

```bash
git clone https://github.com/WilletJiang/mycodexskills.git ~/.codex/skills
```

### Add To An Existing Setup

If you already have a skills directory and only want a few of these:

```bash
git clone https://github.com/WilletJiang/mycodexskills.git ~/src/mycodexskills
ln -s ~/src/mycodexskills/code-gauge ~/.codex/skills/code-gauge
ln -s ~/src/mycodexskills/docx ~/.codex/skills/docx
ln -s ~/src/mycodexskills/webapp-testing ~/.codex/skills/webapp-testing
```

## Recommended Starting Set

| Skill | Use It For |
|------|------------|
| `code-gauge` | force a short planning gate before coding |
| `docx` | create, inspect, or redline Word documents |
| `pdf` | extract, merge, fill, OCR, or generate PDFs |
| `pptx` | build or edit slide decks |
| `xlsx` | clean up or generate spreadsheets |
| `frontend-design` | make web UI feel designed, not generic |
| `webapp-testing` | verify local web apps with Playwright |

## Catalog

- `algorithmic-art` - generative art with p5.js
- `brand-guidelines` - apply brand style consistently
- `canvas-design` - create polished static visual designs
- `code-gauge` - planning, simplification, and compatibility checks before coding
- `cuda-pytorch-performance` - GPU-side PyTorch optimization
- `doc-coauthoring` - structured doc-writing workflow
- `docx` - Word document creation and editing
- `frontend-design` - high-quality frontend UI work
- `internal-comms` - internal updates, newsletters, FAQs, and status writing
- `latex-formula-polish` - clean up LaTeX math layout
- `pdf` - PDF processing workflows
- `pptx` - PowerPoint creation and editing
- `pytorch-python-performance` - Python-level PyTorch optimization
- `web-artifacts-builder` - larger multi-file HTML artifacts
- `webapp-testing` - browser-driven local app testing
- `xlsx` - spreadsheet workflows

## How I Use It

A few common prompts:

```text
Use $code-gauge before touching this refactor.
Use $docx to update the contract and keep tracked changes.
Use $webapp-testing to verify the local dashboard flow.
Use $frontend-design to redesign this landing page.
```

## Notes

- `.system/` is intentionally excluded from version control here.
- Each skill keeps its trigger logic in `SKILL.md`.
- `agents/openai.yaml` is included so the skills behave cleanly in modern Codex setups.

## License

Individual skills may carry their own license files. Check the skill folder if that matters for your use case.

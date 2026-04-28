---
name: web-artifacts-builder
description: Create complex multi-component HTML artifacts with a bundle-time visual harness. Use for artifacts that need React, TypeScript, Tailwind CSS, shadcn UI components, state management, or routing, not for simple single-file HTML artifacts.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder

Use this skill when a complex artifact needs a real frontend project before it can be bundled into one self-contained HTML file. For simple static artifacts, write the HTML directly instead of adding build machinery.

The stack is React 18, TypeScript, Vite, Tailwind CSS, shadcn UI components, Radix UI dependencies, and Parcel bundling. Initialize the project with:

```bash
bash scripts/init-artifact.sh <project-name>
```

Develop the artifact inside the generated project. Treat shadcn components as a component library, not as a design direction by themselves. The visual result still needs a coherent information hierarchy, clear interaction model, and context-specific styling.

When the implementation is ready, bundle it with:

```bash
bash scripts/bundle-artifact.sh
```

The bundler expects `index.html` at the project root and produces `bundle.html`, with JavaScript, CSS, and dependencies inlined for use in Codex or OpenAI workflows.

## Bundle Visual Harness

After bundling, open `bundle.html` in a browser when tooling is available. Check that the artifact runs without a dev server, has no blocking console errors, preserves styling after asset inlining, and works at desktop and mobile widths. Verify the primary interaction path and any stateful controls.

When the artifact contains canvas, media, generated visuals, or complex layout, capture screenshots and check rendered pixels or visible content. If browser execution is unavailable, state the exact command or path needed to verify `bundle.html` and mark visual checks as pending.

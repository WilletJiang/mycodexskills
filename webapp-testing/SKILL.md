---
name: webapp-testing
description: Build browser-based visual and behavioral harnesses for local web applications using Playwright. Use whenever Codex needs to verify frontend behavior, inspect rendered DOM state, capture screenshots, collect browser logs, test responsive layout, check canvas output, or automate a local web UI.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

Use this skill when a browser is the correct verification surface. Static inspection is often enough for simple HTML, but client-rendered applications, local dev servers, canvas output, interactive controls, and layout regressions need Playwright evidence.

First determine whether the target is a static file or a running application. If a server is required, prefer the repository's existing command. When a managed server wrapper is useful, inspect its help before reading the source:

```bash
python scripts/with_server.py --help
```

For dynamic apps, begin with reconnaissance. Open the page, wait for `networkidle` unless the app never becomes idle, inspect the rendered DOM, capture browser console output when behavior is uncertain, and then interact through stable selectors such as roles, labels, visible text, IDs, or durable CSS hooks. Screenshots should support claims about layout, visual state, or canvas output; DOM evidence should support claims about rendered structure and accessible text.

For static HTML, read the file first to learn expected selectors and state. If direct inspection does not answer the question, load it in Playwright and treat it like a rendered app.

## Visual Harness

Define the verification surface before interacting: target URL or file, viewport matrix, expected first meaningful render, key interactions, screenshots to capture, and browser logs to collect. Use desktop and mobile viewports for responsive interfaces unless the task is explicitly single-viewport.

For canvas, video, SVG-heavy, WebGL, or Three.js surfaces, use screenshots or pixel checks to prove the primary visual region is nonblank and correctly framed. DOM assertions alone are insufficient for visual output. For ordinary UI, combine DOM checks with screenshots for layout, overflow, contrast, loading state, and interaction state.

Report the commands, viewports, screenshots or observations, console errors, and any checks that could not be completed.

## Resources

Use `scripts/with_server.py` to manage local servers. The examples under `scripts/examples` show rendered-DOM reconnaissance, local file automation, and console logging. Read `references/playwright-patterns.md` for the decision tree, waiting strategy, selector discipline, screenshot capture, and common failure modes.

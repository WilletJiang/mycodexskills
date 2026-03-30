---
name: webapp-testing
description: Interact with and test local web applications using Playwright. Use whenever Codex needs to verify frontend behavior, inspect rendered DOM state, capture screenshots, collect browser logs, or automate a local web UI, especially when the app requires a dev server, client-side rendering, or browser-driven reproduction steps.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

## Overview

Use Playwright to test local web applications. Keep the main skill focused on choosing the right workflow, then load deeper guidance only if needed.

## Preferred Workflow

1. Decide whether the target is static HTML or a running web app.
2. If a local server is required, run `python scripts/with_server.py --help` before reading the helper source.
3. Use reconnaissance first on dynamic apps: open the page, wait for `networkidle`, inspect the rendered DOM, then act.
4. Use example scripts in `scripts/examples/` as starting points, not as rigid templates.

## Quick Start

### Dynamic App with Managed Server

```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:5173")
    page.wait_for_load_state("networkidle")
    # interact here
    browser.close()
```

### Static HTML

- Read the HTML directly to discover IDs, roles, and selectors.
- If direct inspection is incomplete, treat it like a dynamic app and inspect the rendered result in Playwright.

## Decision Rules

- Prefer bundled helpers as black boxes before reading their implementation.
- Wait for `networkidle` before inspecting dynamic pages unless the app never reaches idle and a more specific wait is required.
- Capture both DOM evidence and screenshot evidence when debugging uncertain UI state.
- Use clear selectors such as roles, visible text, labels, IDs, or stable CSS hooks.

## Resources

### scripts/

- `scripts/with_server.py` manages one or more local servers for browser automation.
- `scripts/examples/element_discovery.py` shows rendered-DOM reconnaissance.
- `scripts/examples/static_html_automation.py` shows `file://` automation for local HTML.
- `scripts/examples/console_logging.py` shows browser console capture.

### references/

Read [references/playwright-patterns.md](references/playwright-patterns.md) for the decision tree, reconnaissance workflow, and common pitfalls.

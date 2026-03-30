# Playwright Patterns for Local Web Apps

Use this file when the task needs more than the short main workflow.

## Decision Tree

```text
User task -> Is it static HTML?
    Yes -> Read the HTML and identify selectors directly.
         -> If that fails, inspect the rendered page with Playwright.
    No  -> Is the app already running?
         -> No: run scripts/with_server.py --help, then start the server with the helper.
         -> Yes: use reconnaissance first, then perform actions.
```

## Reconnaissance-Then-Action

1. Open the page.
2. Wait for `networkidle` or the most appropriate ready signal.
3. Inspect the rendered state:
   - `page.screenshot(...)`
   - `page.content()`
   - `page.locator(...)`
4. Identify stable selectors from the rendered DOM, not just from source assumptions.
5. Execute the minimum actions needed to verify or reproduce the behavior.

Example reconnaissance:

```python
page.screenshot(path="/tmp/inspect.png", full_page=True)
content = page.content()
buttons = page.locator("button").all()
```

## Managed Server Usage

Single server:

```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

Multiple servers:

```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

## Common Pitfalls

- Do not inspect a client-rendered page before it is ready.
- Do not rely on brittle selectors when roles or visible text are available.
- Do not read large helper scripts until the black-box workflow proves insufficient.
- Do not forget to close the browser in standalone scripts.

## Best Practices

- Use synchronous Playwright for simple Python scripts.
- Capture screenshots when visual state matters.
- Record console output when debugging JavaScript behavior.
- Prefer short automation scripts that prove one behavior clearly over broad, fragile test flows.

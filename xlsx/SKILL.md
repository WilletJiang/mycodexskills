---
name: xlsx
description: Create, edit, clean, format, chart, compute, and validate spreadsheets with an integrity harness. Trigger for .xlsx, .xlsm, .csv, and .tsv files when the spreadsheet is the primary input or output. Use for input schema checks, row and column range validation, formula regions, sampled formulas, cross-sheet consistency, source hardcode audit, recalculation, and reopen verification. Do not use when the deliverable is primarily a Word document, PDF, standalone script, database pipeline, or Google Sheets integration.
license: Proprietary. LICENSE.txt has complete terms
---

# Spreadsheet Workflows

Use this skill when the deliverable is a spreadsheet. The workbook should remain editable, recalculable, and professionally formatted. Preserve existing templates and conventions when editing an existing file; established local formatting overrides general guidance.

Use `pandas` for data analysis, cleaning, joins, aggregation, and simple exports. Use `openpyxl` when formulas, formatting, workbook structure, charts, named ranges, comments, or Excel-specific behavior matter. Remember that `openpyxl` writes formulas as strings and does not calculate them.

Read `references/integrity-harness.md` before creating or substantially editing a workbook, financial model, multi-sheet report, or cleaned spreadsheet deliverable.

## Formula Discipline

When the spreadsheet is meant to be a model or reusable workbook, put calculations in Excel formulas rather than hardcoding Python-computed results. Source data may be written as values, but totals, ratios, growth rates, margins, checks, and projections should remain dynamic unless the user explicitly asks for static output.

After writing formulas, recalculate and scan for errors:

```bash
python scripts/recalc.py output.xlsx
```

If the script reports `errors_found`, fix the specific locations and recalculate again. Deliver no workbook with `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, or `#NAME?` errors unless the user explicitly asks to preserve them for diagnosis.

## Financial Model Standards

Use a consistent professional font unless the template dictates otherwise. For financial models, apply standard color conventions unless the existing workbook has its own system: blue font for hardcoded inputs, black for formulas, green for same-workbook links, red for external links, and yellow fill for key assumptions requiring attention.

Use text formatting for years, clear units in headers, currency formats such as `$#,##0`, one decimal place for percentages, `0.0x` for valuation multiples, and parentheses for negative values. Display zeros as `-` when that matches financial-modeling convention.

Place assumptions in dedicated cells and reference them from formulas. Document hardcoded values with source, date, and precise reference when available. Check ranges, row offsets, far-right columns, multiple matches, cross-sheet references, and denominator safety before scaling formulas across periods.

## Verification

For each workbook, verify the intended sheet structure, input schema, row and column ranges, formula regions, sampled formulas, cross-sheet consistency, hardcoded source cells, number formats, column widths, frozen panes or filters when relevant, recalculation output, and reopen behavior. If reading calculated values with `data_only=True`, never save that workbook afterward because formulas can be replaced by stale values.

Keep Python helpers concise. Comments belong in the workbook when they clarify assumptions, sources, or complex formulas; avoid verbose script comments that do not improve maintainability.

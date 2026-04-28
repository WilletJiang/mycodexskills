# Spreadsheet Integrity Harness

A spreadsheet deliverable should be checked as a workbook, not only as a file that opens. The integrity harness protects schema, ranges, formulas, cross-sheet links, source assumptions, and recalculation behavior.

## Input Schema

Before transforming data, record the expected sheet names, required columns, column order when meaningful, data types, date handling, uniqueness keys, required non-null fields, and row count expectations. For messy CSV or TSV inputs, preserve a raw copy or raw sheet when useful and document any rows dropped or repaired.

## Workbook Ranges

After writing or editing the workbook, verify each populated sheet's used range, header row, expected row count, expected column count, hidden rows or columns when relevant, named ranges, freeze panes, filters, and table boundaries. Check that formulas and formatting extend through the intended rows and stop where they should.

## Formula Regions

Identify formula regions by sheet and range. Sample the first, middle, and last formula in each region, plus edge rows and any subtotal or total rows. Verify that relative and absolute references are intentional, cross-sheet references target the right sheets, denominators are protected where needed, and formulas remain consistent across projection periods or repeated blocks.

## Recalculation

Run the bundled recalculation script after writing formulas:

```bash
python scripts/recalc.py output.xlsx
```

Fix any reported Excel errors, then recalculate again. Reopen the saved workbook with `openpyxl` after recalculation to verify formulas, cached values when available, sheet names, and workbook structure. Never save a workbook opened with `data_only=True`.

## Cross-Sheet Consistency

For multi-sheet models or reports, check that summary sheets reconcile to detail sheets, totals match source tables, lookup keys have expected coverage, and charts or pivots reference the intended ranges. If the workbook contains a control sheet, tie checks, balance checks, or validation flags, verify they pass.

## Source Hardcode Audit

Hardcoded inputs should be intentional, styled consistently, and documented with source, date, and reference when material. Audit hardcoded values in formula-heavy areas so accidental constants do not replace formulas. In financial models, verify color conventions for hardcoded inputs, formulas, same-workbook links, external links, and key assumptions.

## Reporting

Report the input schema checks, workbook range checks, formula samples, recalculation result, cross-sheet checks, source hardcode audit, and reopen verification. If a check is impossible in the current environment, leave the exact command or inspection step needed to complete it.

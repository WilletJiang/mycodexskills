# Creating New DOCX Documents

Use the `docx` JavaScript library to create new files, then validate the generated document before handing it off.

## Setup

```javascript
const {
  AlignmentType,
  Bookmark,
  BorderStyle,
  Column,
  Document,
  ExternalHyperlink,
  Footer,
  FootnoteReferenceRun,
  Header,
  HeadingLevel,
  ImageRun,
  InternalHyperlink,
  LevelFormat,
  PageBreak,
  PageNumber,
  PageOrientation,
  Packer,
  Paragraph,
  PositionalTab,
  PositionalTabAlignment,
  PositionalTabLeader,
  PositionalTabRelativeTo,
  SectionType,
  ShadingType,
  Table,
  TableCell,
  TableOfContents,
  TableRow,
  TabStopPosition,
  TabStopType,
  TextRun,
  VerticalAlign,
  WidthType,
} = require("docx");
```

```javascript
const doc = new Document({
  sections: [{ children: [/* content */] }],
});

Packer.toBuffer(doc).then((buffer) => fs.writeFileSync("doc.docx", buffer));
```

Validate after generation:

```bash
python scripts/office/validate.py doc.docx
```

## Page Setup

- `docx` defaults to A4. Set page size explicitly for consistent US Letter output.
- `1440 DXA = 1 inch`.
- For US Letter, use `width: 12240` and `height: 15840`.
- Set margins explicitly to control usable content width.

```javascript
sections: [{
  properties: {
    page: {
      size: { width: 12240, height: 15840 },
      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
    },
  },
  children: [/* content */],
}]
```

For landscape output, pass the portrait dimensions and set `orientation: PageOrientation.LANDSCAPE`. The library swaps the edges internally.

## Styles and Headings

- Use widely supported fonts such as Arial unless the document requires a specific brand font.
- Override built-in heading IDs such as `Heading1` and `Heading2`.
- Include `outlineLevel` so table-of-contents generation works.

```javascript
styles: {
  default: { document: { run: { font: "Arial", size: 24 } } },
  paragraphStyles: [
    {
      id: "Heading1",
      name: "Heading 1",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { size: 32, bold: true, font: "Arial" },
      paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 },
    },
  ],
}
```

## Lists

Never insert Unicode bullets manually. Use numbering definitions:

```javascript
numbering: {
  config: [
    {
      reference: "bullets",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "•",
        alignment: AlignmentType.LEFT,
      }],
    },
  ],
}
```

The same numbering reference continues a list. A different reference restarts it.

## Tables

Tables need dual widths:

- Set `width` on the table.
- Set `columnWidths` on the table.
- Set matching `width` values on each cell.
- Use `WidthType.DXA`, not percentage widths.
- Use `ShadingType.CLEAR`, not `SOLID`.

```javascript
new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [4680, 4680],
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 4680, type: WidthType.DXA },
          shading: { fill: "D5E8F0", type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph("Cell")],
        }),
      ],
    }),
  ],
})
```

## Images

- `ImageRun` requires a `type`.
- Include `altText`.

```javascript
new Paragraph({
  children: [new ImageRun({
    type: "png",
    data: fs.readFileSync("image.png"),
    transformation: { width: 200, height: 150 },
    altText: { title: "Title", description: "Desc", name: "Name" },
  })],
})
```

## Layout Features

- Page breaks must live inside a `Paragraph`.
- Use bookmarks plus `InternalHyperlink` for internal navigation.
- Use `FootnoteReferenceRun` for footnotes.
- Use tab stops for right-aligned text and TOC-style leaders.
- Use section properties for multi-column layouts.
- Use `TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" })` for a generated TOC.
- Use headers and footers directly in section definitions.

## Hard Rules for `docx`

- Set page size explicitly.
- Never use `\n` instead of separate paragraphs.
- Never use Unicode bullets as plain text.
- Keep table widths exact and internally consistent.
- Keep TOC headings on `HeadingLevel` styles.
- Prefer paragraph borders or tab stops over tables for decorative separators.

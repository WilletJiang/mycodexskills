---
name: research-paper-framing
description: Use when drafting or revising academic research paper abstracts, introductions, related-work framing, literature-gap statements, contribution lists, titles, or positioning paragraphs for journal, conference, thesis, or preprint manuscripts. Helps identify the real contribution, compare against verified literature, write concise contrast-driven abstracts, build coherent introductions, and validate citations and LaTeX manuscript quality across fields and venues.
---

# Research Paper Framing

## Operating Rule

Frame the contribution before polishing prose. If the claimed novelty is vague, unsupported, or weaker than the writing suggests, state that directly and tighten the claim before drafting.

## Workflow

1. Identify the target venue or genre. Use provided exemplars for rhythm, ordering, and density, but do not copy wording, sentence skeletons, or field-specific conventions that do not fit the manuscript.
2. Extract the actual research object: problem, setting, assumptions, method primitive, theorem or empirical result, evidence, application, limitation, and closest competing baselines.
3. Build a literature map before making novelty claims. Separate established background, neighboring work, direct competitors, and the precise missing combination or obstruction.
4. Draft the contribution map in explicit contrast form: existing approach, why it is insufficient here, what the manuscript changes, what result follows, and what evidence supports it.
5. Write the abstract as a compressed argument. Prefer problem, contrast, core result, consequence, and application. Avoid citations in abstracts unless the venue explicitly permits them.
6. Write the introduction as a sequence of narrowing claims: broad field, implementation or scientific bottleneck, existing lines of work, unresolved gap, proposed direction, contributions, and paper organization.
7. Validate aggressively: references must be real and complete, citation commands must resolve, broad claims need citations, abstract length must fit the venue, and the manuscript must compile cleanly when LaTeX is involved.

For detailed paragraph patterns, contribution templates, citation discipline, and checklists, load `references/paper-framing-patterns.md`.

## Literature Discipline

Never invent references, DOIs, venues, page numbers, author lists, or publication years. When the user asks for literature research, current coverage, DOI filtering, clickable references, or a bibliography update, verify metadata against external sources or authoritative databases before editing the bibliography.

Every cited paper must earn its place. Do not add citations merely to inflate count. If the user requests many references, organize them by role so that each paragraph has a clear evidential purpose.

## Abstract Standard

Make the abstract comparison-heavy when novelty depends on distinction from prior work. Use phrases such as compared with, different from, unlike, and in contrast only when the comparison is specific and true.

Do not spend abstract space on proof mechanics unless the technical mechanism is itself the contribution. State what problem is solved, what assumption is relaxed, what class is covered, what criterion or result is obtained, and where it applies.

## Introduction Standard

Each paragraph must answer why the next paragraph is necessary. Avoid isolated background blocks. Move from mature baseline to unresolved limitation, then to the manuscript's exact intervention.

Contribution bullets should be falsifiable. Each bullet should name a baseline limitation, state the positive result, and explain its significance without exaggerating priority.

## Style Rules

Use professional academic prose with concrete nouns and explicit logical links. Avoid hype, metaphors, generic phrases, decorative complexity, and unsupported first-ever claims.

When the user provides a model paper, imitate structure only. Change vocabulary, syntax, ordering, and argumentative route enough to avoid textual dependence while preserving the useful rhetorical function.

## Verification

For LaTeX projects, check at least: undefined citations, missing bibliography entries, repeated or unused references when relevant, abstract word count, title consistency, hyperlink support, overfull boxes near edited text, and whether all user-specified style constraints are satisfied.

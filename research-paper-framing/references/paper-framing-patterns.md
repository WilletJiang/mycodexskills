# Paper Framing Patterns

## Table of Contents

1. Contribution diagnosis
2. Literature map
3. Abstract patterns
4. Introduction patterns
5. Contribution bullets
6. Citation and bibliography checks
7. Venue adaptation
8. Failure modes

## 1. Contribution Diagnosis

Before drafting, write a compact diagnostic table:

| Item | Required content |
| --- | --- |
| Object | Exact system, dataset, theorem class, task, or phenomenon studied |
| Baseline | What existing work already does |
| Obstruction | Why the baseline does not handle this case |
| Mechanism | The new primitive, condition, construction, algorithm, estimate, or design |
| Result | Theorem, guarantee, empirical finding, criterion, or application outcome |
| Evidence | Proof, experiment, simulation, benchmark, ablation, or case study |
| Limitation | What is not solved and what assumptions remain |

If the obstruction cannot be stated in one or two precise sentences, the novelty is not yet ready for abstract or introduction writing.

## 2. Literature Map

Use four roles, not one undifferentiated citation pile:

| Role | Purpose |
| --- | --- |
| Background | Establish the field and standard tools |
| Implementation or setting | Show why the paper's information pattern, data regime, assumptions, or platform matters |
| Neighboring methods | Show close but incomplete solutions |
| Direct comparison | Support the final gap statement and contribution claims |

Each introduction paragraph should cite papers that serve the paragraph's exact claim. A claim about a missing technical combination needs citations to the closest works, not only broad surveys.

## 3. Abstract Patterns

### Contrast-Driven Abstract

Use this when the contribution relaxes assumptions, changes the information pattern, or handles a class excluded by prior methods.

1. State the paper's problem and setting.
2. Compare with the dominant line of existing work.
3. State the specific limitation removed or assumption avoided.
4. Identify the new analytical, algorithmic, modeling, or experimental principle.
5. State the main result and consequence.
6. Close with the application or validation domain.

Good abstract sentences do concrete work:

- Compared with methods that require [assumption], the present framework allows [excluded case].
- Different from formulations based on [baseline mechanism], the proposed treatment uses [new mechanism] to handle [obstruction].
- Under [checkable condition], the method yields [guarantee] and applies to [representative class].

Avoid:

- Long proof-route descriptions.
- Unverifiable claims such as highly efficient, novel framework, comprehensive solution.
- Citations, unless the venue requires or permits them.
- Vague result verbs such as discusses, explores, or investigates when the paper proves, designs, estimates, characterizes, or demonstrates something sharper.

## 4. Introduction Patterns

### Standard Narrowing Sequence

1. Mature baseline: introduce the field and cite established foundations.
2. Practical or scientific pressure: explain why the idealized baseline is insufficient.
3. Existing response: review methods that address part of the pressure.
4. Remaining obstruction: state exactly what combination, assumption, regime, or information pattern is still missing.
5. Manuscript aim: describe what this paper will establish, without overclaiming.
6. Contributions: list three or four precise contributions.
7. Organization: summarize the paper structure.

### Gap Paragraph Pattern

A strong gap paragraph should contain:

- Direct competitors by name or citation group.
- What each competitor covers.
- What remains uncovered.
- Why the missing piece is not cosmetic.
- One sentence that motivates the present paper.

Avoid a gap paragraph that says only there are few results or this problem has not been studied. That is weak unless backed by a precise obstruction.

## 5. Contribution Bullets

A contribution bullet should usually follow this form:

1. Contrast: Unlike or different from [specific baseline].
2. Positive claim: this paper establishes, designs, characterizes, proves, or demonstrates [specific result].
3. Significance: this matters because [excluded case, weaker assumption, computability, implementability, improved evidence, or broader applicability].

Keep claims falsifiable. Do not write first, novel, or unprecedented unless the literature review supports it strongly. Prefer more exact claims such as removes the need for, covers the case where, gives an explicit condition for, or proves convergence under.

## 6. Citation and Bibliography Checks

For bibliography work:

- Verify author names, title, venue, year, volume, issue, pages or article number, and DOI when requested.
- Remove or flag entries without DOI if the user requires DOI coverage.
- Do not cite a source for a claim it does not support.
- Prefer primary sources for technical claims and surveys for broad field summaries.
- Compile or otherwise check that citation keys resolve.
- Ensure hyperlinks are enabled when the user requests clickable references.

## 7. Venue Adaptation

Use the target venue's examples for density and ordering. For control theory journals, comparison-heavy abstracts and explicit contribution lists are common. For machine learning venues, emphasize task, method, empirical protocol, baselines, ablations, and limitations. For mathematical journals, emphasize problem lineage, theorem novelty, assumptions, and proof architecture. For applied science journals, emphasize phenomenon, measurement or model, evidence, and practical implication.

Do not let venue imitation override truth. If the manuscript does not support a claim, weaken the claim rather than making the prose sound more confident.

## 8. Failure Modes

Watch for:

- Background paragraphs with no connection to the manuscript's problem.
- Citation dumps that do not support the sentence they appear in.
- Abstracts that describe proof steps but not the contribution.
- Contribution bullets that rename sections instead of stating advances.
- Claims of generality without naming the exact assumption relaxed.
- Model-paper plagiarism through copied syntax or paragraph choreography.
- Bibliographies containing unverifiable, incomplete, or fabricated entries.
- A gap that is merely chronological rather than mathematical, empirical, or conceptual.

---
name: doc-coauthoring
description: Guide users through a structured workflow for co-authoring documentation, proposals, technical specs, decision documents, and similar structured writing. Use when the user is starting or revising substantial documentation and needs context gathering, section-by-section drafting, and reader-oriented validation.
---

# Document Co-Authoring

Use this skill when the user is writing a document that must work for real readers. The goal is to transfer context from the user, sharpen the structure, draft section by section, and verify that the result answers the questions readers will actually bring.

Offer the structured workflow when the user mentions documentation, proposals, technical specs, RFCs, PRDs, decision documents, project writeups, or similar writing tasks. If the user prefers freeform work, follow their preference.

## Stage One: Context

Start by identifying the document type, primary audience, desired reader action, required template, deadline, and constraints. Ask only questions that change the document materially. The user may answer in shorthand, paste rough notes, link related material, or dump context without organizing it.

Encourage a broad context dump after the initial questions. Useful context includes project background, rejected alternatives, stakeholder concerns, organizational constraints, technical architecture, dependencies, timeline pressure, prior incidents, and links to related discussions or documents. When connected tools are available and the user authorizes their use, read the relevant sources. If a shared document contains images without alt text, explain that downstream model readers may miss those images and ask whether descriptions should be generated.

Once enough context exists to ask edge-case and tradeoff questions rather than basic orientation questions, ask five to ten focused clarifying questions. Exit this stage when the user agrees there is enough context to draft.

## Stage Two: Structure And Drafting

Choose the document structure from the template, the genre, or the problem itself. For decision documents, the core proposal is usually the hardest section and should often be drafted before the executive summary. For technical specs, the system design and operational constraints usually need early treatment. Summaries are usually best written after the body is stable.

Create a scaffold with section headings and placeholders in an artifact when available, otherwise in a local Markdown file. Then work section by section. For each section, ask focused questions, propose candidate points, let the user select or reject them, check for missing content, draft the section, and revise with targeted edits rather than reprinting the full document.

As the draft matures, re-read the whole document for flow, redundancy, contradictions, weak transitions, unsupported claims, generic filler, and sentences that do not carry information. When most sections are complete, perform a full coherence pass before reader testing.

## Stage Three: Reader Testing

Reader testing asks whether the document works without the private conversation that produced it. Predict five to ten questions a real reader would ask. By default, perform a reader simulation in the current thread: temporarily adopt the perspective of a reader who only has the document, answer the predicted questions from the text, and identify ambiguity, assumed context, contradictions, or unsupported claims.

Use subagents only when the user explicitly asks for a fresh reader, parallel review, independent review, or subagent-based validation in the current conversation. If the user does not explicitly request that, do not spawn a subagent. When subagents are unavailable or not requested, keep the test in-thread and be clear that it is a simulation rather than an independent fresh context.

Any failed answer is useful evidence. Fix the section that caused the failure, then retest the affected question. The document is ready when reader questions are answered accurately and no new ambiguity or contradiction appears.

## Guidance Style

Be direct, procedural, and adaptive. Explain the reason for a step only when it changes user behavior. Keep the user in control of pace and process, but do not let missing context silently accumulate. Favor concrete reader value over formal completeness.

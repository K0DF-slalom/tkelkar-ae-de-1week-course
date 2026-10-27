# 1-Week Course — Day 1: Foundations & Governance

Day 1 builds baseline Codex literacy, safe usage habits, and a shared vocabulary for context engineering.

## Outcomes

- Apply safe-use guardrails (no secrets, no client data; verify outputs).
- Use prompting patterns for small coding and SQL tasks.
- Explain what “context engineering” is and why it matters.
- Complete the first self-service labs and capture evidence.

## Pre-Work (30–60 min)

- Read [Codex Development Best Practices](codex-best-practices.md).If you are using Microsoft Copilot, apply the general prompting, review, and verification guidance; commands and features named specifically for Codex may not be available in your Copilot experience.
- Confirm you have a **practice repo** you can modify (no production systems, no regulated data).

Use the approved AI assistant you selected on Day 0. Codex examples throughout this day illustrate the workflow. If you are using Microsoft Copilot, provide the relevant task instructions and approved file excerpts yourself. Review its suggestions, make any repository changes in your editor, and run the verification steps locally.

## Core Modules (Async)

### Module 1 — How Codex Works (30–45 min) → [Lab 1](#lab-1-prompt-to-task-basics)

See [Module 1 — How Codex Works](module-1-how-codex-works.md) for a full lesson plan covering Codex strengths vs. failure modes, workflow habits, and the verify-first checklist exercise.

### Module 2 — Prompting Fundamentals (30–45 min) → [Lab 1](#lab-1-prompt-to-task-basics)

See [Module 2 — Prompting Fundamentals](module-2-prompting-fundamentals.md) for the four-part prompt structure, side-by-side prompt comparison activity, and reusable template guidance.

### Optional Reading — OpenAI Cookbook (20–30 min)

- Start here: <https://cookbook.openai.com/>
- Recommended picks (choose 2–3):
  - [GPT-5.2 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-2_prompting_guide)
  - [GPT-5.1-Codex-Max Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-1-codex-max_prompting_guide)
  - [Modernizing your Codebase with Codex](https://cookbook.openai.com/examples/codex/code_modernization)
  - [How to use functions with a knowledge base](https://cookbook.openai.com/examples/how_to_call_functions_for_knowledge_retrieval)
  - [Getting Started with OpenAI Evals](https://cookbook.openai.com/examples/evaluation/getting_started_with_openai_evals)
  - [Evals API Use-case - Structured Outputs Evaluation](https://cookbook.openai.com/examples/evaluation/use-cases/structured-outputs-evaluation)
  - [Evals API Use-case - Tools Evaluation](https://cookbook.openai.com/examples/evaluation/use-cases/tools-evaluation)

### Module 3 — Responsible Use & Governance (30–45 min) → [Lab 1](#lab-1-prompt-to-task-basics)

See [Module 3 — Responsible Use & Governance](module-3-responsible-use-governance.md) for policy summaries, the red-line checklist template, and attribution/documentation expectations.

### Module 4 — Context Engineering Intro (30–45 min) → [Lab 2](#lab-2-context-engineering-lite)

See [Module 4 — Context Engineering Intro](module-4-context-engineering-intro.md) for framework overviews, context-asset planning worksheets, and guidance for prepping the Day 1 labs.

## Hands-On Labs (Self-Service)

### Lab 1: Prompt-to-Task Basics

_Time estimate: 60–90 min_

- Choose a small task in your practice repo (e.g., add a CLI flag, refactor a function, improve a query).
- Write a prompt with constraints and a verification step (build/test/lint or a manual checklist).
- Record what you asked, what changed, and how you verified it.

### Lab 2: Context Engineering Lite

_Time estimate: 60–90 min_

- Add lightweight scaffolding (README notes, TODO list, expected inputs/outputs, sample data).
- Re-run the task with the new context and compare quality.
- Capture the minimal context that made the biggest difference.

### Workshop: Codex Basic

We have prepared a functional repository for you to practice some of the Codex features. The workshops covers all the topics you have learned in day1 and serves as a great milestone project to wrap up day1

Learners using Microsoft Copilot can complete the prompting and verification exercises with their approved Copilot experience. Codex-specific features, including automatic use of `AGENTS.md` and agent skills, require Codex; Copilot learners should read those instructions as examples and explicitly include any relevant rules in their prompts.

[Workshop 1](../workshops/workshop1): Prompting Basics

[Workshop 2](../workshops/workshop1): Introduction to AGENTS.md and Agent Skills

## Artifacts to Submit

- A short daily log (bullets): tasks attempted, prompts used, verification performed, lessons learned.
- Links/paths to changed files or snippets in your practice repo (as allowed).

## Optional Touchpoints

- 15-minute “office hours” for environment setup and safe-use Q&A.

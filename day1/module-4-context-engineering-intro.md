# Module 4 — Context Engineering Intro

**Timebox:** 30–45 minutes
**Prereqs:** Finish Modules 1–3 and gather at least one real task you plan to tackle this week.

## Overview

Context engineering is the discipline of packaging the right clues—requirements, code excerpts, test cases, domain rules—so Codex can reason effectively. If you are brand new to Codex, think of context packs as mini briefcases you hand to the agent. This module explains, step by step, how to build those briefcases using the exact topics referenced in the Day 1 README.

## Context Engineering Basics for New Users

- **Why it matters:** Codex only sees what you paste or attach. Missing context leads to hallucinations or rework.
- **What counts as context:** README excerpts, `AGENTS.md` rules, API contracts, sample payloads, error logs, test plans, screenshots.
- **Lightweight approach:** You do not need a complex system; even a short markdown snippet that lists goals, files, and verification steps dramatically improves output quality.

## Common Context Assets (Pick 3 This Week)

1. **Rules & Guardrails** — e.g., copy relevant bullets from `AGENTS.md` so Codex knows styling, forbidden actions, or security policies.
2. **Task Checklist** — Steps the agent should follow (open files, search for strings, write tests).
3. **Sample Input/Output** — JSON payloads, CLI commands, screenshots that show desired behavior.
4. **Minimal Test Harness** — Instructions for running `pytest`, `npm test`, or manual validation.
5. **Reference Implementation** — A working example from another module or function.

Each asset should answer: *Why does this matter? Where is it stored? How will I keep it updated?*

## Learning Objectives

- Define context engineering and explain why it improves both speed and reliability.
- Identify at least three context assets you can assemble this week (e.g., `AGENTS.md`, task checklists, sample inputs/outputs, data contracts).
- Practice mapping a task to the minimal context Codex needs to avoid hallucinations.
- Outline how you will evolve context assets as complexity grows.

## Required Reading

- [Context Engineering Frameworks Overview](https://bitbucket.org/slalom-consulting/field-cto-data-docs/src/main/codex-enablement/context-engineering-frameworks-overview.md)
- Optional: [Context Engineering Quick Start Guides](https://bitbucket.org/slalom-consulting/field-cto-data-docs/src/main/codex-enablement/context-engineering-quick-start-guides.md)

## Session Flow

1. **Define the Practice (5 min)** — Align on terminology: context packs, agent briefs, prompt scaffolds. Make sure every participant can describe them without jargon.
2. **Framework Tour (10 min)** — Walk through the recommended frameworks (e.g., Checklist + Assets + Verification). Highlight how each reduces back-and-forth with Codex by eliminating guesswork.
3. **Asset Brainstorm (10 min)** — Inventory artifacts you already have (README, ADRs, tests) and gaps you can fill quickly (sample payloads, interface diagrams). Use sticky notes or a shared doc to list them.
4. **Task Mapping (10 min)** — For an upcoming task, list the context Codex needs, where to source it, and how to share it succinctly. If information is missing, note who can provide it.
5. **Plan the Lab (5 min)** — Decide which assets you will build before Lab 2 to measure lift in quality. Set owners and due dates so the plan moves forward.

## Hands-On Practice

Use the table below to plan three context assets for the week:

| Task | Context Asset | Owner | Source/Location | Evidence of Impact |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Then, draft a short “context brief” for one task:

```markdown
## Task
## Current Pain
## Minimal Context (files, constraints, examples)
## Verification
## Risks if Missing
```

Share the brief with a peer or mentor for feedback before running Lab 2.

## Example Context Brief (Fill and Customize)

```markdown
## Task
Add pagination to `/reports` API to return 50 results at a time.

## Current Pain
Endpoint returns all rows (10k+) causing timeouts for analysts.

## Minimal Context
- Files: `api/reports.py`, serializer in `api/schemas/report.py`, integration tests in `tests/integration/test_reports.py`.
- Constraints: Must stay compatible with BI dashboard; query must sort by `created_at`.
- Examples: Include sample request `/reports?page=2&page_size=50` and response headers `X-Total-Count`.

## Verification
1. Run `pytest tests/integration/test_reports.py -k pagination`.
2. Manual curl request verifying `page_size=50`.
3. Confirm changelog entry updated.

## Risks if Missing
- Codex might change unrelated endpoints.
- Pagination could break dashboards if headers omitted.
- Timeouts could persist if query not optimized.
```

## Discussion Prompts

- Which assets travel well across projects vs. which must stay repo-specific?
- How will you keep context packs current without duplicating effort?
- What automation could assemble context (e.g., `context.sh` script, issue templates)?

## Evidence to Capture

- Completed asset planning table plus one context brief.
- Notes on feedback received and planned edits before Lab 2.
- Links to any new artifacts you created (e.g., sample payloads, test harness docs).

## Resources & Next Steps

- Framework overview and quick-start guides linked above.
- Internal examples of `AGENTS.md`, task checklists, or context packs.
- Optional: schedule a 15-minute async review of your context brief with a senior engineer.

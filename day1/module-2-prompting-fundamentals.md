# Module 2 — Prompting Fundamentals

**Timebox:** 30–45 minutes
**Prereqs:** Finish Module 1 and confirm access to your practice repo.

## Overview

Prompts are the “requirements document” you hand to Codex. If the requirements are fuzzy, the model guesses—and beginners often interpret that guess as truth. This module breaks down every part of a high-signal prompt so someone with zero Codex experience can describe a task, provide repository clues, and insist on verifiable outputs that match the Day 1 README guidance.

## Prompting 101

- **Prompt = Instructions + Evidence Request.** You tell Codex what to do *and* how you will check the work.
- **Structure beats style.** Consistently using the same fields (goal, context, output format, definition of done) trains you to include the essentials every time.
- **Short does not mean vague.** You can be concise while still specifying the files, commands, and boundaries that matter.

## Learning Objectives

- Explain why each prompt component matters for Codex performance.
- Translate task requirements into explicit constraints and verification steps.
- Write two prompts for the same task (vague vs. constrained) and analyze the delta in responses.
- Capture a reusable prompt template tailored to your project or repo.

## Prompt Shape Reference

| Component | What to Explain (even if you’re new) | Example Wording |
| --- | --- | --- |
| **Goal** | Describe the exact change in one sentence. Avoid multi-part asks. | “Add a `--dry-run` flag to `cli.py` so users can simulate runs.” |
| **Context** | Mention relevant files, frameworks, versions, business rules, and links to specs. | “Project uses Click 8.1, logging via `utils/logger.py`, tests in `tests/test_cli.py`.” |
| **Output Format** | Tell Codex how to reply: diff, command list, numbered steps, etc. | “Respond with a unified diff limited to `cli.py` and `tests/test_cli.py` plus test commands.” |
| **Definition of Done** | Spell out the checks that prove success: tests, lint, screenshots, acceptance criteria. | “Do not change behavior when flag missing. Include pytest command and expected output.” |

## Worked Example (Vague vs. Constrained)

> **Task:** Add a dry-run option so analysts can preview changes.

- **Vague Prompt:** “Update the CLI to support a dry run to test changes. Provide code.”
  - Likely issues: Codex might edit the wrong file, rename arguments, skip tests, or introduce new dependencies.
- **Constrained Prompt:**

  ```
  Goal: Add a `--dry-run` flag to `cli.py` so no database writes occur when it is set.
  Context: Repo uses Click 8.1; handler function is `execute_jobs`. Current tests live in `tests/test_cli.py`. Dry run should log "Dry run complete" via `utils/logger.py`.
  Output: Unified diff limited to `cli.py` and `tests/test_cli.py`, followed by pytest command.
  Definition of Done: Default behavior unchanged; new flag defaults to False. Provide pytest command I can run locally; mention log expectation.
  ```

  - Benefits: Codex knows exactly where to work, how to log, and what proof you need.

## Workshop Steps

1. **Pick a Task (5 min)** — Choose a self-contained change in your practice repo. Document success criteria before prompting.
2. **Draft a Vague Prompt (5 min)** — Intentionally omit details; capture the raw response.
3. **Draft a Constrained Prompt (10 min)** — Use the four-part structure. Require post-change validation.
4. **Compare Outputs (10 min)** — Note correctness, completeness, verbosity, and confidence. What changed and why?
5. **Template Creation (5–10 min)** — Turn your constrained prompt into a fill-in-the-blank snippet you can reuse for code, SQL, or documentation tasks.

## Hands-On Practice

```text
Task: __________________________________________
Key Files / Constraints: _______________________
Definition of Done: ____________________________
Verification Step: _____________________________
```

Fill in the prompt template twice (vague vs. constrained), run both with Codex, and log:

- Number of follow-up questions required.
- Manual edits needed before merging.
- Any hallucinated files or commands.
- Whether the definition of done was already satisfied or required extra work.

## Discussion Prompts

- Which part of the prompt yielded the biggest quality jump?
- What is the least context you must always include for your repo?
- How do you keep prompts short without losing critical constraints?
- How will you store successful prompts so future teammates can reuse them?

## Evidence to Capture

- Both prompts and the resulting Codex outputs.
- Notes on differences in accuracy, scope, and time spent editing.
- Updated prompt template stored in your daily log or repo docs.
- Screenshot or paste of the verification commands you ran.

## Resources & Next Steps

- [Prompt Engineering Cheat Sheet](https://cookbook.openai.com/examples/gpt-5/gpt-5-2_prompting_guide) (see “Structure your asks”).
- [Codex Prompt Taxonomy](https://cookbook.openai.com/examples/gpt-5/gpt-5-1-codex-max_prompting_guide) for advanced patterns like role prompting and multi-turn plans.
- Optional: convert your prompt template into a `PROMPTS.md` or shared snippet for the team.

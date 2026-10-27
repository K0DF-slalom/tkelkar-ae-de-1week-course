# Module 1 — How Codex Works

**Timebox:** 30–45 minutes
**Prereqs:** Complete the course pre-work and skim the Codex Development Best Practices doc.

## Overview

This module explains, in plain language, how Codex reads your instructions, reasons over repository files, and generates suggested changes. We will spell out every concept that appears in the Day 1 README so that even first-time Codex users understand what is happening behind the scenes and what proof you should require before trusting an answer.

## Codex in Plain Language

- **What Codex is:** Codex is a large language model that predicts text (code, docs, commands) one token at a time. It does not “understand” projects the way humans do; it relies entirely on the prompt and any files you let it read.
- **How it thinks:** The model receives your natural-language intent, snippets of repository context, and previous conversation turns. It searches its internal patterns (learned from public code and documents) to guess the most likely next text.
- **Why context matters:** Without explicit files, constraints, and success criteria, Codex fills gaps with assumptions. Providing accurate context shrinks the guesswork and produces safer suggestions.

## How Codex Processes a Task

1. **You craft a prompt** that includes the goal, important files, constraints (dependencies, style guides), and how you will verify the result.
2. **Codex ingests the prompt plus any referenced files** (for example, when you tell the agent to open `cli.py`, it streams that file in the background).
3. **The model predicts edits**—diffs, commands, or narrative steps—based on patterns it has seen.
4. **You review the suggestion** with human judgment, run tests, and compare against your verify-first checklist.
5. **You accept or reject** the change only after proof (passing tests, screenshots, logs) shows the behavior matches expectations.

## Strengths and Practical Examples

- **Speed:** Codex can draft boilerplate or repetitive changes (e.g., adding similar validations across endpoints) in minutes.
- **Pattern Matching:** It quickly identifies similarities between files; for example, it can mirror an existing SQL query pattern in a new report.
- **Scaffolding:** When you provide the high-level structure, Codex fills in function signatures, doc sections, or migration templates, saving setup time.

## Failure Modes to Watch

- **Hallucinations:** Codex may invent files, APIs, or configuration options that do not exist because it would rather guess than admit uncertainty.
- **Wrong Assumptions:** If the prompt is vague, Codex may pick defaults (libraries, versions, business rules) that conflict with your repo.
- **Hidden Breaking Changes:** Even when the diff looks reasonable, downstream tests, performance, or security settings might regress because the model does not execute the code.
- **Context Window Limits:** If you reference too many files or large files, Codex might drop important details as the prompt exceeds the context limit.

Understanding these pitfalls up front is the foundation for safe-use guardrails called out in the README (“no secrets, no client data; verify outputs”).

## Learning Objectives

- Summarize how Codex workflows combine natural-language intent, repo context, and guardrails.
- Describe at least three strengths (e.g., speed, pattern matching, scaffolding) and three failure modes (e.g., hallucinations, hidden breaking changes, wrong assumptions).
- Build a lightweight “verify-first” checklist for a small coding or SQL task.
- Capture evidence that demonstrates the checklist prevented or caught an error.

## Required Reading

- [Codex Development Best Practices](codex-best-practices.md) — focus on the “Codex Workflow Habits” section.

> Tip: Read actively. Highlight habits you already follow, star the ones you need to adopt, and note any blockers you must escalate.

## Session Flow

1. **Model Overview (5 min)** — Review how Codex consumes repo state, plans edits, and validates outputs. Emphasize that Codex predicts text, not intent.
2. **Strengths vs. Failure Modes (10 min)** — Fill out a two-column table capturing real examples from prior projects (speed, bulk edits vs. hallucinations, silent regressions, narrow context windows).
3. **Workflow Habits (10 min)** — Map the best-practice checklist to your current rituals (issue tracking, branching, reviews, testing). Identify gaps.
4. **Verify-First Checklist (10–15 min)** — Pick a micro-task from your practice repo and write the evidence you will collect (tests to run, log lines to check, screenshots, or diffs).
5. **Share-Out (5 min)** — Compare checklists with a partner or the async channel; refine based on feedback.

## Verify-First Checklist Template

1. **Task Summary:** “Add a `--dry-run` flag to `cli.py`.”
2. **Expected Behavior:** “When you set the flag, the system writes no records; instead, results print to stdout.”
3. **Evidence to Capture:**
   - Automated: `pytest tests/test_cli.py -k dry_run`.
   - Manual: run `python cli.py --dry-run sample.json` and confirm “Dry run complete” message.
   - Code: confirm only `cli.py` and `tests/test_cli.py` changed.
4. **Rollback Plan:** “Revert commit or toggle feature flag if unexpected writes appear.”

You must fill this out **before** prompting so that Codex sees the acceptance criteria and you know exactly how to verify after applying the diff.

## Hands-On Practice

1. Choose a task with a bounded blast radius (e.g., “add a CLI flag” or “tighten a SQL filter”).
2. Draft a checklist that proves success from the outside in: user behavior → service/API signals → code diff.
3. Execute (or simulate) the task with Codex, enforcing the checklist before accepting the patch.
4. Record what the checklist caught (even if you found “nothing” — explain why that still built confidence).

## Guided Exercise — Adding a Dry-Run Flag

> If your repo does not have a `cli.py`, pick any small script/entrypoint you control (Python, Node, Bash) or create a tiny placeholder so the exercise is self-contained. For example, a minimal Python CLI that reads a JSON file and prints a summary is enough; you just need something where a `--dry-run` flag makes sense and can be verified with a command.
>
> Placeholder example (Python):
>
> ```python
> # cli.py
> import json
> import argparse
>
> parser = argparse.ArgumentParser()
> parser.add_argument("path")
> parser.add_argument("--dry-run", action="store_true")
> args = parser.parse_args()
>
> data = json.load(open(args.path))
> print(f"Processing {len(data)} records")
> if args.dry_run:
>     print("Dry run complete — no writes performed")
> else:
>     # placeholder for a write
>     print("Would write records here")
> ```
>
> Command to verify manually: `python cli.py sample.json --dry-run`

Each step mirrors the habits discussed above and shows how to collect proof before accepting Codex output.

1. **Pick the Task:** “Add a `--dry-run` flag to `cli.py` so analysts can preview changes without writing to the database.”
2. **Fill the Verify-First Checklist:**
   - Automated proof: `pytest tests/test_cli.py -k dry_run`.
   - Manual proof: run `python cli.py --dry-run sample.json` and confirm no rows written, log message “Dry run complete.”
   - Diff scope: `cli.py`, `tests/test_cli.py` only.
3. **Gather Context:**
   - Open `cli.py` and `tests/test_cli.py`.
   - Note dependencies (Click 8.1, logger utility).
4. **Craft the Prompt:** Include goal, context, output format (diff), definition of done (tests + log message), and explicitly forbid touching other files.
5. **Review Codex Output:**
   - Check the diff for unintended imports or logic changes.
   - Ensure the new flag defaults to `False`.
   - Copy the suggested pytest command.
6. **Run Verification:**
   - Execute the pytest command, capture output.
   - Perform the manual CLI call, take a screenshot or log snippet.
7. **Decide & Document:** Accept only if both proofs succeed. Add a note to your PR describing Codex’s role and the verification performed.

## Independent Exercise — Harden a SQL Filter

**Scenario:** The `reports.sql` query currently returns records for all regions. Product owners want the query scoped to the requesting analyst’s `region_id` to prevent accidental data exposure.

**Embedded example (`queries/reports.sql`):**

```sql
-- Stored procedure used by the reporting service.
CREATE OR REPLACE FUNCTION get_reports(p_region_id INT)
RETURNS TABLE (
  report_id INT,
  region_id INT,
  report_name TEXT,
  created_at TIMESTAMPTZ
) AS $$
BEGIN
  RETURN QUERY
  SELECT r.id, r.region_id, r.name, r.created_at
  FROM reports r
  WHERE r.is_active = TRUE;

  RETURN QUERY
  SELECT a.report_id, a.region_id, a.note, a.created_at
  FROM report_audits a
  WHERE a.created_at >= NOW() - INTERVAL '90 days';
END;
$$ LANGUAGE plpgsql;
```

1. **Goal:** Update `queries/reports.sql` so every `SELECT` statement filters by `region_id` passed into the stored procedure.
2. **Context:** Repo uses PostgreSQL 14; parameter name is `p_region_id`; integration test lives in `tests/integration/test_reports.py::test_region_scope`. Do not change other files.
3. **Definition of Done:** Query only returns rows for the provided region, integration test updated (or added) to prove isolation, manual psql command documented.
4. **Assignment:** Build a verify-first checklist, craft the Codex prompt, review the diff, run tests, and capture evidence (test output + manual query screenshot). Submit your checklist, prompt, and verification artifacts in your daily log.

Expect to spend 30–40 minutes end-to-end. The goal is to practice every step from planning to verification without instructor hints.

## Discussion Prompts

- When does Codex speed you up the most? When does it slow you down?
- Which failure mode worries you the most in your current project and why?
- What automated or manual guardrail could you add this week?
- How will you document the checklist evidence so reviewers can trust the change?

## Evidence to Capture

- Screenshot or snippet of your strength vs. failure-mode table.
- The written verify-first checklist linked to the task.
- Notes on what changed after applying the checklist (issues caught, time saved, next steps).

## Resources & Next Steps

- Codex Best Practices “Habits” section with explicit do/don’t lists.
- Internal examples of Codex change reviews (ask your lead for sanitized diffs).
- Optional follow-up: convert your checklist into a template stored alongside `AGENTS.md`.

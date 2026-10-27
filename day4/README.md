# 1-Week Course — Day 4: Mini Capstone Build

Day 4 is a build day: apply the full workflow on a small, realistic modernization or automation project.

Goal: run a flexible “Capstone” where participants can pick from curated options or bring their own, with light guardrails that work for different levels (guided or free-form).

> You can refer to workshops/workshop-spark-streaming-mcp project for an example on how to do one of these.

## Outcomes

- Deliver a small, working artifact with clear scope and verification.
- Show strong context engineering (scaffolded repo, examples, constraints).
- Produce a demo narrative: value, approach, risks, and next steps.

## Definition of Done (Day 4 Checklist)

- Problem + scope written, with explicit “done” criteria for a 1-day build.
- Repo/context scaffolded (README, samples, constraints, run + verify steps).
- Reproducible run + verification path (`command`, inputs, expected output).
- Evidence captured (logs/output/screenshots or description if time-boxed).
- Risks/limitations noted; next steps listed.

## Capstone Rules of Engagement

- Use only approved, non-sensitive inputs (no client data, no secrets).
- Keep scope small enough to finish and demo in one day.
- Prefer incremental change over “rewrite everything”.
- Only synthetic/sample datasets. No credentials, tokens, PII, or regulated data. Double-check `.gitignore` before committing.

## Capstone Options (Suggested — or Bring Your Own)

Use these as starting points. You can pick one or propose your own capstone if it fits the Day 4 scope and rules of engagement.

### Suggested Options (recommendations, not requirements)

- Modernize a small legacy component (refactor + tests + docs). *Recommended option.*
- Improve a pipeline/job (idempotency + validation + observability stubs). *Recommended option.*
- Bring your own challenge (free project) with a written scope. *Recommended for advanced participants.*
- Build a data quality or lineage micro-tool (checks + report + usage docs).
- System discovery (“Systems X-Ray Discovery”): use GenAI to document, map, and verify systems from sample/example artifacts.
- Data pipeline conversion / modernization (“ETL Reloaded”): migrate legacy jobs to Databricks or Snowflake; build out lakes/warehouses with GenAI help (a common migration workstream/phase).
- Data modeling (“Data Blueprint”): create/update/rationalize data models and generate automated documentation (a “blueprint” of data structures and relationships).

## Minimal Guardrails and Quick Start

- Success criteria: meet the Definition of Done, ship a runnable slice, and capture verification evidence.
- Suggested deliverables: Capstone README, runnable command/notebook, verification output (log/screenshot), demo outline.
- Quick start steps: (1) pick an option + scope; (2) create the repo scaffold; (3) pick a sample dataset (Day 3 resources or other synthetic); (4) define verification command + expected output; (5) build in two slices, capturing evidence.

### Concrete Scope Examples (pick one or adapt)

- Modernize component: migrate a Bash script into a Python CLI with logging + unit tests + usage docs.
- Data quality micro-tool: add 3–5 Great Expectations rules over a sample CSV, expose a `validate` CLI, and emit an HTML/JSON report.
- Pipeline improvement: refactor a daily job to be idempotent, add input validation, and instrument with stubbed metrics/logging.
- Systems X-Ray: given 3–5 sample config/log files, generate a system map + data flow + “unknowns” list with verification prompts.
- ETL Reloaded: take a legacy SQL/CSV transform and port to Databricks/Snowflake style SQL or PySpark with a verification query + sample output.
- Data Blueprint: model 3–5 tables (DDL + diagram/link) and auto-generate schema docs with a short narrative.

## Build Plan (Self-Service)

1. Define the problem and “definition of done” (30 min) — write the checklist.
2. Create scaffolding as context: README, examples, constraints, and verification steps (45 min).
3. Build in small slices with continuous verification (2h slice 1, 2h slice 2).
4. Package the demo: what changed, how to run, evidence it works (45–60 min).

## Resources and Environment Suggestions

- Datasets: reuse Day 3 sample datasets/resources (synthetic only) or generate your own synthetic data for edge cases.
- Sandboxes/trials: Snowflake demo/trial (sign up with Slalom email), Databricks Community Edition, or local Dockerized databases (e.g., Postgres) for reproducible runs.
- Environment tips: keep creds out of the repo; use env vars/placeholders; validate `.gitignore`.

## Artifacts to Submit

- Capstone README: problem, approach, how to run, how to verify, limitations.
- Verification evidence: tests/logs/output samples.
- Demo outline in self-recorded video format (Duration: 5-10 minute): value, workflow, risks, next steps.

### Capstone README Template (copy/paste)

```
# <Project Name>
- Problem + scope:
- Hypothesis/value:
- Approach/architecture/flow:
- How to run:
- How to verify (command + expected):
- Evidence (logs/output/screenshots):
- Limitations/risks:
- Next steps:
```

### Minimal Repository Layout (suggested)

- `README.md` (use template above).
- `src/` (code or notebooks), `data-sample/` (synthetic only), `tests/` or `notebooks/`.
- `docs/evidence/` (logs, screenshots), `constraints.md` (guardrails, assumptions).

### Verification Expectations

- Provide the exact command or notebook cell used to verify and the expected output shape/value.
- If timeboxed, describe how you would verify and what “pass” looks like.

### Quick Evaluation Criteria

- Value and clarity of problem framing.
- Context quality (scaffold, examples, constraints).
- Verification strength (commands, outputs, evidence).
- Demo narrative (what changed, why it matters, risks, next steps).

### Demo Outline (5-10 minutes)

- 1-2 min: Problem and value.
- 2-3 minute: Walkthrough of artifact (code/flow).
- 1-2 minute: Evidence it works (logs/tests/output).
- 1-2 minute: Risks, limitations, and next steps.

## Flexibility by Participant

- Guided/novice: pick a recommended option, use the Capstone README template and timeboxes above, start with Day 3 datasets, and follow the quick start steps.
- Advanced: choose “bring your own” or expand scope; minimize guardrails but keep a written scope, verification command, and evidence. If ahead of schedule, add validation/observability or a second slice (e.g., perf or lineage).

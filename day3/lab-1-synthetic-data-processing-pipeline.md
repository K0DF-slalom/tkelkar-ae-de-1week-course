# Lab 1: Synthetic Data Processing Pipeline

_Time estimate: 90–120 min_

- Kick off with targeted prompt techniques (e.g., structured spec prompts, “options then choose,” checklist prompts) to clarify the problem, success criteria, and constraints before you touch the data.
- Generate or load a vetted synthetic dataset that reflects your real-world domain; document how you produced it so teammates can reproduce it safely.
- Ask Codex to scaffold a lightweight processing flow (ingest ➜ transform) that readies the synthetic data for analysis.
- Perform data profiling (column stats, value distributions, distinct counts) and note any surprises you uncover.
- Add explicit data-quality checks (null thresholds, valid ranges, schema expectations) and capture how you would track failures.
- Use the processed data to model a simple analytic output (e.g., summary table, dimensional model, or feature set) and describe the business question it answers.
- Derive at least one actionable metric or KPI (e.g., churn rate, daily max temperature, total incidents) with a clear calculation (formula + aggregation) and note where the result will live (table, dashboard, alert).
- Optional: package the profiling and quality results into a sharable notebook or markdown snippet so reviewers can follow your reasoning.

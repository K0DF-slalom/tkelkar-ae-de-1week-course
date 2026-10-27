# 1-Week Course — Day 3: Advanced Codex for Data & Apps

Day 3 applies Codex patterns to realistic data engineering and application modernization scenarios.

## Outcomes

- Prompt Codex effectively to build synthetic data pipelines that include profiling, quality checks, metric derivation, and clear documentation.
- Modernize data pipelines end-to-end: bronze ingestion, silver optimization, CDC integration, data protection, and gold-layer analytics.
- Strengthen data processing and observability by partnering with Codex on metric curation, data masking, auditable execution, and lightweight monitoring.

## Pre-Work (30–60 min)

- Skim [Context Engineering Quick Start Guides](https://bitbucket.org/slalom-consulting/field-cto-data-docs/src/main/codex-enablement/context-engineering-quick-start-guides.md).
- Review the 'Artifacts to Submit' section before starting the modules.
- Identify a representative data/app scenario you can work on using **non-sensitive** assets.
- Day 3 will require access to tooling that can build and run a data pipeline, here are some suggestions:
  - (local development) [duckdb](https://duckdb.org/) + [dbt core](https://github.com/dbt-labs/dbt-core)
  - (Snowflake) [Slalom Snowflake iLabs](https://twodegrees1.sharepoint.com/teams/GlobalAlliances/SitePages/Snowflake-Sandbox-Request.aspx) or [Snowflake Trial Account](https://signup.snowflake.com/) Refer the instructions for setting up Snowflake [here](snowflake_setup.md).
  - (Databricks) [Slalom Databricks iLabs](https://twodegrees1.sharepoint.com/teams/GlobalAlliances/SitePages/Databricks-Sandbox-Request.aspx) or [Databricks Free Edition](https://docs.databricks.com/aws/en/getting-started/free-edition)

### Sample Dataset & Repo Ideas

Use the datasets below or any synthetic dataset with non-sensitive data.

- [dbt Labs Jaffle Shop](https://github.com/dbt-labs/jaffle_shop): E-commerce tables, good for pipeline idempotency and schema change drills.
- [Kaggle Titanic Survival Dataset](https://www.kaggle.com/c/titanic/data): Ubiquitous starter dataset for classification, feature engineering practice, and quick ELT checks.

## Core Modules (Async)

### Module 1 — Synthetic Data Pipelines (45–60 min) → [Lab 1](https://bitbucket.org/slalom-consulting/ae-de-1week-course/src/sree/day3/lab-1-synthetic-data-processing-pipeline.md)

See [Module 1 — Synthetic Data Pipelines](module-1-synthetic-data-pipelines.md) to translate a real-world scenario into a safe synthetic dataset.

### Module 2 — Data Modernization & CDC (45–60 min) → [Lab 2](https://bitbucket.org/slalom-consulting/ae-de-1week-course/src/sree/day3/lab-2-data-pipeline-modernization.md)

See [Module 2 — Data Modernization & CDC](module-2-data-modernization-and-CDC.md) to modernize an end-to-end data pipeline.

### Module 3 — Data Processing & Observability (45–60 min) → [Lab 3](https://bitbucket.org/slalom-consulting/ae-de-1week-course/src/sree/day3/lab-3-data-processing-and-observability.md)

See [Module 3 — Data Processing & Observability](module-3-data-processing-and-observability.md) to learn how Codex can be leveraged for data processing and observability.

## Hands-On Labs (Self-Service)

> Tip: before each exercise, prime Codex with structured prompts—use your go-to methods or try context-engineering frameworks like PRP, BMAD, SPECKIT, or an Open Spec outline so the assistant has the right context.

### Lab 1: Synthetic Data Processing Pipeline

_Time estimate: 90–120 min_

- Kick off with targeted prompt techniques (e.g., structured spec prompts, “options then choose,” checklist prompts) to clarify the problem, success criteria, and constraints before you touch the data.
- Generate or load a vetted synthetic dataset that reflects your real-world domain; document how you produced it so teammates can reproduce it safely.
- Ask Codex to scaffold a lightweight processing flow (ingest ➜ transform) that readies the synthetic data for analysis.
- Perform data profiling (column stats, value distributions, distinct counts) and note any surprises you uncover.
- Add explicit data-quality checks (null thresholds, valid ranges, schema expectations) and capture how you would track failures.
- Use the processed data to model a simple analytic output (e.g., summary table, dimensional model, or feature set) and describe the business question it answers.
- Derive at least one actionable metric or KPI (e.g., churn rate, daily max temperature, total incidents) with a clear calculation (formula + aggregation) and note where the result will live (table, dashboard, alert).
- Optional: package the profiling and quality results into a sharable notebook or markdown snippet so reviewers can follow your reasoning.

### Lab 2: Snowflake Pipeline Modernization

_Time estimate: 90–120 min_

- Establish a secure connection to your Snowflake environment (worksheet, Snowsight, or scripted connector) and document the roles/warehouses you’re using.
- Ingest a vetted synthetic, non-sensitive dataset into a bronze-stage table; capture the raw-to-stage copy commands and any file-format choices you make.
- Provide an intentionally inefficient query that promotes data into a silver-layer table. Ask Codex to refactor it for performance and clarity, then apply the suggested improvements.
- Use Codex to design and build change data capture (CDC) logic for data/dataset_2.csv, ensuring incremental updates flow from bronze to silver.

#### Steps to Connect to Snowflake

- Gather your account locator, region, username, database, schema, and a role with the right warehouse access.
- Pick your access method (Snowsight worksheet, SnowSQL CLI, or programmatic connector) and authenticate, including MFA if prompted.
- Set the active role and warehouse, e.g., `USE ROLE <role>; USE WAREHOUSE <warehouse>;`, then sanity-check with `SELECT CURRENT_VERSION(), CURRENT_ROLE(), CURRENT_WAREHOUSE();`.
- Install Python helpers with `pip install snowflake-connector-python python-dotenv`.
- Populate `.env` with account/host, user, warehouse, database, schema, role, plus a single auth choice (`SNOWFLAKE_PASSWORD`, key pair, or `SNOWFLAKE_AUTHENTICATOR=externalbrowser`).
- Add overrides such as `SNOWFLAKE_HOST`, `SNOWFLAKE_TARGET_TABLE`, or `CSV_SOURCE_PATH` if you need custom behavior.
- Run the Python script to load the `.env`, handle the SSO browser flow when required, create the schema/table, and execute ingestion.

##### Useful Links

- Obtain Snowflake Sandbox access: <https://twodegrees1.sharepoint.com/teams/GlobalAlliances/SitePages/Snowflake-Sandbox-Request.aspx>
- Use the link to review Slalom Sandbox roles and access.
- Admin access might be required for database/schema creation: <https://twodegrees1.sharepoint.com/:w:/r/teams/GlobalAlliances/_layouts/15/Doc.aspx?sourcedoc=%7B785303E9-D884-4FE8-82E0-68237694DA68%7D&file=SNOWFLAKE%20INNOVATION%20LABS%20MANAGEMENT%20POLICY.docx&action=default&mobileredirect=true>
- Snowflake Database/Schema Creation: <https://docs.snowflake.com/en/sql-reference/commands-database>

### Lab 3: Data Processing & Observability

_Time estimate: 60–120 min_

- Collaborate with Codex to define the business questions, compute the necessary metrics, and persist the curated results in a gold-layer table or view ready for consumption.
- Ask Codex for data masking techniques (tokenization, hashing, view-based filtering) and apply them to any sensitive-looking fields before sharing silver data with downstream consumers.
- Execute the generated SQL/scripts step by step, capturing screenshots or notes on the Snowflake history tab so beginners can trace what ran and when.

- Optional: add lightweight monitoring notes (query history checks, warehouse usage, alert thresholds, masking policy audits) so future runs can be verified quickly.

## Artifacts to Submit

- Synthetic pipeline dossier:
Prompts used, profiling summary, data-quality checks, metric formulas, and final outputs (tables/views/notebooks).
- Data modernization log:
Bronze/silver/gold SQL snippets, CDC approach, masking steps, optimization notes, and run evidence (history screenshots or logs).
- Observability checklist:
Metrics captured, monitoring hooks (query history, warehouse usage, alert thresholds), and next-step recommendations.

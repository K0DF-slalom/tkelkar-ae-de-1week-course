# README

## Goal

The goal of the workshop is to introduce you to VS Code Codex Plugin. You will be provided with a scenario and will use Codex to accomplish the software development tasks.


## Scenario
You are hired as a consultant by a local shop to help understand the performance of the business. Your job is to use the provided sales, customer, and product data to build reports.

The client has build a simple Python script that generates 3 reports. Your job is to make that script production-ready.

1. Product popularity: total quantity sold per product_id (overall).
2. Revenue by age band: map age to buckets (20-29, 30-39, 40-50) and sum revenue per bucket.
3. Product affinity: pairs of products that are most frequently bought together in the same order_id.

You can run the script with:

```bat
python src/jobs/report.py
```

### Target structure

Below is a simple service-oriented layout you can use as a target structure. It separates data access, business logic, and job entry points. We will ask the agent to refactor the code into the following structure

```
src/
  data_access/
    sales_repository.py
    customer_repository.py
  services/
    reporting_service.py
  models/
    sales.py
    customer.py
  jobs/
    report_job.py
  utils/
    file_io.py
```

## Environment setup

1. Install the latest stable version of Python 3 (as of 2/23/2026, the latest stable version is v3.14)

After you install Python 3, you can use the following code to create and activate a virtual environment. The workshop can be completed without installing additional Python modules.

On Windows:
```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

On macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install VS Code and the `Codex – OpenAI’s coding agent` extension.

If you prefer, you can also use the Codex CLI for this workshop.

3. Ask Codex to set the working directory to `workshops/workshop1` 

If you have multiple folders in your VS workspace, Codex uses the first folder as the workspace folder. If that's the case, you might need to give the absolute path of `ae-de-1week-course/workshops/workshop1`

## Tasks

Use Codex to answer questions on the project structure:

1. Understand the current folder structure
```
Please describe the current folder structure under `workshop1`. Explain what each top-level folder appears to be used for.
```

2. Understand on a high level what `report.py` does

```
Please read report.py and explain what it does in business terms, including any reports or outputs it produces.
```

Use Codex to make code changes

1. Refactor `report.py` into a target directory structure 

Putting the entire ETL logic into one file is not a good design. Let's ask the agent to refactor the code into a modular design.

```
Refactor the report.py into the service-oriented structure shown below by following best software development practice. Create new files and update imports as needed, but do not change behavior.

# Target structure
src/
  data_access/
  services/
  models/
  jobs/
    report.py
  utils/
```

You can add more specific details in the prompt, which will help the agent to produce a more accurate and relevant result. Here are some examples:
- Naming convention of directory/folder/modules/functions etc
- State which functions/classes should live in each layer (e.g., CSV reading in data_access, aggregation logic in services, path helpers in utils)


2. Run `python src/jobs/report.py`. The code behavior should be the same as before

If you encountered any error, try pasting the error into Codex and ask the agent to troubleshoot and fix the bug. I ran into some import errors after the agent refactored the code. The agent was able to identify and fix the errors.

3. Add comments and docstrings
```
Add docstrings to each module and function in src: describing purpose, inputs, and outputs. Keep them concise.
```


## Extra Tasks

I hope you enjoyed the workshop and experienced how powerful Codex can help with software development. Below are some of the other tasks you can ask Codex to do. 

1. Update code base to use pandas or pyspark

```
Update report.py to use pandas for the ETL
```

2. Update the output for report1 and report3 by replacing product_id with product_name

```
For report1 and report3, replace product_id with product_name.
Use product.csv for the mapping between product_id and product_name
```

3. Add unit tests

```
Create unit tests for `src/jobs/report.py` under `tests/` that validate each report output file is generated and has the expected headers and row counts.
```

4. Generate data

```
You are provided the schema of the data model in `schema.md`. Generate sample data that follows the same structure as `test_data/source`. Save the new data in `test_data/source2`. Do not violate any foreign key constraints.
```

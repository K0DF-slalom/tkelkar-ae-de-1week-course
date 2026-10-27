# Steps to connect to Postgres via DBeaver

## Step 1: Install Postgres

- Install Postgres following the OS-specific installer: <https://www.postgresql.org/download/>.

## Why Postgres?

- PostgreSQL is an open-source, object-relational system with 35+ years of development; it powers many cloud products such as Redshift, GreenplumDB, and Hydra because of its reliability and extensibility.

## Step 2: Install DBeaver

- Download the latest DBeaver release for your platform: <https://dbeaver.io/download/>.

## Why DBeaver?

- DBeaver is a universal, open-source SQL client that lets you browse schemas, edit tables, run queries, and manage connections across relational and NoSQL databases through a single GUI.

## Step 3: Automate the workflow with Codex

- Create a dedicated folder for the project and `cd` into it.
- Prompt Codex to connect to your local Postgres instance, create the requested schema/table, and keep secrets/configuration out of the repository.

### Prompts used

- “Write a python script that connects to `postgres` on `jdbc:postgresql://localhost:5432/postgres` using Database Native authentication with user `postgres`.”
- “Store the password in a separate file and source it from the scripts.”
- “Create a helper script that builds a virtual environment, keeps packages isolated, and avoids Homebrew conflicts so the scripts use the right interpreter.”
- “Add a Python script that creates a table whose name is provided by the user only after a successful connection to the `postgres` database that already exists.”
- “Refine the prompts based on Codex’s output until the scripts run cleanly.”

## Step 4: Query via DBeaver

- After Codex sets up the helper scripts and table, open DBeaver, connect to `localhost:5432/postgres`, and run `SELECT * FROM <your_table>;` to verify the data structure and connectivity.

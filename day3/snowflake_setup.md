# Steps to Connect to Snowflake

- Gather your account locator, region, username,database,schema and a role with the right warehouse access.
- Pick your access method (Snowsight worksheet, SnowSQL CLI, or programmatic connector) and authenticate, including MFA if prompted.
- Set the active role and warehouse, e.g., `USE ROLE <role>; USE WAREHOUSE <warehouse>;`, then sanity-check with `SELECT CURRENT_VERSION(), CURRENT_ROLE(), CURRENT_WAREHOUSE();`.
- Install Python helpers with `pip install snowflake-connector-python python-dotenv`.
- Populate `.env` with account/host, user, warehouse, database, schema, role, plus a single auth choice (`SNOWFLAKE_PASSWORD`, key pair, or `SNOWFLAKE_AUTHENTICATOR=externalbrowser`).
- Add overrides such as `SNOWFLAKE_HOST`, `SNOWFLAKE_TARGET_TABLE`, or `CSV_SOURCE_PATH` if you need custom behavior.
- Run python script to load the `.env`, handle SSO browser flow when required, create the schema/table, and execute ingestion.

## Useful Links

- Obtain Snowflake Sandbox access: <https://twodegrees1.sharepoint.com/teams/GlobalAlliances/SitePages/Snowflake-Sandbox-Request.aspx>
- Refer the link to know about Slalom Sandbox roles and access.
 Admin access could be required for database/schema creation: <https://twodegrees1.sharepoint.com/:w:/r/teams/GlobalAlliances/_layouts/15/Doc.aspx?sourcedoc=%7B785303E9-D884-4FE8-82E0-68237694DA68%7D&file=SNOWFLAKE%20INNOVATION%20LABS%20MANAGEMENT%20POLICY.docx&action=default&mobileredirect=true>
- Snowflake Database/Schema Creation: <https://docs.snowflake.com/en/sql-reference/commands-database>

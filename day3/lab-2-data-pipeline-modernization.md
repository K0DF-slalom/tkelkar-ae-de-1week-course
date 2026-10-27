# Lab 2: Data Pipeline Modernization

_Time estimate: 90–120 min_

- Establish a secure connection to your preferred platform (Worksheet, Snowsight, or scripted connector) and document the roles/warehouses you’re using.
- Ingest a vetted synthetic, non-sensitive dataset into a bronze-stage table; capture the raw-to-stage copy commands and any file-format choices you make.
- Provide an intentionally inefficient query that promotes data into a silver-layer table. Ask Codex to refactor it for performance and clarity, then implement the suggested improvements.
- Use Codex to design and implement change data capture (CDC) logic for your preferred dataset, ensuring incremental updates flow from bronze to silver.

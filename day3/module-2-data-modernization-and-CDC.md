# Module 2 — Data Modernization & CDC

**Timebox:** 45–60 minutes

## Overview

Pair Codex with your preferred platform to modernize an end-to-end pipeline: document roles/warehouses, harden bronze ingestion, refactor silver promotion SQL for readability and performance, and stand up reliable CDC paths for incremental files. The output is a repeatable playbook that proves the modernization choices and the evidence behind them.

## Process

- Capture the connection setup (roles, warehouses, tooling) for your preferred platform. Share it with Codex so prompts include accurate runtime constraints.
- Load the vetted synthetic dataset into bronze, narrating copy commands, file formats, and any security or masking considerations along the way.
- Provide an intentionally inefficient silver-layer query and co-author an optimized version with Codex, then document which improvements you kept.
- Design Change Data Capture (CDC) logic for your preferred dataset, validating how incremental updates move from bronze to silver and how conflicts are resolved.
- Summarize modernization decisions, CDC behavior, and verification evidence so the lab log doubles as an audit trail.

## Lab

Please proceed to [Lab 2](https://bitbucket.org/slalom-consulting/ae-de-1week-course/src/main/day3/lab-2-data-pipeline-modernization.md).

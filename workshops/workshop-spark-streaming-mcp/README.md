# IMPORTANT
 Use this README as the guide to this project.

> This is something you should be able to build after getting to Day 4 course material.

 The rest of the code in this codebase is what I produced using the CODEX prompts and my objective of the project to build a stock data streaming service hosting its own MCP.

 The aim for you would be to achieve something similar with the guidelines listed below. It is also aimed to teach you a more practical use of using all the concepts such as AGENTS and SKILLS. Feel free to add as many SKILLS you want or use a completely different approach to it. The QUICKSTART.md is the way I run this project.

If you wish you can use different Agentic Frameworks to achieve this like,
https://docs.bmad-method.org/tutorials/getting-started/
https://github.com/Fission-AI/OpenSpec
https://github.com/obra/superpowers/tree/main

# Build a Local Streaming Platform with Codex CLI

You're going to build a real-time data pipeline from scratch using an AI coding agent. Data flows in, gets transformed on the fly, lands in a database, and becomes queryable through an MCP server. How you get there is up to you.

The companion repo is **one** example of a finished version. Your version will probably look different — different structure, different libraries, different database, maybe a completely different domain. That's the point.



### Setting Up an AGENTS.md File

An AGENTS.md file is a persistent instruction set that lives in your repo and shapes how Codex behaves across every interaction within that project. Unlike a SKILL.md that you call on for specific context, the AGENTS.md is always active — Codex reads it automatically and follows its rules for every task.
For a project like this, your AGENTS.md might say things like:

Always use Python 3.12+ syntax
Follow functional style — no classes unless explicitly asked
All database queries must use parameterized statements
Put configuration constants in config.py, never hardcode connection strings
Write docstrings on every public function
When creating new files, follow the existing directory layout under src/
Test any Docker changes by including the docker-compose up verification step

>As your project takes shape, you'll find yourself correcting Codex on the same things repeatedly. That's your signal to add a rule to AGENTS.md. Over time it becomes a codified version of "how we do things in this repo" and Codex stops making those mistakes.

### Using a SKILL.md File
A SKILL.md is a markdown file you keep in your repo that Codex can read on demand for context about a specific task. It's not a persistent system prompt — it's a reference doc you point Codex to when it needs to understand something about your setup before generating code.

For example, you might create a SKILL.md that describes your project's streaming architecture, which database you picked, how the Docker services connect, and what schema your data follows. Then when you ask Codex to add a new MCP tool or a new source reader, you tell it to read the SKILL.md first so it has the full picture.

The more specific your SKILL.md is to the task at hand, the better the output. A good one for this project might cover your chosen tech stack, your data schema, your Docker networking setup, and the MCP server's tool conventions — whatever Codex would need to produce code that actually fits.
You can find community-contributed skills and learn more about the format at skills.sh

> AGENTS.md is like your employee handbook everyone reads it on day one and it governs how they work. SKILL.md is like a standard operating procedure document it sits in a binder until someone needs to do that specific task, then they pull it out and follow it.

---

## What You're Building

```
Live Data  →  Stream Processor  →  Database  →  MCP Query Layer
```

A source generates data. A stream processing engine picks it up, transforms and aggregates it in real time. Results land in a persistent store. An MCP server sits on top and lets any MCP client query the results.

---

## Prerequisites

- Docker running locally (Colima, Docker Desktop, or native)
- Codex CLI installed and authenticated
- A terminal

---

## Phase 1 — Infrastructure

**The goal:** Get a containerized environment running with a stream processing engine and a database, all talking to each other.

Prompt Codex to set up a Docker Compose project that runs:

1. A stream processing engine (Spark, Flink, or anything you want to learn)
2. A database for storing results (Postgres, SQLite, MySQL, DuckDB — your call)
3. Enough configuration that services can find each other

You're done with this phase when you can `docker-compose up`, all containers come up healthy, and you can connect to your database from inside one of the containers.

---

## Phase 2 — Data Generation

**The goal:** Have something producing realistic-looking data that your stream processor can consume.

Pick a domain you find interesting — stock trades, IoT sensor readings, web clickstreams, game events, whatever. Then prompt Codex to build a data generator that:

- Produces records with at least 4–5 fields including a timestamp
- Sends data over a transport your stream processor can read (TCP socket, file drops, HTTP, etc.)
- Runs continuously at a configurable rate

You're done when you can start the generator and see data flowing (even if nothing is consuming it yet).

---

## Phase 3 — Stream Processing

**The goal:** Ingest the generated data, transform it, and write results to your database.

This is the core of the project. Prompt Codex to build a stream processor that:

1. **Reads** from your data source
2. **Enriches** the raw data — add at least one computed field and one conditional/categorized field
3. **Aggregates** using time windows — pick a window size that makes sense for your data rate
4. **Writes** both the enriched records and the aggregated results to your database

You're done when you can start the generator, start the processor, and then query your database to see rows appearing.

---

## Phase 4 — Validate End to End

**The goal:** Confirm the whole pipeline works.

Run the generator and processor together. Query the database and verify:

- Raw/enriched records are landing
- Aggregated results are appearing
- Timestamps make sense and data looks reasonable

If something's broken, paste the error into Codex and work through it. Debugging a streaming pipeline is half the learning.

---

## Phase 5 — MCP Server

**The goal:** Make your streaming data queryable through MCP.

Prompt Codex to build an MCP server that:

- Connects to your database
- Exposes at least 3 tools that answer different questions about the data (recent records, aggregations, summaries, etc.)
- Runs as a service alongside the rest of your stack

Test it with MCP Inspector or any MCP client. You're done when you can call your tools and get back real data from the pipeline.

---

## Phase 6 — Add a Second Source

**The goal:** Show that your pipeline can handle multiple input types.

Prompt Codex to add an alternative data source — a different transport, a different format, or a built-in test generator. Update your processor to handle both. This demonstrates that the processing logic is decoupled from the ingestion layer.

---

## Phase 7 — Explore and Extend

Pick one or more of these and prompt Codex to help you build it:

- A monitoring dashboard or web UI showing pipeline health
- Deduplication logic in the stream processor
- A filtered alert stream (e.g., high-value events written to a separate table with its own MCP tool)
- A join between the stream and a static reference dataset
- Proper checkpointing so the pipeline can recover from crashes

---

## Alternative Prompts to Try

The same project brief can produce very different results depending on how you prompt. Here are starting points that would each lead to a different codebase:

**Different processing engine:**
> "Build a real-time data pipeline using Flink instead of Spark. I want to process streaming stock data, store it in Postgres, and query it via MCP."

**Different language:**
> "Build this streaming pipeline in Scala/Java instead of Python. Use Spark's native API."

**Different database:**
> "Use DuckDB as an embedded analytical database instead of Postgres. I don't want a separate database container."

**Different architecture:**
> "Build the stream processor as a simple Python async application using asyncio instead of Spark. No heavy framework — just read from a socket, process, and write to SQLite."

**Different domain:**
> "Instead of stock trades, generate IoT temperature sensor data from 50 simulated devices. Aggregate by device and time window. Alert when a device exceeds a threshold."

**OOP vs functional:**
> "Structure the stream processor using classes — a SourceReader base class, a Transformer class, and a SinkWriter class. I want clean separation of concerns with inheritance."

**Kafka in the mix:**
> "Add Kafka as the message broker between the data generator and Spark. I want the generator to produce to a topic and Spark to consume from it."

**Different MCP tools:**
> "Design the MCP server to expose analytical tools — trend detection, anomaly flagging, and comparative summaries — not just raw queries."

**Minimal version:**
> "Build the simplest possible version of this pipeline. One Python file for the generator, one for the processor, one for the MCP server. No Spark, no Docker. Everything runs locally."

**Production-hardened version:**
> "Add retry logic, dead letter queues, idempotent writes, health checks, and structured logging to the pipeline. I want it closer to production-grade."

Each of these will teach you something different about the same problem space. The streaming concepts stay the same — sources, transforms, sinks, windowing, state — but the implementation varies wildly. That's what makes it worth trying more than once.
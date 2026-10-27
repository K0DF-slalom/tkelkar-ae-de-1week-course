## Goal

The goal of the workshop is to introduce core agent configuration concepts and show how they improve coding workflow quality, safety, and consistency.

In this workshop, you will:
- Understand how `AGENTS.md` sets project-specific behavior, coding standards, and collaboration rules.
- Use skills to give the agent reusable, task-specific workflows (for example, onboarding, refactoring, testing, or release tasks).
- See how good agent configuration reduces ambiguity, improves prompt quality, and produces more reliable code changes.

## Scenario

This workshop builds on what you have learned from [Workshop 1](../workshop1/README.md). However, you can complete this workshop without going through Workshop 1. To begin, you can try asking the agent to explain the project structure.

## Environment setup

Refer to [Workshop 1 setup instructions](../workshop1/README.md) and complete that setup before starting Workshop 2.

1. **After your environment is set up, activate the virtual environment:**

On Windows:
```bat
.venv\Scripts\activate.bat
```

On macOS:
```bash
source .venv/bin/activate
```

<br /><br />

2. **Install the python modules:**
```
pip install -r requirements.txt
```

<br /><br />

3. **Verify that you can execute the ETL**
`python -m src.jobs.report_main`

## Tasks

### Task 1: Introduce `AGENTS.md`

#### Intro

`AGENTS.md` is a file that serves as a knowledge base and instruction manual for AI coding agents working on your project. It provides context, guidelines, and project-specific information that helps agents understand how to work effectively within your codebase. When an AI agent is tasked with coding work, it reads agents.md first to understand the project structure, conventions, and constraints before making any changes.

Here are some examples that we can put in `AGENTS.md`.
- Python environment details - Python version requirements, virtual environment setup, package manager (pip/poetry/conda), and dependency management approach
- Project structure and conventions - Directory layout, module organization, naming conventions (PEP 8), and where agents should create/modify files
- Testing framework and practices - Test runner (pytest, unittest), test file locations, coverage requirements, fixture patterns, and mocking strategies

#### Steps
Below, we will put documentation guideline in `AGENTS.md` and see how the agent generates the documentation

1. **Run this prompt:**

```text
Add documentation to reporting_service
```

<br /><br />

2. **Check the result in `src/services/reporting_service.py`.**

<br /><br />

3. **Add the following to `AGENTS.md`, which is already created on the root of this workshop directory:**

```md
## Documentation
- Use Google-style docstrings
- Document all public functions
- Include type information and examples
```

<br /><br />

4. **Run the same prompt again:**

```text
Add documentation to reporting_service
```

Since we added an instruction to include examples in `AGENTS.md`, the comments now include usage examples.


### Task 2: Introduce Skills

#### Intro

Skills are reusable, task-specific workflow documents that guide AI agents through complex, multi-step processes. While agents.md provides general project guidelines, skills define detailed procedures for specific tasks like testing, refactoring, code review, or deployment.

When you reference a skill in your prompt (e.g., "Use the generate_tests skill"), the agent reads that skill file and follows its step-by-step instructions to complete the task consistently and thoroughly.

What to Include in a Skill?
- Purpose and scope - What the skill accomplishes and when to use it
- Step-by-step workflow - Detailed procedures the agent should follow in order
- Success criteria - How to verify the skill was executed correctly
- Tool and command usage - Specific commands to run (e.g., pytest, black, mypy)
- Examples and templates - Sample inputs/outputs or code patterns to follow
- Error handling - What to do when steps fail or produce unexpected results

#### Steps
We will work through the following steps to create a skill that helps the agent generate consistent, high-quality test cases.

1. **We have created a skill, which is located at `skills/generate_tests/SKILL.md`. Open up the file and take a look at the skill definition.**
   - This skill is focused on creating pytest unit tests for Python modules.
   - It requires coverage across happy paths, edge cases, and error handling.
   - It enforces test naming and structure conventions so outputs are consistent.
   - It includes a simple success checklist so you can verify quality quickly.

<br />

2. **Ask the agent following prompt to install the skill:**
   ```text
   Use skill-installer to install the skill from skills/generate_tests
   ```
   During installation, the agent will:
   - Copy the skill into Codex's global skills directory: `$CODEX_HOME/skills/generate_tests`.
   - Windows example: `C:/Users/<your-username>/.codex/skills/generate_tests`.
   - macOS example: `/Users/<your-username>/.codex/skills/generate_tests`.
   - Register it for discovery so future prompts can invoke it by name (`generate_tests`).
   After this step, ask the agent to list available skills and confirm `generate_tests` is present. You might need to start a new Codex chat window for the agent to see the new skill.

<br />

3. **Ask the agent to generate the test cases for `services/reporting_service.py`**
   ```text
   Create unit tests for all functions in services/reporting_service.py
   ```
   You should see that the agent is using the `generate_tests` skill to generate the test cases.

<br />

4. **Run the unit tests by running**
   `pytest`

    If you encountered any error, ask the agent to fix it!
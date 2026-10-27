# Module 2 — Prompt Engineering Workshop

**Timebox:** 45–60 minutes

## Overview

In this module, you will create prompts and learn best practices for the process.

You will create four prompts. Each prompt must start from a **fresh Codex session**.

⚠️ This module is intentionally designed for you to make mistakes.
You are not expected to “get it right” on the first attempt.

The goal is to:
Observe how Codex behaves with vague, incomplete, or flawed prompts
Learn how small changes in structure, constraints, and clarity affect results
Build intuition for what works and what breaks when prompting
If something goes wrong, notice what Codex assumed, invented, or misunderstood.

Common mistakes:
Forgetting edge cases
Being ambiguous about inputs/outputs
Assuming Codex “knows the repo”

## Process

1. **Story creation prompt**: generate a Markdown story file (or files) that describe the task you want Codex to complete.

    Purpose: Externalize your intent before thinking about implementation.

    Focus on:
    Describe what should be built, not how
    Capture constraints, boundaries, and “out of scope” areas
    Expect to miss things — that’s okay

    Template

    ```markdown
    ## Story: <Short, descriptive title>

    ## User Story

    As a ____________________________,
    I want to be able to ____________________________,
    so that ____________________________.

    ## Background

    This problem exists because ____________________________.

    This capability will primarily be used by ____________________________.

    ## Objective

    Codex should help implement a solution that:

    - __________________________________
    - __________________________________
    - __________________________________

    ## Inputs

    The solution will receive:

    - __________________________________
    - __________________________________

    ## Outputs

    The solution should produce:

    - __________________________________

    ## Acceptance Criteria

    - The solution should ____________________________
    - The solution should NOT _________________________
    - Success is measured by __________________________

    ## Constraints

    - Must / must not __________________________________
    - Performance / scale expectations (if any): __________
    - Data assumptions: _________________________________

    ## Out of Scope

    This solution should NOT:

    - __________________________________
    - __________________________________

    ## Open Questions / Known Gaps

    - __________________________________
    - __________________________________
    ```

1. **Story review prompt**: review the story, return a confidence score, and run an anti‑hallucination check (missing files, assumptions, unclear constraints).

    Purpose: Force Codex to critique your thinking, not just generate code.

    Focus on:
    Asking Codex to be skeptical
    Surfacing assumptions and hallucination risks
    Treating Codex like a reviewer, not a builder

    Template

    ```markdown
    You are reviewing the following story for clarity, completeness, and risk.

    Please do the following:

    1. Return a confidence score (0–100%) for how implementable this story is.
    2. Identify any missing files, inputs, or context you would need.
    3. Call out assumptions you would have to make.
    4. Flag areas that are ambiguous or underspecified.

    Be direct and critical.

    Story:

    <PASTE STORY HERE>
    ```

1. **Optimized developer prompt**: a concise, high‑signal implementation prompt derived from the approved story.

    Purpose: Translate intent into a high-signal execution prompt.

    Focus on:
    Being concise without losing constraints
    Removing narrative fluff
    Making expectations explicit

    Template

    ```markdown
    You are implementing a solution based on the approved story below.

    Requirements:

    - Implement ____________________________
    - Inputs: _______________________________
    - Outputs: ______________________________
    - Constraints: ___________________________

    Guidelines:

    - Follow the story exactly
    - Do not invent new requirements
    - If something is unclear, call it out before implementing

    Story reference:
    <PASTE FINAL STORY OR SUMMARY HERE>
    ```

1. **Code review prompt**: review the implemented code against the story, risks, and verification steps.

    Purpose: Close the loop and detect drift, risk, and silent failure.

    Focus on:
    Verifying alignment with the story
    Identifying hidden assumptions
    Evaluating correctness, not style alone

    Template

    ```markdown
    You are reviewing the following implementation against the original story.

    Please:

    1. Identify where the code aligns with the story.
    2. Call out any deviations or invented behavior.
    3. Identify risks, edge cases, or failure modes.
    4. Suggest verification or test steps.

    Story:
    <PASTE STORY>

    Code:
    <PASTE CODE>
    ```

## Lab

Please proceed to [Lab 1](./lab-1-four-prompt-sequence.md).

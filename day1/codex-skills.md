# Codex Bootcamp (Day 1): Skills — what they are, why they matter, and how to use them

## What “Skills” mean for AI Software Engineering Agents

**Skills** are a lightweight way to package **reusable expertise** (workflows, guardrails, scripts, templates, references) so an AI coding agent can apply them **automatically when relevant**, instead of you rewriting the same instructions every session.

In both Anthropic’s and OpenAI’s implementations, the key idea is **progressive disclosure**:

- The agent learns **only the essentials** about each skill up front (so context stays small).
- The agent opens the **full instructions and resources** from disk only when the task calls for it.

## What a Codex skill is (Codex CLI)

Codex can discover “skills” you keep on disk. A skill is a small bundle with:

- a **name**
- a **short description** (what it does and when to use it)
- an optional **body of instructions** (and often supporting files like scripts/templates)

Crucially, Codex keeps runtime context lean by injecting only **name + description + file path**—the skill body stays on disk until needed.

> Note: Codex skills are currently an **alpha** feature. You can enable them today by running `codex --enable skills` from your terminal. In the future, skills should default to enabled. Treat skills as a productivity aid, not a guarantee, and verify outputs.

---

## Why you should use Skills in a bootcamp (and beyond)

## 1) Consistency and reliability

Skills capture “the right way” your team wants things done (repo conventions, testing habits, release steps, security checks), so Codex repeats good patterns—not random variations.

## 2) Faster onboarding and less prompt wrangling

Instead of re-explaining your stack and workflow every time, you install it once and let Codex pull it in on demand.

## 3) Token efficiency (the hidden superpower)

Skills scale without bloating prompts:

- load only metadata initially
- read instructions/resources only when triggered

## 4) Composability (real workflows are multi-skill)

You can “stack” skills: the agent can coordinate several skills when a task crosses concerns (e.g., “API changes” + “security review” + “release checklist”).

---

## How Codex Skills work in practice

## Where skills live on disk

Codex discovers skills at startup from:

- **macOS (typical):** `~/.codex/skills/`

Each folder under that directory can represent one skill.

### Recommended structure (example)

```text
~/.codex/skills/
  repo-first-10-min/
    SKILL.md
  docx-markdown-converter/
    SKILL.md
    scripts/
      convert.sh
    references/
      style-reference.docx
```

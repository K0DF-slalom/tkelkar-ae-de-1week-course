# Codex Development Best Practices

Last updated: 2026-01-08 12:10 CST by Codex

Guidance for building and maintaining Codex projects with predictable quality.

This guide focuses on day-to-day Codex workflow and team practices.

## Codex Workflow Habits

- **Codify expectations in `AGENTS.md`**: Treat the closest `AGENTS.md` as the live operations manual for Codex. Add explicit rules—"make lots of small commits," "prefer uv over pip," security gates, etc.—so the CLI ingests them automatically. Promote recurring heuristics into Codex "memories" so the assistant recalls tribal knowledge without re-prompting every session.
- **Keep the context buffer healthy**: Resist filling the Codex context window to 100%. Run `/compact` proactively and aim to hover near 50% utilization so you can paste new logs, stack traces, or PR feedback without evicting critical instructions.
- **Review before you commit**: Use `/review` (or your repo’s equivalent automation) prior to every commit to surface lint/test reminders, summarize the diff, and catch surprises while changes are still small.

## Working Agreement (Before You Code)

Codex is most effective when you start with crisp constraints and a testable definition of success.

- **Frame the task**: Write 2–6 bullets that cover goal, non-goals, constraints (time/perf/security), and acceptance criteria.
- **Prefer small, reviewable diffs**: Keep PRs narrowly scoped; avoid drive-by refactors unless explicitly required by the task.

Suggested prompt skeleton:

```text
Goal:
Non-goals:
Constraints:
Acceptance criteria:
```

## Execution Loop (While You Code)

- **Repro-first debugging**: Capture exact repro steps, the commands you ran, and expected vs actual behavior. Paste only the minimal logs needed.
- **Quality gates in order**: Run the smallest checks first (format/lint/typecheck/unit tests), then broader suites. For doc-only repos, run `pre-commit run -a`.

## Model Selection (Codex)

- **Default to the standard model**: Use the general-purpose model for most tasks; it balances quality and speed.
- **Choose faster models for iteration**: If you are exploring or running quick changes, pick a lighter model to reduce latency and cost.
- **Escalate for complexity**: For tricky refactors, cross-cutting changes, or high-risk fixes, use a stronger reasoning model and plan for extra review time.
- **Align with risk**: The higher the impact, the more you should bias toward accuracy and add stricter review and testing.
- **Track the latest releases**: See <https://openai.com/index/introducing-gpt-5-2-codex/> for the current GPT-5.2 Codex announcement and availability details. If GPT-5.2 is not available for your account yet, use the latest GPT-5 Codex variant offered in your environment.
- **Prefer Codex variants**: When GPT-5.2 Codex options are available, choose the fastest option for iteration, the default option for routine work, and the highest-capability option for complex changes.
- **Keep the docs handy**: Reference the Codex documentation at <https://developers.openai.com/codex> for updates, examples, and API guidance.

Decision table (map these tiers to the latest GPT-5 Codex options available in your account):

| Scenario | Model tier | Why |
| --- | --- | --- |
| Learning, experiments, quick edits | Fast | Short feedback loop, lower cost |
| Everyday feature work, routine fixes | Standard | Balanced speed and quality |
| Complex refactors, risky changes | High-capability | Higher accuracy, better planning |

## Safety & Security (Always)

- **Protect secrets and data**: Never paste secrets/PII into prompts, issues, or chat transcripts. Treat generated code as untrusted until reviewed.
- **Be explicit about privilege/network**: Call out when a command needs network access or elevated permissions so reviewers understand the risk envelope.

## Traceability & Communication (For Teams)

- **Record decisions**: When a choice is non-obvious, capture assumptions and tradeoffs in the PR description (or an ADR/notes file) and link to it.
- **Definition of done**: Add a small PR checklist (checks run, docs updated, risks/rollback notes) and require `/review` before merge.

# Module 3 — Responsible Use & Governance

**Timebox:** 30–45 minutes
**Prereqs:** Complete Modules 1–2 and confirm you understand your local AI usage policy.

## Overview

Responsible AI use is non-negotiable, especially for new Codex users who may not realize how easily sensitive data can leak into prompts. This module explicitly walks through each rule mentioned in the Day 1 README—no secrets, no client data, constant verification—and turns them into everyday behaviors you can follow even if this is your first week with Codex.

## Why Governance Matters (for Beginners)

- **Cloud services remember prompts.** Providers may retain anything you paste (logs, database rows, API keys) or trigger compliance reviews.
- **Clients trust us with confidential work.** Sending regulated data through Codex can violate contracts and laws.
- **Human review is still required.** Codex accelerates draft creation, but decisions, approvals, and accountability stay with you.

## Learning Objectives

- Articulate what data may and may not enter Codex for your engagement.
- Create a personalized escalation checklist for ambiguous or high-risk scenarios.
- Summarize your organization’s AI or data-handling policy in five bullets.
- Show how you will document attribution and human review for Codex-driven work.

## Key Topics Explained

1. **Data Classification Basics**
   - *Public:* Docs already on the internet. Safe to share.
   - *Internal:* Team processes, sprint boards, architecture diagrams. Share only if policy allows.
   - *Confidential/Regulated:* Client data, PII, financials, healthcare records. **Never** paste into Codex.
   - Action: Label each artifact you plan to share before you open a prompt window.
2. **Secret Management**
   - Secrets include API keys, passwords, certificates, tokens, SSH keys.
   - Use env vars, secret managers, or redacted placeholders (`OPENAI_API_KEY=***`) when describing issues.
   - If a secret slips into a prompt, treat it as a breach: rotate the credential, notify your security contact, and document the incident.
3. **Attribution & Intellectual Property**
   - When Codex provides code or prose you keep, note it in the PR description or changelog (e.g., “Implemented with Codex help; manually verified.”).
   - Cite external sources (Stack Overflow, docs) that you included in the prompt or output.
4. **Human Review & Verification**
   - Every Codex-generated change must pass tests/linting and receive human review just like hand-written code.
   - Keep a log of what you ran (`pytest`, `npm test`, manual steps) so auditors can trace your verification.
5. **Personal Red Lines**
   - Examples: “I stop and escalate if I’m unsure about data classification,” “I never run Codex-generated SQL against production without review,” “I reject any diff that lacks tests for behavior changes.”
   - Write these down and keep them near your prompt template.

## Workshop Steps

1. **Policy Digest (10 min)** — Read or re-read your org’s AI usage policy. Summarize it in five concise bullets, focusing on data boundaries and approval flows.
2. **Risk Brainstorm (10 min)** — List recent incidents or near misses (e.g., sensitive datasets uploaded to SaaS tools). Map each to a mitigation.
3. **Red Line Checklist (10 min)** — Convert mitigations into a checklist you can apply before sending prompts or accepting Codex output.
4. **Share & Calibrate (5–10 min)** — Compare checklists with peers or your lead to ensure consistent thresholds.

## Hands-On Practice

- Draft a “Codex-ready” snippet of context for a current ticket, ensuring you scrub all sensitive data.
- Run your checklist before prompting; document any red flags discovered.
- Capture how you will log attribution for the resulting change (e.g., PR template, changelog entry).
- Pair with a teammate and simulate an escalation call: one person reports a potential policy violation, the other walks through the remediation steps.

## Discussion Prompts

- How will you prove compliance if an audit occurs next quarter?
- Which tool or automation could prevent accidental disclosure?
- What is your escalation path if you see risky Codex usage?
- What language will you use in PRs or documentation to show Codex involvement without exposing sensitive info?

## Evidence to Capture

- Five-bullet summary of the AI usage or data policy (store in your daily log).
- Personal red-line checklist (include owners for each escalation path).
- Example attribution note or PR comment showing human review.
- Screenshot or log entry proving you ran verification steps after using Codex.

## Resources & Next Steps

- Organization-specific AI governance docs (link internally if available).
- [OpenAI Trust & Safety hub](https://openai.com/policies/trust-safety) for public references.
- Optional: propose a lightweight `RESPONSIBLE_USE.md` addition to your repo with the agreed checklist.

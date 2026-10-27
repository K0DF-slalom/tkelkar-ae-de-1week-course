# 1-Week Course — Day 0: Prerequisites & Setup

Day 0 gets your environment and access ready so Day 1 can start on time. Expect about 3–4 hours for most learners.

## Outcomes

- Access is confirmed for required systems and the course repository.
- An approved AI assistant is available: Codex through an OpenAI Enterprise account, or Microsoft Copilot for learners without that account.
- Core tools are installed and verified for Day 1 through Day 3.
- A data platform path is chosen and ready for Day 3+ labs.
- Learners have a clear checklist to confirm readiness.

  - Knowledge check: confirm these foundations so you get the best experience throughout the course.
    - Foundational AI concepts [OpenAI Partner Portal courses](https://openai-partneru.sana.ai/>)
    - GenAI fundamentals (LLMs, agents, prompting)

  - Working knowledge of Python, Bash shell, and Git:
    - Shell: comfortable at a shell prompt, navigating directories, and setting environment variables.
    - Git: comfortable cloning a repo, checking status, and making commits.
    - Python: comfortable with language fundamentals and setting up a virtual environment.

  Note: To enroll in the OpenAI courses, please complete the Partner Training Portal Access Request Form [here](<https://twodegrees1.sharepoint.com/teams/GlobalAlliances/SitePages/OpenAI.aspx?ct=1749060701191&or=Teams-HL&ga=1&LOF=1>)

## Pre-Work (60–90 min)

- Supported platforms: macOS 12+ (Apple Silicon or Intel), Windows 11 with WSL2, Ubuntu 22.04+ or equivalent Linux distribution.
  - Access and accounts:
    - Confirm which approved AI assistant you will use:
      - **OpenAI Enterprise path:** sign in with your organization-provided OpenAI Enterprise account and confirm that you can access Codex.
      - **Microsoft Copilot path:** if you do not have an OpenAI Enterprise account, sign in to your organization-provided Microsoft Copilot experience with your work account.
  - An OpenAI API key is not required for this course.
  - Bitbucket access to this [repository](<https://bitbucket.org/slalom-consulting/ae-de-1week-course/src/main/>)
    - If you get "Access Denied", submit a ticket via Slalom Support.
    - Ensure you are added to the "AA - Slalom Developers" Bitbucket group.
    - If you run into permission issues post receiving access, Add SSH key to Bitbucket by following any of the below paths:
        1. [Setup SSH on MAC](<https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-macos/>)
        2. [Setup SSH on Windows](<https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-windows/>)
- Local tools:
  - Git installed and configured with your name and email for commits.
- A data platform for Day 3+ (choose one):
  - Local: PostgreSQL + DBeaver (setup: [Postgres + DBeaver](../day3/postgres-dbeaver-setup.md))
  - Local: DuckDB + dbt Core (<https://duckdb.org/> and <https://github.com/dbt-labs/dbt-core>)
  - Snowflake: iLabs or Trial Account (setup: [Snowflake](../day3/snowflake_setup.md))
  - Databricks: iLabs or Free Edition (<https://docs.databricks.com/aws/en/getting-started/free-edition>)

## Core Modules (Async)

### Module 1 — Environment & Access Setup (60–90 min)

1. Confirm Bitbucket access and open the repo link above.
2. Install Git if needed and set your identity (name and email).
3. Set up your approved AI assistant:
   - **OpenAI Enterprise path:** install [Codex CLI](<https://developers.openai.com/codex/cli>) if you will use it for the labs. Launch Codex and sign in with your organization-provided OpenAI Enterprise account. On Windows, follow the [Codex Windows setup guide](<https://developers.openai.com/codex/windows>).
   - **Microsoft Copilot path:** open your organization's approved Microsoft Copilot experience and sign in with your work account. You do not need to install Codex CLI for this path.
4. Verify your chosen assistant:
   - **Codex:** run `codex --help` to check the installation, then launch Codex and confirm you can use your signed-in account.
   - **Microsoft Copilot:** confirm you can start a conversation using your licensed work account.
5. Choose and set up one data platform option for Day 3+.
6. Skim the optional refresher content below if you are new to AI/Codex workflows.

## Hands-On Labs (Self-Service)

### Lab 0: Setup Verification

_Time estimate: 30–45 min_

- You can open the repository in Bitbucket without an access error.
- You can clone the repository locally and run `git status`.
- `git config user.name` and `git config user.email` are set.
- Your approved AI assistant is working:
  - **OpenAI Enterprise path:** `codex --help` prints usage text, and you can launch Codex with your signed-in Enterprise account.
  - **Microsoft Copilot path:** you can start a conversation using your licensed work account.
- You have a working data platform environment (local or cloud) selected.
- You can open `day1/README.md` and `day2/README.md` locally.

## Artifacts to Submit

- Completed verification checklist (copy/paste or notes in your daily log).

## Troubleshooting

- **Bitbucket access denied**: request access via Slalom Support and confirm membership in the "AA - Slalom Developers" group.
- **Git identity missing**: set name/email and re-run `git config --list` to verify.
- **OpenAI Enterprise or Codex access issues:** confirm you are signed in with the organization-provided account and that Codex access is enabled for it. If access is unavailable, use the approved Microsoft Copilot path or request access through your organization's support process.
- **Microsoft Copilot access issues:** confirm you are using the licensed work account. If access is unavailable, request help through your organization's support process.
- **Tool install blocked**: check corporate device permissions or proxies, then retry with admin approval.

## Useful Intro Videos (60 min)

- [Getting Started with Codex](<https://www.youtube.com/watch?v=px7XlbYgk7I>)
- [Intro to Context Engineering](<https://www.youtube.com/watch?v=Egeuql3Lrzg&t=8s>)
- [Deep dive with examples](<https://www.youtube.com/watch?v=Mk87sFlUG28>)

## Recorded Demos

- Here is a [link](https://twodegrees1.sharepoint.com/:f:/r/teams/DataModernizationAccelerated-Codex-Bench/Shared%20Documents/Recorded%20Demos?csf=1&web=1&e=F9MwBa) to the recorded demos from past cohorts.
- Browse the demos only to see the kinds of outcomes others have showcased. Treat them as inspiration, not as a prescription, for how you could frame your own demo.

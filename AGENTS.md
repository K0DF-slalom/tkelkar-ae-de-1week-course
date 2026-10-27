# Repository Guidelines

## Project Structure & Module Organization

- `README.md` is the entry point and links to the 5‑day curriculum.
- `day1/` … `day5/` each contain a `README.md` with agenda, concepts, and exercises.
- Most contributions are edits to `dayN/README.md`; keep cross-links in `README.md` accurate.
- Quality/config files live at the repo root: `.pre-commit-config.yaml`, `.markdownlint.yaml`, `.yamllint`, `.commitlintrc.json`.

## Build, Test, and Development Commands

This repository is primarily Markdown-based (no build step required). Use pre-commit to keep docs consistent:

- Install `pre-commit` (choose one): `pipx install pre-commit` (recommended), `brew install pre-commit`, or `python3 -m pip install --user pre-commit`
- Install hooks: `pre-commit install` and `pre-commit install --hook-type commit-msg`
- Run on all files: `pre-commit run --all-files`
- Update hook versions (optional): `pre-commit autoupdate`

## Coding Style & Naming Conventions

- Markdown: follow `markdownlint` rules from `.markdownlint.yaml` (the hook runs with `--fix` where possible).
- YAML: follow `yamllint` rules from `.yamllint`.
- General hygiene: no trailing whitespace, ensure final newline, keep files reasonably sized.
- Naming: keep day folders as `dayN/` and prefer descriptive section headings in `dayN/README.md`.

## Testing Guidelines

No automated test suite exists in this repo. Treat `pre-commit run --all-files` as the primary “CI-like” check before opening a PR.

## Commit & Pull Request Guidelines

- Commit messages: use Conventional Commits with a required scope, e.g. `docs(day2): clarify spec → plan flow`.
- Common scopes (see `.commitlintrc.json`): `docs`, `ci`, `build`, `deps`, `security`, `test`, `perf`, `refactor`, `core`, `infra`, `api`, `ui`, `auth`.
- Keep commits focused and scoped to one day/topic where possible.
- PRs: include a short summary, link any related issue/material, and call out any curriculum changes (added/removed sections, updated links, new exercises).

## Security & Content Safety

- Do not add secrets (API keys, tokens) or sensitive/client data to examples or docs.
- Prefer placeholders (e.g., `OPENAI_API_KEY=...`) and clearly mark simulated data.

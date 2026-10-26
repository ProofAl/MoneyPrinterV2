# Dormant MoneyPrinterV2: no-spend source review

The AVOS portfolio catalog lists this repository as an **archived reusable asset**. This change adds source scanning only; it does not reactivate the product or modify marketing/publication.

- Workflow: `.github/workflows/archived-security-review.yml`.
- Triggers: only a relevant new internal PR or a deliberate manual GitHub Actions dispatch. No scheduled runs and no main-branch push events. Archived/no-PR periods therefore generate no model or CI calls from this workflow.
- Engine: pinned Semgrep CE v1.181.0 Docker image, four local Python rules. Network is disabled inside the scanner; repo mounted read-only; no env secrets or outbound API. Findings appear as a GitHub job summary only and are **advisory**.
- Safety: never run `src/main.py`, `src/cron.py`, Selenium, TTS, SMTP, publishing, outreach or scheduled workflows as part of this scan. Do not enable external AI/cloud code access merely to run the scanner.
- Re-activation: after a future owner portfolio decision, add actual tests/build checks and permission-scoped external services separately. The scanner is not a qualified R2/R3 independent AI reviewer.

GitHub-hosted Actions minutes may be consumed for future qualifying PRs or manual runs, even though no AI API usage is incurred. Disable the workflow or revert the PR to roll back safely.

GitHub Issues is disabled in this repository (HTTP 410 when creating an issue). Portfolio tracking is via `ProofAl/autonomous-venture-os#78`.

CI workflows and run controls

Overview
- Unit & Integration: `.github/workflows/python-app.yml`
- Playwright E2E: `.github/workflows/playwright-e2e.yml`
- Selenium E2E: `.github/workflows/selenium-e2e.yml`
- Robot Framework: `.github/workflows/robot-tests.yml`
- BDD (pytest-bdd / Playwright): `.github/workflows/bdd-tests.yml`
- Generic E2E helper: `.github/workflows/e2e-tests.yml` (keeps additional logic)

Automatic behavior (default)
- Each workflow is configured to run automatically only when files relevant to that    workflow change. For example:
  - The primary `python-app` workflow runs when `app/**`, `tests/unit/**`, or `tests/integration/**` change.
  - Playwright/Selenium E2E workflows run when `app/**` or `tests/ui/**` change.
  - Robot runs when `tests/robot/**` or `app/**` change.
  - BDD runs when `tests/acceptance/**` or `app/**` change.

- Documentation-only changes (Markdown under `docs/`, `README*`, or other docs) do not trigger these workflows.

Manual runs
- Every workflow includes `workflow_dispatch`, so instructors or teammates can run any workflow on demand using the "Run workflow" button in the Actions tab.

PR label overrides (force run)
- If path filters don't detect changes but you still want a workflow to run for a PR, add one of these labels to the PR:
  - `run-unit-integration` — forces the `python-app` (unit+integration) workflow
  - `run-e2e` — forces Playwright or Selenium E2E workflows
  - `run-bdd` — forces the BDD workflow
  - `run-robot` — forces the Robot Framework workflow

Implementation notes
- For push events we use `paths` filters so workflows don't run for docs-only commits.
- For pull requests we intentionally perform an in-job check (compare changed files and read PR labels) so that a label can override the default path filtering.
- This repo uses small, focused workflows so CI stays fast while keeping an easy way to run full E2E when needed.

How to add a PR label in GitHub UI
1. Open the pull request on GitHub.
2. On the right-hand panel, find "Labels" and click the gear icon (or the label area).
3. Type or pick the label (e.g., `run-e2e`) and save.


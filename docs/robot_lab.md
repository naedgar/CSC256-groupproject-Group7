# Robot Framework Instructional Lab

## Before You Start

- Ensure Python 3.11+ is installed and a virtual environment is active.
- Install project dependencies: `pip install -r requirements.txt` and `pip install robotframework-requests`.
- If you are behind a proxy, set `NO_PROXY` for localhost before running the tests:

```zsh
export NO_PROXY=127.0.0.1,localhost
export no_proxy=127.0.0.1,localhost
```

## Objectives

- Teach team members to read and maintain the Robot Framework acceptance test suite for the Task Tracker app.
- Show how to run the suite locally and in CI, and how to extend it with new edge-case tests.
- Verify the core TaskService flows (POST/GET/PUT/DELETE) and TimeService regression tests.

## Lab Structure

1. Environment setup (virtualenv + dependencies)
2. Run the baseline Robot suite and confirm it passes
3. Add a POST test (create task) and observe the application behavior
4. Add validation/edge tests (empty title, too-long title, non-string fields)
5. Add TimeService acceptance checks
6. Add CI workflow to run Robot tests (template included)

## Step-by-Step Instructions

1. Start the application (in one shell):

```zsh
cd /path/to/repo
export NO_PROXY=127.0.0.1,localhost
python3 -m app.main
```

2. In another shell, run the Robot suites:

```zsh
cd /path/to/repo
export NO_PROXY=127.0.0.1,localhost
robot --outputdir robot-reports --pythonpath . --loglevel DEBUG tests/robot/suites
```

3. Observe `robot-reports/log.html` and `robot-reports/report.html` for details.

4. To add a new test, create a `.robot` file under `tests/robot/suites/` and reuse keywords from `tests/robot/resources/keywords.robot`.

## Testing (Regression + CI)

- The Robot suite is intended to form the acceptance/regression suite for Task and Time services.
- Locally, ensure `NO_PROXY` is set so RequestsLibrary bypasses corporate proxies.
- In CI, add a Robot job that starts the application using the same `python -m app.main` step used for pytest, and then runs the Robot CLI pointing to `tests/robot/suites`.

### CI Notes

- Use the provided workflow template `.github/workflows/robot-tests.yml` as a starting point. The template deliberately reuses the application start step and does not switch to a live external server.
- Keep Robot runs in a separate job from unit/integration tests to avoid long-running E2E on every push.

## Tutorials / Learning Exercises

1. Convert RequestsLibrary deprecated keywords to `* On Session` variants (exercise included in `tests/robot/resources/keywords.robot`).
2. Add an edge-case test that asserts validation errors for missing title and length limits.
3. Pair-review: one teammate writes tests, another runs them and documents any unexpected app behavior.

## Troubleshooting

- If Requests seem to hit an external proxy (responses not from the app), ensure `NO_PROXY` is set.
- If Robot reports `Non-existing index or alias 'api'`, verify the RequestsLibrary session alias is created before any `* On Session` call (suite setup ordering).

## Lab Completion

- Commit multiple small PRs: (1) Add baseline tests, (2) Add validation tests, (3) Add CI workflow, (4) Add lab documentation. Each PR should be reviewed by teammates.

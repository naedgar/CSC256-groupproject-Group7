Robot Framework tests for Task Tracker

Run locally:

```zsh
export NO_PROXY=127.0.0.1,localhost
export no_proxy=127.0.0.1,localhost
robot --outputdir robot-reports --pythonpath . --loglevel DEBUG tests/robot/suites
```

Notes:
- Ensure `tests/robot/resources/keywords.robot` uses `Create Session` before any `* On Session` calls.
- If tests hit an external proxy, set `NO_PROXY` as shown above.
Robot tests quick start

Prerequisites
- Install Robot deps (see `requirements-robot.txt` at repo root if present).

Run tests
```
python -m pip install -r requirements-robot.txt
robot --outputdir robot-reports tests/robot/suites
```

Notes
- The Robot suites in `tests/robot/suites` use the app API endpoints. Start the Flask app locally before running tests (the lab will show how to reuse the existing app start command used by pytest).
- Reports will be written to `robot-reports/` (add to `.gitignore`).

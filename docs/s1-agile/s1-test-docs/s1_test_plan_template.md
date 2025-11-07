# 🍪 Sprint 1 Test Plan

Understand that while *In-Scope Functionality* defines **what features are being tested**, the *Test Objectives* clarify **why** each feature is tested and **how success is measured**. Including both ensures a complete plan aligned to both development goals and QA validation.

## 📝 Purpose

This test plan documents the initial validation of the Flask development environment, test infrastructure, and the first set of functional requirements from User Stories US000, US001, US002, US003, and US004.

The plan outlines both automated and manual testing strategies used during Sprint 1, with a focus on:

- Establishing test-driven development (TDD) workflows using `pytest`
- Validating continuous integration (CI) through GitHub Actions
- Measuring code coverage using `pytest-cov`
- Performing functional testing on API endpoints (GET, POST) using tools such as `curl`, Postman, and `Invoke-RestMethod`
- Verifying core task creation functionality through a basic **command-line interface (CLI UI)** implemented in `cli_app.py` as defined in **US004**

Manual tests will be used to validate the CLI UI stub prior to the introduction of a web interface. Results (screenshots or test notes) will be stored in `/tests/screenshots/` and referenced in this plan as needed.



## 📅 Sprint Information

* **Sprint:** 1
* **Iteration Dates:** YYYY-MM-DD → YYYY-MM-DD
* **Version under test:** `main` branch after merging Sprint 4 PRs
* **Prepared by:** [Your Name]
* **Last updated:** YYYY-MM-DD

## 🎯 Test Objectives

| ID     | Objective                                                                      | Success Metric                                                                                               |
|--------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| OBJ-1  | Verify that a new task can be **created** with valid JSON (US002)              | `POST /api/tasks` returns 201 + JSON body containing `id`, `title`, and (optional) `description`.            |
| OBJ-2  | Validate **negative paths** when the `title` field is missing or empty (US002) | Request returns 400 with descriptive error JSON.                                                             |
| OBJ-3  | Confirm that all stored tasks can be **retrieved** (US003)                     | `GET /api/tasks` returns 200 and a JSON array reflecting the current in-memory store (empty list when none). |
| OBJ-4  | Verify basic **task creation via CLI UI stub** (US004)                         | Manually adding a task through `cli_app.py` prompts for input, stores it in memory, and confirms success.    |
| OBJ-5  | Provide automated regression safety-net in CI                                  | All tests pass locally **and** in GitHub Actions on every push/PR.                                           |
                                       |

## 📎 Test Scope by User Story

### US001: Health Check

* `GET /api/health` returns `{ "status": "ok" }` and HTTP 200

### US002: Add Task

* `POST /api/tasks` creates a task with valid input
* `POST /api/tasks` returns error if `title` is missing or empty

### US003: View Tasks

* `GET /api/tasks` returns a list of tasks

### US004: Add Task via CLI (stub)

*  CLI prompts for `title` and `description`
*  Valid input adds task to in-memory list
*  Task creation is confirmed with a printed message
*  Functionality is manually validated through terminal interaction
* 📸 Screenshot required for submission (or captured test log)




| Test Type            | Description                                                                      |
|----------------------|----------------------------------------------------------------------------------|
| Unit Tests           | Test individual route logic and validation. Implemented with `pytest`.           |
| API Tests            | Ensure endpoints return expected responses using Flask's test client.            |
| Error Handling Tests | Simulate invalid inputs to confirm proper 4xx responses.                         |
| CI Tests             | Validate tests run and pass automatically on each push or PR via GitHub Actions. |
| Manual Tests         | Validate CLI UI behavior through interactive input/output and screenshots.       |


## 🛠️ Testing Tools

| Tool              | Purpose                                           |
|-------------------|---------------------------------------------------|
| `pytest`          | Main testing framework                            |
| `pytest-cov`      | Test coverage measurement                         |
| Flask Test Client | Simulates API requests internally                 |
| GitHub Actions    | Executes tests automatically on push/PR to `main` |
| CLI UI (`cli_app.py`) | Manual entry and inspection of task functionality     |
| Postman           | Manual API testing with saved collections         |


## 🛠️ Test Environment Setup

* **OS:** Ubuntu 22.04 runner (CI) & local developer machines
* **Python:** 3.12 (or course-mandated version)
* **Dependencies:** Flask 2.x, pytest 7.x – installed via `requirements.txt`
* **Virtualenv:** `.venv` per developer – ensure isolation
* Flask installed (via `requirements.txt`)
* Test files located in `/tests/`
* Run tests with:

```bash
pytest -v
```

* Coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

## 📈 Test Data & Preconditions

| Scenario         | Sample Input / Request Body                              | Notes                              |
|------------------|----------------------------------------------------------|-------------------------------------|
| Valid API task   | `{ "title": "Buy groceries", "description": "Milk, eggs" }` | `POST /api/tasks` → Expected 201 |
| Missing title    | `{ "description": "Oops" }`                              | Expected 400 (title required)       |
| Empty title      | `{ "title": "", "description": "Empty" }`               | Expected 400                        |
| Valid CLI input  | Title: `Call Mom`, Description: `Sunday afternoon`       | CLI input → task stored in-memory   |

*API tests assume the `tasks` list starts empty via fixture setup.*  
*CLI tests*

## 📊 Test Coverage Goals

* 100% coverage of the following endpoints:
  * `GET /api/health`
  * `POST /api/tasks` (valid + invalid input)
  * `GET /api/tasks`
* Confirm appropriate 4xx error responses are returned for invalid input (e.g., missing or empty title)
* Global error handling will be implemented and tested in Sprint 2 (US015)
* Identify and fix any untested edge cases
* Manually verify CLI functionality for US004 (add task via CLI stub)


## 🔄 CI Integration (GitHub Actions)

* Test suite runs on every push and pull request
* If tests fail, CI blocks merge to `main`
* CI uses `.github/workflows/python-app.yml`

## 📜 Notes for Testers

* Document results in `test_report.md` with:
  - Screenshots of CLI output (e.g., task added confirmation)
  - Screenshots of Postman/curl responses
* Saved Postman collections must be included in `/tests/postman/`
* GitHub PRs should be linked to Issues US000, US001, US002, US003, and **US004**


## 🔐 Entry / Exit Criteria

### Entry

* US002, US003, and US004 issues moved to **In Progress**
* Required route skeletons and CLI stub file (`cli_app.py`) exist (even if `pass`)

### Exit

* All test cases executed – **pass**
* Manual test of CLI UI completed and documented (screenshot/log in `test_report.md`)
* No open critical / high-severity defects
* CI pipeline shows green for latest commit on `main`
* Documentation (API Ref, Test Plan, Test Cases, Test Report) updated & committed


## ⚠️ Risks & Mitigations

| Risk                                           | Impact                                  | Likelihood | Mitigation                                                        |
|------------------------------------------------|------------------------------------------|------------|-------------------------------------------------------------------|
| Shared in-memory list leaks state across tests | False-positive / false-negative results | Medium     | Use fixture to reinitialize `tasks` list before each test         |
| GitHub Actions config drift vs local env       | Build failures in CI                    | Low        | Pin Python version & dependencies; run tests locally before push  |
| Manual testing skipped or incomplete           | US004 (CLI UI) is unverified            | Medium     | Require screenshot or CLI log in test report; checklist enforcement |


### 📏 Test Artifacts

Artifacts students must create and commit include:

* `tests/test_basics.py`: Pytest file with initial arithmetic test
* `tests/test_app_factory.py`: Validates `create_app()` function
* `tests/test_health.py`: Tests `/api/health` endpoint
* `tests/test_add_task.py`: Tests for valid and invalid task creation
* `tests/test_get_tasks.py`: Tests retrieval of all tasks
* `development/api/tasktracker_apis.md`: API documentation
* `docs/test_documentation/s1_test_cases.md`: Includes test cases for US000, US001, US002, US003, and **US004**
* `docs/test_documentation/s1_test_plan.md`: Includes test plan for Sprint 1
* `docs/test_documentation/s1_test_report.md`: Screenshots of API/CLI test results and summary of test runs
* `/tests/postman/`: Contains saved Postman collection (if used)
* `.github/workflows/python-app.yml`: GitHub Actions CI workflow configuration


## ✍️ Approvals

> **Note:** Approvals are not required in this course but mirror real-world QA review processes.

| Role                 | Name | Signature / Date |
| -------------------- | ---- | ---------------- |
| Product Owner        |      |                  |
| QA Lead / Instructor |      |                  |
| Developer            |      |                  |

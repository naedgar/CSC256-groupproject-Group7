# 🎨 Sprint 4 Test Plan: Database, Web UI, and Acceptance Testing

> **Teaching Note:** While *In-Scope Functionality* outlines what is being tested, *Test Objectives* define why each test matters and what constitutes success. Students should reference both to fully understand testing intent and alignment with user stories.

---

## 📝 Purpose

This Sprint 4 test plan focuses on validating the newly introduced **SQLite database integration**, **form-based Web UI**, and new **acceptance testing workflows** for the TaskTracker application.

Unit, integration, and acceptance tests will ensure correctness across the stack:

- `TaskService` logic now depends on a database-backed `DatabaseTaskRepository` (via SQLAlchemy)
- The application no longer uses `tasks.json`; all storage is now handled via SQLite and SQLAlchemy ORM models
- Form-based UI enables task submission and reporting
- Tests are automated using `pytest`, `requests`, `Selenium`, `Playwright`, and `behave`

---

## 📅 Sprint Information

| Field              | Value                             |
|--------------------|-----------------------------------|
| **Sprint**         | 4                                 |
| **Iteration**      | YYYY-MM-DD → YYYY-MM-DD           |
| **Version**        | `main` branch after Sprint 4 merge |
| **Prepared by**    | Your Name                         |
| **Last Updated**   | YYYY-MM-DD                        |

---

## 🌟 Test Objectives

| ID    | Objective                                                       | Success Metric                                                          |
|-------|------------------------------------------------------------------|--------------------------------------------------------------------------|
| OBJ-1 | Add a new task via UI using Flask form                          | Form submits correctly; response is 201; task appears on refresh         |
| OBJ-2 | View report summary from database                               | Report displays accurate task breakdown from SQLite                     |
| OBJ-3 | Use SQLAlchemy to persist all CRUD operations                   | TaskService correctly interacts with SQLite DB                          |
| OBJ-4 | Validate UI workflows using Selenium/Playwright                 | All browser flows pass in headless and interactive runs                 |
| OBJ-5 | Validate task workflows using BDD (Gherkin + behave)            | All feature scenarios pass, simulating user intent                      |

---

## 📊 In-Scope Functionality

| ID     | Area     | Method          | Description                           |
|--------|----------|------------------|---------------------------------------|
| US012  | Web UI   | GET/POST         | Submit task via HTML form             |
| US014  | Web UI   | 
| US026  | Web UI   | GET              | Navigation menu across UI pages       |
| US027  | Web UI   | GET              | Task report summary view              |
| US030  | Web UI   | POST/Validation  | Form-level error handling             |
| RF010–RF012 | Database | All         | Replace JSON with SQLite + SQLAlchemy |
| US032  | BDD      | behave           | Gherkin scenarios for task workflow   |

---

## ✅ Acceptance Criteria Summary

### US012: Add Task via UI

- [x] Displays form with title and description inputs
- [x] Submits to Flask route and creates task
- [x] Redirects or shows message after success
- [x] Fails gracefully with validation error

### US026: Navigation Menu

- [x] Navbar exists across pages
- [x] Links route to: Add Task, Report, Home
- [x] Highlights current route

### US027: Task Report View

- [x] Shows summary of completed/incomplete
- [x] Uses data from database (not static)
- [x] Handles empty task list gracefully

### US030: Form Validation (Web)

- [x] Shows error if title is blank
- [x] Retains form values on failure

### RF010–RF012: DB Repository Refactor

- [x] Replaces all JSON-based operations
- [x] Uses SQLAlchemy ORM models
- [x] Validated with `sqlite:///:memory:` in tests

---

## 🔗 Traceability Matrix

| ID     | Acceptance Criterion                         | Test Case ID(s)                |
|--------|----------------------------------------------|-------------------------------|
| US012  | Valid task form submission                   | TC-US012-001, TC-US012-002    |
| US026  | Navbar navigation works                      | TC-US026-001                  |
| US027  | Report view shows summary                    | TC-US027-001                  |
| US030  | Form validation messages shown               | TC-US030-001                  |
| RF010  | All add/edit/delete ops use SQLite           | TC-RF010-001 → TC-RF010-003   |
| US032  | Task flow works via Gherkin scenarios        | TC-US032-001 (feature file)   |

---

## 🧪 Test Types and Approach

| Test Type         | Purpose / Focus                                                |
|-------------------|----------------------------------------------------------------|
| Unit Tests        | Database logic, template rendering, validation edge cases     |
| Integration Tests | Form POSTs, DB-backed services via Flask test client          |
| UI Acceptance     | Selenium/Playwright simulate real user flows                  |
| BDD Tests         | `behave` validates task lifecycle end-to-end                  |
| Regression Tests  | Confirm legacy endpoints still pass with DB backend           |

---

## 🛠️ Tools Used

| Tool             | Purpose                              |
|------------------|--------------------------------------|
| `pytest`         | Unit/integration tests               |
| `pytest-cov`     | Coverage tracking                    |
| `requests`       | API route testing                    |
| `Selenium`       | UI browser automation (form, nav)    |
| `Playwright`     | Faster UI testing for Web            |
| `behave`         | Gherkin-based BDD flow               |
| `SQLAlchemy`     | ORM for SQLite-backed repository     |
| `GitHub Actions` | CI test runner and badge             |

---

## 📋 Test Data & Scenarios

| Scenario               | Input/Action                   | Expected Result                       |
|------------------------|--------------------------------|----------------------------------------|
| Valid Task Submission  | Fill form and submit           | Task appears in DB and report view     |
| Invalid Title Input    | Submit with blank title        | Error shown, task not saved            |
| View Task Report       | Visit `/tasks/report`          | Counts reflect DB state                |
| Navigation Flow        | Click between UI links         | Pages load with no error               |
| TaskService DB CRUD    | Create, update, delete tasks   | Reflected in persistent DB             |

---

## 🔍 Sample Test Cases

```python
# ✅ Unit: Add to DB
def test_add_task_creates_record(db_session):
    repo = DatabaseTaskRepository(session=db_session)
    task = repo.add_task("UI Test", "Test via form")
    assert task.id is not None

# ✅ Integration: POST Task
def test_add_task_route(client):
    res = client.post("/tasks/new", data={"title": "Form Task", "description": "UI"})
    assert res.status_code == 200 or 302  # Redirect OK
    assert b"Task Created" in res.data or res.request.path == "/tasks"

# ✅ UI: Selenium Test
def test_ui_add_task_selenium(browser):
    browser.get("http://localhost:5000/tasks/new")
    browser.find_element(By.NAME, "title").send_keys("Browser Task")
    browser.find_element(By.NAME, "description").send_keys("Via Selenium")
    browser.find_element(By.ID, "submit").click()
    
    # Assert success message or redirect
    assert "Task Created" in browser.page_source or browser.current_url.endswith("/tasks")


## 📊 Test Data & Preconditions

| Scenario              | Input / Action             | Expected Result                     |
| --------------------- | -------------------------- | ----------------------------------- |
| Valid task submission | Fill and submit UI form    | Task added and stored in DB         |
| Filter incomplete     | Select filter = incomplete | Only uncompleted tasks shown        |
| Invalid task form     | Submit form without title  | Error message displayed             |
| Report view           | Visit report route         | Shows count of completed/incomplete |
| Database integration  | Use DB repo in app         | All task features persist in DB     |

## 📊 Test Coverage Goals

* 100% of UI user stories tested via automated browser tests
* 100% of form and navigation paths validated
* All repository methods for SQLAlchemy tested
* Backend endpoints covered via integration testing

## 🔄 CI Integration

* All new tests must pass in GitHub Actions
* Use sqlite:///:memory: for isolated DB tests in CI
* Selenium/Playwright can be headless for speed
* Add BDD runner (e.g., behave features/) to CI workflow

## 🔐 Entry / Exit Criteria

### Entry

* CLI deprecated
* DB repo and models complete
* Flask routes accept UI form input
* Initial Playwright/Selenium tests scaffolded

### Exit

* SQLite used for all storage (JSON removed)
* UI forms functional and validated
* All new tests and coverage included
* features/ Gherkin tests pass
* CI badge remains green post-merge

## ⚠️ Risks & Mitigations

| Risk                          | Impact             | Likelihood | Mitigation                                        |
| ----------------------------- | ------------------ | ---------- | ------------------------------------------------- |
| DB migration bugs             | Data loss/errors   | Medium     | Validate all repo methods and back up data        |
| UI test flakiness             | Test failure       | Medium     | Use explicit waits and stable selectors           |
| Playwright/Selenium confusion | Slower progress    | High       | Provide code-along tutorials and working examples |
| UI not aligned with backend   | Form or route bugs | Medium     | Validate integration and form submission paths    |


| File / Directory                            | Contents                                |
| ------------------------------------------- | --------------------------------------- |
| `tests/repositories/`                       | Unit tests for `DatabaseTaskRepository` |
| `tests/ui/test_ui_add_task.py`              | UI form test with browser automation    |
| `tests/ui/test_ui_nav.py`                   | Navbar routing tests                    |
| `features/task_workflow.feature`            | BDD Gherkin scenarios                   |
| `docs/test_documentation/s4_test_plan.md`   | This file                               |
| `docs/test_documentation/s4_test_cases.md`  | Detailed test cases                     |
| `docs/test_documentation/s4_test_report.md` | Screenshots and summaries               |


📣 Teaching Note
* Selenium is used for detailed interaction flows (form entry, redirect, error capture)
* Playwright offers faster feedback and headless execution for CI
* BDD (behave) helps think in terms of user behavior, not just code logic

## ✍️ Approvals

> **Note:** Approvals are not required in this course but mirror real-world QA review processes.

| Role                 | Name | Signature / Date |
| -------------------- | ---- | ---------------- |
| Product Owner        |      |                  |
| QA Lead / Instructor |      |                  |
| Developer            |      |                  |

# ✅ Sprint 4 Epic: Database, Web UI, and Acceptance Testing

This Sprint introduces the SQLite database (via SQLAlchemy), replaces the file-based task repository, and transitions from the CLI to a web interface. It also integrates UI testing using Selenium and Playwright and adds BDD tests for task workflows.

This document provides guidance on creating GitHub issues for Sprint 4 tasks. Issues should be modular, test-driven, and assigned to appropriate branches. Be sure to group tasks by user story or refactor, and follow the GitHub Flow (feature branches + pull requests).

---

## 🗂️ Epic Issue: Sprint 4 Acceptance Criteria

📌 **Title:** Sprint 4 – DB, Web UI, Acceptance Testing

**Description:**  
Sprint 4 completes the transition to persistent database storage and introduces a basic web UI for core task operations. It includes database integration using SQLAlchemy with SQLite, UI built using Flask templates, and acceptance testing using BDD and browser automation tools.

---

### ✅ Sprint-Level Completion Criteria

- [ ] `DatabaseTaskRepository` is implemented using SQLAlchemy
- [ ] JSON file storage is fully deprecated
- [ ] App factory injects `DatabaseTaskRepository`
- [ ] Web UI exists for task creation and report viewing
- [ ] Form submissions are validated and errors are shown
- [ ] CLI is no longer used
- [ ] BDD tests validate core workflows
- [ ] Selenium/Playwright tests are passing in CI
- [ ] Code coverage ≥ 80%

---

### 🟩 Sprint-Level Definition of Done

- [ ] SQLite DB is used for all persistent storage
- [ ] TaskService supports injected DB repository
- [ ] Flask templates exist for core views (add, report)
- [ ] Acceptance tests (Selenium or Playwright) are passing
- [ ] GitHub Actions includes all test types
- [ ] All legacy tests continue to pass
- [ ] Docs are updated for DB, UI, and new test types

---

## 📂 Sprint 4 Tracked User Stories

| Story ID | Title                          | Route Type | Description                          |
|----------|--------------------------------|------------|--------------------------------------|
| US012    | Add Task via Web Form          | Web UI     | Allows users to submit tasks via HTML form |
| US014    | Add UI for Task Creation       | Web UI     | Displays a form-based UI page for task input |
| US018    | View Task Report (Web)         | Web UI     | Displays tasks grouped by status     |
| US026    | Task Menu UI                   | Web UI     | Basic nav bar/menu across pages      |
| US032    | BDD Web UI Test                | UI Tests   | Run `behave` with `task_workflow.feature` |
| US033    | Manual Task Workflow           | UI Manual  | Manual UI test walkthrough (HTML forms) |
| US034    | CI Automation Coverage         | DevOps     | All tests run in GitHub CI pipeline |
| US036    | Web Form Validation            | Web UI     | Displays validation errors and prevents form submission |

---

## 🔧 Sprint-Level Technical Tasks

| Task ID | Description                                       |
|---------|---------------------------------------------------|
| RF010   | Implement `DatabaseTaskRepository` with SQLAlchemy |
| RF011   | Refactor `TaskService` for DB injection            |
| RF012   | Replace CLI with HTML-based Web UI                |
| RF013   | Refactor UI routing to support form submissions   |
| RF014   | Add acceptance test strategy (UI, BDD)            |

---

## 📋 Sub-Issue Tracker

These GitHub issues should be created under the Sprint 4 Epic.

### 📌 User Stories

- [ ] #US012 – Add Task via Web Form
- [ ] #US014 – Add UI for Task Creation
- [ ] #US018 – View Task Report (Web)
- [ ] #US026 – Task Menu UI
- [ ] #US032 – BDD Web UI Test
- [ ] #US033 – Manual Task Workflow
- [ ] #US034 – CI Automation Coverage
- [ ] #US036 - Web Form Validation

### 🛠️ Refactors / Architecture Tasks

- [ ] #RF010 – Implement `DatabaseTaskRepository`
- [ ] #RF011 – Refactor `TaskService` for DB injection
- [ ] #RF012 – Replace CLI with Web UI
- [ ] #RF013 – Refactor UI routing for form GET/POST
- [ ] #RF014 – Add acceptance test strategy (UI, BDD)

---

## 🧪 Test Strategy References

📁 Associated test directories:

- `tests/repositories/` – Unit tests for database logic  
- `tests/ui/` – Selenium, Playwright tests  
- `tests/api/` – Requests-based tests (continued from Sprint 3)  
- `features/` – BDD Gherkin scenarios

🔍 View in test plan: `s4_test_plan.md`

---

📌 **Note:** This Sprint retires the CLI. All future enhancements use the Web UI. Test strategy now includes database testing, UI workflows, and BDD user journeys.


## 🔧 Detailed Sub-Issues – Sprint 4 (Web UI & DB Integration)

---

### 🎯 US012 – Add UI for Task Creation

**Description:**  
As a user, I want to use a form to create tasks via the UI, so I don’t have to rely on API tools or CLI input.

#### ✅ Acceptance Criteria

- [ ] UI displays a form with task title and description fields
- [ ] Submitting the form creates a new task (via POST or form handler)
- [ ] Task is saved to the database and shown on refresh
- [ ] Error is shown if title is blank or invalid
- [ ] Tested via Selenium or Playwright automation

#### 📌 Sub-Tasks

- [ ] Create `templates/create_task.html` with Jinja2 form
- [ ] Add route handler for GET and POST `/tasks/new` in `routes/ui.py`
- [ ] Validate user input in route (empty title, too long, etc.)
- [ ] Display success or error message on the same page
- [ ] Write automated UI test simulating task submission

---

### 🎯 US026 – Task Menu UI

**Description:**  
As a user, I want a consistent navigation menu across all pages so I can easily move between task actions and reports.

#### ✅ Acceptance Criteria

- [ ] Menu appears at the top of every page (using base layout)
- [ ] Menu includes links: Home, Add Task, Task Report
- [ ] Active page is visually highlighted
- [ ] Menu is responsive and styled consistently

#### 📌 Sub-Tasks

- [ ] Add nav bar HTML to base Jinja2 template
- [ ] Extract nav bar into a reusable `_menu.html` partial
- [ ] Ensure all relevant routes use the base layout
- [ ] Test each page manually and verify navigation flow

---

### 🎯 US027 – View Task Report

**Description:**  
As a user, I want to see a report summarizing my task progress—how many tasks I’ve completed vs. those still pending.

#### ✅ Acceptance Criteria

- [ ] Task report view shows total task count
- [ ] Displays counts of completed vs. incomplete tasks
- [ ] Includes percentage or visual bar for completion
- [ ] Dynamically updates based on database content
- [ ] Styled for readability and accessibility

#### 📌 Sub-Tasks

- [ ] Add `/tasks/report` route and view logic in `routes/ui.py`
- [ ] Create `templates/report.html` with Jinja2 layout
- [ ] Query TaskService for all tasks and group by status
- [ ] Display visual breakdown (bar chart or summary box)
- [ ] Add test for task report route (status 200, content check)

### 🎯 US036 – Web Form Validation

**Description:**  
As a user, I want real-time validation and feedback when submitting forms with errors, so that I can understand and correct mistakes before resubmitting

✅ **Acceptance Criteria**
- [ ] Validation errors shown when form input is missing/invalid
- [ ] The form is not submitted if required fields are missing
- [ ] Input values are preserved when validation fails
- [ ] Consistent styling for error messages
- [ ] Tested via UI test (Selenium or Playwright)

📌 **Sub-Tasks**
- [ ] Add validation logic in `/routes/ui.py` for title and description
- [ ] Update `create_task.html` to display field-specific error messages
- [ ] Ensure form fields retain user input on validation failure
- [ ] Write UI test to simulate empty/invalid submission and verify feedback

---

### 🔧 Detailed Sub-Issues – Sprint 4 Refactors

---

### 🎯 RF010 – Refactor: Convert Service Layer to Use Database (SQLite)

* **Description:**
  Update `TaskService` methods to interact with the **SQLAlchemy ORM backed by SQLite** instead of JSON. This includes replacing manual list manipulations with ORM-based `add`, `query`, and `delete` operations.

* ✅ **Acceptance Criteria**

  * [ ] `add_task`, `edit_task`, `delete_task`, `get_all_tasks` use SQLAlchemy with SQLite
  * [ ] Query methods use ORM queries
  * [ ] Services raise appropriate exceptions on failure
  * [ ] Tests use in-memory SQLite database for isolation

* 📌 **Sub-Issues**

  * [ ] Update all `TaskService` methods to use repository pattern with DB
  * [ ] Add test cases for database behavior
  * [ ] Confirm SQLite database (`tasks.db`) is created in local dev
  * [ ] Document changes in `services/task_service.py`

---

### 🎯 RF011 – Refactor: Remove JSON Storage and Use DB Repository

* **Description:**
  Replace the JSON file-based persistence logic with a database-backed repository using **SQLAlchemy and SQLite**.

* ✅ **Acceptance Criteria**

  * [ ] `utils/storage.py` logic is deprecated and removed
  * [ ] All repository operations use SQLAlchemy with SQLite
  * [ ] File-based persistence is removed from `task_service.py`
  * [ ] Regression tests confirm parity with JSON logic

* 📌 **Sub-Issues**

  * [ ] Delete or archive file-based JSON helpers
  * [ ] Implement DB-based logic in `DatabaseTaskRepository`
  * [ ] Ensure SQLite file `tasks.db` is created and populated
  * [ ] Confirm all behavior is covered by database tests

---

### 🎯 RF012 – Refactor: Add SQL-Based Test Fixtures (SQLite In-Memory)

* **Description:**
  Replace mocks and stubs with realistic test fixtures using **SQLite in-memory** databases for fast and isolated testing.

* ✅ **Acceptance Criteria**

  * [ ] `conftest.py` includes an in-memory SQLite session fixture
  * [ ] All tests simulate real DB interactions using `sqlite:///:memory:`
  * [ ] Setup and teardown preserve isolation
  * [ ] Code coverage remains above 80%

* 📌 **Sub-Issues**

  * [ ] Create `conftest.py` with SQLAlchemy + SQLite fixture
  * [ ] Update unit/integration tests to use new DB-based fixtures
  * [ ] Verify GitHub Actions can run SQLite tests cleanly

---

### 🎯 RF013 – Refactor: Document Final ERD and Class Diagram

* **Description:**
  Finalize and publish both the **Entity Relationship Diagram** (reflecting SQLite schema) and updated class diagram for project architecture.

* ✅ **Acceptance Criteria**

  * [ ] ERD reflects SQLite schema: `Task` table with appropriate fields
  * [ ] Class diagram shows new model/service/repo relationships
  * [ ] Diagrams published as `.md`, `.png`, or `.svg` in `/docs`
  * [ ] Diagrams linked from `README.md`

* 📌 **Sub-Issues**

  * [ ] Finalize `docs/s4_erd.md` and `docs/s4_class_diagram.md`
  * [ ] Add diagram images or Mermaid diagrams as needed
  * [ ] Ensure diagrams match live SQLite schema

---

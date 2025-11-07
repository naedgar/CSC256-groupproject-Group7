# 📊 Sprint 4 Test Cases

🔬 This document includes detailed test cases for Sprint 4 features, refactors, and architecture. All test cases follow the traceability from user stories, refactors, and technical tasks.

---

## ✅ Test Areas

* SQLAlchemy-based `DatabaseTaskRepository`
* Flask UI rendering and form processing
* Acceptance tests using Selenium and Playwright
* Automated API regression tests using requests
* Regression validation for all core task operations

---

## Summary Refactors for Sprint 4

| Refactor ID | Description                                              | Notes                                              |
| ----------- | -------------------------------------------------------- | -------------------------------------------------- |
| RF010       | Convert `TaskService` to use SQLAlchemy DB session       | DB-backed repository logic for all task operations |
| RF011       | Refactor `TaskService` to support DB injection           | Uses constructor injection with DB repository      |
| RF012       | Replace CLI with Web UI                                  | UI renders HTML via Flask templates                |
| RF013       | Refactor UI routing to support GET/POST form submissions | Adds GET/POST views in `routes/ui.py`              |
| RF014       | Extend test strategy to UI layers                        | Selenium and Playwright added    

---
## ✅ Database-Related Refactors

### 🧱 RF010 – Convert TaskService to Use SQLAlchemy

| Test Case ID | Description                                | Test Type | Notes                                   |
| ------------ | ------------------------------------------ | --------- | --------------------------------------- |
| TC-RF010-001 | TaskService uses DB repo for `add_task()`  | Automated | Uses `DatabaseTaskRepository` injection |
| TC-RF010-002 | TaskService uses ORM for `get_all_tasks()` | Automated | No file reads; ORM query validated      |
| TC-RF010-003 | Exceptions raised for invalid operations   | Automated | Covers error cases like missing task ID |

### 🧱 RF011 – Follows RF010 by injecting `DatabaseTaskRepository` into `TaskService`.

| ------------ | ----------------------------------------------------- | ------------- | --------------------------------------------------- |
| TC-RF011-001 | `TaskService` accepts repository as constructor param | Manual/Static | Verified in `__init__.py` and `services/` injection |
| TC-RF011-002 | Flask uses DB-injected `TaskService`                  | Manual/Static | Confirmed in `__init__.py` application factory      |
| TC-RF011-003 | DatabaseTaskRepository Used by API Routes             | Integration (API with DB) |   |

### 🧪 TC-RF010-001: Add Task via Database Repository

* **Title:** Create Task in DB
* **Description:** Verify that a task can be added to the database using the `DatabaseTaskRepository`.
* **Test Type:** Unit
* **Precondition:** DB is initialized, no tasks present
**Steps:**
1. Create a `DatabaseTaskRepository` instance
2. Call `add_task("Test", "Created via DB")`
**Expected Result:**
* Task is persisted and has a non-null ID

---

### 🧪 TC-RF010-002: Retrieve All Tasks

* **Title:** Read All Tasks from DB
* **Description:** Ensure the `get_all_tasks()` method returns a list of all tasks from the database
* **Test Type:** Unit
**Steps:**

1. Add multiple tasks via repository
2. Call `get_all_tasks()`
**Expected Result:**
  * List includes all inserted tasks with correct attributes

---

### 🧪 TC-RF010-003: Update Task Completion

* **Title:** Mark Task Complete in DB
* **Description:** Verify that a task's `completed` field is correctly updated to True
* **Test Type:** Unit
**Steps:**
1. Add a task
2. Call `mark_task_complete(id)`
**Expected Result:**
* DB reflects `completed: True`

---

### 🧪 TC-RF010-004: Delete Task from Database

* **Title:** Remove Task from DB
* **Description:** Verify that a task can be deleted and is no longer present
* **Test Type:** Unit
**Steps:**
1. Add a task
2. Call `delete_task(id)`
**Expected Result:**
* Task is removed and `get_all_tasks()` confirms deletion

### 🧪 TC-RF011-001: Inject Database Repository into TaskService

* **Title:** DB Injection via Constructor
* **Description:** Ensure `TaskService` receives a `DatabaseTaskRepository` instance via constructor injection.
* **Test Type:** Static + Manual
**Expected Result:**
- `TaskService.__init__` accepts a repository parameter
- App factory injects `DatabaseTaskRepository` into service
- No hardcoded repository or storage logic in service

### 🧪 TC-RF011-002: Replace JSON Logic with DB Queries

* **Title:** All Logic Delegates to DB Repository
* **Description:** Confirm all service logic uses injected DB repository and JSON logic is removed.
* **Test Type:** Static + Regression
**Expected Result:**
- All service methods (`add_task`, `get_tasks`, etc.) delegate to repository
- `task_storage.py` file no longer used in app logic
- Tests confirm behavior unchanged compared to previous storage

### 🧪 TC-RF011-003: DatabaseTaskRepository Used by API Routes

* **Title:** API endpoints interact with DB backend
* **Description:** API tests using Flask test client should show tasks being persisted via `DatabaseTaskRepository`.
* **Test Type:** Integration (API with DB)
* **Expected Result:**
  - `POST /api/tasks` adds record to SQLite
  - `GET /api/tasks` fetches tasks from DB

---

## ✅ Refactor/Architecture Test Cases

### 🧱 RF012 – Replace CLI with Web UI

| Test Case ID | Description                     | Test Type | Notes                                            |
| ------------ | ------------------------------- | --------- | ------------------------------------------------ |
| TC-RF012-001 | CLI code removed or deprecated  | Manual    | `cli_app.py` no longer in production flow        |
| TC-RF012-002 | UI rendered via Flask templates | Automated | Validated with GET `/tasks/new` and UI form load |

### 🧪 TC-RF012-001: Render Task Creation Form

* **Title:** UI displays task creation form page
* **Description:** Verify that a GET request to /tasks/new renders the HTML form
* **Test Type:** UI
**Steps:**
- Navigate to `/tasks/new` displays HTML form
- Check for presence of form fields
**Expected Result:**
- Page loads successfully
- Form fields include task title and optional description

### 🧪 TC-RF012-002: Submit Empty Task Form

* **Title:** Form rejects empty title on submission
* **Description:** Attempting to submit the task form without a title should result in a validation error
* **Test Type:** UI Manual / Automated
**Steps**
  * Navigate to /tasks/new
  * Submit form with blank title
**Expected Result:**
  * Error message is shown
  * Form input is retained

### TC-US012-003: Successful Task Creation via Form

* **Title:** Task is created when form is filled and submitted
* **Description:** Ensure task is persisted and redirect occurs after submission
* **Test Type:** UI + Integration
**Expected Result:**

Task appears in task list or redirect occurs
---
### 🧱 RF013 – Form Routing and POST Submission

| Test Case ID | Description                             | Test Type | Notes                               |
| ------------ | --------------------------------------- | --------- | ----------------------------------- |
| TC-RF013-001 | UI form rendered at `/tasks/new` (GET)  | Automated | Returns HTML with form              |
| TC-RF013-002 | Task created via form submission (POST) | Automated | Redirect or success message appears |

### 🧪 TC-RF013-001: UI GET and POST Views Implemented

* **Title:** Form Route Supports GET and POST
* **Description:** Confirm Flask view handles both displaying form and processing submission.
* **Test Type:** Static + Integration

**Expected Result:**
- `routes/ui.py` has a `@app.route('/tasks/new', methods=['GET', 'POST'])`
- GET renders form
- POST processes data and returns success

---
## 🧱 RF014 – UI Acceptance Testing Strategy

| Test Case ID | Description                                       | Test Type              | Notes                                             |
| ------------ | ------------------------------------------------- | ---------------------- | ------------------------------------------------- |
| TC-RF014-001 | Selenium test adds task via form                  | Automated (Selenium)   | Simulates form input, submit, validates result    |
| TC-RF014-002 | Playwright test confirms navigation and form flow | Automated (Playwright) | Lightweight test for links, buttons, form actions |

### 🧪 TC-RF014-001: Selenium Test for Form Submission

* **Title:** UI Form Validated via Selenium
* **Description:** Simulate browser task creation flow using Selenium.
* **Test Type:** UI Automated

**Expected Result:**
- Open `/tasks/new`
- Fill and submit form
- Check page shows task or confirmation
- Verify task stored in DB


---

### 🧪 TC-RF014-002: Playwright Headless Test for UI

* **Title:** UI Acceptance Test via Playwright
* **Description:** Perform the same browser test using Playwright for CI.
* **Test Type:** UI Automated

**Expected Result:**
- Script runs in headless mode
- Task is created and visible on task list page
- Run succeeds in CI pipeline

---

## UI Feature Test Cases

| Test Case ID | Description                               | Test Type                              | Notes                |
|--------------|-------------------------------------------|----------------------------------------|----------------------|
| TC-US012-001 | Render Task Creation Form                 | UI Manual / Automated (Selenium)       |                      |
| TC-US012-002 | Submit Empty Task Form                    | UI Manual / Automated                  |                      |
| TC-US012-003 | Successful Task Creation via Form         | UI + Integration                       |                      |
| TC-US036-001 | Form Field Required Validation|Automated  | UI Automated (Selenium or Playwright)  |                      |

### 🧪 TC-US012-001: Render Task Creation Form

* **Title:** UI displays task creation form page
* **Description:** Verify that a GET request to `/tasks/new` renders the HTML form
* **Test Type:** UI Manual / Automated (Selenium)

**Steps:**

1. Navigate to `/tasks/new`
2. Check for presence of form fields


**Expected Result:**

* Page loads successfully
* Form fields include task title and optional description

---

### 🧪 TC-US012-002: Submit Empty Task Form

* **Title:** Form rejects empty title on submission
* **Description:** Attempting to submit the task form without a title should result in a validation error
* **Test Type:** UI Manual / Automated

**Steps:**

1. Navigate to `/tasks/new`
2. Submit form with blank title

**Expected Result:**

* Error message is shown
* Form input is retained

### 🧪 TC-US012-003: Successful Task Creation via Form

* **Title:** Task is created when form is filled and submitted
* **Description:** Ensure task is persisted and redirect occurs after submission
* **Test Type:** UI + Integration

**Expected Result:**

* Task appears in task list or redirect occurs


### 🧪 TC-US036-001: Form Field Required Validation

* **Title:** Prevent submission without required fields
* **Description:** Verify that HTML5 required validation prevents form submission
* **Test Type:** UI Automated (Selenium or Playwright)

**Steps:**

1. Navigate to `/tasks/new`
2. Attempt to submit without entering a title

**Expected Result:**

* Browser prevents submission
* Error shown via UI

---

## Navigation Test Cases

| Test Case ID | Description                               | Test Type         | Notes                |
|--------------|-------------------------------------------|-------------------|----------------------|
| TC-US026-001 | Render Navigation Menu                    | Manual / Static   |                      |


### 🧪 TC-US026-001: Render Navigation Menu

* **Title:** Base template includes navigation menu
* **Description:** Every page should render menu from layout
* **Test Type:** Manual / Static

**Expected Result:**

* Menu includes Home, Add Task, Report
* Active link is highlighted

---

## ✅ Task Report Page Test Cases

| Test Case ID | Description                               | Test Type         | Notes                |
|--------------|-------------------------------------------|-------------------|----------------------|
| TC-US027-001 | Task Report Page Test Cases               | UI / Integration  |                      |

### 🧪 TC-US027-001: Report Page Displays Task Summary

* **Title:** View task statistics
* **Description:** Report should summarize completed and pending tasks
* **Test Type:** UI / Integration

**Expected Result:**

* Report shows task totals
* Visual indicators for completed vs incomplete

---

## BDD Test Case

| Test Case ID | Description                               | Test Type         | Notes                |
|--------------|-------------------------------------------|-------------------|----------------------|
| TC-US032-001 |BDD Task Workflow (Gherkin)                | BDD (behave)      |                      |

---

### 🧪 TC-US026-001: UI Navigation Menu

* **Title:** Navigation Links Work
* **Description:** Verify that nav links route correctly and highlight active route
* **Test Type:** Automated (Selenium / Playwright)

**Steps:**

1. Click on each nav link
2. Observe page content

**Expected Result:**

* Page changes accordingly
* Active link is highlighted

---

## 📦 Database Functionality

### 🧪 TC-DB-US002-001: Add Task via Database Repository

* **Description:** Verify that a task can be added to the SQLAlchemy database.
* **Precondition:** DB is initialized, no task present.
* **Test Type:** Unit
* **Expected Result:** Task is assigned an ID and persisted in the database.

### 🧪 TC-DB-US003-001: : Retrieve All Tasks from Database

* **Description:** Verify all tasks can be retrieved using `get_all_tasks()`.
* **Test Type:** Unit
* **Expected Result:** Returns a list containing all tasks stored in the DB.

### 🧪 TC-DB-US005-003: Update Task Completion

* **Description:** Ensure tasks can be marked complete using DB repository.
* **Test Type:** Unit
* **Expected Result:** Task's `completed` field is set to `True` in DB.

### 🧪 TC-DB-US007-004: Delete Task from Database

* **Description:** Verify a task can be deleted and is no longer returned.
* **Test Type:** Unit
* **Expected Result:** Task is removed from the database.

## 🔄 Regression Test Cases (DB-backed API)

### 🧪 TC-REG-001: Add Task via API

* **Title:** POST /api/tasks with DB
* **Description:** Ensure API call to create task persists to database
* **Test Type:** Integration

**Steps:**

1. POST to `/api/tasks` with valid data

**Expected Result:**

* Status 201, task saved in DB

---

### 🧪 TC-REG-002: View Tasks via API

* **Title:** GET /api/tasks from DB
* **Description:** Ensure API returns DB-backed tasks
* **Test Type:** Integration

**Steps:**

1. GET `/api/tasks`

**Expected Result:**

* JSON matches current DB contents

---

### 🧪 TC-REG-003: Complete Task via API

* **Title:** PUT /api/tasks/<id>
* **Description:** Ensure API marks task as complete
* **Test Type:** Integration

**Steps:**

1. PUT `/api/tasks/1`

**Expected Result:**

* 200 OK, `completed` now True

---

### 🧪 TC-REG-004: Delete Task via API

* **Title:** DELETE /api/tasks/<id>
* **Description:** Ensure task is removed from DB
* **Test Type:** Integration

**Steps:**

1. DELETE `/api/tasks/1`

**Expected Result:**

* Status 204 No Content
* Task removed from DB

---

## ✅ Test Case – BDD Acceptance Workflow

### 🧪 TC-US032-001: Create Task via BDD Workflow

**Title:** BDD – User Creates Task via Web UI
**Test Type:** Automated (BDD with Selenium)
**Related User Story:** US032 – Acceptance Test via behave
**File:** `features/task_workflow.feature`, `test_ui_steps.py`
**Test Tool:** `behave` with `selenium`

#### Precondition:

* Flask server running locally on `http://localhost:5000`
* ChromeDriver installed and in PATH

#### Steps:

1. Navigate to `/tasks/new` using Selenium via `behave`
2. Fill in `"BDD Task"` as title and `"Via behave"` as description
3. Submit the form
4. Navigate to `/tasks`
5. Check that `"BDD Task"` appears on the page

#### Expected Result:

* Task appears in the task list page
* No validation errors
* Scenario passes with green success
---

## 📄 File Structure for Tests

| Directory             | Purpose                              |
| --------------------- | ------------------------------------ |
| `tests/repositories/` | Unit tests for DB repository methods |
| `tests/ui/`           | Browser-based UI tests               |
| `tests/api/`          | Requests-based API tests             |
| `features/`           | BDD scenarios                        |

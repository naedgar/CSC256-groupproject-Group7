# ✅ Sprint 3 Test Cases – Detailed Format

## 🧪 Test Type Legend

| Type             | Meaning                                                                 |
|------------------|-------------------------------------------------------------------------|
| **Static**        | Read-only inspection of codebase (no execution)                        |
| **Manual**        | Performed by a user via browser, CLI, Postman, etc.                    |
| **Automated**     | Run via test code (e.g., pytest) and asserts actual behavior           |
| **Static + Manual**| Code inspection followed by a manual runtime check                    |


## Regression Log

### ✅ User Story Test Cases

* 📌 US002 – Add Task

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US002-001     | Add valid task                       | Automated        | Basic happy path                       |
| TC-US002-002     | Missing title                        | Automated        | Should return 400                      |
| TC-US002-003     | Empty title                          | Automated        | Should return 400                      |
| TC-US002-004     | Missing description                  | Automated        | Optional field                         |

---

* 📌 US003 – View Tasks

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US003-001     | View tasks when none exist           | Automated        | Should return empty list (`[]`)       |
| TC-US003-002     | View tasks when tasks exist          | Automated        | Should return list of task objects     |

---

* 📌 US005 – Mark Task Complete

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US005-001     | Mark task complete (valid ID)        | Automated        | Expects 200 and `"completed": true`    |
| TC-US005-002     | Mark task complete (nonexistent ID)  | Automated        | Expects 404 Not Found                  |

---

* 📌 US007 – Delete Task

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US007-001     | Delete task (valid ID)               | Automated        | Should return 200                      |
| TC-US007-002     | Delete task (nonexistent ID)         | Automated        | Should return 404                      |

---

* 📌 US011 – Persist Tasks (File Storage)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US011-001     | Tasks persist after restart          | Automated        | Check `tasks.json` after POST          |
| TC-US011-002     | Load tasks from file on startup      | Automated        | File used as source of truth           |

---

* 📌 US006 – UI for Add Task (CLI Stub)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US006-001     | CLI prompt accepts task input        | Manual           | Uses `input()` in CLI stub             |
| TC-US006-002     | CLI task passed to service           | Manual           | Requires verifying console output      |

---

* 📌 US027 – View Task Report (via CLI)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US027-001     | CLI lists tasks                      | Manual           | Read-only task display                 |

---

* 📌 US028 – CLI Complete Task

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US028-001     | CLI marks task as complete           | Manual           | Verifies behavior of `TaskService`     |

---

## ✅ Error Handling & Validation (US015)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-US015-001     | Invalid JSON format                  | Automated        | Expects 400 Bad Request                |
| TC-US015-002     | Missing JSON content-type header     | Automated        | Expects 415 Unsupported Media Type     |
| TC-US015-003     | PUT/DELETE with invalid ID           | Automated        | Expects 404 Not Found                  |

---

## ✅ Architecture & Refactor Test Cases

### 🧱 Blueprint Routing (RF001)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-ARCH-001      | Routes use Blueprints                | Manual/Static    | `main.py` registers blueprints only    |
| TC-ARCH-002      | No route defined in `main.py`        | Manual/Static    | All routes moved to `routes/`          |
| TC-NFR001-001 | Confirm all routes are available via Blueprint | Automated | GET, POST, PUT, DELETE all succeed via `/api/tasks` endpoints |

---

### 🧱 File Storage Refactor (RF002)

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-ARCH-003      | `task_storage.py` reads from file    | Automated        | Check that it returns task list        |
| TC-ARCH-004      | `task_storage.py` writes to file     | Automated        | Should save tasks after add/delete     |

---

### 🧱 App Factory Pattern

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-ARCH-005      | App initializes via `create_app()`   | Automated        | Used in tests via `conftest.py`        |
| TC-ARCH-006      | Blueprint registration verified      | Automated        | Tests confirm endpoints are mounted    |
| TC-NFR001-002 | Test `create_app()` correctly registers Blueprints | Automated | No 404 errors from misrouting; routes mounted without exception |

---

## ✅ Manual Tests via Postman or CLI

| Test Case ID     | Description                          | Test Type        | Notes                                  |
|------------------|--------------------------------------|------------------|----------------------------------------|
| TC-MANUAL-001    | Add task via Postman/curl            | Manual           | Screenshot required                    |
| TC-MANUAL-002    | View tasks via Postman/curl          | Manual           | Screenshot required                    |
| TC-MANUAL-003    | Mark task complete via Postman       | Manual           | Verifies PUT endpoint                  |
| TC-MANUAL-004    | Delete task via Postman              | Manual           | Verifies DELETE endpoint               |

---

## Summary Refactors for Sprint 3

| Refactor ID | Description                                                  | Notes                                                           |
| ----------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| RF004       | Introduce `Task` class                                       | Replace dictionary-based task model                             |
| RF005       | Create `TaskService` class                                   | Encapsulates all logic for add/view/edit/delete                 |
| RF006A      | Create `TaskStorage` wrapper for DI                          | Enables `load_tasks`/`save_tasks` injection into services       |
| RF006B      | Inject `TaskService` via `__init__.py`                       | Passes service instance into Flask app context for route access |
| RF006C      | Refactor `routes/tasks.py` to use `current_app.task_service` | Updates route handlers for DI-based architecture                |
| RF007       | Blueprint Modularization                                     | Separate task and health routes into Blueprints                 |
| RF008       | Introduce `MockTaskService` for test isolation               | Replaces file storage in tests for fast, isolated test behavior |


## 🧱 Introduce `Task` Class for Domain Modeling (RF004)

This refactor lays the foundation for object-oriented architecture by creating a `Task` class to represent tasks as structured objects rather than plain dictionaries. This enables better encapsulation, easier refactoring, and compatibility with future database or validation layers.

### Test Cases for RF004

| Test Case ID | Description                                  | Test Type | Notes                                                   |
| ------------ | -------------------------------------------- | --------- | ------------------------------------------------------- |
| TC-RF004-001 | Task object can be instantiated              | Automated | `Task(title, description)` creates object               |
| TC-RF004-002 | Task object tracks completed status          | Automated | Default is `False`; `mark_complete()` updates to `True` |
| TC-RF004-003 | Task object has correct ID, title, desc      | Automated | Validate attributes after construction                  |
| TC-RF004-004 | Object comparison works with service methods | Automated | Used by `TaskService` to store and return objects       |

---

> ✅ Note: The `Task` class is defined in `app/models/task.py` in **Sprint 3 Lab 2**, and tested using pure unit tests. It is injected into the service layer (`TaskService`) in later steps.

### TC-RF004-001: TaskService Adds Task

* **Description:** Verify `add_task()` correctly stores a new task in memory
* **Preconditions:** TaskService is initialized with empty task list
* **Steps:**
  1. Call `add_task("Title", "Description")`
* **Expected:** Returns a `Task` with correct title, description, and ID=1
* **Test Type:** Automated

### TC-RF004-002: TaskService Marks Task Complete

* **Description:** Verify `complete_task()` sets a task’s `completed` field to `True`
* **Preconditions:** Task exists in TaskService with `completed = False`
* **Steps:**
  1. Call `complete_task(task_id)`
* **Expected:** `completed` field of task is updated to `True`
* **Test Type:** Automated

### TC-RF004-003: TaskService Deletes Task

* **Description:** Verify `delete_task()` removes a task by ID
* **Preconditions:** Task with ID=1 exists in TaskService
* **Steps:**
  1. Call `delete_task(1)`
* **Expected:** Task with ID=1 is no longer in the list
* **Test Type:** Automated

### TC-RF004-004: Validate Task Class Instantiation and Attributes

* **Description:** Create a `Task` object and verify attributes are correctly set
* **Preconditions:** None
* **Steps:**
  1. Instantiate `Task(title="T", description="D")`
* **Expected:** Fields `title`, `description`, `completed`, and `id` are set as expected
* **Test Type:** Automated

---

## 🧱 TaskService Class Refactor (RF005)

| Test Case ID | Description                                 | Test Type | Notes                                       |
| ------------ | ------------------------------------------- | --------- | ------------------------------------------- |
| TC-RF005-001 | `TaskService.add_task()` stores task        | Automated | Returns correct task with ID and title      |
| TC-RF005-002 | `TaskService.get_tasks()` returns task list | Automated | Should return all tasks from in-memory list |
| TC-RF005-003 | `TaskService.complete_task()` updates task    | Automated | Updates completion status to `True`         |
| TC-RF005-004 | `TaskService.delete_task()` removes task    | Automated | Task is removed and no longer in list       |

### TC-RF005-001: TaskService.add_task() Stores Task

* **Description:** `add_task()` stores and returns a new task
* **Preconditions:** Service initialized
* **Steps:**
  1. Call `add_task("Test", "Try")`
* **Expected:** Returns task with ID and correct title/description
* **Test Type:** Automated

### TC-RF005-002: TaskService.get_tasks() Returns Task List

* **Description:** `get_tasks()` returns full list of tasks
* **Preconditions:** Service has multiple tasks
* **Steps:**
  1. Call `get_tasks()`
* **Expected:** List of task objects returned
* **Test Type:** Automated

### TC-RF005-003: TaskService.update_task() Updates Completion Status

* **Description:** `update_task()` updates the completion status of a task
* **Preconditions:** Task exists with `completed=False`
* **Steps:**
  1. Call `update_task(task_id, completed=True)`
* **Expected:** Task is marked as complete
* **Test Type:** Automated

### TC-RF005-004: TaskService.delete_task() Removes Task

* **Description:** `delete_task()` deletes task with valid ID
* **Preconditions:** Task exists
* **Steps:**
  1. Call `delete_task(task_id)`
* **Expected:** Task is removed from list
* **Test Type:** Automated

---
## 🧱 Dependency Injection Refactor (RF006A–RF006C)

| Test Case ID  | Description                                          | Test Type       | Notes                                                     |
| ------------- | ---------------------------------------------------- | --------------- | --------------------------------------------------------- |
| TC-RF006A-001 | `TaskStorage` wrapper supports load/save             | Automated       | Abstracts file I/O for easier injection                   |
| TC-RF006B-001 | App factory injects `TaskService` with `TaskStorage` | Automated       | DI pattern wired in `__init__.py` using factory pattern   |
| TC-RF006B-002 | TaskService Injected in Flask App Factory            | Static          | validate the injection is implemented as expected         |
| TC-RF006C-001 | Flask routes use `current_app.task_service`          | Static + Manual | Confirms DI usage in `routes/tasks.py` (no direct import) |

---

### TC-RF006A-001: TaskStorage Wrapper Supports Load/Save

* **Description:** Validates `TaskStorage.load_tasks()` and `save_tasks()` wrap file operations
* **Preconditions:** `data/tasks.json` file exists
* **Steps:**

  1. Create a `TaskStorage` instance
  2. Use `.load_tasks()` to retrieve current data
  3. Use `.save_tasks()` to write a new task list
* **Expected:** Loads and saves task list successfully
* **Test Type:** Automated

---

### TC-RF006B-001: App Injects TaskService via `__init__.py`

* **Description:** Ensures Flask app is initialized with injected `TaskService` instance
* **Preconditions:** DI is implemented in `__init__.py`
* **Steps:**

  1. Call app factory `create_app()`
  2. Access `app.task_service`
* **Expected:** `app.task_service` is an instance of `TaskService` with injected `TaskStorage`
* **Test Type:** Automated

---
### TC-RF006B-002: TaskService Injected in Flask App Factory

* **Description:** Confirm that TaskService is created and attached to the Flask app via `create_app()`
* **Preconditions:** Flask app factory pattern in use
* **Steps:**

  1. Inspect `__init__.py`
  2. Confirm instance of `TaskService` is created with `TaskStorage`
  3. Ensure it is assigned to `app.task_service`
* **Expected:** App has injected task\_service ready for use
* **Test Type:** Static

---

### TC-RF006C-001: Flask Routes Use Injected TaskService

* **Description:** Verifies routes use `current_app.task_service` for all logic calls
* **Preconditions:** App created using app factory
* **Steps:**

  1. Inspect code in `routes/tasks.py`
  2. Confirm no direct import of `task_service`
  3. Look for `current_app.task_service` usage
* **Expected:** All logic routed through injected instance
* **Test Type:** Static + Manual


---

## 🧪 Mock Service and Integration Refactor (RF008)

| Test Case ID | Description                         | Test Type            | Storage Mode | Notes                                   |
| ------------ | ----------------------------------- | -------------------- | ------------ | --------------------------------------- |
| TC-RF008-001 | Add task via `requests.post()`      | Automated (requests) | Real         | Integration test for POST               |
| TC-RF008-002 | View task via `requests.get()`      | Automated (requests) | Real         | Integration test for GET                |
| TC-RF008-003 | Complete task via `requests.put()`  | Automated (requests) | Real         | Integration test for PUT                |
| TC-RF008-004 | Delete task via `requests.delete()` | Automated (requests) | Real         | Integration test for DELETE             |
| TC-RF008-005 | Inject mock service into app        | Automated (unit)     | Mocked       | `conftest.py` injects `MockTaskService` |
| TC-RF008-006 | Add task with mock service          | Automated (unit)     | Mocked       | No file I/O — memory-only               |
| TC-RF008-007 | Complete task with mock service     | Automated (unit)     | Mocked       | Task is updated in memory               |
| TC-RF008-008 | Delete task with mock service       | Automated (unit)     | Mocked       | Task is removed from mock list          |

<!-- Detailed test cases follow -->

### TC-RF008-001: Add Task via POST

* **Description:** Add a task using `requests.post()`
* **Preconditions:** Server running, no existing tasks
* **Steps:**

  1. Send POST `/api/tasks` with valid payload
* **Expected:** Status 201, JSON response includes task
* **Test Type:** Automated (requests)

### TC-RF008-002: View Tasks via GET

* **Description:** View tasks using `requests.get()`
* **Preconditions:** Tasks exist in storage
* **Steps:**

  1. Send GET `/api/tasks`
* **Expected:** List of tasks returned with status 200
* **Test Type:** Automated (requests)

### TC-RF008-003: Mark Task Complete via PUT

* **Description:** Mark task complete using `requests.put()`
* **Preconditions:** Task exists
* **Steps:**

  1. Send PUT `/api/tasks/1` to mark as complete
* **Expected:** Status 200 and `"completed": true` in response
* **Test Type:** Automated (requests)

### TC-RF008-004: Delete Task via DELETE

* **Description:** Delete task using `requests.delete()`
* **Preconditions:** Task exists
* **Steps:**

  1. Send DELETE `/api/tasks/1`
* **Expected:** Status 200, task removed
* **Test Type:** Automated (requests)

### TC-RF008-005: Inject MockTaskService

* **Description:** Verify that `MockTaskService` can be injected into `app.task_service`
* **Preconditions:** Flask app created via `create_app()`
* **Steps:**

  1. Create instance of `MockTaskService()`
  2. Assign it to `app.task_service`
  3. Confirm test client uses the mock for requests
* **Expected:** All API requests interact with mock, not real file
* **Test Type:** Automated (unit)

### TC-RF008-006: Add Task Using MockTaskService

* **Description:** Verify that `add_task()` on `MockTaskService` correctly adds a task in-memory
* **Preconditions:** `MockTaskService` initialized with no tasks
* **Steps:**

  1. Create `MockTaskService` instance
  2. Call `add_task("Write test", "Add test case for mock")`
  3. Call `get_all_tasks()`
* **Expected:** Task list contains one task with correct data, ID = 1, `completed = False`
* **Test Type:** Automated (unit)

### TC-RF008-007: Complete Task Using MockTaskService

* **Description:** Verify `complete_task()` updates `completed` to `True`
* **Preconditions:** Task exists with `completed = False`
* **Steps:**

  1. Call `add_task("Mock Complete", "Mark complete test")`
  2. Call `complete_task(1)`
  3. Retrieve updated task
* **Expected:** Task ID = 1, `completed = True`
* **Test Type:** Automated (unit)

### TC-RF008-008: Delete Task Using MockTaskService

* **Description:** Verify that `delete_task()` removes a task from mock list
* **Preconditions:** Task with ID = 1 exists in mock
* **Steps:**

  1. Call `add_task("Delete Me", "Will be deleted")`
  2. Call `delete_task(1)`
  3. Call `get_all_tasks()`
* **Expected:** List is empty; task was removed
* **Test Type:** Automated (unit)

---


# ✅ Sprint 3 Test Cases – Detailed Format

## 🧪 Test Type Legend

| Type               | Meaning                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **Static**         | Read-only inspection of codebase (no execution)                        |
| **Manual**         | Performed by a user via CLI, curl, Postman, etc.                       |
| **Automated**      | Run via test code (e.g., pytest) and asserts actual behavior           |
| **Static + Manual**| Code inspection followed by a manual runtime check                     |

---

## Regression Log

### ✅ User Story Test Cases (Sprint 3 Focus: Full CRUD + Persistence)

> Sprint 3 ensures **Add/View/Complete/Delete** all work end-to-end through the **TaskService + FileTaskRepository + routes**, with **requests-based API tests** and **JSON persistence**.

---

### 📌 US002 – Add Task

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US002-001     | Add valid task via API               | Automated   | POST `/api/tasks` → 201 + task JSON          |
| TC-US002-002     | Missing title                        | Automated   | Should return 400 Bad Request                 |
| TC-US002-003     | Empty/whitespace-only title          | Automated   | Should return 400 Bad Request                 |
| TC-US002-004     | Missing description (optional)       | Automated   | Description optional; still 201 Created       |

---

### 📌 US003 – View Tasks

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US003-001     | View tasks when none exist           | Automated   | Should return empty list `[]`                 |
| TC-US003-002     | View tasks when tasks exist          | Automated   | Should return list of task objects            |

---

### 📌 US005 – Mark Task Complete (PUT /api/tasks/<id>)

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US005-001     | Mark task complete (valid ID)        | Automated   | Expects 200 and `"completed": true`           |
| TC-US005-002     | Mark task complete (nonexistent ID)  | Automated   | Expects 404 Not Found                         |

---

### 📌 US007 – Delete Task (DELETE /api/tasks/<id>)

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US007-001     | Delete task (valid ID)               | Automated   | Should return 200 and removed task            |
| TC-US007-002     | Delete task (nonexistent ID)         | Automated   | Should return 404 Not Found                   |

---

### 📌 US011 – Persist Tasks (File Storage via FileTaskRepository)

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US011-001     | Tasks persist after restart          | Automated   | POST → restart → GET shows same data          |
| TC-US011-002     | Load tasks from `tasks.json` at startup | Automated | File is source of truth for TaskService       |

---

### 📌 US006 – CLI Add Task (Sprint 3 CLI Integration)

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US006-001     | CLI prompt accepts task input        | Manual      | Uses `input()` from CLI menu                  |
| TC-US006-002     | CLI passes new task to TaskService   | Manual      | Verify via console output or GET `/api/tasks` |

---

### 📌 US027 – CLI View Task Report

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US027-001     | CLI lists tasks                      | Manual      | Read-only display of tasks from TaskService   |

---

### 📌 US028 – CLI Complete Task

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US028-001     | CLI marks task as complete           | Manual      | Calls `TaskService.complete_task()`           |

---

## ✅ Error Handling & Validation (US015 – API Robustness)

> In Sprint 3, error handling must work correctly for **PUT/DELETE** and invalid JSON/payloads.

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-US015-001     | Invalid JSON format                  | Automated   | Expects 400 Bad Request                       |
| TC-US015-002     | Missing JSON content-type header     | Automated   | Expects 415 or 400 (as implemented)           |
| TC-US015-003     | PUT/DELETE with invalid ID           | Automated   | Expects 404 Not Found                         |

---

## ✅ Architecture & Refactor Test Cases

> These cover **OOP architecture, DI, persistence**, and are especially relevant after Sprint 3’s refactor.

### 🧱 Blueprint Routing (Regression from Prior Sprint)

| Test Case ID     | Description                          | Test Type        | Notes                                         |
|------------------|--------------------------------------|------------------|-----------------------------------------------|
| TC-ARCH-001      | Routes mounted via Blueprints        | Static + Manual  | `main.py` uses `create_app()` + `register_blueprint()` |
| TC-ARCH-002      | No routes defined in `main.py`       | Static           | All routes must live in `routes/` modules     |
| TC-NFR001-001    | All task endpoints available via /api/tasks | Automated  | GET, POST, PUT, DELETE all reachable          |

---

### 🧱 File Storage Refactor (RF002 → FileTaskRepository in Sprint 3)

| Test Case ID     | Description                               | Test Type   | Notes                                        |
|------------------|-------------------------------------------|-------------|----------------------------------------------|
| TC-ARCH-003      | `FileTaskRepository.load_tasks()` works   | Automated   | Returns list of tasks from `tasks.json`      |
| TC-ARCH-004      | `FileTaskRepository.save_tasks()` works   | Automated   | Persists tasks after add/complete/delete     |

---

### 🧱 App Factory Pattern & DI

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-ARCH-005      | App initializes via `create_app()`   | Automated   | Used in tests via `conftest.py`              |
| TC-ARCH-006      | Blueprints registered correctly      | Automated   | Endpoints mount without 404                  |
| TC-NFR001-002    | `create_app()` wires TaskService + FileTaskRepository | Automated | DI is correct; no runtime injection errors   |

---

## ✅ Manual Tests via Postman, curl, or CLI

| Test Case ID     | Description                          | Test Type   | Notes                                         |
|------------------|--------------------------------------|-------------|-----------------------------------------------|
| TC-MANUAL-001    | Add task via Postman/curl            | Manual      | Screenshot/log required                       |
| TC-MANUAL-002    | View tasks via Postman/curl          | Manual      | Screenshot/log required                       |
| TC-MANUAL-003    | Mark task complete via Postman/curl  | Manual      | Validates PUT `/api/tasks/<id>`               |
| TC-MANUAL-004    | Delete task via Postman/curl         | Manual      | Validates DELETE `/api/tasks/<id>`            |

---

## Summary Refactors for Sprint 3

> These map directly to **PR2, PR6, PR7, PR8** and are the core of Sprint 3.

| Refactor ID | Description                                                  | Notes                                                           |
|-------------|--------------------------------------------------------------|-----------------------------------------------------------------|
| RF004       | Introduce `Task` class                                      | Replace dictionary-based model with structured domain object    |
| RF005       | Implement `TaskService`                                     | Encapsulates all CRUD logic for tasks                           |
| RF006A      | Introduce `TaskRepository` / `FileTaskRepository`           | Abstraction layer for JSON storage                              |
| RF006B      | Inject `TaskService` via app factory (`create_app()`)       | Attaches service to Flask app instance                          |
| RF006C      | Refactor routes to use `current_app.task_service`           | Ensures all routes use DI instead of direct imports             |
| RF007       | Add PUT/DELETE task endpoints                               | API supports complete & delete operations                       |
| RF008       | Introduce `MockTaskService` + `requests`-based API testing  | Enables fast, isolated tests and end-to-end API validation      |

---

## 🧱 Introduce `Task` Class for Domain Modeling (RF004)

> In Sprint 3, `Task` becomes a first-class domain object used by `TaskService` and stored via `FileTaskRepository`.

### Test Cases for RF004

| Test Case ID | Description                                  | Test Type   | Notes                                                   |
|--------------|----------------------------------------------|-------------|---------------------------------------------------------|
| TC-RF004-001 | Task object can be instantiated              | Automated   | `Task(title, description)` creates valid object         |
| TC-RF004-002 | Task object tracks completed status          | Automated   | Default `completed=False`; update to `True` supported   |
| TC-RF004-003 | Task object has correct ID, title, desc      | Automated   | Validate all attributes after construction              |
| TC-RF004-004 | Task interacts correctly with TaskService    | Automated   | Stored, retrieved, and updated via service methods      |

---

### TC-RF004-001: TaskService Adds Task

* **Description:** Verify `add_task()` correctly stores a new Task  
* **Preconditions:** TaskService initialized with empty repository  
* **Steps:**  
  1. Call `add_task("Title", "Description")`  
* **Expected:** Returns Task with correct title, description, and non-null ID  
* **Test Type:** Automated  

### TC-RF004-002: TaskService Marks Task Complete

* **Description:** Verify `complete_task()` sets Task.completed to `True`  
* **Preconditions:** Task exists with `completed=False`  
* **Steps:**  
  1. Call `complete_task(task_id)`  
* **Expected:** Task’s `completed` becomes `True`  
* **Test Type:** Automated  

### TC-RF004-003: TaskService Deletes Task

* **Description:** Verify `delete_task()` removes a Task by ID  
* **Preconditions:** Task with ID exists  
* **Steps:**  
  1. Call `delete_task(task_id)`  
* **Expected:** Task no longer appears in `get_all_tasks()`  
* **Test Type:** Automated  

### TC-RF004-004: Validate Task Class Instantiation

* **Description:** Create a `Task` and verify all attributes  
* **Preconditions:** None  
* **Steps:**  
  1. Instantiate `Task(title="T", description="D")`  
* **Expected:** ID assigned, `completed=False`, title/description correct  
* **Test Type:** Automated  

---

## 🧱 TaskService Class Refactor (RF005)

| Test Case ID | Description                                 | Test Type   | Notes                                       |
|--------------|---------------------------------------------|-------------|---------------------------------------------|
| TC-RF005-001 | `TaskService.add_task()` stores Task        | Automated   | Returns new Task with ID and correct data   |
| TC-RF005-002 | `TaskService.get_all_tasks()` returns list  | Automated   | Includes all Tasks from repository          |
| TC-RF005-003 | `TaskService.complete_task()` updates Task  | Automated   | Sets `completed=True`                       |
| TC-RF005-004 | `TaskService.delete_task()` removes Task    | Automated   | Task removed from repository                |

(Descriptions consistent with RF004 details above.)

---

## 🧱 Dependency Injection Refactor (RF006A–RF006C)

| Test Case ID  | Description                                          | Test Type       | Notes                                                     |
|---------------|------------------------------------------------------|-----------------|-----------------------------------------------------------|
| TC-RF006A-001 | FileTaskRepository supports load/save                | Automated       | Abstracts file I/O into repository class                  |
| TC-RF006B-001 | App factory injects TaskService with repository      | Automated       | `create_app()` wires `TaskService(FileTaskRepository(...))` |
| TC-RF006B-002 | TaskService attached to Flask app instance           | Static          | `app.task_service` or `current_app.task_service` present  |
| TC-RF006C-001 | Routes use `current_app.task_service`                | Static + Manual | No direct imports of TaskService/Repository in routes     |

---

### TC-RF006A-001: FileTaskRepository Load/Save

* **Description:** Validates `load_tasks()` and `save_tasks()` wrap JSON file operations  
* **Preconditions:** `tasks.json` exists or is creatable  
* **Steps:**  
  1. Instantiate FileTaskRepository with file path  
  2. Call `load_tasks()`  
  3. Modify list and call `save_tasks()`  
* **Expected:** File updated, data read back correctly  
* **Test Type:** Automated  

---

### TC-RF006B-001: App Injects TaskService

* **Description:** Ensures Flask app uses injected TaskService instance  
* **Preconditions:** App factory implemented  
* **Steps:**  
  1. Call `create_app()` in test  
  2. Assert `app.task_service` exists and is TaskService  
* **Expected:** No errors; DI successful  
* **Test Type:** Automated  

---

### TC-RF006B-002: Static Verification of Injection

* **Description:** Confirm that TaskService is created and attached in `__init__.py`  
* **Test Type:** Static  

---

### TC-RF006C-001: Routes Use Injected TaskService

* **Description:** Verify `routes/tasks.py` uses `current_app.task_service` exclusively  
* **Preconditions:** App factory + DI in place  
* **Steps:**  
  1. Inspect code in `routes/tasks.py`  
  2. Confirm no direct imports of TaskService/FileTaskRepository  
  3. Confirm usage of `current_app.task_service`  
* **Expected:** All business logic calls go through injected service  
* **Test Type:** Static + Manual  

---

## 🧪 Mock Service and Integration Refactor (RF008)

| Test Case ID | Description                         | Test Type            | Storage Mode | Notes                                   |
|--------------|-------------------------------------|----------------------|--------------|-----------------------------------------|
| TC-RF008-001 | Add task via `requests.post()`      | Automated (requests) | Real         | Integration test for POST               |
| TC-RF008-002 | View tasks via `requests.get()`     | Automated (requests) | Real         | Integration test for GET                |
| TC-RF008-003 | Complete task via `requests.put()`  | Automated (requests) | Real         | Integration test for PUT                |
| TC-RF008-004 | Delete task via `requests.delete()` | Automated (requests) | Real         | Integration test for DELETE             |
| TC-RF008-005 | Inject mock service into app        | Automated (unit)     | Mocked       | `conftest.py` injects `MockTaskService` |
| TC-RF008-006 | Add task with mock service          | Automated (unit)     | Mocked       | No file I/O — memory-only               |
| TC-RF008-007 | Complete task with mock service     | Automated (unit)     | Mocked       | Verifies `completed=True` update        |
| TC-RF008-008 | Delete task with mock service       | Automated (unit)     | Mocked       | Removes task from mock list             |

---

### High-Level Flows (RF008)

- **Requests-based E2E tests** verify that the **real Flask server + JSON file** behave correctly.  
- **MockTaskService tests** verify that business logic can run **without touching the file system**, improving speed and reliability.

---

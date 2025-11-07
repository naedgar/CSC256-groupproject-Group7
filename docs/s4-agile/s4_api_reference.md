# 🌐 Sprint 4 API Documentation

This document outlines the updated API endpoints and implementation details for the TaskTracker project. 

> Sprint 4 introduces web-based form interfaces, integrates SQLAlchemy for persistent storage using SQLite, and expands the test strategy to include UI and BDD testing layers. This document includes updated API routes, form endpoints, model details, and testing notes.

---

## Overview of Changes in Sprint 3

* Introduced `TaskService` class for business logic
* Introduced `TaskRepository` interface for persistence layer
* CLI: Implemented `Mark Task Complete` (US029)
* Introduced automated API tests using `requests` (US035)

**Authentication:** Not required  
**Versioning:** Not required  
**Environment:** Local development only (e.g., http://localhost:5000)  
**Base Route:** `/api`

---


## Overview of Changes in Sprint 4

## ✅ Overview
| Category         | Technology         |
|------------------|--------------------|
| Framework        | Flask              |
| Storage          | SQLite (via SQLAlchemy ORM) |
| UI               | Flask Templates + HTML Forms |
| API Format       | REST (JSON)        |
| Validation       | HTML5 + Server-Side |
| Testing Tools    | Pytest, Requests, Selenium, Playwright, behave |
| Design Pattern   | Dependency Injection (DI) |
| Architecture     | Layered (Blueprints, Services, Repository) |


## 📌 Key Notes (Sprint 4)

- The application will now uses **SQLAlchemy ORM with SQLite** (no external DB install required)
- `TaskService` is injected with a `DatabaseTaskRepository`
- Tasks are created through both API (`POST /api/tasks`) and Web Form (`POST /tasks/new`)
- Validation occurs at both **form/UI level** and **service layer**
---

## 📬 API Endpoints (JSON)

| Method | URL                 | Description                            | Status Code |
|--------|---------------------|----------------------------------------|-------------|
| GET    | `/api/health`       | Health check                           | 200         |
| GET    | `/api/tasks`        | Get all tasks                          | 200         |
| POST   | `/api/tasks`        | Add a new task                         | 201         |
| PUT    | `/api/tasks/<id>`   | Mark task as completed                 | 200 / 404   |
| DELETE | `/api/tasks/<id>`   | Delete task                            | 200 / 404   |
| POST   | `/api/tasks/reset`  | Reset tasks (used for test automation) | 204         |


## 🖥️ UI Form Routes

These endpoints render HTML templates and are designed for direct user interaction in the browser.

| Method | URL             | Description                                  |
|--------|------------------|----------------------------------------------|
| GET    | `/tasks/new`     | Render the task creation form (US012)        |
| POST   | `/tasks/new`     | Handle task form submission (US012, US036)   |
| GET    | `/tasks/report`  | View task report summary page (US027)        |



---

## 🔧 Extended Endpoint Behavior

### PUT /api/tasks/<id>

> 📌 `PUT /api/tasks/<id>` now handles two use cases:
>
> * Mark task as complete (`completed: true`)
> * Update the `title` (edit task)

#### ✅ Example Request (Edit Task Title)

```http
PUT /api/tasks/1
Content-Type: application/json

{
  "title": "Update task title"
}
```

#### ✅ Expected Response

```json
{
  "id": 1,
  "title": "Update task title",
  "description": "Previous description",
  "completed": false
}
```

> ✅ Partial updates supported for `title` or `completed` fields.

---

## 🧠 Business Logic: `TaskService` (RF005)

The service layer abstracts the task logic. It is injected into the controller to promote testability and separation of concerns.

### RF005
```python
from services.task_service import TaskService

task_service = TaskService(storage_path="data/tasks.json")
```
💡 Note: TaskService separates "what the app does" (business logic) from "how it's stored" (repository), making it easier to swap file storage for a database.

### 🔧 RF011 – Inject Database Repository into TaskService

**Refactor Title:** Database Injection via Dependency Injection (DI)  
**Sprint:** Sprint 4  
**Related Architecture:** RF005 (TaskService), RF006 (DI Setup)  

**Description:**  
Replaces the file-based `FileTaskRepository` with a SQLAlchemy-backed `DatabaseTaskRepository`, injected into `TaskService` via constructor-based dependency injection. This completes the shift from JSON persistence to a database-backed model while preserving modular architecture and testability.

**Why Not Just Extend RF005?**  
RF005 introduced `TaskService` as a business logic abstraction. RF011 builds on it by injecting a new backend (SQLAlchemy DB) into that same service, requiring different testing, models, and configuration. It warrants its own ID to mark the storage backend transition.

#### ✅ Updated Example

```python
from repositories.database_repository import DatabaseTaskRepository
from services.task_service import TaskService

db_repo = DatabaseTaskRepository(session_factory)
task_service = TaskService(db_repo)
```
---

## 🔄 Design Note

* Validation ensures:

  * Nonexistent tasks return `404`
  * Empty or invalid payloads return `400`
* Global error handler ensures consistent JSON errors

---

## 🧪 Testing Strategy

### ✅ Updated Testing Strategy

* Unit tests now cover the new `Task` and `TaskService` classes introduced in Sprint 3.
* API route tests use the Flask test client to validate Blueprint-based routing behavior.
* End-to-end automated API tests using the requests library are now split into integration tests (real storage) and unit tests using a mock service. Files include:
  * In `tests/api/test_tasks_api.py` (integration using real file storage)
  * In `tests/mocks/test_mock_task_service.py`, the `TaskService` is instantiated using a `MockRepository` to simulate storage. This supports RF008 by isolating logic from the file system.
* Regression tests confirm that previously implemented endpoints (add, list, complete, delete) remain functional after the object-oriented refactor.
* New CLI feature (US029) calls `TaskService.mark_task_complete()` directly for manual testing.
* API tests from US035 are implemented in `tests/api/test_tasks_api.py` and run via GitHub Actions.
* Unit tests also ensure that business logic remains consistent across refactors, preserving behavior.

---

### 📋 API Architecture Validation Test Cases

✅ **TC-NFR001-001: Routes Accessible via Blueprint**

* Verify `GET /api/health`, `GET /api/tasks`, and `POST /api/tasks` return status `200` or `201` using the Flask test client.
* Ensures routes are correctly registered through `app.register_blueprint()`.

🛠️ **TC-NFR001-002: Modular Architecture Enforcement**

* Manual test: comment out `app.register_blueprint()` in `app/__init__.py`, then verify `GET /api/tasks` returns a `404`.
* Confirms routing is now dependent on Blueprint registration (modular design).

---

✅ These cases ensure that the refactored architecture is functional, testable, and modular—laying the groundwork for database integration in Sprint 4.
🔁 These validations support the architecture introduced in RF006 (Dependency Injection) and RF007 (Blueprint Modularization), ensuring that route logic, injection, and structure remain modular and maintainable.

---

## 📌 Reminder: ERD and Class Diagram

The current API does not include database integration yet. However, the object model has been updated in the class diagram.

> Full ERD implementation will occur in Sprint 4.

---
## 🪡 Internal Refactor Notes

* `TaskService` is now responsible for handling task logic.
* `FileTaskRepository` abstracts JSON I/O and implements a common `TaskRepository` interface. `FileTaskRepository` is used in Sprint 3 but will be swapped for SQLAlchemy in Sprint 4.
* Routes now reside in `routes/tasks.py` and register via Blueprint.
* `create_app()` wires the app, repository, and service using constructor injection.

---

## 🔍 Testing Considerations

* Unit tests now target the service layer directly.
* Controller tests interact with the service via test clients.
* `tests/` folder includes modular tests like `test_add_task.py`, `test_complete_task.py`, etc.
* Mocking is introduced using MockTaskService in unit tests to simulate repository behavior without file I/O. This supports RF008 and improves test isolation and speed.

---

### 🔁 CI Integration Notes

CI continues from Sprint 2 but now additionally validates:

* Modular test coverage of route handlers and service classes
* Successful object-oriented refactor (`TaskService`)
* Continued adherence to endpoint contracts (no regressions)
* ✅ Automated end-to-end API tests using Python’s `requests` library

Your updated GitHub Actions workflow now runs both modular unit tests and full API tests:

```yaml
- name: Run modular unit tests
  run: pytest tests/ --cov=app --cov-report=term-missing

- name: Run automated API tests with requests
  run: pytest tests/api/ --cov=app --cov-report=term-missing
```

> 🧪 Note: `tests/api/` contains external API tests written using `requests` that call the running Flask server, simulating real HTTP traffic.
🔧 To simulate a real system without touching actual storage, MockTaskService is injected during CI unit tests. This ensures we isolate business logic from infrastructure and speed up test execution.

---

## System Diagram (Sprint 3)

```mermaid
flowchart TD
  subgraph Real_API_Tests
    A1["requests.post() etc."] --> B1[Flask Routes]
    B1 --> C1[TaskService]
    C1 --> D1[FileTaskRepository]
    D1 --> E1[JSON File]
  end

  subgraph Mock_API_Tests
    A2[MockTestClient] --> B2[Injected TaskService]
    B2 --> D2[MockTaskRepository]
    D2 --> E2[In-Memory List]
  end
```

> 🧠 This updated system diagram shows the introduction of OOP, DI, and Blueprint modularity while preserving all endpoint behavior.

## System Diagram (Sprint 4)

```mermaid
flowchart TD
  subgraph Real_API_Tests
    A1["requests.post() / client.post()"] --> B1[Flask Routes]
    B1 --> C1[TaskService]
    C1 --> D1[DatabaseTaskRepository]
    D1 --> E1["SQLite DB (SQLAlchemy)"]
  end

  subgraph Mock_API_Tests
    A2[MockTestClient] --> B2[Injected TaskService]
    B2 --> D2[MockTaskRepository]
    D2 --> E2[In-Memory List]
  end
```


---
## 📋 User Stories and Endpoint Summary

## ✅ Endpoints and CLI Features

| User Story | Title                      | Endpoint or Notes                                 | Refactor(s)  |
| ---------- | -------------------------- | ------------------------------------------------- | ------------ |
| US002      | Add Task                   | `POST /api/tasks`                                 | RF005, RF008 |
| US003      | View Tasks                 | `GET /api/tasks`                                  | RF005, RF008 |
| US004      | Mark Task Complete         | `PUT /api/tasks/<id>`                             | RF005, RF008 |
| US005      | Remove Task                | `DELETE /api/tasks/<id>`                          | RF005, RF008 |
| US007      | Remove Task (CLI complete) | CLI-based implementation only                     | RF005        |
| US015      | API Error Handling         | Applies to all endpoints                          | RF005, RF006 |
| US029      | CLI UI: Mark Task Complete | CLI-only; uses `TaskService.mark_task_complete()` | RF005        |
| US035      | API Testing Automation     | `requests` tests for all above                    | RF008        |


---

> 🔎 **Note:**  
> - US029 applies to CLI only; does not affect API.  
> - US035 introduces automated testing using `requests`, replacing manual `curl`/Postman.

---

---

## 🔄 Regression Coverage Summary

✅ API Regression Tests (RF008 / US035)

The following endpoints are validated using `requests` tests and mock injection strategies to ensure full CRUD functionality is preserved after refactors:

- `POST /api/tasks`
- `GET /api/tasks`
- `PUT /api/tasks/<id>`
- `DELETE /api/tasks/<id>`


## 📊 Summary

Sprint 3 API documentation confirms that although no new endpoints were added, all previously implemented endpoints now follow a service-oriented, modular architecture with injected dependencies. This refactor supports maintainability, testability, and prepares the app for database migration in Sprint 4.

Next Sprint: Replace JSON persistence with a database, implement models via SQLAlchemy, and extend automated testing to use the `requests` module.

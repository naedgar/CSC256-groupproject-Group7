# ✅ Sprint 3 Test Plan – Object-Oriented Refactor, Persistence & API Automation

## 🎯 Overview

Sprint 3 introduces major architectural changes to the TaskTracker project, refactoring procedural code into an object-oriented design using a `Task` model, `TaskService` class, and a persistence abstraction (`FileTaskRepository`). This test plan ensures that all previous functionality is preserved and that the new architectural components (OOP, dependency injection, and JSON-based persistence) are validated through unit, integration, and API-level tests using `requests`.

---

## 1. Scope of Testing

| Category        | Scope                                                                 |
| --------------- | --------------------------------------------------------------------- |
| ✅ Functional    | Add, view, complete, delete tasks (full CRUD)                        |
| 🧠 Architecture | Validate use of `Task`, `TaskService`, `TaskRepository/FileTaskRepository`, and dependency injection via `create_app()` |
| 💾 Persistence  | Ensure tasks are stored and loaded from `app/data/tasks.json`         |
| ⚙️ Integration  | Route → Service → Repository → JSON file                              |
| 🧪 Automation   | Replace Postman/manual tests with `requests`-based API automation     |
| 🖥️ CLI         | Maintain CLI logic to call `TaskService` methods (add/complete/delete) |

---

## 2. Features Being Tested

| Feature                        | User Story(s) | Notes                                                         |
| ------------------------------ | ------------- | ------------------------------------------------------------- |
| Add Task                       | US002         | Tested via `TaskService.add_task()` and POST `/api/tasks`     |
| View Tasks                     | US003         | Includes empty-list and multi-task scenarios                  |
| Mark Task Complete             | US004         | PUT `/api/tasks/<id>` and CLI integration with TaskService    |
| Remove Task                    | US005         | DELETE `/api/tasks/<id>` and repository update                |
| Persist Tasks to JSON          | US011         | `FileTaskRepository` reads/writes `tasks.json`                |
| Error Handling                 | US015         | Validates 400/404 responses and malformed JSON handling       |
| OOP Refactor (Task + Service)  | US027/US028   | `Task` model and `TaskService` encapsulate task logic         |
| CLI Integration                | US029         | CLI calls TaskService methods instead of direct data access   |
| API Automation (`requests`)    | US035         | Replaces Postman with automated end-to-end API tests          |

---

## 3. Out of Scope

| Out of Scope                 | Reason                                               |
| ---------------------------- | ---------------------------------------------------- |
| Task title editing           | Moved to group project scope (US009 not implemented) |
| Database-related persistence | Scheduled for Sprint 4 (future DB or ORM integration) |
| UI-based features            | Web UI and acceptance testing are Sprint 4+          |
| Time/History features        | Implemented in other sprints (not part of Sprint 3)  |

---

## 4. Types of Testing

| Type               | Tool/Location                           | Description                                                                     |
| ------------------ | --------------------------------------- | ------------------------------------------------------------------------------- |
| ✅ Unit Testing     | `tests/services/test_task_service.py`   | Tests `Task` and `TaskService` behavior in isolation (no Flask, no real file I/O) |
| ✅ Unit Testing     | `tests/storage/test_file_repository.py` | Validates `FileTaskRepository.load_tasks()` and `.save_tasks()`                 |
| ✅ Integration Test | `tests/routes/test_tasks.py`            | Verifies Route → TaskService → FileTaskRepository → `tasks.json` workflow       |
| ✅ API Testing      | `tests/api/test_tasks_api.py`           | Validates endpoints using `requests` and a running Flask server                 |
| ✅ CLI Manual Test  | `app/cli/cli_app.py`                    | CLI interface to test add/complete/delete via TaskService                       |
| ✅ Regression Test  | `pytest` suite                          | Ensures all prior endpoints still function after OOP/DI/persistence refactor    |

---

## 5. Test Environment

| Component    | Value                         |
| ------------ | ----------------------------- |
| OS           | Windows 11 or macOS/Linux     |
| Flask Port   | `http://localhost:5000`       |
| Python       | 3.11+                         |
| Flask        | 2.x                           |
| JSON Storage | `app/data/tasks.json`         |
| CLI Entry    | `python -m app.cli.cli_app`   |
| API Server   | `python -m app.main`          |
| CI           | GitHub Actions                |

---

## 6. Tools

| Purpose             | Tool          | Notes                                                       |
| ------------------- | ------------- | ----------------------------------------------------------- |
| Test Runner         | `pytest`      | All tests structured into modular test files                |
| API Test Automation | `requests`    | Replaces Postman; drives live Flask server for E2E testing  |
| Coverage            | `pytest-cov`  | Required minimum: **80%** overall (focus on service & routes) |
| Manual API Tests    | curl/Postman  | Optional; superseded by automated `requests` tests          |
| CLI Testing         | Terminal/Shell| Used to manually verify CLI integration with TaskService    |

---

## 7. Test Data

| Scenario                  | Input                                          | Expected Outcome                            |
| ------------------------- | ---------------------------------------------- | ------------------------------------------- |
| Valid task creation       | `{"title": "Test", "description": "Desc"}`     | `201 Created`, Task JSON with assigned ID   |
| Complete valid task       | `PUT /api/tasks/1`                             | `200 OK`, `"completed": true`               |
| Delete valid task         | `DELETE /api/tasks/1`                          | `200 OK`, returns deleted task or success   |
| View all tasks            | `GET /api/tasks`                               | `200 OK`, list of tasks or empty list       |
| Invalid ID for PUT/DELETE | `/api/tasks/999`                               | `404 Not Found`                             |
| Malformed JSON            | `POST /api/tasks` with invalid JSON payload    | `400 Bad Request`                           |
| Persistence check         | POST task → restart app → GET `/api/tasks`     | Task still present (loaded from `tasks.json`) |

---

## 8. Risk Mitigation

| Risk                                      | Mitigation Strategy                                                     |
| ----------------------------------------- | ----------------------------------------------------------------------- |
| Refactor breaks existing logic            | Maintain and run all tests from Sprints 1–2 and add new Sprint 3 tests |
| Persistence bugs (data loss/corruption)   | Add unit tests for FileTaskRepository and regression tests for restart |
| DI wiring issues (service not injected)   | Add tests around `create_app()` and `current_app.task_service` usage   |
| CLI becomes outdated vs API behavior      | Manually test CLI after major changes; plan deprecation in Sprint 4     |
| Over-reliance on manual Postman testing   | Migrate flows to automated `requests` tests to reduce human error      |

---

## 9. Test Case References

| Test Case ID | Description                                 | File Location                              |
| ------------ | ------------------------------------------- | ------------------------------------------ |
| TC-US002-001 | Add valid task via API                      | `tests/api/test_add_task.py`               |
| TC-US002-002 | Reject invalid/empty titles                 | `tests/api/test_add_task_validation.py`    |
| TC-US003-001 | View tasks when none exist                  | `tests/api/test_view_tasks.py`             |
| TC-US003-002 | View tasks when tasks exist                 | `tests/api/test_view_tasks.py`             |
| TC-US004-001 | Mark task complete (PUT `/api/tasks/<id>`)  | `tests/api/test_complete_task.py`          |
| TC-US005-001 | Delete task (DELETE `/api/tasks/<id>`)      | `tests/api/test_delete_task.py`            |
| TC-US011-001 | Persist tasks across restart                | `tests/storage/test_persistence.py`        |
| TC-US015-001 | Handle invalid/malformed requests           | `tests/api/test_error_handling.py`         |
| TC-US027-001 | OOP: Task + TaskService unit tests          | `tests/services/test_task_service.py`      |
| TC-US029-001 | CLI completes/deletes task via TaskService  | `app/cli/cli_app.py` (manual verification) |
| TC-US035-001 | End-to-end task workflow via `requests`     | `tests/api/test_tasks_api.py`              |

---

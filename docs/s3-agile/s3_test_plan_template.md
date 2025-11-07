# ✅ Sprint 3 Test Plan – Object-Oriented Refactor & API Automation

## 🎯 Overview

Sprint 3 introduces major architectural changes to the TaskTracker project, refactoring procedural code into an object-oriented design using a `TaskService` class and persistence abstraction. This test plan ensures that all previous functionality is preserved and that new architectural components are validated through unit, integration, and API-level tests.

---

## 1. Scope of Testing

| Category        | Scope                                                               |
| --------------- | ------------------------------------------------------------------- |
| ✅ Functional    | Add, view, complete, delete tasks                                   |
| 🧠 Architecture | Validate use of `TaskService`, `TaskRepository`, and modular design |
| ⚙️ Integration  | Route → Service → Repository → JSON file                            |
| 🧪 Automation   | Replace Postman/manual tests with `requests`-based test automation  |
| 🖥️ CLI         | Maintain CLI logic to call `TaskService.mark_task_complete()`       |

---

## 2. Features Being Tested

| Feature                   | User Story(s) | Notes                                          |
| ------------------------- | ------------- | ---------------------------------------------- |
| Add Task                  | US002         | Tested via service layer and API route         |
| View Tasks                | US003         | Includes view-none and view-multiple scenarios |
| Mark Task Complete        | US004         | PUT request via API and CLI integration        |
| Remove Task               | US005         | DELETE route and logic validation              |
| Error Handling            | US015         | Validates 404s, bad inputs, malformed JSON     |
| CLI Integration           | US029         | CLI calls `TaskService.mark_task_complete()`   |
| API Automation (requests) | US035         | Replaces Postman with automated API tests      |

---

## 3. Out of Scope

| Out of Scope                 | Reason                                               |
| ---------------------------- | ---------------------------------------------------- |
| Task title editing           | Moved to group project scope (US009 not implemented) |
| Database-related persistence | Scheduled for Sprint 4                               |
| UI-based features            | Web UI and acceptance testing are Sprint 4+          |

---

## 4. Types of Testing

| Type               | Tool/Location                         | Description                                                            |
| ------------------ | ------------------------------------- | ---------------------------------------------------------------------- |
| ✅ Unit Testing     | `tests/services/test_task_service.py` | Tests business logic in isolation                                      |
| ✅ Integration Test | `tests/routes/test_tasks.py`          | Verifies route → service → storage workflow                            |
| ✅ API Testing      | `tests/api/test_tasks_api.py`         | Validates endpoints using `requests` and a running Flask server        |
| ✅ CLI Manual Test  | `app/cli/cli_app.py`                  | CLI interface to test task completion using service layer              |
| ✅ Regression Test  | `pytest` suite                        | Ensures all prior endpoints still function after architecture refactor |

---

## 5. Test Environment

| Component    | Value                       |
| ------------ | --------------------------- |
| OS           | Windows 11 or macOS/Linux   |
| Flask Port   | `http://localhost:5000`     |
| Python       | 3.11+                       |
| Flask        | 2.x                         |
| JSON Storage | `app/data/tasks.json`       |
| CLI Entry    | `python -m app.cli.cli_app` |
| API Server   | `python -m app.main`        |
| CI           | GitHub Actions              |

---

## 6. Tools

| Purpose             | Tool         | Notes                                          |
| ------------------- | ------------ | ---------------------------------------------- |
| Test Runner         | `pytest`     | All tests structured into modular test files   |
| API Test Automation | `requests`   | Replaces Postman, calls live Flask server      |
| Coverage            | `pytest-cov` | Required minimum: 80%                          |
| Manual API Tests    | curl/Postman | Deprecated – replaced by automated requests    |
| CLI Testing         | Terminal     | CLI maintained to test task completion (US029) |

---

## 7. Test Data

| Scenario                  | Input                                  | Expected Outcome                      |
| ------------------------- | -------------------------------------- | ------------------------------------- |
| Valid task creation       | `{title: "Test", description: "Desc"}` | `201 Created`, JSON with assigned ID  |
| Complete valid task       | `PUT /api/tasks/1`                     | `200 OK`, `completed: true`           |
| Delete valid task         | `DELETE /api/tasks/1`                  | `200 OK`, returns deleted task info   |
| View all tasks            | `GET /api/tasks`                       | `200 OK`, list of tasks or empty list |
| Invalid ID for PUT/DELETE | `/api/tasks/999`                       | `404 Not Found`                       |
| Malformed JSON            | `POST /api/tasks` with invalid JSON    | `400 Bad Request`                     |

---

## 8. Risk Mitigation

| Risk                           | Mitigation Strategy                                             |
| ------------------------------ | --------------------------------------------------------------- |
| Refactor breaks existing logic | Maintain all tests from Sprints 1–2 and run CI after every push |
| Test fragility with service    | Isolate `TaskService` unit tests from Flask                     |
| CLI becomes outdated           | Flag for deprecation in Sprint 4                                |

---

## 9. Test Case References

| Test Case ID | Description                             | File Location                            |
| ------------ | --------------------------------------- | ---------------------------------------- |
| TC-US002-001 | Add valid task via API                  | `test_add_task.py`                       |
| TC-US003-001 | View tasks when none exist              | `test_view_tasks.py`                     |
| TC-US003-002 | View tasks when tasks exist             | `test_view_tasks.py`                     |
| TC-US004-001 | Mark task complete (PUT /tasks/1)       | `test_complete_task.py`                  |
| TC-US005-001 | Delete task (DELETE /tasks/1)           | `test_delete_task.py`                    |
| TC-US015-001 | Handle invalid/malformed requests       | `test_error_handling.py`                 |
| TC-US029-001 | CLI completes task via TaskService      | `cli_app.py` (manual/print verification) |
| TC-US035-001 | End-to-end task workflow via `requests` | `test_tasks_api.py`                      |

---

Let me know if you'd like this exported to a downloadable Markdown file, or if we should start populating the individual test case document (`s3_test_cases.md`) next.

# 🔮 Sprint 2 Test Plan

## 🌟 Test Objectives

| ID    | Objective                                                                | Success Metric                                                                  |
| ----- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| OBJ-1 | Verify that a task can be **marked complete** (US004)                    | `PUT /api/tasks/<id>` toggles `completed` field to `true`; returns updated task |
| OBJ-2 | Confirm that a task can be **deleted** (US005)                           | `DELETE /api/tasks/<id>` returns 204 No Content and removes task                |
| OBJ-3 | Validate negative scenarios for invalid IDs                              | Nonexistent IDs return `404` error in JSON format                               |
| OBJ-4 | Confirm file-based JSON persistence of tasks (US011)                        | Tasks persist to and load from `data/tasks.json` file                           |
| OBJ-5 | CI integration ensures regression testing of new endpoints & persistence | All tests pass locally and in GitHub Actions                                    |
| OBJ-6 | Confirm CLI Add/View flow supports current task operations (US006) | Tasks added via CLI persist to JSON and reflect correct state |


---

## Test Strategy

This sprint continues TDD practices while introducing error handling. All endpoints will be tested using pytest and verified manually using Postman. Regression testing ensures features from Sprint 1 remain functional.

* Test suite expanded to include title edit behavior
* Regression tests ensure prior features (add, list, complete, delete) still function post-refactor
* ✅ **TC-NFR001-001**: Routes Accessible via Blueprint

  * `GET /api/health`, `GET /api/tasks`, `POST /api/tasks` tested via Flask test client
  * Asserts all return `200` or `201` (no 404 errors)
* 🛠️ **TC-NFR001-002**: Modular Architecture via Flask Blueprint

  * Manual test case: comment out `app.register_blueprint()` and verify `GET /api/tasks` returns `404`
---

## 🔍 Test Types

* **Unit Tests** – Validate individual route logic and edge cases.
* **Integration Tests** – Confirm route behavior with persistence logic.
* **Manual API Tests** – Use Postman to verify JSON responses and error handling.

---

## Tools

* `pytest` — unit/integration testing
* `pytest-cov` — coverage analysis
* `Postman` — manual test verification
* `GitHub Actions` — continuous integration
* Flask Test Client - Simulates API requests 

---

## Test Coverage Goal

* ≥ 90% line coverage
* Coverage checked locally and in CI via pytest-cov
* TC-NFR001-001: Routes accessible via Blueprint (Automated)
* TC-NFR001-002: Modular Architecture via Blueprint (Manual)

## 📌 Test Scope by User Story

### US004: Mark Task Complete

* PUT `/api/tasks/<id>` marks a task as complete
* Must return 200 OK if task exists
* Return 404 Not Found if task ID does not exist

### US005: Delete Task

* `DELETE /api/tasks/<id>` removes the task
* Returns HTTP 204 No Content if task was deleted
* Invalid or missing ID returns 404 JSON error

### US011: Persistence

* Tasks are saved to and loaded from data/tasks.json
* Data must survive server restarts
* File must remain readable and writable by app logic

### US015: Error Handling

* Implement centralized error handler
* Return all errors in JSON format:
  
  ```bash
    { "error": "Invalid request" }
  ```
* Validate proper codes and formats:
   * 400 for malformed input
   * 404 for resource not found
   * 405 for method not allowed
   * 500 for unexpected server issues

Based on the user stories and your attached test plan (`s2_test_plan.md`), here's the **updated Sprint 2 Test Plan section for CLI** with the correct scope and terminology for US006 and US028:

---

## 🧪 CLI Testing Scope

The CLI serves as a **manual testing and instructional interface**. It allows students to test key logic flows without needing Postman or a browser. This is especially helpful before introducing OOP design and the full web UI in Sprint 4.

🧠 Design Insight: This CLI uses the same shared persistence layer (load_tasks, save_tasks) as the Flask API. This reinforces good software design (single source of truth) showing separation of concerns and reuse.

### ✅ Scope for Sprint 2:

* **US006 – CLI UI: Add Task**

  * Prompt user for a task title and optional description.
  * Task is persisted to `data/tasks.json`.
  * Confirmation message shown on success.
  * Input validation shown on blank title.

* **US028 – CLI UI: View Tasks**

  * Print a readable list of tasks, including ID, title, description, and completed status.
  * Show empty message if no tasks exist.

### ❌ Out of Scope for Sprint 2:

* Marking tasks complete via CLI (US029)
* Deleting tasks via CLI (US030)

These will be introduced with object-oriented design and dependency injection in Sprint 3 and 4.

> ⚠️ **Note**: The CLI will remain a *manual testing tool* this sprint. There are no automated test hooks, so validation is performed by running the CLI and observing output.

---
## Manual API Testing (Postman)

For each endpoint:
* Test valid/invalid inputs for all endpoints
* Confirm status codes and response structure
* Export and submit Postman collection
* Use screenshots/logs to document behavior

## Test Execution Schedule

* Run all unit/integration tests locally before PR
* GitHub Actions CI runs tests on all pushes to main
* Coverage reports reviewed before merge
* Postman collection executed before marking stories Done


## 📏 Test Artifacts


* [ ] `tests/test_complete_task.py`
* [ ] `tests/test_delete_task.py`
* [ ] `tests/test_error_handling.py`
* [ ] `tests/test_task_storage.py`
* [ ] Postman collection (`docs/postman/sprint2_collection.json`)
* [ ] API Documentation updated with error responses
* [ ] Updated Test Plan `docs/test_documentation/s2_test_plan.md`)
* [ ] Updated Test Cases (`docs/test_documentation/s2_test_cases.md`)
* [ ] Test Report (`docs/test_documentation/s2_test_report.md`)
* [ ] Updated `.github/workflows/python-app.yml`: CI updates (if modified)
* [ ] * `tests/test_blueprint.py` or add to `test_tasks.py`

---

## ✍️ Approvals

> **Note:** Approvals are not required in this course but reflect industry QA review processes.

| Role                 | Name | Signature / Date |
| -------------------- | ---- | ---------------- |
| Product Owner        |      |                  |
| QA Lead / Instructor |      |                  |
| Developer            |      |                  |

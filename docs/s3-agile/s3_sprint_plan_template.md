# 🔧 Sprint 3 Focus: Object-Oriented Refactor and Automated Integration Testing

In **Sprint 3**, we begin a major evolution of our Task Tracker application by applying **Software Design** and **Testing Best Practices**. This sprint focuses on two foundational improvements:

1. **Refactor to Object-Oriented Architecture**

    We will refactor our procedural Flask code to use **Object-Oriented Programming (OOP)** by introducing a new `TaskService` class. This class will:

    * Encapsulate **all task-related operations** (add, retrieve, complete, delete)
    * Serve as a **service layer** between the API routes and the persistence layer (our JSON file)
    * Prepare the codebase for future enhancements like **database integration**, **validation logic**, or **business rules**

    Although we will continue using the JSON file for task persistence, the application logic will now be centralized in a reusable class that improves:

    * 🔄 **Modularity** – logic separated from routes
    * 🧪 **Testability** – methods can now be unit tested
    * 🚀 **Maintainability and Extensibility** – easier to adapt in future sprints (e.g., database swap, CLI/Web UI reuse)

    This step mirrors professional refactoring workflows that improve architecture without changing outward-facing behavior.

2. **Automated Integration Testing with `requests`**

    We will replace our earlier **manual Postman or `curl` tests** with **automated integration tests** using Python’s `requests` library. These tests:

    * Interact with the **real Flask server** over HTTP (just like a user or frontend app would)
    * Verify the **end-to-end behavior** of the API (POST, GET, PUT, DELETE)
    * Are **scripted and repeatable**, and can be included in CI pipelines (e.g., GitHub Actions)

    This ensures we catch regressions early and confirms that our new service layer and API routes work together correctly.

    By combining **OOP refactoring** with **automated integration testing**, Sprint 3 significantly boosts the quality, structure, and test coverage of the Task Tracker project.

## 🧭 Educational Context

Why this sprint matters:

* Introduces **Object-Oriented Programming (OOP)** to centralize task logic in a `TaskService` class.
* Emphasizes testability and reusability through class-based design.
* Begins decoupling storage from logic to support swapping the JSON file for a database in Sprint 4.
* Teaches how to write **automated API tests** using `requests`, moving away from manual tools like Postman and curl.
* Keeps CLI available for transitional manual testing—but it will be deprecated in Sprint 4.
* Reinforces single responsibility and modular design to support growing complexity.

> This is a foundational architecture sprint that enables database integration, web UI development, and automated system testing in future sprints.

## Sprint Goals Overview

Sprint 3 focuses on preparing the application for future growth by transitioning from procedural design to object-oriented architecture. The goals for this sprint are reflected in the Refactor IDs (RF00X) below and include:

* Introduce `TaskService` to encapsulate task logic
* Implement `TaskRepository` interface to decouple persistence
* Modularize route logic with Flask Blueprints
* Use dependency injection via `create_app()` for wiring services
* Replace test cases with automated API tests using `requests` (US035)

## User Stories

* ✅ **US011 – Persist Tasks**: Already implemented (Sprint 2, supports refactor)
* ✅ **US027 – View Task Report (CLI)**: Supports CLI-to-UI migration in Sprint 4
* ✅ **US028 – CLI Logic (Add/View/Quit)**: Fully implemented
* 🆕 **US029 – CLI UI: Mark Task Complete**
  * Implemented in CLI and will later be deprecated when UI is available
* 🆕 **US035 – API Testing Automation (requests)**
  * Replace Postman/manual API tests with Python `requests`-based automation

## Summary of Refactors

| Refactor ID | Description                                               | Notes                                                                 |
|-------------|-----------------------------------------------------------|-----------------------------------------------------------------------|
| RF004       | Introduce `Task` class                                    | Replace dictionary-based task model                                   |
| RF005       | Create `TaskService` class                                | Encapsulates all logic for add/view/edit/delete                       |
| RF006A      | Create `TaskStorage` wrapper for DI                       | Enables `load_tasks`/`save_tasks` injection into services             |
| RF006B      | Inject `TaskService` via `__init__.py`                    | Passes service instance into Flask app context for route access       |
| RF006C      | Refactor `routes/tasks.py` to use `current_app.task_service` | Updates route handlers for DI-based architecture                  |
| RF008       | Introduce `MockTaskService` for test isolation            | Replaces file storage in tests for fast, isolated test behavior       |

## Testing & Automation

* Unit tests for `Task`, `TaskService`, and route handlers using `pytest`
* Create `tests/api/test_requests_api.py` for API validation
* Continue using `conftest.py` for test setup and cleanup
* CLI testing will not be expanded — web UI and BDD to replace in Sprint 4+

## 5. CI/CD Updates

* Add `requests`-based API tests to GitHub Actions CI pipeline
* Track code coverage for service and route layers

## 6. Technical Design & Architecture

* **Task Model Class:** Implement a `Task` class to represent a task object with attributes and behavior. (RF004)
* **Service Layer:** Introduce a `TaskService` class to handle business logic (add, retrieve, complete, delete tasks). (RF005)
* **Dependency Injection (DI):**
  - RF006A: Add a `TaskStorage` class that wraps file storage methods.
  - RF006B: Inject `TaskService` in `__init__.py` using `TaskStorage`.
  - RF006C: Refactor route handlers to use `current_app.task_service`.
* **Modularization:** Separate business logic and data access from route files.
* **Blueprints:** Continue building with Flask Blueprints for routes. (RF007)
* **Testing Architecture:** Use `MockTaskService` and `requests` to isolate and automate API testing. (RF008)

## Epic-Level Acceptance Criteria (Sprint 3)

* [ ] A `TaskService` class exists and is used by the API to handle all task operations. (RF005)
* [ ] A `TaskStorage` wrapper class is used to encapsulate file operations. (RF006A)
* [ ] The Flask app injects `TaskService` using DI in `__init__.py`. (RF006B)
* [ ] All route logic for tasks (`/api/tasks`) uses `current_app.task_service`. (RF006C)
* [ ] The `Task` object model is used throughout service and test logic. (RF004)
* [ ] Manual CLI testing remains available for students to verify core logic. (US029)
* [ ] Automated API tests using the `requests` library are implemented and pass. (RF008 / US035)
* [ ] All previously completed tasks are still functional and tested.
* [ ] A persistent storage interface is abstracted and ready for database swap in Sprint 4.

## 8. Risk Management

* **Refactor Complexity**: Risk of breaking working features during OOP refactor. *Mitigation:* Use TDD, refactor incrementally, and validate with tests.
* **Test Breakage**: Existing tests may fail due to interface changes. *Mitigation:* Update tests alongside implementation; maintain old behavior as needed.
  
## 9. Documentation Plan

* **README**: Add OOP and service explanations
* **API Documentation**: Review and update endpoint descriptions and structures
* **Design Docs**: Add `docs/architecture.md` to describe Task and Service classes
* **Test Plan/Test Cases**: Update based on new architecture
* **Sprint Report**: Document refactoring results and design improvements

## 10. Collaboration & Communication

* Use GitHub Project Board to track task progress
* Link issues to Key Tasks for visibility and tracking
* Create detailed pull request descriptions summarizing architecture changes
* Share CI build results and test coverage metrics with the team

## ✅ Sprint-Level Definition of Done (DoD)

Each User Story or Refactor is only considered **Done** when:

* [ ] All features are implemented and tested (unit and integration)
* [ ] Architecture uses `TaskService` and `TaskStorage` (DI pattern established)
* [ ] CLI feature (US029) supports marking tasks complete using `TaskService`
* [ ] CLI persists to `tasks.json` via `TaskService` and injected `TaskStorage`
* [ ] Flask app injects `TaskService` into `current_app` (RF006B)
* [ ] Routes use `current_app.task_service` (RF006C) instead of direct calls
* [ ] Automated API tests using `requests` are created and pass (US035, RF008)
* [ ] Test coverage remains ≥ 80%
* [ ] All changes committed with meaningful messages
* [ ] API Reference and README are updated to reflect new architecture

---


## 📦 Sprint Deliverables

| Deliverable                      | Location                                 |
| -------------------------------- | ---------------------------------------- |
| `TaskService` class              | `app/services/task_manager.py`           |
| `TaskStorage` wrapper class      | `app/services/task_storage.py`           |
| `__init__.py` with service injection | `app/__init__.py`                    |
| Updated route logic (DI usage)   | `app/routes/tasks.py`                    |
| CLI updated to use service       | `app/cli/cli_app.py`                     |
| End-to-end API tests (`requests`)| `tests/api/test_tasks_api.py`            |
| `MockTaskService` class          | `tests/mocks/mock_task_service.py`       |

📌 **Deprecation Notice**: The CLI will be deprecated in **Sprint 4**, once the Flask-based web UI is introduced. All future work will target web interaction and BDD/UI automation.

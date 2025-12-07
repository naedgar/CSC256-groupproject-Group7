# Sprint 3 Sprint Plan

## Sprint Goal
Transition the application to an object-oriented architecture using TaskService, implement dependency injection, enable JSON file persistence, and replace manual API testing with automated requests-based testing.

---

## In Scope
- Introduce Task class (RF004)
- Implement TaskService (RF005)
- Implement FileTaskRepository (PR6)
- Inject service via create_app() (RF006B)
- Refactor routes to use current_app.task_service (RF006C)
- Enable PUT and DELETE endpoints (PR7)
- Implement automated API testing using requests (PR8)
- Maintain CLI with complete/delete support

---

## Out of Scope
- Database persistence
- Web UI
- Robot Framework / BDD
- Authentication

---

## Tools
- Flask
- pytest
- requests
- GitHub Actions
- JSON file storage

---

## Acceptance Criteria
- All task operations use TaskService
- Tasks persist to tasks.json
- PUT and DELETE endpoints function correctly
- Automated requests tests pass
- CLI supports task completion and deletion

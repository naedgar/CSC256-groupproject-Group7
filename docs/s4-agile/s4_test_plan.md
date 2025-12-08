# 🧪 Sprint 4 Test Plan – Final Group Project

**Course:** CSC-256  
**Project:** TaskTracker – Group Project  
**Sprint:** 4 (Final Sprint)  

---

## 1. 🎯 Test Plan Objective

The objective of this Test Plan is to verify that all **Sprint 4 (final sprint)** features, user stories, and project requirements are fully implemented, validated, and stable for final submission and presentation. This includes full regression testing, validation of external API integration, enforcement of hybrid test organization, and verification of all CI and Robot Framework workflows.

This Test Plan directly supports:
- **US031:** Show Current Time via External API  
- **US039:** View Time Created in Task Summary  
- **US0XX:** Hybrid Test Organization with pytest Markers  
- **PR1–PR10:** All final Group Project requirements

---

## 2. 📌 In Scope

- All Task API endpoints:
  - `GET /api/tasks`
  - `POST /api/tasks`
  - `PUT /api/tasks/<id>`
  - `DELETE /api/tasks/<id>`
- Time Service API:
  - `GET /api/time`
- Health endpoint:
  - `GET /api/health`
- Centralized validation in `TaskService` (PR-5)
- Task creation timestamp feature (`createdAt`) – US039
- External Time API integration – US031
- Hybrid test organization using pytest markers – US0XX
- Full regression testing – PR-7
- Robot Framework acceptance tests – PR-8
- CI workflow execution and verification – PR-2

---

## 3. ⛔ Out of Scope

- New feature development beyond US031, US039, and US0XX
- Architectural refactors
- Database or ORM migrations
- UI redesign beyond validation and display confirmation

---

## 4. 🧰 Tools & Test Environment

- **Backend:** Python, Flask
- **Services:** TaskService, TimeService
- **Storage:** JSON persistence (`data/tasks.json`)
- **Testing Tools:**
  - pytest
  - pytest-cov
  - pytest markers (`unit`, `integration`, `e2e`)
  - Playwright or Selenium (UI tests)
  - Robot Framework (acceptance tests)
- **CI/CD:** GitHub Actions
- **External API:** WorldTimeAPI (or equivalent)
- **Test Environment:** Localhost (`http://localhost:5000`) and GitHub CI runners

---

## 5. 🧪 Test Strategy

Testing in Sprint 4 follows a **layered and hybrid strategy**:

- **Unit Testing:**  
  Focus on isolated business logic and validation in `TaskService` and `TimeService`.

- **Integration Testing:**  
  Verify API endpoints, service integration, and JSON persistence.

- **End-to-End (E2E) / UI Testing:**  
  Validate real user interactions and UI behavior using browser automation.

- **Acceptance Testing (Robot Framework):**  
  Validate critical user journeys across the full application stack.

- **Regression Testing:**  
  Ensure all previously implemented features continue to function correctly.

---

## 6. 🧱 Test Levels & Coverage

### 6.1 Unit Tests (`@pytest.mark.unit`)
- Task creation with valid input
- Task validation (empty, whitespace, duplicate titles)
- Task completion logic
- Timestamp generation (`createdAt`) – US039
- TimeService response parsing – US031
- TimeService fallback behavior on API failure – US031

### 6.2 Integration Tests (`@pytest.mark.integration`)
- `POST /api/tasks` – valid and invalid inputs
- `GET /api/tasks` – empty and populated lists
- `PUT /api/tasks/<id>` – valid and invalid IDs
- `DELETE /api/tasks/<id>` – valid and invalid IDs
- `GET /api/time` – successful external API call
- `GET /api/time` – simulated API failure handling

### 6.3 End-to-End / UI Tests (`@pytest.mark.e2e`)
- Add a task through the UI and verify it appears in Task Summary
- Verify task creation timestamp is visible in the UI – US039
- View current time from the Time Service in the UI – US031
- Attempt invalid task submission and verify validation messages
- Mark task complete and verify state update in UI

### 6.4 Acceptance Tests (Robot Framework)
- Add Task (happy path)
- Invalid Task Input Handling
- Mark Task Complete
- Delete Task
- Verify Time Display – US031
- Verify Timestamp Display – US039

---

## 7. 🧪 Hybrid Test Organization – US0XX (PR-3)

Sprint 4 enforces a **Hybrid Test Organization model**:

- Tests are organized by **concern-based folders**:
  - `tests/api`
  - `tests/service`
  - `tests/storage`
  - `tests/ui`
  - `tests/robot`
- Tests are executed by **pytest markers**:
  - `unit`
  - `integration`
  - `e2e`

The following commands are validated as part of Sprint 4:
```bash
pytest -m unit
pytest -m integration
pytest -m e2e

# 🧪 Sprint 4 Test Plan – Final Group Project 

**Course:** CSC-256  
**Project:** TaskTracker – Group Project  
**Sprint:** 4 (Final Sprint)  

---

## 1. 🎯 Test Plan Objective

The objective of this Test Plan is to verify that all **final Group Project features delivered through PR-1 to PR-10** are fully implemented, validated, and production-ready for submission and presentation. This includes:

- Full regression testing across all APIs
- External Time API validation
- Task timestamp (`createdAt`) verification
- Centralized validation enforcement
- Hybrid test organization using pytest markers
- Robot Framework acceptance test execution
- CI workflow validation across all test layers

This Test Plan directly supports the following **final Group User Stories**:

- **US031** – Show Current Time via External API  
- **US039** – View Time Created in Task Summary  
- **US041** – Hybrid Test Organization with pytest Markers  
- **US042** – Automated TimeService Testing (API + UI)  
- **US043** – Centralized Task Validation (Service Layer + Schemas)  

---

## 2. 📌 In Scope (PR-Aligned)

### ✅ Core API Coverage (PR-1, PR-7)

- `GET /api/tasks`
- `POST /api/tasks`
- `PUT /api/tasks/<id>`
- `DELETE /api/tasks/<id>`

### ✅ Time Service (PR-4, PR-6)

- `GET /api/time`
- External API integration (WorldTimeAPI or equivalent)
- API failure handling and fallback behavior

### ✅ Health Endpoint (PR-1)

- `GET /api/health`

### ✅ Centralized Validation (PR-5)

- All validation enforced at:
  - `TaskService`
  - Shared validation schemas
- Applied consistently to:
  - API
  - CLI
  - UI

### ✅ Timestamp Support (PR-6)

- `createdAt` field automatically assigned at task creation
- Timestamp visible in Task Summary UI – **US039**

### ✅ Hybrid Test Organization (PR-3, PR-7)

- pytest folder structure by concern
- pytest markers by test scope – **US041**

### ✅ Full Regression Testing (PR-7)

- Re-validation of all previously delivered features and user stories

### ✅ Robot Framework Acceptance Tests (PR-8)

- Full end-to-end task workflow validation

### ✅ CI Workflow Verification (PR-2, PR-7)

- Automated execution of:
  - unit
  - integration
  - e2e
  - robot tests

---

## 3. ⛔ Out of Scope

- New feature development beyond US031, US039, US041, US042, and US043
- Major architectural refactors
- Database or ORM migrations
- UI redesign beyond validation and display of time/timestamps

---

## 4. 🧰 Tools & Test Environment

- **Backend:** Python, Flask  
- **Services:** `TaskService`, `TimeService`  
- **Storage:** JSON persistence (`data/tasks.json`)  

**Testing Tools:**

- `pytest`
- `pytest-cov`
- `pytest` markers (`unit`, `integration`, `e2e`)
- Playwright or Selenium (UI tests)
- Robot Framework (acceptance tests)

**CI/CD:**

- GitHub Actions (runs all test stages and enforces pass/fail)

**External API:**

- WorldTimeAPI (or equivalent time service)

**Test Environments:**

- Local development: `http://localhost:5000`
- GitHub Actions CI runners

---

## 5. 🧪 Test Strategy

Sprint 4 uses a **hybrid, layered testing strategy**:

- **Unit Testing (Service & Validation Focus)**  
  Validate isolated business logic in `TaskService` and `TimeService`, and all centralized validation rules.

- **Integration Testing (API + Persistence)**  
  Verify route behavior, service integration, and JSON persistence (`data/tasks.json`).

- **End-to-End / UI Testing**  
  Validate real user workflows and UI behavior using browser automation tools.

- **Acceptance Testing (Robot Framework)**  
  Validate critical user journeys across the full stack, from UI down to persistence.

- **Regression Testing**  
  Ensure all previously implemented features from earlier sprints and PRs still function correctly after Sprint 4 changes.

---

## 6. 🧱 Test Levels & Coverage

### 6.1 Unit Tests – `@pytest.mark.unit`  
*(Primarily PR-3, PR-5, PR-6)*

**Scope:**

- Task creation with valid input
- Task validation rules:
  - Empty or whitespace-only titles
  - Missing required fields
  - Any centralized schema validation in `TaskService` – **US043**
- Task completion logic
- Timestamp generation (`createdAt`) on task creation – **US039**
- `TimeService` response parsing – **US031**
- `TimeService` fallback behavior on external API failure – **US042**

**Goals:**

- High confidence in business logic correctness
- Fast feedback cycle for developers
- All validation rules enforced in one place (centralized validation)

---

### 6.2 Integration Tests – `@pytest.mark.integration`  
*(Primarily PR-4, PR-6, PR-7)*

**Scope:**

- `POST /api/tasks`  
  - Valid payload → 201 Created  
  - Invalid payload (missing/empty title, bad data) → 400 with JSON error
- `GET /api/tasks`  
  - Empty list → `[]`  
  - Populated list → array of task objects with `id`, `title`, `completed`, `createdAt`
- `PUT /api/tasks/<id>`  
  - Valid ID → update task, return 200  
  - Invalid/nonexistent ID → 404 with JSON error
- `DELETE /api/tasks/<id>`  
  - Valid ID → 204 No Content  
  - Invalid/nonexistent ID → 404
- `GET /api/time` – **US031 / US042**  
  - Successful external API call → current time returned as JSON  
  - Simulated failure (mocked) → graceful fallback or error response as defined

**Goals:**

- Verify full request/response cycles
- Confirm `TaskService` and `TimeService` integrate correctly with Flask routes
- Ensure JSON file (`data/tasks.json`) is updated correctly for add/edit/delete

---

### 6.3 End-to-End / UI Tests – `@pytest.mark.e2e`  
*(Primarily PR-6, PR-7)*

**Scope:**

- Add task via Web UI
  - Verify new task appears in Task Summary
  - Verify `createdAt` timestamp is shown – **US039**
- View current time via TimeService in Web UI
  - Verify displayed time matches API result – **US031 / US042**
- Submit invalid task form (e.g., empty title)
  - Verify validation message appears (centralized validation rules surfaced in UI) – **US043**
- Mark task complete via UI
  - Verify UI shows completed state
  - Verify API data updated (`completed: true`)
- Delete task via UI
  - Verify it no longer appears in the list
  - Confirm with `GET /api/tasks` result

**Goals:**

- Ensure UI and API are consistent
- Validate user journeys used in the final presentation
- Confirm that timestamp and time display are visible and correct

---

### 6.4 Acceptance Tests – Robot Framework  
*(PR-8)*

**Robot Framework Suites Validate:**

- Add Task End-to-End
- Handle Invalid Task Input
- Mark Task Complete
- Delete Task
- Verify Time Display in UI – **US031 / US042**
- Verify Task `createdAt` Timestamp in UI – **US039**

**Goals:**

- High-level, scenario-based validation
- Demonstrate BDD-style acceptance coverage for final grading and presentation

---

## 7. 🧪 Hybrid Test Organization – US041 (PR-3, PR-7)

Sprint 4 enforces a **Hybrid Test Organization** pattern so that tests are easy to navigate and run by concern and by scope.

### 7.1 Folder Structure

```bash
tests/
├── api/        
├── service/    
├── storage/    
├── ui/         
├── robot/      

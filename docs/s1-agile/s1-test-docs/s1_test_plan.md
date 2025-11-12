# 🍪 Sprint 1 Test Plan – Group Project Edition  

Understand that while *In-Scope Functionality* defines **what features are being tested**, the *Test Objectives* clarify **why** each feature is tested and **how success is measured**.  
Including both ensures a complete plan aligned to both development goals and QA validation.

---

## 📝 Purpose  

This plan documents the validation of the **migrated TaskTracker Group Project environment**, its new **hybrid testing framework**, and updated functional requirements from the following User Stories:

- US0XX – Hybrid pytest Organization  
- US0XX – Centralized Task Validation  
- US0XX – Automated TimeService Testing  
- US0XX – Robot Framework Acceptance Suite  
- US0XX – Team-selected feature (from `group_projects_choice.md`)

The plan outlines both automated and manual testing strategies with a focus on:

- Establishing **pytest markers** and concern-based test folders  
- Refactoring and validating **TaskService input rules**  
- Verifying **TimeService** output via Playwright/Selenium  
- Introducing **Robot Framework** acceptance testing and lab documentation  
- Maintaining continuous integration through **GitHub Actions**  
- Ensuring regression of existing endpoints from individual projects  

Manual verification will supplement automated coverage for UI and Robot flows; screenshots or logs are stored in `/tests/screenshots/`.

---

## 📅 Sprint Information  

* **Sprint:** 1 – Agile Documentation & Hybrid Testing Setup  
* **Iteration Dates:** YYYY-MM-DD → YYYY-MM-DD  
* **Version Under Test:** `main` branch in Group Repo  
* **Prepared by:** [Your Name]  
* **Last Updated:** YYYY-MM-DD  

---

## 🎯 Test Objectives  

| ID | Objective | Success Metric |
|----|------------|----------------|
| OBJ-1 | Verify hybrid pytest organization and markers function as intended | `pytest -m unit`, `-m integration`, `-m e2e` run only targeted tests successfully |
| OBJ-2 | Validate centralized Task validation logic in `TaskService` | Invalid or duplicate titles return 400 with error JSON; valid tasks pass |
| OBJ-3 | Confirm TimeService automated tests update and display current time correctly | UI and API tests pass across browsers |
| OBJ-4 | Execute Robot Framework acceptance tests for core flows | All Robot cases (log.html/report.html) show Pass |
| OBJ-5 | Maintain CI pipeline stability | All pytest + Robot workflows green in GitHub Actions |

---

## 📎 In-Scope Functionality by User Story  

### US001 – Hybrid pytest Organization  
- Concern-based folder structure (`tests/api`, `tests/service`, `tests/ui`)  
- Markers: `unit`, `integration`, `e2e`

### US002 – Centralize Task Validation  
- All validation moved to `TaskService` and `schemas.py`  
- Same rules for API and UI inputs  
- Edge tests for empty, too-long, duplicate titles  

### US003 – Automated TimeService Testing  
- Validate `/api/time` endpoint and browser display  
- Check time format (HH:MM[:SS]) and auto-update  

### US004 – Robot Framework Acceptance Suite  
- Covers Add, List, Delete Tasks and TimeService  
- Generates artifacts (`log.html`, `report.html`)  
- Taught through Robot Framework Lab  

### US005 – Team Choice Feature  
- Feature as defined in `group_projects_choice.md`  
- Corresponding unit, integration, and Robot tests  

---

## 🧩 Test Types  

| Type | Description |
|------|--------------|
| Unit Tests | Validate functions and service logic in isolation |
| Integration/API Tests | Use Flask test client to verify endpoints and DB interactions |
| UI/E2E Tests | Playwright or Selenium browser tests for TimeService |
| Acceptance Tests | Robot Framework behavioral flows |
| Edge Tests | Boundary cases for title length, duplicates, etc. |
| CI Tests | Workflows validate build and test status on each push |
| Manual Tests | Optional visual validation for UI and Robot lab steps |

---

## 🛠️ Testing Tools  

| Tool | Purpose |
|------|-----------|
| `pytest` | Core test framework |
| `pytest-cov` | Coverage tracking |
| `Flask Test Client` | Simulate HTTP requests |
| `Playwright` / `Selenium` | Automate UI flows (TimeService) |
| `Robot Framework` | Acceptance tests + lab |
| `GitHub Actions` | CI/CD automation |
| `Postman` | Manual API validation |
| `MS Teams` | Defect and status communication |

---

## ⚙️ Test Environment Setup  

* **OS:** Ubuntu runner (CI) and local Windows/macOS dev machines  
* **Python:** 3.11 (required for course CI)  
* **Dependencies:** Installed via `requirements.txt`  
* **Virtual Env:** `.venv` per developer  
* **App Start:** `flask --app app run` (local only)  
* **Run Tests:**  
  ```bash
  pytest -v --cov=app

# Sprint 1: Test Cases (Group Project – TaskTracker)

These test cases verify that new features introduced in the **Group Project Sprint 1** function correctly and do not break existing functionality from the individual project.

Each test case includes:
- **Test Case ID**
- **Description**
- **Preconditions**
- **Test Steps**
- **Expected Results**
- **Test Type** (Automated, Manual, or Both)

This document maps each case to a user story listed in `tt_user_stories.md`.

* **US001** – Hybrid pytest Organization  
* **US002** – Centralized Task Validation  
* **US003** – Automated TimeService Testing  
* **US004** – Robot Framework Acceptance Suite  
* **US005** – Team-Selected Feature  

> [!NOTE]
> Clearly labeling **Test Type** prepares teams for real-world QA and CI/CD workflows, showing which cases should remain manual and which are automated for continuous validation.

---

## US001 – Hybrid pytest Organization

### 🧪 TC-US001-001: Verify pytest markers execute by scope
* **Description:** Ensure pytest markers (`unit`, `integration`, `e2e`) correctly filter and run only targeted test scopes.
* **Test Type:** Automated  
* **Preconditions:**
  - `pytest.ini` configured with `unit`, `integration`, and `e2e` markers.
  - Concern-based folder structure exists under `/tests/`.
* **Test Steps:**
  1. Run `pytest -m unit`
  2. Run `pytest -m integration`
  3. Run `pytest -m e2e`
* **Expected Result:**
  - Each command runs only its associated test files.
  - No unrelated tests are executed.
* **Status:** ☐ Pass ☐ Fail

---

## US002 – Centralized Task Validation

### 🧪 TC-US002-001: Reject Empty Task Title
* **Description:** Verify that `TaskService` rejects creation of a task with an empty or whitespace-only title.
* **Test Type:** Automated  
* **Preconditions:** Centralized validation implemented in `TaskService` and `schemas.py`.
* **Test Steps:**
  1. POST `/api/tasks` with body:
     ```json
     { "title": " " }
     ```
  2. Observe response.
* **Expected Result:**
  - HTTP 400 Bad Request  
  - JSON error message: `"title required"`
* **Status:** ☐ Pass ☐ Fail

### 🧪 TC-US002-002: Enforce Title Length Limit
* **Description:** Ensure tasks cannot exceed maximum length (e.g., 100 chars).
* **Test Type:** Automated  
* **Preconditions:** API is running with validation active.
* **Test Steps:**
  1. POST `/api/tasks` with 256-character title.
* **Expected Result:**
  - HTTP 400 Bad Request  
  - JSON error message: `"title too long"`
* **Status:** ☐ Pass ☐ Fail

### 🧪 TC-US002-003: Reject Duplicate Title
* **Description:** Prevent duplicate task titles using shared validation logic.
* **Test Type:** Automated  
* **Preconditions:** A task with title “Buy milk” already exists.
* **Test Steps:**
  1. POST `/api/tasks` with:
     ```json
     { "title": "Buy milk" }
     ```
* **Expected Result:**
  - HTTP 400 Bad Request  
  - JSON error message: `"Duplicate task"`
* **Status:** ☐ Pass ☐ Fail

---

## US003 – Automated TimeService Testing

### 🧪 TC-US003-001: Validate TimeService API
* **Description:** Verify `/api/time` endpoint returns correct time format and status code.
* **Test Type:** Automated  
* **Preconditions:** App running with `/api/time` implemented.
* **Test Steps:**
  1. Send `GET /api/time`.
* **Expected Result:**
  - HTTP 200 OK  
  - JSON includes fields such as `datetime`, `timezone`.
* **Status:** ☐ Pass ☐ Fail

### 🧪 TC-US003-002: Verify Time Updates in UI
* **Description:** Ensure displayed time on the web page updates automatically.
* **Test Type:** Automated (UI / Playwright)  
* **Preconditions:** Web UI running locally or in CI.
* **Test Steps:**
  1. Launch browser.  
  2. Observe TimeService element on home page.  
  3. Wait 5 seconds and check that time value changes.  
* **Expected Result:**  
  - Time displayed updates within 5 seconds.  
  - Format matches `HH:MM[:SS]`.  
* **Status:** ☐ Pass ☐ Fail

---

## US004 – Robot Framework Acceptance Suite

### 🧪 TC-US004-001: Add Task via Robot Framework
* **Description:** Simulate user adding a task through the web interface using Robot Framework.
* **Test Type:** Automated (Robot)  
* **Preconditions:** Robot suite configured with working URL.  
* **Test Steps:**
  1. Run Robot suite `robot tests/robot/add_task.robot`.
* **Expected Result:**
  - All keywords execute successfully.  
  - `log.html` and `report.html` show Pass.  
* **Status:** ☐ Pass ☐ Fail

### 🧪 TC-US004-002: Delete Task via Robot Framework
* **Description:** Confirm a task can be deleted and no longer appears in the list.
* **Test Type:** Automated (Robot)  
* **Preconditions:** At least one task exists.  
* **Test Steps:**
  1. Run `robot tests/robot/delete_task.robot`.
* **Expected Result:**
  - Task removed successfully.  
  - Robot results = Pass.  
* **Status:** ☐ Pass ☐ Fail

---

## US005 – Team-Selected Feature (Custom)

### 🧪 TC-US005-001: Validate Custom Feature Behavior
* **Description:** Verify team-selected feature works as defined in `group_projects_choice.md`.
* **Test Type:** Automated / Manual (as applicable)  
* **Preconditions:** Feature implemented and accessible.  
* **Test Steps:**  
  1. Execute test steps defined in related user story.  
* **Expected Result:**  
  - Matches acceptance criteria in `tt_user_stories.md`.  
* **Status:** ☐ Pass ☐ Fail

---

## US006 – Regression Verification

### 🧪 TC-US006-001: Ensure All Existing Tests Still Pass
* **Description:** Run full regression suite from individual project to confirm no previous features broke.
* **Test Type:** Automated  
* **Preconditions:** Legacy tests integrated into current repo.  
* **Test Steps:**  
  1. Run all pytest tests without markers:  
     ```bash
     pytest -v
     ```
* **Expected Result:**  
  - All legacy tests report Passed.  
* **Status:** ☐ Pass ☐ Fail

---

# Sprint 1: Test Cases (Group Project – TaskTracker)

These test cases verify that core features introduced in **Sprint 1 (PR-1)** function correctly and do not break the basic functionality of the TaskTracker application.

Each test case includes:
- **Test Case ID**
- **Description**
- **Preconditions**
- **Test Steps**
- **Expected Results**
- **Test Type** (Automated or Manual)

This document maps each case to a user story listed in `tt_user_stories.md`.

* **US001** – Health Check Endpoint  
* **US002** – Add Task via API  
* **US003** – View Tasks (List)  
* **US004** – Add Task via CLI (Stub)  

---

## ✅ US001 – Health Check Endpoint

### 🧪 TC-US001-001: Verify Health Endpoint Returns OK
* **Description:** Ensure the API health endpoint returns a success response.
* **Test Type:** Automated  
* **Preconditions:** Flask app is running.
* **Test Steps:**
  1. Send `GET /api/health`
* **Expected Result:**
  - HTTP 200 OK  
  - JSON response: `{ "status": "ok" }`
* **Status:** ✅ Pass  

---

## ✅ US002 – Add Task via API

### 🧪 TC-US002-001: Add Valid Task
* **Description:** Verify a task can be successfully added with a valid title.
* **Test Type:** Automated  
* **Preconditions:** API running, task list empty.
* **Test Steps:**
  1. Send `POST /api/tasks` with:
     ```json
     { "title": "Buy groceries" }
     ```
* **Expected Result:**
  - HTTP 201 Created  
  - JSON includes `id`, `title`, and `completed = false`
* **Status:** ✅ Pass  

---

### 🧪 TC-US002-002: Reject Empty Title
* **Description:** Ensure task cannot be created with empty title.
* **Test Type:** Automated  
* **Preconditions:** API running.
* **Test Steps:**
  1. Send `POST /api/tasks` with:
     ```json
     { "title": "" }
     ```
* **Expected Result:**
  - HTTP 400 Bad Request  
  - Error message returned
* **Status:** ✅ Pass  

---

### 🧪 TC-US002-003: Reject Missing Title
* **Description:** Ensure task cannot be created without a title.
* **Test Type:** Automated  
* **Preconditions:** API running.
* **Test Steps:**
  1. Send `POST /api/tasks` with:
     ```json
     { "description": "No title" }
     ```
* **Expected Result:**
  - HTTP 400 Bad Request  
  - Error message returned
* **Status:** ✅ Pass  

---

## ✅ US003 – View Tasks

### 🧪 TC-US003-001: View Empty Task List
* **Description:** Ensure API returns empty list when no tasks exist.
* **Test Type:** Automated  
* **Preconditions:** No tasks added.
* **Test Steps:**
  1. Send `GET /api/tasks`
* **Expected Result:**
  - HTTP 200 OK  
  - Response body: `[]`
* **Status:** ✅ Pass  

---

### 🧪 TC-US003-002: View Task List After Add
* **Description:** Ensure tasks appear after being added.
* **Test Type:** Automated  
* **Preconditions:** One task exists.
* **Test Steps:**
  1. Add a task  
  2. Send `GET /api/tasks`
* **Expected Result:**
  - List includes created task
* **Status:** ✅ Pass  

---

## ✅ US004 – Add Task via CLI (Stub)

### 🧪 TC-US004-001: Add Task Using CLI
* **Description:** Verify task can be added manually using CLI.
* **Test Type:** Manual  
* **Preconditions:** `cli_app.py` is available.
* **Test Steps:**
  1. Run:
     ```bash
     python -m app.cli.cli_app
     ```
  2. Select Add Task
  3. Enter:
     - Title: `CLI Task`
     - Description: `Test task`
* **Expected Result:**
  - Task added successfully  
  - Confirmation message shown
* **Status:** ✅ Pass  

---

### 🧪 TC-US004-002: View Tasks via CLI
* **Description:** Verify tasks added via CLI can be viewed.
* **Test Type:** Manual  
* **Preconditions:** At least one task exists.
* **Test Steps:**
  1. Run CLI  
  2. Select View Tasks
* **Expected Result:**
  - All tasks displayed correctly
* **Status:** ✅ Pass  

---

## ✅ Regression Test

### 🧪 TC-REG-001: Full Test Suite Passes
* **Description:** Ensure no existing tests fail after Sprint 1 changes.
* **Test Type:** Automated  
* **Preconditions:** All Sprint 1 tests written.
* **Test Steps:**
  ```bash
  pytest -v

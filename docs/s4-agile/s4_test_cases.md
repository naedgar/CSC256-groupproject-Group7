# 📋 Sprint 4 Test Cases – Final Group Project

This document lists the core regression test cases for Sprint 4, aligning with PR-7 and covering user stories US031, US039, and US0XX.

---

## ✅ Task Service & Validation (PR-5, PR-7)

**TC-001 – Add Valid Task**

- **Precondition:** API server running.
- **Steps:**  
  1. POST `/api/tasks` with `{"title": "Finish homework"}`.  
- **Expected Result:**  
  - 201 Created  
  - Response contains `id`, `title`, `completed: false`, `createdAt`.

---

**TC-002 – Add Task with Empty Title**

- **Steps:**  
  1. POST `/api/tasks` with `{"title": ""}`.  
- **Expected Result:**  
  - 400 Bad Request  
  - Error message: e.g., `"Title is required"`.

---

**TC-003 – Add Task with Whitespace Title**

- **Steps:**  
  1. POST `/api/tasks` with `{"title": "   "}`.  
- **Expected Result:**  
  - 400 Bad Request  
  - Error message indicating invalid/empty title.

---

**TC-004 – Add Duplicate Task Title**

- **Steps:**  
  1. POST `/api/tasks` with title `"Pay bills"`.  
  2. POST `/api/tasks` again with title `"Pay bills"`.  
- **Expected Result:**  
  - First request: 201 Created  
  - Second request: 400 Bad Request (duplicate).

---

**TC-005 – Get Tasks (Non-Empty)**

- **Steps:**  
  1. Ensure at least one task exists.  
  2. GET `/api/tasks`.  
- **Expected Result:**  
  - 200 OK  
  - JSON list of tasks with `createdAt` present for each.

---

**TC-006 – Mark Task Complete (Valid ID)**

- **Steps:**  
  1. Create a task.  
  2. PUT `/api/tasks/<id>` to mark as complete.  
- **Expected Result:**  
  - 200 OK  
  - JSON shows `"completed": true`.

---

**TC-007 – Mark Task Complete (Invalid ID)**

- **Steps:**  
  1. PUT `/api/tasks/9999`.  
- **Expected Result:**  
  - 404 Not Found  
  - Error message indicates missing task.

---

**TC-008 – Delete Task (Valid ID)**

- **Steps:**  
  1. Create a task.  
  2. DELETE `/api/tasks/<id>`.  
- **Expected Result:**  
  - 204 No Content.  

---

**TC-009 – Delete Task (Invalid ID)**

- **Steps:**  
  1. DELETE `/api/tasks/9999`.  
- **Expected Result:**  
  - 404 Not Found.

---

## 🕒 Time Service – US031 (PR-4, PR-7)

**TC-010 – Get Current Time (Happy Path)**

- **Steps:**  
  1. GET `/api/time`.  
- **Expected Result:**  
  - 200 OK  
  - JSON contains `datetime` and `timezone`.

---

**TC-011 – Time Service External API Failure**

- **Setup:** Configure or simulate TimeService failure (e.g., mock external call).  
- **Steps:**  
  1. GET `/api/time`.  
- **Expected Result:**  
  - 503 or 200 with error payload (depending on design).  
  - JSON error message like `"Time service unavailable"`.

---

## 🕓 Timestamp Feature – US039 (PR-6, PR-7)

**TC-012 – Task Creation Timestamp Stored**

- **Steps:**  
  1. POST `/api/tasks` with a valid title.  
- **Expected Result:**  
  - Response includes `createdAt` as ISO 8601 string.

---

**TC-013 – Task Summary Shows Timestamp (UI)**

- **Type:** E2E/UI test.  
- **Steps:**  
  1. Navigate to Task Summary page in browser.  
  2. Add a new task.  
- **Expected Result:**  
  - New task appears in list with human-readable creation time based on `createdAt`.

---

## 🧪 Hybrid Test Organization – US0XX (PR-3, PR-2, PR-7)

**TC-014 – Run Unit Tests via Marker**

- **Steps:**  
  1. Run `pytest -m unit`.  
- **Expected Result:**  
  - Only unit tests execute (e.g., service-layer tests).  
  - All pass.

---

**TC-015 – Run Integration Tests via Marker**

- **Steps:**  
  1. Run `pytest -m integration`.  
- **Expected Result:**  
  - Only integration tests execute (API + repository).  
  - All pass.

---

**TC-016 – Run E2E Tests via Marker**

- **Steps:**  
  1. Run `pytest -m e2e`.  
- **Expected Result:**  
  - Only E2E/UI/Robot-related tests execute.  
  - All pass.

---

## 🤖 Robot Framework – Acceptance Tests (PR-8)

**TC-017 – Robot: Add Valid Task**

- **Steps:**  
  1. Run Robot suite for “Add Task”.  
- **Expected Result:**  
  - Task is added, appears in UI or API verification step.

---

**TC-018 – Robot: Invalid Task Input**

- **Steps:**  
  1. Run Robot test for invalid task title (empty/whitespace).  
- **Expected Result:**  
  - Error message displayed; task not created.

---

**TC-019 – Robot: Complete & Delete Task Flow**

- **Steps:**  
  1. Run Robot end-to-end scenario (Create → Complete → Delete).  
- **Expected Result:**  
  - All actions succeed; final state as expected.

---

## 📊 CI Verification – Regression

**TC-020 – CI Pipelines Green**

- **Steps:**  
  1. Push changes / open PR.  
  2. Inspect GitHub Actions “Actions” tab.  
- **Expected Result:**  
  - Required workflows (unit/integration, E2E, Robot) show green for final run before submission.


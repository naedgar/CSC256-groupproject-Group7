# 🧪 Sprint 5 Test Cases

Sprint 5 focuses on final enhancements, edge-case validation, external API interaction, and robust end-to-end testing using Postman and Robot Framework. It includes exploratory testing, regression checks, and mock-based unit validation.

---

## ✅ Test Areas

* UI/UX edge case validation
* External API integration tests (Time API)
* Robot Framework acceptance tests
* Mock-based unit testing for external services
* Regression tests from Sprints 1–4
* Exploratory and cross-browser testing

---

## 🧩 UI/UX Edge Case Tests

> **Test Type:** Manual + Automated (Selenium / Playwright)

### 🧪 TC-UIEDGE-001: Add Task with Excessively Long Title

* **Description:** Attempt to add a task with a title >255 characters.
* **Expected Result:** Task rejected or validated with an error message.

### 🧪 TC-UIEDGE-002: Submit Task with Only Whitespace

* **Description:** Enter a task title consisting of only spaces.
* **Expected Result:** Task not added; validation error shown.

### 🧪 TC-UIEDGE-003: Navigate UI Without JavaScript Enabled

* **Description:** Use browser dev tools to disable JS.
* **Expected Result:** UI degrades gracefully or prompts user appropriately.

---

## 🔄 Regression & Exploratory Testing

> **Test Type:** Manual + Automated (CI + Browser)

### 🧪 TC-REGSPRINT5-001: Full Add/Edit/Delete Cycle

* **Description:** Simulate user flow of adding → editing → deleting task.
* **Expected Result:** Task is fully created, updated, and deleted correctly.

### 🧪 TC-REGSPRINT5-002: Multi-Browser Testing

* **Description:** Open app in Chrome, Firefox, and Edge.
* **Expected Result:** No visual or behavioral issues across browsers.

### 🧪 TC-REGSPRINT5-003: Data Persistence Check After Refresh

* **Description:** Add task, then refresh browser.
* **Expected Result:** Task remains visible; database is intact.

---

## 🌐Test Case Summary (Time API and UI)

| TC ID        | Description                                           | Tool            | Type                   |
| ------------ | ----------------------------------------------------- | --------------- | ---------------------- |
| TC-US031-001 | GET `/api/time` returns mocked time                   | requests/pytest | Integration (API)      |
| TC-US031-002 | GET `/api/time` returns real current time             | requests/pytest | Integration (API)      |
| TC-US031-003 | TimeService returns correct datetime string           | pytest          | Unit                   |
| TC-US031-004 | Handles API failure and returns fallback error        | pytest + mock   | Integration (Negative) |
| TC-US039-001 | Time shown in Task Report UI (mocked)                 | Playwright      | UI                     |
| TC-US039-002 | User sees current time in UI summary (mocked)         | Robot Framework | Acceptance             |
| TC-US039-003 | Inject MockTimeService for predictable test rendering | pytest          | Unit                   |


> **Test Type:** Unit + Integration + Acceptance (Postman + Robot + Mock)

## ✅ Time API Test Cases (`US031`)

### 🧪 TC-US031-001: API Time (Mocked)

**Title:** GET `/api/time` returns mocked time
**Description:** When using `MockTimeService`, the `/api/time` route should return a fixed, predictable response for testing.
**Preconditions:**

* Mock service is injected in test setup
* Flask test client is active
  **Steps:**

1. Send `GET /api/time`
2. Parse response JSON

**Expected Result:**

* Status: `200 OK`
* JSON contains predictable mock time fields (`datetime`, `timezone`, `abbreviation`)

**Test Type:** Automated (requests, mock)

---

### 🧪 TC-US031-002: API Time (Real)

**Title:** GET `/api/time` returns real time
**Description:** Validate `/api/time` works with the actual WorldTimeAPI service (when not mocked).
**Preconditions:**

* Internet access and no mocking
  **Steps:**

1. Send `GET /api/time`
2. Parse response

**Expected Result:**

* Status: `200 OK`
* JSON includes `datetime`, `timezone`, `abbreviation`

**Test Type:** Automated (requests)

---

### 🧪 TC-US031-003: API Fallback on Error

**Title:** Fallback if external API fails
**Description:** Simulate external API failure and confirm service fallback logic works
**Preconditions:**

* Inject mock or patch the external call to raise an exception
  **Steps:**

1. Call `/api/time`
2. Catch fallback response

**Expected Result:**

* Status: `503 Service Unavailable`
* JSON includes: `error: "Unable to retrieve time"`

**Test Type:** Integration (mock error path)

---

### 🧪 TC-US031-004: TimeService Unit – Parse Logic

**Title:** TimeService parses external response correctly
**Description:** Validate that `TimeService` extracts datetime from raw API JSON
**Preconditions:**

* Inject sample API response
  **Steps:**

1. Call `TimeService.get_current_time()`
2. Verify time string formatting

**Expected Result:** Returns valid formatted string `"2025-08-06 17:25"`

**Test Type:** Unit

---

## ✅ UI Time Display Test Cases (`US039`)

---

### 🧪 TC-US039-001: Time in Task Report (Playwright)

**Title:** Task report view shows current time (mocked)
**Description:** Using mock time, confirm that `/tasks/report` renders expected value
**Preconditions:**

* MockTimeService is injected
* Task exists (or not)
  **Steps:**

1. Load `/tasks/report`
2. Look for time string in HTML

**Expected Result:** Time string (e.g., "2025-08-06 17:25") is visible in summary

**Test Type:** UI (Playwright)

---

### 🧪 TC-US039-002: Robot Framework Acceptance

**Title:** End-to-end test shows time to user
**Description:** Ensure time shown in browser reflects service output
**Preconditions:**

* Start server with mock injected
  **Steps:**

1. Use Robot to open `/tasks/report`
2. Validate page contains correct time

**Expected Result:** Page contains time element with expected value

**Test Type:** Acceptance (Robot Framework)

---

### 🧪 TC-US039-003: Unit Test Mock UI Context

**Title:** Inject MockTimeService into render context
**Description:** Unit test that Jinja template is passed correct time from mock
**Preconditions:**

* Render view with mocked context
  **Steps:**

1. Call Flask `render_template()` with mocked service
2. Inspect context

**Expected Result:** `"current_time"` context var matches mock time

**Test Type:** Unit

---

## 🤖 Robot Framework Acceptance Testing

> **Test Type:** Automated (UI Acceptance)

### 🧪 TC-RF-US031-001: Time Display via UI Workflow

* **Description:** Launch UI, navigate to time report page, verify live time is displayed.
* **Expected Result:** Browser renders valid time response from API.

---

## 📘 Summary

| Test Case ID      | Description                             | Type                        |
| ----------------- | --------------------------------------- | --------------------------- |
| TC-UIEDGE-001     | Long title input validation             | Manual / Automated (UI)     |
| TC-UIEDGE-002     | Whitespace-only task submission         | Manual / Automated (UI)     |
| TC-UIEDGE-003     | No JavaScript behavior                  | Manual (exploratory)        |
| TC-REGSPRINT5-001 | Add → Edit → Delete full cycle          | Automated / Manual          |
| TC-REGSPRINT5-002 | Multi-browser testing                   | Manual (Chrome, Firefox...) |
| TC-REGSPRINT5-003 | Persistence across reloads              | Manual / Automated          |
| TC-EXPLORE-001    | Exploratory feedback from QA peers      | Manual (report-based)       |
| TC-US031-001      | Valid external API call                 | Automated (requests)        |
| TC-US031-002      | API error/failure handling              | Automated (mocked)          |
| TC-US031-003      | Unit test using mock client             | Unit                        |
| TC-US031-004      | Optional live API call                  | Manual (opt-in)             |
| TC-RF-US031-001   | UI-based time workflow (BDD acceptance) | Automated (Robot Framework) |

All tests should be documented with results, screenshots, and logs under `docs/test_documentation/` and `tests/robot/results/` as applicable.

# 🌐 Sprint API Documentation

This document provides a complete reference for the TaskTracker application's REST API across Sprints. It includes all task-related endpoints, health checks, UI routes, and the newly added `/api/time` route for external API integration.

Refactors across Sprints 3–5 introduce service classes, dependency injection, database migration, and test automation.

---

## 🔍 Overview

| Category       | Technology / Approach                                                        |
| -------------- | ---------------------------------------------------------------------------- |
| Framework      | Flask                                                                        |
| Storage        | SQLite (via SQLAlchemy ORM)                                                  |
| UI             | Flask Templates + HTML Forms                                                 |
| API Format     | REST (JSON)                                                                  |
| External APIs  | World Time API (`/api/time`) via `requests`                                  |
| Validation     | HTML5 + Server-Side (WTForms / Flask validation)                             |
| Testing Tools  | Pytest, Requests, Postman, Selenium, Playwright, Behave, **Robot Framework** |
| Test Strategy  | Unit, Integration, API, UI, BDD, Regression, Acceptance                      |
| CI/CD          | GitHub Actions for multi-tool automated testing                              |
| Design Pattern | Dependency Injection (DI)                                                    |
| Architecture   | Layered (Blueprints, Services, Repository)                                   |

---

## 📬 API Endpoints (JSON)

| Method | URL                | Description                            | Status Code     |
| ------ | ------------------ | -------------------------------------- | --------------- |
| GET    | `/api/health`      | Health check                           | 200             |
| GET    | `/api/tasks`       | Get all tasks                          | 200             |
| POST   | `/api/tasks`       | Add a new task                         | 201 / 400       |
| PUT    | `/api/tasks/<id>`  | Mark task as completed or update title | 200 / 400 / 404 |
| DELETE | `/api/tasks/<id>`  | Delete task                            | 200 / 404       |
| POST   | `/api/tasks/reset` | Reset tasks (test automation only)     | 204             |
| GET    | `/api/time`        | Get current time from external API     | 200 / 502       |

---

## 🖥️ UI Form Routes

These endpoints render HTML templates and are designed for direct user interaction in the browser.

| Method | URL             | Description                                |
| ------ | --------------- | ------------------------------------------ |
| GET    | `/tasks/new`    | Render the task creation form (US012)      |
| POST   | `/tasks/new`    | Handle task form submission (US012, US036) |
| GET    | `/tasks/report` | View task report summary page (US027)      |

---

## 📍 Base URL

```
http://localhost:5000
```

---

## 📦 Sprint 4: Core Task Management Endpoints

### `GET /api/tasks`

Returns a list of all tasks.

**Status Code:** `200 OK`
**Sample Response:**

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk and eggs",
    "completed": false
  }
]
```
---

### `POST /api/tasks`

Creates a new task.

**Status Codes:** `201 Created`, `400 Bad Request`
**Request:**

```json
{
  "title": "Do homework",
  "description": "Math and English"
}
```
---

### `PUT /api/tasks/<id>`

Marks a task complete or updates its title (partial update supported).

**Status Codes:** `200 OK`, `400 Bad Request`, `404 Not Found`
**Request Example:**

```json
{
  "title": "Update task title"
}
```

**OR:**

```json
{
  "completed": true
}
```

---

### `DELETE /api/tasks/<id>`

Deletes a task by ID.

**Status Codes:** `200 OK`, `404 Not Found`

---

### `GET /api/tasks/report`

Returns summary report of task completion.

**Sample Response:**

```json
{
  "total_tasks": 5,
  "completed": 3,
  "pending": 2
}
```

---

### `GET /api/health`

Returns system status.

**Sample Response:**

```json
{
  "status": "ok"
}
```

---

## 🌐 Sprint 5: External API Integration

### `GET /api/time`

Returns current UTC time using [TimeAPI.io](https://timeapi.io/api/Time/current/zone?timeZone=UTC). `
The endpoint supports mock injection for testing and graceful fallback on error.

**Status Codes:** `200 Time retrieved successully`, `503 Service Unavailable`: External aPI failed or timed out

#### ✅ Success Response (Real or Mock):

{
  "datetime": "2025-08-06T17:40:00Z",
  "timezone": "UTC",
  "abbreviation": "UTC"
}

ℹ️ The field datetime is used consistently regardless of real or mocked service. The format is ISO-8601 UTC.

#### ❌ Error Response:

```json
{
  "error": "Unable to retrieve time"
}
```

---

## 🧪 Testing and Mocking Support

* `/api/time`  is served by an injected TimeService class
* Mocking is enabled via test fixtures and MockTimeService
* Covered by:

  * ✅ Unit tests for service logic
  * ✅ Integration test (mock and real))
  * ✅ UI validation with Playwright
  * ✅ Acceptance test with Robot Framework

---

## ✅ Test Coverage Summary

| Endpoint                 | User Story | Test Cases                                       |
| ------------------------ | ---------- | ------------------------------------------------ |
| `GET /api/tasks`         | US003      | TC-US003-001 to TC-US003-002                     |
| `POST /api/tasks`        | US002      | TC-US002-001 to TC-US002-003                     |
| `PUT /api/tasks/<id>`    | US004      | TC-US004-001 to TC-US004-002                     |
| `DELETE /api/tasks/<id>` | US005      | TC-US005-001                                     |
| `GET /api/tasks/report`  | US027      | TC-US027-001                                     |
| `GET /api/health`        | US001      | TC-US001-001                                     |
| `GET /api/time`          | US031      | TC-US031-001 to TC-US031-004, TC-US039-001 - 003 |

---

## 🧱 Design Highlights

* 🧩 Dependency Injection (`create_app()` with service injection)
* 🔄 Routes modularized via Flask Blueprints
* ✅ Mock services for unit and integration tests
* ✅ CI runs all test types: Pytest, Postman, Playwright, Selenium, Robot Framework

---

## 🔧 Extended PUT Endpoint Behavior

### `PUT /api/tasks/<id>`

Updates a task's title and/or marks it complete.

**Partial updates are allowed.**

**Request Example (Update title):**

```json
{
  "title": "Buy groceries and eggs"
}
```

**Request Example (Complete task):**

```json
{
  "completed": true
}
```

**Success Response:**

```json
{
  "id": 1,
  "title": "Buy groceries and eggs",
  "description": "Milk",
  "completed": true
}
```

**Error Response (Missing/invalid data):**

```json
{
  "error": "Invalid or missing fields"
}
```

---

## 📋 User Stories and Endpoints Summary

| User Story | Title                   | Endpoint / Feature             | Refactor(s)  |
| ---------- | ----------------------- | ------------------------------ | ------------ |
| US002      | Add Task                | `POST /api/tasks`              | RF005, RF008 |
| US003      | View Tasks              | `GET /api/tasks`               | RF005, RF008 |
| US004      | Mark Task Complete      | `PUT /api/tasks/<id>`          | RF005, RF008 |
| US005      | Remove Task             | `DELETE /api/tasks/<id>`       | RF005, RF008 |
| US007      | CLI Remove Task         | CLI-only; internal TaskService | RF005        |
| US027      | Task Summary Report     | `GET /api/tasks/report`        | RF005, RF008 |
| US031      | Get External Time       | `GET /api/time`                | RF020        |
| US035      | Test Automation with CI | `requests` module integration  | RF008        |

---

## 🔄 Regression Strategy

✅ Full regression tests across all endpoints using:

* Pytest (unit/integration)
* `requests` (API layer)
* Postman (manual/automated)
* Robot Framework (acceptance)
* CI orchestration (GitHub Actions)

---

## 📊 Summary

Sprint 5 adds robustness to the TaskTracker application without expanding the API surface.

✅ Major accomplishments:

* Dependency Injection across all services
* External API integration with fallback
* Robot Framework test support
* Full CI-compatible test strategy

🛠️ All endpoints are now modular, testable, and production-ready.


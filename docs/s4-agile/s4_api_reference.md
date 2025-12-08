# 🌐 Sprint 4 API Documentation

This document outlines the updated API endpoints and implementation details for the TaskTracker Group Project.

> Sprint 4 completes the Group Project by finalizing the Time Service via external API, adding task creation timestamps to the Task Summary, enforcing Hybrid Test Organization with pytest markers, validating centralized task validation, executing Robot Framework acceptance testing, and preparing the Final Test Report and Presentation.

---

## ✅ Overview of Changes in Sprint 3

* Introduced `TaskService` class for business logic
* Introduced `TaskRepository` interface for persistence layer
* Implemented API automation using pytest
* Introduced object-oriented architecture and modular routing

**Authentication:** Not required  
**Versioning:** Not required  
**Environment:** Local development only (e.g., http://localhost:5000)  
**Base Route:** `/api`

---

## ✅ Overview of Changes in Sprint 4

### ✅ Major Group Project Enhancements
- Implemented **US031 – Time Service via External API**
- Implemented **US039 – Task Creation Timestamp in Task Summary**
- Enforced **US041 – Hybrid Test Organization using pytest markers**
- Completed **Centralized Validation (PR5)**
- Integrated **Robot Framework acceptance testing (PR8)**
- Verified **full regression testing (PR7)**
- Finalized **CI pipeline execution rules (PR2)**

---

## ✅ Application Overview (Sprint 4)

| Category         | Technology                                      |
|------------------|--------------------------------------------------|
| Framework        | Flask                                            |
| Storage          | JSON Persistence                                 |
| UI               | Flask Templates + HTML                           |
| API Format       | REST (JSON)                                      |
| Validation       | Centralized via TaskService + Schema             |
| Testing Tools    | pytest, Playwright, Selenium, Robot Framework    |
| Architecture     | Layered (Blueprints, Services, Repository)       |
| CI/CD            | GitHub Actions                                   |

---

## 📌 Key Notes (Sprint 4)

- The application enforces **centralized validation** at the Service layer.
- `TaskService` is responsible for all business rules.
- Tasks now store and display a **`createdAt` timestamp (US039)**.
- The application integrates with the **WorldTimeAPI** for time retrieval (**US031**).
- Tests are maintained using a **Hybrid organization model** with:
  - Concern-based folders
  - pytest markers: `unit`, `integration`, `e2e`
- Robot Framework provides **acceptance-level regression testing**.

---

## 📬 API Endpoints (JSON)

| Method | URL                   | Description                              | Status Code |
|--------|------------------------|------------------------------------------|-------------|
| GET    | `/api/health`          | Health check                             | 200         |
| GET    | `/api/tasks`           | Get all tasks                            | 200         |
| POST   | `/api/tasks`           | Add a new task (with timestamp)          | 201 / 400   |
| PUT    | `/api/tasks/<id>`      | Mark task as completed                   | 200 / 404   |
| DELETE | `/api/tasks/<id>`      | Delete task                              | 200 / 404   |
| GET    | `/api/time`            | Get current time via external API        | 200 / 503   |

---

## 🖥️ UI Routes

These endpoints render HTML templates and support direct user interaction.

| Method | URL              | Description                                 |
|--------|------------------|---------------------------------------------|
| GET    | `/tasks/new`     | Render task creation form                  |
| POST   | `/tasks/new`     | Handle task form submission                |
| GET    | `/tasks/report`  | Display Task Summary with timestamps       |

---

## 🔧 Extended Endpoint Behavior

### ✅ POST /api/tasks (US039)

- Automatically generates and stores:
  - `id`
  - `title`
  - `completed`
  - `createdAt`

#### ✅ Example Response
```json
{
  "id": 4,
  "title": "Finish Sprint 4 Docs",
  "completed": false,
  "createdAt": "2025-03-08T14:23:00"
}

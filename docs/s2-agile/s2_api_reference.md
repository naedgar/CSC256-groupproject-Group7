# API Reference Update - Sprint 2

This document provides an overview of the API endpoints implemented and enhanced in Sprint 2. These specifications support PR3 (Hybrid Testing), PR4 (Time Service), and PR5 (Centralized Task Validation).

---

## 📘 Overview

**Sprint Goal:** Introduce centralized validation, add the Time Service endpoint, and restructure automated testing using hybrid pytest markers.  
**Authentication:** Not required.  
**Versioning:** Not required at this stage.  
**Environment:** Local development only (e.g., http://localhost:5000)  
**Base Route:** `/api`  

**Major Enhancements:**

* Centralized task input validation (PR5)
* Time Service endpoint `/api/time` (PR4)
* Hybrid pytest structure using markers (PR3)
* Continued use of Blueprint routing and App Factory pattern

> [!NOTE] Sprint 1 established baseline task creation and retrieval using in-memory storage and a basic CLI. Sprint 2 enhances validation and testing but does **not** introduce task deletion, completion, or persistence yet.

---

## US001 - Endpoint: Health Check

| Field            | Description                         |
| ---------------- | ----------------------------------- |
| **Method**       | GET                                 |
| **URL**          | `/api/health`                       |
| **Description**  | Verifies that the API is online     |
| **Parameters**   | None                                |
| **Request Body** | None                                |
| **Response**     | `{ "status": "ok" }`                |
| **Status Code**  | `200 OK`                            |
| **Error Codes**  | None                                |
| **Expected Use** | Used by developers, CI, and testers |

### 📎 Example Request (Postman)

* Method: GET  
* URL: `http://localhost:5000/api/health`  
* Expect: `{ "status": "ok" }`

---

## US002 - Endpoint: Add Task (With Centralized Validation)

| Field            | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| **Method**       | POST                                                        |
| **URL**          | `/api/tasks`                                                |
| **Description**  | Creates a new task with centralized validation             |
| **Parameters**   | None                                                        |
| **Request Body** | `{ "title": "Buy groceries" }`                              |
| **Response**     | Task object with ID and completed flag                     |
| **Status Code**  | `201 Created`                                               |
| **Error Codes**  | `400 Bad Request` – invalid title                          |
| **Expected Use** | Called when a user submits a new task                       |

### ✅ Validation Rules (PR5)

- Title is required  
- Title is trimmed of whitespace  
- Empty or whitespace-only titles are rejected  
- Duplicate titles are rejected  

### ✅ Valid Request Body
```json
{
  "title": "Buy groceries"
}

# 📌 Sprint 3 Issue Guidance – OOP, Dependency Injection & API Automation

## Epic: Sprint 3 Acceptance Criteria

📁 **Title:** Sprint 3 Acceptance Criteria  
📄 **Description:**  
This sprint transforms the TaskTracker app from procedural code into a clean, scalable architecture using **Object-Oriented Programming (OOP)**, **Dependency Injection (DI)**, **JSON persistence**, and **automated API testing** using `requests`.

Completion of Sprint 3 requires the following:

* [ ] Implement `Task` and `TaskService` classes (PR2)  
* [ ] Add JSON persistence through `FileTaskRepository` (PR6)  
* [ ] Apply Dependency Injection via `create_app()` and route refactors (PR6)  
* [ ] Update all API routes to use `current_app.task_service` (PR6)  
* [ ] Implement PUT and DELETE endpoints (PR7)  
* [ ] Add automated API tests using `requests` (PR8)  
* [ ] Ensure CLI supports complete/delete through TaskService  

---

## 🧩 User Stories & Refactor Stories (Sub-Issues)

#### US003-01 – Represent tasks as objects  
As a developer, I want tasks to be represented as objects so that they can carry attributes consistently.

#### US003-02 – Centralize business logic  
As a developer, I want a `TaskService` class so that task logic is encapsulated, testable, and reusable.

#### US003-03 – Enable dependency injection for storage  
As a developer, I want storage wrapped in a repository class so business logic can remain independent of file format.

#### US003-04 – Inject TaskService into the app factory  
As a developer, I want the service injected through `create_app()` so routes can access it via `current_app.task_service`.

#### US003-05 – API routes must use service layer  
As a user of the API, I want consistent behavior through the service so logic stays unified.

#### US003-06 – Verify behavior with automated tests  
As a developer, I want unit, integration, and API-level tests to confirm all components work after refactor.

---

## 🔧 Refactor Stories

### 🔹 #RF004 – Task & TaskService OOP Refactor (PR2)
* [ ] Create `Task` class with id/title/description/completed  
* [ ] Create `TaskService` class (add/view/complete/delete)  
* [ ] Write unit tests for service methods  
* [ ] Validate Task objects correctly instantiated  

---

### 🔹 #RF005 – Update Routes to Use TaskService (PR2 → PR6)
* [ ] Refactor all task routes to call TaskService  
* [ ] Remove direct JSON or list manipulation in routes  
* [ ] Add service-based integration tests  

---

### 🔹 #RF006A – Add FileTaskRepository for DI (PR6)
* [ ] Create `FileTaskRepository` with load/save methods  
* [ ] Replace old storage functions  
* [ ] Ensure compatibility with TaskService  
* [ ] Add repository-level tests  

---

### 🔹 #RF006B – Inject TaskService in App Factory (PR6)
* [ ] Modify `create_app()` to attach service instance  
* [ ] Store service in `app.task_service`  
* [ ] Verify app starts without errors  

---

### 🔹 #RF006C – Refactor Routes for DI (PR6)
* [ ] Remove imports of storage or TaskService from routes  
* [ ] Replace with `from flask import current_app`  
* [ ] Validate functionality through integration tests  

---

### 🔹 #RF007 – Implement PUT & DELETE Endpoints (PR7)
* [ ] Add `/api/tasks/<id>` PUT for mark complete  
* [ ] Add `/api/tasks/<id>` DELETE for remove task  
* [ ] Write tests for success & 404 error handling  

---

### 🔹 #RF008 – API Automation Using `requests` (PR8)
* [ ] Add automated API tests using `requests`  
* [ ] Add mocking tests with `MockTaskService`  
* [ ] Validate end-to-end workflow: add → complete → delete  

---

## 🔍 Automated Testing Coverage (Atomic Tasks)

| Test Case ID  | Summary                                          | Responsible Test File                        |
|---------------|--------------------------------------------------|----------------------------------------------|
| TC-RF004-001  | Unit test TaskService `add_task()`               | `tests/services/test_task_service_add.py`    |
| TC-RF004-002  | Unit test TaskService `complete_task()`          | `tests/services/test_task_service_complete.py` |
| TC-RF004-003  | Unit test TaskService `delete_task()`            | `tests/services/test_task_service_delete.py` |
| TC-RF004-004  | Test `Task` class instantiation                  | `tests/services/test_task_model.py`          |
| TC-RF005-001  | Route uses service `add_task()`                  | `tests/routes/test_routes_add.py`            |
| TC-RF005-002  | Route uses service `get_all_tasks()`             | `tests/routes/test_routes_get.py`            |
| TC-RF005-003  | Route uses service `complete_task()`             | `tests/routes/test_routes_complete.py`       |
| TC-RF005-004  | Route uses service `delete_task()`               | `tests/routes/test_routes_delete.py`         |
| TC-RF006A-001 | FileTaskRepository wrapper load/save behavior    | `tests/storage/test_repository.py`           |
| TC-RF006B-001 | `create_app()` injects TaskService correctly     | `tests/test_app_factory.py`                  |
| TC-RF006C-001 | Routes use `current_app.task_service`            | `tests/routes/test_dependency_routes.py`     |
| TC-RF007-001  | PUT completes task                               | `tests/api/test_put_request.py`              |
| TC-RF007-002  | DELETE removes task                              | `tests/api/test_delete_request.py`           |
| TC-RF008-001  | Add task via `requests.post()`                   | `tests/api/test_requests_flow.py`            |
| TC-RF008-002  | View tasks via `requests.get()`                  | `tests/api/test_requests_flow.py`            |
| TC-RF008-003  | Complete task via `requests.put()`               | `tests/api/test_requests_flow.py`            |
| TC-RF008-004  | Delete task via `requests.delete()`              | `tests/api/test_requests_flow.py`            |
| TC-RF008-005  | Use `MockTaskService` injected via conftest      | `tests/conftest.py`                          |

---

## 📊 Sprint Board Setup

Create a **Sprint 3 Project Board** in GitHub with these columns:

1. **Backlog**  
2. **Ready**  
3. **In Progress**  
4. **Review**  
5. **Done**

Each of the refactor stories (#RF004–#RF008) should be individual cards with matching user stories and test case IDs.

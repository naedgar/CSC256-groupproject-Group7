# 📌 Sprint 3 Issue Guidance – OOP & Integration Testing 

## Epic: Sprint 3 Acceptance Criteria

📁 **Title:** Sprint 3 Acceptance Criteria
📄 **Description:**
This Sprint focuses on transitioning the procedural Flask app to a more scalable architecture using **object-oriented programming**, **dependency injection**, and **automated API tests**. Completion of Sprint 3 requires the following:

* [ ] Refactor into `TaskService` and `Task` classes
* [ ] Apply full Dependency Injection via `TaskStorage`, `__init__.py`, and Blueprint updates
* [ ] Add unit tests for `TaskService` logic
* [ ] Add integration tests using `requests` library
* [ ] Replace manual tests with automated mock and real service tests
* [ ] CLI interface is finalized and deprecated for individual labs (still usable for group work with full test coverage)

---

## 🧩 User Stories & Refactor Stories (Sub-Issues)
#### US0003-01 - Manage tasks
As a developer, I want tasks to be represented as objects so that they can be managed with attributes.

#### US003-02 - Centralize task business logic
As a developer, I want a TaskService class with methods so that the application's task logic is encapsulated in one place

#### US003-03 - Use dependency injection for storage
As a developer, I want to wrap storage logic into a TaskStorage class so that storage can be swapped, mocked, extended without changing business logic.

#### US003-04 – Inject service into app factory

As a developer, I want the TaskService to be injected into create_app() so that routes can access it through current_app.task_service without tight coupling.

#### US003-05 – Ensure API endpoints use service layer

As a user of the API, I want task endpoints to call the TaskService so that business logic is consistent across the system.

#### US003-06 – Verify app behavior with automated tests

As a developer, I want both unit tests and integration tests using mocks and requests so that I can confirm the app works correctly without relying on manual testing.

### 🔧 Refactor Stories

#### 🔹 #RF004 – TaskService OOP Refactor

* [ ] Create `Task` class with `id`, `title`, `description`, `completed`
* [ ] Create `TaskService` class with `add_task`, `get_tasks`, `complete_task`, `delete_task`
* [ ] Write unit tests for `TaskService` methods
* [ ] Validate correct instantiation of `Task` objects

#### 🔹 #RF005 – Use TaskService as Main Task Logic

* [ ] Update all task routes to call `TaskService` methods
* [ ] Remove direct usage of storage functions from `routes/tasks.py`
* [ ] Add unit tests for service-based route behavior

#### 🔹 #RF006A – Add `TaskStorage` Wrapper for Dependency Injection

* [ ] Add `TaskStorage` class to wrap existing `load_tasks()` and `save_tasks()`
* [ ] Expose a singleton `task_storage` instance
* [ ] Ensure compatibility with existing service logic
* [ ] Test TaskService using this wrapper

#### 🔹 #RF006B – Inject `TaskService` in `__init__.py`

* [ ] Modify `create_app()` to create and inject `TaskService(task_storage)`
* [ ] Attach service to `app.task_service`
* [ ] Confirm app starts and routes still function

#### 🔹 #RF006C – Refactor Routes for Dependency Injection

* [ ] Remove all direct imports from `task_storage` in `routes/tasks.py`
* [ ] Use `current_app.task_service` in route functions
* [ ] Confirm functionality and backward compatibility

#### 🔹 #RF008 – Mock + Requests API Tests

* [ ] Create test module for `requests` tests with real server
* [ ] Use `MockTaskService` in test config
* [ ] Add tests for API behavior (add, get, complete, delete) using both mock and requests

---

## 🔍 Automated Testing Coverage (Atomic Tasks)

| Test Case ID  | Summary                                  | Responsible Test File                        |
| ------------- | ---------------------------------------- | -------------------------------------------- |
| TC-RF004-001  | Unit test TaskService `add_task()`       | `tests/tasks/test_task_service_add.py`       |
| TC-RF004-002  | Unit test TaskService `complete_task()`  | `tests/tasks/test_task_service_complete.py`  |
| TC-RF004-003  | Unit test TaskService `delete_task()`    | `tests/tasks/test_task_service_delete.py`    |
| TC-RF004-004  | Test `Task` class instantiation          | `tests/tasks/test_task_model.py`             |
| TC-RF005-001  | Route uses service `add_task()`          | `tests/tasks/test_routes_add.py`             |
| TC-RF005-002  | Route uses service `get_tasks()`         | `tests/tasks/test_routes_get.py`             |
| TC-RF005-003  | Route uses service `complete_task()`     | `tests/tasks/test_routes_complete.py`        |
| TC-RF005-004  | Route uses service `delete_task()`       | `tests/tasks/test_routes_delete.py`          |
| TC-RF006A-001 | TaskStorage wrapper created + callable   | `tests/storage/test_task_storage_wrapper.py` |
| TC-RF006B-001 | `create_app()` injects service correctly | `tests/test_app_factory.py`                  |
| TC-RF006C-001 | Routes call `current_app.task_service`   | `tests/tasks/test_dependency_routes.py`      |
| TC-RF008-001  | Add task via `requests.post()`           | `tests/tasks/test_api_requests.py`           |
| TC-RF008-002  | View tasks via `requests.get()`          | `tests/tasks/test_api_requests.py`           |
| TC-RF008-003  | Complete task via `requests.put()`       | `tests/tasks/test_api_requests.py`           |
| TC-RF008-004  | Delete task via `requests.delete()`      | `tests/tasks/test_api_requests.py`           |
| TC-RF008-005  | Inject `MockTaskService` via conftest    | `tests/conftest.py`                          |
| TC-RF008-006  | Mock add task unit test                  | `tests/tasks/test_mock_service_add.py`       |
| TC-RF008-007  | Mock complete task unit test             | `tests/tasks/test_mock_service_complete.py`  |
| TC-RF008-008  | Mock delete task unit test               | `tests/tasks/test_mock_service_delete.py`    |

---

## 📊 Sprint Board Setup

Create a **Sprint 3 Project Board** in GitHub using the following columns:

1. **Backlog**
2. **Ready**
3. **In Progress**
4. **Review**
5. **Done**



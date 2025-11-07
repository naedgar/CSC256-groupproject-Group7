# 🍪 Sprint 2 Test Cases

These test cases ensure new features from US004, US005, US011, and US015 function correctly and do not break existing functionality.

Each test case includes:
- **Test Case ID**
- **Description**
- **Preconditions**
- **Test Steps**
- **Expected Results**
- **Test Type** (Automated, Manual, or Both)

This document includes formal test cases that verify functionality added in Sprint 2:

* **US004** – Mark Task Complete
* **US005** – Delete Task
* **US011** – Persistent JSON File Storage
* **US015** - API Error Handling
* **NFR001** – Routes Accessible via Blueprint
* **NFR001-002** - Modular Architecture via Flask Blueprint
* **Manual API Testing Tool:** - Postman

## US004 - Mark Task Complete

### TC-US004-001: Mark Task Complete (Valid ID)

- **Description:** Mark a task as complete with valid ID
- **Preconditions:** Task exists with `completed = false`
- **Steps:**
  1. Send PUT `/api/tasks/<id>` with `{ "completed": true }`
- **Expected:** Response 200 with updated task (`completed: true`)
- **Test Type:** Automated

###  TC-US004-002: Mark Non-Existent Task Complete

### TC-US004-002
- **Description:** Attempt to complete a non-existent task
- **Preconditions:** Task ID does not exist
- **Steps:**
  1. Send `PUT /api/tasks/999`
- **Expected:** **Expected:** 404 Not Found with `{ "error": "Task not found" }`
- **Test Type:** Automated, Manual

---
## US005 - Delete Task

### TC-US005-001: Delete Existing Task (Valid ID)

- **Description:** Delete an existing task
- **Preconditions:** Task exists
- **Steps:**
  1. Send DELETE `/api/tasks/<id>`
- **Expected:** 204 No Content
- **Test Type:** Automated, Manual

### TC-US005-002: Delete Non Existent Task
- **Description:** Attempt to delete a non-existent task
- **Preconditions:** No task exists with provided ID
- **Steps:**
  1. Send `DELETE /api/tasks/999`
- **Expected:** 404 Not Found
- **Test Type:** Automated, Manual

---
### US011 - Persistent JSON Storage

###  TC-US011-001: Persist Tasks to JSON File

* **Description:** Verify that tasks added through the API are saved to `data/tasks.json` and persist after application restart.
* **Preconditions:** Empty `data/tasks.json` file
* **Steps:**
  1. Add a task
  2. Restart server
  3. Call `GET /api/tasks`
* **Expected:** Task still exists
* **Test Type:** Automated, Manual

### TC-US011-002

* **Description:** Manual check of data/tasks.json
* **Preconditions**: Task has been added or modified
* **Steps:**
  1. Open `data/tasks.json` in VS Code or a text editor.
  2. Inspect the structure.
* **Expected:** File contains a valid JSON array of task objects with keys like `id`, `title`, `completed`.
* **Test Type:** Manual

## US015– API Error Handling

### TC-US015-001
- **Description:** Trigger 404 by fetching nonexistent task
- **Steps:**
  1. Send `GET /api/tasks/999`
- **Expected:** 404 status with `{ "error": "Task not found" }`
- **Test Type:** Automated, Manual

### TC-US015-002
- **Description:** Send bad POST request without `title`
- **Steps:**
  1. Send `POST /api/tasks` with `{}`
- **Expected:** 400 status with JSON error
- **Test Type:** Automated, Manual

### TC-US015-003
- **Description:** Use unsupported HTTP method on `/api/tasks`
- **Steps:**
  1. Send `PATCH /api/tasks`
- **Expected:** 405 Method Not Allowed
- **Test Type:** Automated, Manual

## NFR001 - Routes and Blueprint

###  TC-NFR001-001: Routes Accessible via Blueprint

* **Description:** Ensure that all expected endpoints remain accessible after modularization via Flask Blueprints.
* **Test Type:** Automated

**Steps:**

1. Ensure app uses `create_app()` with registered Blueprint.
2. Use Flask test client to send requests to:

   * `GET /api/health`
   * `GET /api/tasks`
   * `POST /api/tasks`
3. Observe responses.

**Expected Result:**

* All endpoints return successful responses (`200`, `201`, etc.).
* No routing errors (`404`) from missing registration.

###  TC-NFR001-002: Modular Architecture via Flask Blueprint

* **Description:** Validate that if the `tasks` Blueprint is not registered in `create_app()`, expected routes return `404 Not Found`.
* **Preconditions**
   * Your app uses the create_app() function in app/__init__.py.
   * The blueprint is defined in app/routes/tasks.py and registered with app.register_blueprint(tasks_bp).
* **Test Type:** Manual

**Steps:**

1. Temporarily comment out the `app.register_blueprint()` line for the tasks module in `create_app()`.
2. Run the Flask app.
3. Open Postman (or curl) and try this request

  GET http://localhost:5000/api/tasks


**Expected Result:**

* Response returns `404 Not Found`.
* Confirms modular registration is required for route availability.

###  TC-MANUAL-001: Add Task via API (Manual)

* **Test Type:** Manual (`Postman`, `curl` and `Invoke RestMethod`)
* **Steps:**

  1. Open Postman
  2. Set method to `POST`, URL to `http://localhost:5000/api/tasks`
  3. Use JSON body: `{ "title": "Laundry", "description": "Do laundry" }`
  4. Click Send
* **Expected Result:** 201 Created, returns task JSON with ID

###  TC-MANUAL-002: ListTask via API (Manual)

* **Test Type:** Manual (`Postman`, `curl` and `Invoke RestMethod`)
* **Steps:**

  1. Open Postman
  2. Set method to `GET`, URL to `http://localhost:5000/api/tasks`
  3. Click Send
* **Expected Result:** []


###  TC-MANUAL-003: Mark Task Complete via API (Manual)

* **Test Type:** Manual (`Postman`, `curl` and `Invoke RestMethod`)
* **Steps:**

  1. Use `PUT` method with URL `http://localhost:5000/api/tasks/1`
  2. Use JSON body: `{ "completed": true }`
* **Expected Result:** 200 OK, returns updated task with `completed: true`

###  TC-MANUAL-004: Delete Task via API (Manual)

* **Test Type:** Manual (`Postman`, `curl` and `Invoke RestMethod`)
* **Steps:**

  1. Use `DELETE` method with URL `http://localhost:5000/api/tasks/1`
* **Expected Result:** 204 No Content

- **Description**: Add a task via `cli_app.py` input prompts.
- **Preconditions**: `cli_app.py` is implemented and runs.
- **Steps**:
  1. Run `python -m app.cli.cli_app`
  2. Follow menu to add a task (e.g., enter title/description)
- **Expected**: Task is added, appears in `GET /api/tasks` or file.
- **Test Type**: Manual

## CLI Manual Tests (US006)

### TC-CLI-001: Add Task via CLI
- **Description**: Add a task via `cli_app.py` input prompts.
- **Preconditions**: `cli_app.py` is implemented and runs.
- **Steps**:
  1. Run `python -m app.cli.cli_app`
  2. Follow menu to add a task (e.g., enter title/description)
- **Expected**: Task is added, appears in `GET /api/tasks` or file.
- **Test Type**: Manual

### TC-CLI-002: View Tasks via CLI
- **Description**: View all tasks through the CLI
- **Steps**:
  1. Run `python -m app.cli.cli_app`
  2. Select "View Tasks"
- **Expected**: CLI prints task list, matching the API state.
- **Test Type**: Manual

---

### 3. **Final Test Case Set Confirmed**

This leaves you with the following test case groupings:

* `/tests/tasks/`

  * TC-US004-001: Mark Complete (Valid)
  * TC-US004-002: Mark Complete (Invalid ID)
  * TC-US005-001: Delete Task (Valid)
  * TC-US005-002: Delete Task (Invalid ID)
* `/tests/storage/`

  * TC-US011-001: Save to File
  * TC-US011-002: Load from File
* `/tests/health/`

  * TC-US015-001: Invalid JSON Body
  * TC-US015-002: Missing Required Field
  * TC-US015-003: Invalid Method
* CLI (Manual)

  * TC-CLI-001: Add Task
  * TC-CLI-002: View Tasks

---


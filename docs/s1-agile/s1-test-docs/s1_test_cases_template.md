# Sprint 1: Test Cases (Task Tracker)

These test cases ensure new features from US004, US005, US009, and US014 function correctly and do not break existing functionality.

Each test case includes:
- **Test Case ID**
- **Description**
- **Preconditions**
- **Test Steps**
- **Expected Results**
- **Test Type** (Automated, Manual, or Both)

This document contains formal test cases related to individual user stories. Each test case maps to a requirement in `user_stories.md`.

* **US000** – Initial Setup & Validation
* **US001** – Health Check Endpoint (with GitHub Actions)
* **US002** – Add Task (with validation)
* **US003** – View Tasks (List)
* **US004** – Add Task via CLI (stub)

> [!NOTE] **Why Specify Test Type?**
> In real-world QA documentation, explicitly identifying whether a test is **manual**, **automated**, or **both** is essential.
>
> * **Manual tests** are useful for exploratory testing, UI validation, or steps that are difficult to script.
> * **Automated tests** enable fast, repeatable validation of core features and are key to continuous integration pipelines.
>
> Clearly labeling test types prepares students for real-world software testing practices by helping them:
>
> * Allocate testing effort based on complexity and importance
> * Communicate testing strategy to developers and stakeholders
> * Plan which tests should be automated in future sprints
>
> Including `Test Type` supports maintainable test suites, better sprint planning, and robust CI/CD integration.

## US000 - Initial Setup & Validation

### 🧪TC_US000-001: Basic Pytest Function Executes

* **Description:** Verify that a simple standalone Python test (e.g., `assert 2 + 2 == 4`) can be discovered and executed using `pytest`.
* **Test Type**: Automated
* **Preconditions:**
    1. Python virtual environment is active
    2. `pytest` is installed
    3. Test file `tests/test_basics.py` exists with at least one test function
* **Test Steps:**
  1. Open terminal in the project root directory
  2. Run the command: `pytest`
  3. Observe output for discovery and execution of the basic test

* **Expected Result:**
  1. Pytest reports the test in `test_basics.py`
  2. The test passes and output shows a green checkmark and `1 passed`
* **Status:** ☐ Pass ☐ Fail

### 🧪 TC-US000-002: Verify that `create_app()` returns a Flask instance

**Description:** Verify that `create_app()` returns a Flask instance.
**Test Type**: Automated
**Preconditions:** Flask is installed and the app scaffolding exists.
**Test Steps:**

1. Import `create_app` from `app`.
2. Call `create_app()` and assign the result to a variable.
3. Check if the result is an instance of `Flask`.
  
**Expected Result:** `isinstance(app, Flask)` is `True`.
**Status:** ☐ Pass ☐ Fail

### 🧪 TC-US000-003: Flask Returns 404 without Routes Defined

**Description:** Ensure the Flask app returns 404 on root when no routes are defined.
**Test Type**: Automated
**Preconditions:** Flask is installed, app is scaffolded, and test client is available.
**Test Steps:**

   1. Use Flask’s test client to request `/`.
   2. Evaluate the response status code.
  
**Expected Result:** Status code is `404`.
**Status:** ☐ Pass ☐ Fail

### 🧪 TC-US000-004 Flask Creates Local Server

* **Description:** Ensure that the Flask application can start without errors using `flask run`.
* **Test Type**: Manual
* **Preconditions:** Flask and dependencies are installed.
* **Test Steps:**

  1. Activate the virtual environment.
  2. Run `flask run` in the terminal.
  3. Navigate to `http://127.0.0.1:5000/`.

* **Expected Result:** The application starts without crashing; 404 or default response is shown.
* **Status:** ☐ Pass ☐ Fail

## US001 – Health Check Endpoint (with GitHub Actions)

### 🧪 TC-US001-001: Health Check API

* **Description:** Verify that `/health` endpoint returns 200 OK and a JSON payload.
* **Test Type:** Automated
* **Preconditions:** App is running with `/health` route defined.
* **Test Steps:**

  1. Send a `GET /health` request.
  2. Observe the response.
* **Expected Result:** HTTP 200 with JSON:

  ```json
  { "status": "ok" }
  ```

* **Status:** ☑ Pass ☑ Fail

---

## US002 – Add Task (with validation)

### 🧪 TC-US002-001: Add Valid Task - Happy Path

* **Description:** Verify that a valid task is added with a title and description.
* **Test Type:** Automated
* **Preconditions:** API is running and in-memory task list is empty.
* **Test Steps:**

  1. Send a `POST /api/tasks` request with:

  2. Observe the response.
* **Expected Result:**

  * Status `201 Created`
  * JSON includes new task with `id`, `title`, `description`
* **Status:** ☑ Pass ☑ Fail

### 🧪 TC-US002-002: Add Task with Empty Title - Form Input Edge Case

* **Description**: Verify that a task cannot be created when the title is an empty string. This ensures frontend or backend validation correctly blocks invalid input.
* **Test Type:** Automated
* **Test Steps:**

  1. Send:

* **Status:** ☑ Pass ☑ Fail

### 🧪 TC-US002-003: Add Task with Missing Title - Validates JSON structure enforcement

* **Description**: Confirm that a task submission without a title field returns a 400 error, ensuring the API enforces required fields.
* **Test Type:** Automated
* **Test Steps:**
        ```json
        { "description": "Missing title" }
        ```
* **Expected Result:**

  * Status `400 Bad Request`
  * JSON error about missing title
* **Status:** ☑ Pass ☑ Fail

### ### 🧪 TC-US002-004: Send Completely Empty Request

* **Description**: Confirm that sending an empty JSON object results in a 400 Bad Request. This ensures the API enforces that required fields (title) must be present and non-empty.
* **Preconditions:** API is running.
* **Test Type:** Automated
* **Test Steps:** Send a POST /api/tasks request with the following empty JSON body:
        ```json
        {}
        ```
* **Expected Result:**

  * Status `400 Bad Request`
  * JSON error about missing title
* **Status:** ☑ Pass ☑ Fail

### 🧪 TC-US003-001: View Tasks When None Exist

* **Description:** Verify that an empty list is returned when no tasks have been added, to ensure the endpoint gracefully handles the initial state.
* **Test Type:** Automated
* **Test Steps:**

  1. Send `GET /api/tasks`
* **Expected Result:**

  * Status `200 OK`
  * Body: `[]`
* **Status:** ☑ Pass ☑ Fail

### 🧪 TC-US003-002: View Tasks With Field Validation

* **Description:** Validate that tasks are returned with the correct structure and content when at least one task has been created.
* **Test Type:** Automated
* **Steps:**

  1. Add task with POST:

        ```json
        {
        "title": "Sample Task",
        "description": "This is a sample task"
        }
        ```

  2. Call `GET /api/tasks`
     * **Expected Result:**
     * * HTTP status `200 OK`.
     * Response body is a JSON list with at least one task object.
     * Each task object includes:

       * `id` (integer)
       * `title` (string)
       * `description` (string)
       * `completed` (boolean)
* One of the tasks in the list matches:

  * At least one item with:

    ```json
    {
    "title": "Sample Task",
    "description": "This is a sample task",
    "completed": false
    }
    ```

* **Status:** ☑ Pass ☑ Fail

### 🧪 TC-US003-003: Invalid Method on Tasks Endpoint

* **Description:** Ensure unsupported HTTP methods like PUT on the `/api/tasks` collection route return a 405 Method Not Allowed response, following REST principles.

* **Test Type:** Automated

* **Preconditions:**
  - Flask app is running
  - No specific task ID is included in the request (e.g., not `/api/tasks/1`)

* **Steps:**
  1. Send a `PUT` request to `/api/tasks` with any valid or empty JSON body

* **Expected Result:**
  - HTTP status code is `405 Method Not Allowed`
  - Response body (optional)

### 🧪 TC-US003-004: View Task List from CLI

* **Description:** Ensure the CLI displays all in-memory tasks when “View Tasks” is selected.
* **Test Type:** Manual
* **Preconditions:**
  * At least one task exists in memory.
  * cli_app.py has View Task functionality.
* **Test Steps:**
  * Run the CLI interface:
     ```bash
     python -m app.cli.cli_app
     ```
  * Select View Tasks.

* **Expected Result:**
  - CLI displays all tasks in human-readable format.
  - Each task shows title, description, and completed status (if present).
* **Status:** ☐ Pass ☐ Fail

## US004 – Add Task via CLI (stub)

### 🧪 TC-US004-001: Manually Add Task via CLI Prompt

* **Description:** Manually add a task via CLI. Confirms the CLI accepts input and appends to the in-memory list.
* **Test Type:** Manual
* **Preconditions:**
  1. `cli_app.py` is implemented with “Add Task” functionality.
  2. Project can be run with: `python -m app.cli.cli_app`
* **Test Steps:**
  1. Run the CLI interface:
     ```bash
     python -m app.cli.cli_app
     ```
  2. Select the option to add a task
  3. Enter the following input when prompted:
     - Title: `CLI Test Title`
     - Description: `CLI Test Description`
  4. Select the option to view tasks
  5. Confirm the added task is displayed.
* **Expected Result:**
  - CLI displays confirmation of task addition.
  - View tasks shows the newly added task with correct title/description.
* **Status:** ☐ Pass ☐ Fail

### 🧪 TC-US004-002: View Tasks via CLI (Stub)

* **Description:** Verify that tasks previously added using the CLI stub can be displayed when selecting the “View Tasks” option. The task list should show titles and descriptions of all stored tasks in a readable format.

* **Test Type:** Manual

* **Preconditions:**
  1. `cli_app.py` exists and implements both "Add Task" and "View Tasks" options
  2. At least one task has been added via the CLI UI in the current session

* **Test Steps:**
  1. Run the CLI interface:
     ```bash
     python -m app.cli.cli_app
     ```
  2. Select the option to add a task
  3. When prompted, enter:
     - Title: `View Task CLI`
     - Description: `Confirm visibility`
  4. After the task is added, select the option to view tasks
  5. Observe the list of tasks printed to the terminal
* **Expected Result:**
  - The CLI displays a list of tasks, including the one just added
  - Task is shown with correct `title` and `description`
  - Output format is human-readable and reflects in-memory state
* **Status:** ☐ Pass ☐ Fail

> [!TIP] Optional Exploratory Test: Run the CLI and select "View Tasks" without adding any first. Confirm it gracefully displays "No tasks available" or equivalent.


  
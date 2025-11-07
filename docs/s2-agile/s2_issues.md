# 🏁 Sprint 2 Issues

## Parent Epic: Sprint 2 Completion

- *Title:* **Sprint 2 Acceptance Criteria**
- *Description:*
    
  This sprint focuses on enhancing the TaskTracker backend through route modularization, new task operations, persistence, and robust error handling.

    - 📌 Sprint-Level Acceptance Criteria (Product Owner Level) (see `s2_sprint_plan`)
    * Give the ability to mark task complete
    * Give the ability to remove task
    * Give the ability to persist tasks
    * Introduce a unified error handling system using Flask's @errorhandler
    * Refactors the Test Structure into subfolders that match the app’s modular design
    * Refactors CLI to use shared JSON persistence layer 
    * Testing is finished

    - ✅ Definition of Done (applies to each user story or task)(see `s2_sprint_plan`)
    * [ ] Pass all acceptance criteria
    * [ ] Include tests for valid input, invalid input, and edge cases
    * [ ] All tests pass locally and in CI (GitHub Actions)
    * [ ] Code coverage threshold met or exceeded (≥ 90%)
    * [ ] Application runs correctly with JSON file persistence
    * [ ] Documentation updated (code comments, API docs, test docs)
    * [ ] API documentation includes examples for new/refactored endpoints
    * [ ] Main branch is deployable with no critical bugs or regressions
    * [ ] Manual Postman collections committed in `tests/postman/`
  ---
### 📂 Sub-Issues

    - User Story Level Tasks

      * [ ] #US004 – `PUT /api/tasks/<id>` marks task complete
      * [ ] #US005 – `DELETE /api/tasks/<id>` removes a task
      * [ ] #US011 – Persist task list to `data/tasks.json`
      * [ ] #US015 – Add global error handler for `404`, `400`

    ---
    - 🔧 Sprint-Level Refactor Tasks (Sub-Issues)
      * [ ] #RF001 – Refactor: Blueprint modularization (routes/tasks.py)
      * [ ] #RF002 – Refactor: JSON File Storage helpers (utils/storage.py)
      * [ ] #RF003 - Refactor: Organize test files by concern (health, task, storage)
      * [ ] Add regression tests to `test_tasks.py`
      * [ ] Manual tests using Postman (with screenshots)
* 
    - 🔧 Testing & CI

      * [ ] #TEST002-001 – Update and add pytest cases for all new endpoints
      * [ ] #TEST002-002 - Confirm pytest-cov is collecting new test coverage
      * [ ] #TEST002-003 - Confirm GitHub Actions CI still passes on push/PR
      * [ ] #TEST002-004 - Run Postman tests and save collection to /tests/postman/

    - 📄 Documentation
    - [ ] #DOC002-001 - Update docs/api_documentation.md with new endpoints
    - [ ] #DOC002-002 - Update README.md with persistence and blueprint structure
    - [ ] #DOC002-003 - Update `docs/test_documentation/s2_test_plan.md`
    - [ ] #DOC002-004- Add Sprint 2 summary to `docs/test_documentation/s2_test_report.md`
    ---

## **Sprint 2 Acceptance Criteria** 

1. 🎯 *Title:* **US005 – Mark Task Complete** 
     - *Description:* 
   
    As a user, I want to mark a task as completed so I can focus on remaining tasks.
       - ✅ Acceptance Criteria (see `tt_user_stories`)

    
    - 📌 Sub-Issues
      - [ ] #US005-001 - Implement PUT /api/tasks/<id> to mark a task as complete
      - [ ] #US005-002 - Add unit tests for marking a task complete
      - [ ] #US005-003 - Update API documentation with PUT behavior
      - [ ] #US005-004 - Manually test endpoint with Postman and CLI

2. 🎯 *Title:* **US007 – Remove Task**
     - *Description:* 
      
       As a user, I want to delete a task so I can remove completed or irrelevant items.
       - ✅ Acceptance Criteria (see `tt_user_stories`)
         
       - 📌 Sub-Issues
           - [ ] #US007-001 - Implement DELETE /api/tasks/<id> to delete a task
           - [ ] #US007-002 - Add unit tests for deleting a task
           - [ ] #US007-003 - Update API documentation with DELETE behavior
           - [ ] #US007-004 - Manually test delete operation via Postman

3. 🎯 *Title:* **US011 – Persist Tasks**
     - *Description:* 
      
       As a user, I want my tasks saved between sessions so I don’t lose data when the app restarts.
       - ✅ Acceptance Criteria (see `tt_user_stories`)
           

       - 📌 Sub-Issues
           - [ ] #US011-001 - Implement file-based persistence in data/tasks.json
           - [ ] #US011-002 - Create storage module/service abstraction
           - [ ] #US011-003 - Add tests for load/save functionality
           - [ ] #US011-004 - Validate persistence with CLI and API

4. 🎯 *Title:* **US015 - API Error Handling**
    - *Description:* 
     
      As a developer or tester, I want all API errors to be returned in a consistent format so I can handle them more easily and test more effectively.

      - ✅ Acceptance Criteria (see `tt_user_stories`)
       

    - 📌 Sub-Issues
        - [ ] #US015-001 - Add global error handler using @app.errorhandler()
        - [ ] #US015-002 - Define consistent JSON error response schema
        - [ ] #US015-003 - Add tests for 400/404/405 error conditions
        - [ ] #US015-004 - Manually verify error responses using Postman

5. 🎯 *Title:* **RF001 – Refactor: Blueprint modularization (routes/tasks.py)**
     - *Description:* 
      
       Refactor the Flask app to use Blueprints for routing, improving modularity and maintainability.
       - ✅ Acceptance Criteria
           - [ ] Routes are moved to `routes/tasks.py`.
           - [ ] App factory registers blueprint.
           - [ ] Legacy routes in `main.py` are removed.
           - [ ] Tests still pass after refactor.
           - [ ] Project structure reflects modular design.

       - 📌 Sub-Issues 
           
          - [ ] #RF001-001 - Refactor routes to routes/tasks.py and routes/health.py
          - [ ] #RF001-002 - Register blueprints in __init__.py
          - [ ] #RF001-003 - Confirm routes function after blueprint split
          - [ ] #RF001-004 - Update test imports
          - [ ] #RF001-005 - Remove old route definitions
          - [ ] #RF001-006 - Confirm test coverage is intact
          - [ ] #RF001-007 - Update README/project docs
          

6. 🎯 *Title:* **RF002 – JSON File Persistence**
     - *Description:* 
    
        Refactor task storage into a modular file-based system to support persistence and testability.
        - ✅ Acceptance Criteria
            - [ ] New helper functions are in `utils/storage.py`.
            - [ ] Logic to read/write tasks is encapsulated in functions.
            - [ ] Routes call storage functions instead of accessing raw list.
            - [ ] Tests confirm storage behavior.
            - [ ] File read/write errors are handled gracefully.

        - 📌 Sub-Issues 
          - [ ] #RF002-001 - Create services/storage.py with save/load functions
          - [ ] #RF002-002 - Replace in-memory logic in routes with storage access
          - [ ] #RF002-003 - Add unit tests for storage service
          - [ ] #RF002-004 - Update fixtures for file reset in conftest.py

7. 🎯 *Title:* **RF003 – Organize test files by concern (health, task, storage)**
     - *Description:* 
    
    Refactor test/ to be modular based on concern to support testability.
        
    - ✅ Acceptance Criteria
        - [ ] Centralized Test Fixtures (`conftest.py`)
        - [ ] Improved Test Isolation (reset)
        - [ ] Configure pytest to discover and run tests correctly across folders.
        - [ ] Test Files Organized by Concern (health, tasks, storage)
         
    - 📌 Sub-Issues of **RF003
        * [ ] #RF003-001 - Move Existing files into correct locations based on concern
        * [ ] #RF003-002 - Remove tests for US002 and place in separate module (`tests/tasks/test_add_task`.py`)
        * [ ] #RF003-003 - Remove tests for US003 and place in separate module (`tests/tasks/test_get_task`.py`)
        * [ ] #RF003-004 - Perform regression testing to ensure no issues
           
# Sprint 1 Issue

## Parent Epic: Sprint 1 Completion 

- *Title:* **Sprint 1 Acceptance Criteria** 
- *Description:* 
   
    This Sprint includes foundational work on the TaskTracker project including environment setup, testing pipelines, initial API endpoints, and a CLI stub interface. Completion of Sprint 1 requires all the following criteria to be met.

    - **Sprint-Level Completion Criteria** (Product Owner Level) (see `s1_sprint_plan`)
    * Project environment and development workflow is set up.
    * Core API endpoints are implemented and tested.
    * Health check route (`/api/`) is implemented.
    * A task is added (`POST /api/tasks`).
    * GitHub Actions continuous intergration is established.
    * API Documentation has begun
    * A **CLI stub** to support task creation from the command line is added.
    * Manual testing is introduced with curl and Postman.
    
    - **Definition of Done**  (applies to each user story or task) (see `s1_sprint_plan`)

    ---

  - 📂 Sub-Issues from EPIC
    
    -  Break out each of the above to be their own issue (sub-issue of EPIC)
    
**Sub-Issues** 
*Core API Endpoints*
  * [ ] All selected user stories (US000–US004) are completed and marked “Done”
    *Use the `tt_user_stories`* Acceptance Criteria
    * **US001 – Health Check Endpoint**:
        * [ ] `GET /api/health` returns `{ "status": "OK" }`
        * [ ] Response includes HTTP 200 status code
        * [ ] Endpoint has automated test using `pytest`
        * [ ] CI is configured to run the test on every push to `main` 
    * **US002 – Add Task via API**: 
        * [ ] `POST /api/tasks` accepts a JSON body with a task title
        * [ ] Task is added to an in-memory list or temporary storage
        * [ ] Title field is required; request fails with a 400 error if missing or empty
        * [ ] Valid requests return 201 and include the new task in JSON
        * [ ] All logic is covered by unit tests
    * **US003 – View Tasks (List)**: 
        * [ ] `GET /api/tasks` returns a JSON array of all tasks
        * [ ] Each task includes `id`, `title`, and `completed` status
        * [ ] Endpoint returns 200 with correct structure even when task list is empty
        * [ ] Tests validate response structure and content
    * **US004 - Add Task via CLI (stub)**
        * [ ] Prompt for task title and description
        * [ ] Add task to in-memory list (Sprint 1 only)
        * [ ] Display confirmation message 

*Continuous Integration Setup*
  * [ ] Continuous Integration (CI) via GitHub Actions runs on every push and passes for all merged branches
    - [ ] #CI001 – Configure GitHub Actions for testing workflow
    - [ ] #CI002 – Set up and verify `pytest-cov` integration and include report in CI

*Manual Testing & Documentation*
  * [ ] Test endpoints with curl and Postman
  * [ ] Document results in README / Postman collection
  * [ ] Begin API documentation

*Project Environment Setup*
  * [ ] Set up project structure and virutal environment
  * [ ] Configure dependencies (`requirements.txt`)
  * [ ] Confirm development workflow is working

**Atomic Tasks**
* [ ] Write unit tests for `/api/` health check
* [ ] Write unit test for `POST /api/tasks`
* [ ] Add GitHub Actions workflow file
* [ ] Verify task creation persists correctly
* [ ] Document CLI usage in README 
    




# 🏁 Sprint 5 Issue Guidance

 This Sprint extends the Task Tracker with external API support, mock testing, Robot Framework-based acceptance tests, and optional DI refactor.

This document provides guidance on creating GitHub issues for Sprint 5 tasks. Issues should be modular, test-driven, and assigned to appropriate branches. Be sure to group tasks by user story or refactor, and follow the GitHub Flow (feature branches + pull requests).

## Epic Issue:  Sprint 5 Acceptance Criteria

  📌 **Title:** Sprint 5 – External API and Robot Framework

  * **Description:**
  Sprint 5 finalizes the testing and deployment pipeline. It validates all prior features using Robot Framework and ensures modular, well-documented, and CI-validated software. This sprint also introduces a new user storie (US031) and additions to the test suite.

### ✅ Sprint-Level Completion Criteria (Product Owner Level)
**See Sprint 5 Plan**


---

### 📂 Sub-Issues

#### ✅ User Story Tasks
- [ ] #US002 – Add Task
- [ ] #US003 – View Tasks
- [ ] #US005 – Mark Complete
- [ ] #US007 – Delete Task
- [ ] #US012 – Add Task via Web UI
- [ ] #US015 – Error Handling
- [ ] #US026 – View Task List (UI)
- [ ] #US027 – View Task Report
- [ ] #US031 – Show Current Time via External API
- [ ] #US036 – Server-Side Validation

#### 🔁 Refactor Tasks
- [ ] #RF015 – Create `TimeService` wrapper using `requests`
- [ ] #RF016 – Inject `TimeService` into `create_app()`
- [ ] #RF017 – Add `/api/time` endpoint using Blueprint
- [ ] #RF018 – Use `unittest.mock` for TimeService
- [ ] #RF019 – Configure CI to handle external API failure (mark/skip)
- [ ] #RF022 – Finalize Dependency Injection (Optional / Tutorial Only)

#### ⚙️ Technical/Testing
- [ ] #TEST011 – Add Robot Framework acceptance tests for US002–US036
- [ ] #CI004 – Run Robot tests in CI (with retry/failure handling)


##  ✅ Sprint-Level Definition of Done (applies to each task)

   **See Sprint 5 Plan**


  * 📅 Related Documentation

    * `docs/test_plan.md`
    * `docs/test_cases.md`
    * `docs/test_report.md`
    * `docs/api_documentation.md`
    * `docs/ui_docs.md`
    * `README.md`

---

## 📆 Detailed Sub-Issues

1. 🎯 RF015 Create TimeService
* *Description:*

* ✅ Acceptance Criteria
  * [ ] Create a service that wraps the external API logic for fetching time
  * [ ] Should support DI and mocking
  * [ ] Add unit tests using unittest.mock
    
2. 🎯 RF016 Inject TimeService via create_app()
* *Description:*

* ✅ Acceptance Criteria
  * [ ] Update app factory to allow injection of TimeService
  * [ ] Add fallback to WorldTimeClient if none provided

3. 🎯 RF017 Create /api/time Route
* *Description:*

* ✅ Acceptance Criteria
  * [ ] Create a time_bp Blueprint and register it
  * [ ] Add route: GET /api/time that returns the current time in JSON

4. 🎯 RF018 Mock TimeService in Unit Tests
* *Description:*

* ✅ Acceptance Criteria
  * [ ] Use unittest.mock.Mock() or a fake client for service-level testing
  * [ ] Ensure /api/time route is also tested with mocked service
    
5. 🎯 RF019. 
* *Description:*

* ✅ Acceptance Criteria
  * [ ] Skip real API tests in CI if network fails or flag set
  * [ ] Optionally mark flaky or real-time-dependent tests
    

6. 🎯 RF021 – Add Robot Framework Tests for Core Task Flows

* *Description:* Implement Robot Framework test cases for adding, viewing, completing, and deleting tasks.

  * ✅ Acceptance Criteria

    * [ ] Test suite covers `Add`, `View`, `Complete`, `Delete` flows via UI
    * [ ] Tests simulate user interaction through browser
    * [ ] Robot tests are tagged with corresponding user stories
    * [ ] Screenshots saved on test failure
    * [ ] Report page displays task summary data
    * [ ] Tests check UI navigation and expected results

  * 📂 Sprint 5 Acceptance Validation User Stories (Evaluated by Robot Framework)

    * [ ] #US002 – Add Task (Validation)
    * [ ] #US003 – View Tasks
    * [ ] #US004 – Mark Task Complete
    * [ ] #US005 – Delete Task
    * [ ] #US007 – View Completed Tasks
    * [ ] #US012 - Submit new task via UI
    * [ ] #US015 – API Error Handling
    * [ ] Show validation errors for missing title
    * [ ] Submit task with only whitespace --> receive error
    * [ ] #US026 – Task Menu UI
    * [ ] #US027 – View Task Report

7. 🎯 RF022 – Finalize Dependency Injection Structure
  * Group Project 
  * Reference tutorial in Rf022 Dependency Injection Canvas document

---

9. 🎯 TEST005 – Add CI Job for Robot Tests in GitHub Actions

* *Description:* Extend GitHub Actions to include a step that runs Robot Framework test suites.

  * ✅ Acceptance Criteria

    * [ ] Add robot test step to .github/workflows/python-app.yml
    * [ ] Ensure robot test failure halts CI
    * [ ] Skip API tests with marker (e.g. pytest.mark.skipif(...))
    * [ ] Document test strategy in README.md

---

10. 🎯 DOC005 – Update Final Documentation (README, API/UI Docs, Test Plan, Report)

* *Description:* Final documentation must reflect full system functionality, testing, and architecture.

  * ✅ Acceptance Criteria

    * [ ] README includes final setup, usage, testing
    * [ ] UI documentation includes screenshots and nav flows
    * [ ] API documentation lists all endpoints and examples
    * [ ] Test Plan, Test Cases, and Test Report are current

  * 🔹 Subtasks

    * [ ] Update `docs/README.md`
    * [ ] Add/update `docs/ui_docs.md` with screenshots
    * [ ] Confirm `docs/test_report.md` has Robot output summary
    * [ ] Review and revise `docs/test_plan.md`, `docs/test_cases.md`

---

# Sprint 1 – Group Project Planning  

This sprint launches the **Group Project phase** of the TaskTracker system.  
The team will migrate one individual project into a new shared repository, reset Agile documentation, and lay the foundation for collaboration, hybrid testing, and CI refactoring.  

---

## 1. Sprint Goals  

* Establish shared team repository and working CI pipeline.  
* Recreate all Agile documentation (Sprint Plan, Test Plan, Test Cases, API Reference, Diagrams).  
* Implement project refactors for:  
  * Hybrid pytest markers and concern-based test folders.  
  * Centralized task validation in `TaskService`.  
  * Automated TimeService testing (Playwright / Selenium).  
* Add Robot Framework test suite and create its instructional lab.  
* Prepare all artifacts for traceability and Final Test Report.  

---

## 2. User Stories in Scope  

* **US001– Hybrid Test Organization**  
  * Add pytest markers (`unit`, `integration`, `e2e`) and concern-based structure.  
* **US002 – Automated Testing of Time Service**  
  * Create browser-level tests to verify TimeService display and updates.  
* **US003 – Centralize Task Validation**  
  * Refactor `TaskService` to enforce shared validation schema.  
* **US004 – New Feature (Team Choice)**  
  * Select one user story from `group_projects_choice.md` and implement.  

See `tt_user_stories.md` for details, acceptance criteria, and GitHub issue links.  

---

## 3. Test Planning Overview (see `test_plan.md`)  

### Automated Testing Strategy  
* **Frameworks:** `pytest`, `pytest-cov`, `Robot Framework`, `Playwright / Selenium`.  
* **Hybrid Organization:**  
   – Folders by concern (`tests/api`, `tests/ui`, `tests/storage`, etc.)  
   – Markers by scope (`@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.e2e`).  
* **CI Triggers:**  
   – Unit + Integration → run on every push/PR  
   – E2E / BDD / Robot → run conditionally (by paths or manual run)  
* **Coverage Goal:** ≥ 90 % for Unit + Integration layers.  

### Acceptance Testing (Robot Framework)  
* Covers TaskService and TimeService user journeys.  
* Produces `log.html` and `report.html` artifacts.  
* Lab document teaches setup and execution steps.  

---

## 4. Tools & Technologies  

* Python 3.11  |  Flask backend  
* `pytest`, `pytest-cov`, `pytest-playwright`, `selenium`  
* `Robot Framework` for acceptance testing  
* `GitHub Actions` for CI/CD workflows  
* `Pydantic` for validation schemas  
* `MS Teams` for communication  |  `GitHub Projects` for Kanban  

---

## 5. Technical Design & Architecture  

* **Architecture Evolution:** Codebase migrated from individual repo → team repo.  
* **Validation Layer:** Move all business rules to `TaskService` + `schemas.py`.  
* **TimeService Testing:** Automated UI verification for live time updates.  
* **Test Organization:** Hybrid model – concern folders + scope markers.  
* **CI/CD:** Separate workflows for unit/integration, UI, BDD, Robot.  

---

## 6. Key Tasks (Linked to GitHub Issues)  

| Task | Story | Owner | Est. (hrs) | Status |
|------|--------|--------|------------|--------|
| Create new repo + migrate base code | US000 | DevOps Lead | 3 | ✅ Done |
| Rebuild Agile docs (sprint/test plan + cases) | PR-1 | Docs Lead | 5 | ⏳ In Progress |
| Add pytest markers + folder structure | US001 | Dev 1 | 4 | – |
| Centralize Task Validation in service layer | US002 | Dev 2 | 6 | – |
| Automate TimeService UI test | US003 | QA Lead | 6 | – |
| Create Robot Framework suite + lab | US004 | Docs Lead + QA Lead | 5 | – |
| CI split into 4 workflows | PR-2 | DevOps Lead | 4 | – |

---

## 7. Risk Management  

| Risk | Impact | Mitigation |
|------|---------|-------------|
| Merge conflicts | High | Use feature branches + PR reviews |
| CI pipeline failures | Medium | Run CI tests incrementally after each change |
| Robot Framework learning curve | Medium | Pair programming + early lab draft |
| Inconsistent validation rules | High | Centralize logic in TaskService |
| Schedule slippage | Medium | Weekly sync + GitHub milestones tracking |

---

## 8. Documentation Deliverables  

| Artifact | Location | Owner |
|-----------|-----------|--------|
| Sprint Plan | `/docs/s1-agile/sprint-plan.md` | Scrum Master |
| Test Plan | `/docs/s1-agile/test-plan.md` | QA Lead |
| Test Cases | `/docs/s1-agile/test-cases.md` | QA Lead + Devs |
| Traceability Matrix | `/docs/s1-agile/traceability-matrix.md` | QA Lead |
| API Reference | `/docs/api/README.md` | Dev Owner |
| ERD /Class Diagrams | `/docs/diagrams/` | Dev Team |
| Robot Lab | `/labs/robot-framework-lab.md` | Docs Lead |

---

## 9. Collaboration & Communication  

* Use **GitHub Projects** (Kanban: Backlog → In Progress → Review → Done).  
* Create Issues for each story + link to PRs.  
* Weekly standup (MS Teams or chat thread).  
* All code merged via PR after peer review.  
* DevOps Lead monitors CI and pipeline health.  

---

## 10. Sprint Acceptance Criteria  

✅ All Agile docs recreated and committed.  
✅ pytest markers and folder structure implemented.  
✅ Task validation centralized and tested.  
✅ TimeService automated tests added and passing.  
✅ Robot Framework suite and lab delivered.  
✅ CI workflows split and green.  
✅ Team review + sign-off in Final Test Report.  

---

## 11. Definition of Done (Per Story or Task)  

- Code runs without errors.  
- Unit / Integration / Robot tests pass in CI.  
- Docs updated (Sprint Plan, Test Plan, Test Cases, API, ERD).  
- Peer review approved via PR.  
- Feature visible in local and CI test runs.  

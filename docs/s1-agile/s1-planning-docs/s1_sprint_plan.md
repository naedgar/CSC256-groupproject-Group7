
---

# Sprint 1 – Sprint Plan**

```markdown
# Sprint 1 – Group Project Planning

This sprint launches the Group Project phase of TaskTracker.  
No new features are implemented in Sprint 1 — this sprint focuses on migration, documentation, and planning.

---

## 1. Sprint Goals

* Migrate selected Individual Project into shared Group Repository  
* Rebuild all Agile documentation from scratch  
* Validate the baseline API is functioning  
* Verify CI can run existing tests successfully  
* Establish future strategy for testing, CI, and architecture

---

## 2. User Stories in Scope

Sprint 1 includes documentation-level planning only:

* US000 – Migration & Setup  
* US001 – Sprint 1 Documentation Creation  
* US002 – Baseline Testing Strategy  
* US003 – CI Verification  
* US004 – Architecture & Diagram Creation  

No feature user stories are implemented this sprint.

---

## 3. Test Planning Overview

See `s1_test_plan.md` for detailed strategy.

Sprint 1 creates:

* Baseline test strategy  
* Regression plan  
* Test case templates  
* CI testing outline  
* Acceptance testing strategy (planning only)

---

## 4. Tools & Technologies

* Python 3.11  
* Flask backend  
* pytest for baseline regression  
* GitHub Actions for CI  
* Postman for manual endpoint verification  

---

## 5. Key Tasks

| Task | Owner | Status |
|------|--------|--------|
| Create new repo | DevOps Lead | ✔ |
| Migrate Individual Project | Developer | ✔ |
| Rebuild Agile docs | Docs Lead | ✔ |
| Validate baseline API | QA Lead | ✔ |
| Verify CI runs pytest | DevOps Lead | ✔ |

---

## 6. Out-of-Scope Items

Not implemented in Sprint 1:

- Time service feature  
- JSON/file persistence upgrades  
- Centralized validation  
- PUT/DELETE endpoints  
- Robot Framework test suite  
- Hybrid pytest implementation  
- CI workflow splits  

These belong to later sprints.

---

## 7. Acceptance Criteria

All Agile docs recreated  
App runs locally and in CI  
Baseline endpoints return correct responses  
No new features introduced  
Documentation matches PR-1 requirements

---

## 8. Definition of Done

* Documentation committed and reviewed  
* CI green on main branch  
* Project baseline validated  
* All diagrams and plans completed

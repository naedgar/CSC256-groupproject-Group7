# Sprint 4 Plan – Group Project Final Sprint

## Sprint Goal
Finalize all Group Project features delivered through PR-1 to PR-10, complete full regression testing, execute Robot Framework acceptance tests, verify CI workflows, enforce centralized validation and hybrid testing structure, and prepare the Final Test Report and Presentation.

---

## In Scope
- **US031** – Show Current Time via External API  
- **US039** – View Time Created in Task Summary  
- **US041** – Hybrid Test Organization with pytest Markers  
- **US042** – Automated TimeService Testing (API + UI)  
- **US043** – Centralized Task Validation (Service Layer + Schemas)  
- – CI Workflow Verification (GitHub Actions)  
- – Centralized Task Validation Implementation  
- – Task Timestamps (`createdAt`) + Time API Integration  
- – Full Regression Testing  
- – Robot Framework Acceptance Tests + Lab  
- – Final Test Report  
- – Final Presentation  

---

## Out of Scope
- New feature development beyond Sprint 4 user stories  
- Major architectural redesign  
- Database or ORM migrations  
- UI redesign outside of validation and time/timestamp display  

---

## Tools & Technologies
- Python + Flask  
- pytest, pytest-cov  
- Playwright / Selenium  
- Robot Framework  
- GitHub Actions  
- WorldTimeAPI  

---

## Acceptance Criteria
- All CI pipelines are green  
- All unit, integration, E2E, and Robot tests pass  
- Time Service fully verified at API and UI levels (**US031, US042**)  
- Task timestamps verified in API and UI (**US039**)  
- Centralized validation enforced across API, CLI, and UI (**US043**)  
- Hybrid test structure enforced using pytest markers (**US041**)  
- Full regression test suite executed successfully (**PR-7**)  
- Robot Framework acceptance tests pass (**PR-8**)  
- Final Test Report completed and submitted (**PR-9**)  
- Final Presentation completed and delivered (**PR-10**)  

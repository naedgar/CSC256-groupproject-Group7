# 🍪 Sprint 1 Test Plan – Group Project (PR-1 Agile Documentation)

This Sprint 1 Test Plan defines the **testing strategy and preparation** for the TaskTracker Group Project.  
Sprint 1 focuses on **documentation, planning, and environment setup**, not full feature testing execution.

---

## 📝 Purpose  

This plan documents the **testing strategy for the migrated Group Project environment** and prepares the project for advanced testing in future sprints.

This Sprint includes **planning and design** for testing the following upcoming features:

- US0XX – Hybrid pytest Organization  
- US0XX – Centralized Task Validation  
- US0XX – Automated TimeService Testing  
- US0XX – Robot Framework Acceptance Suite  
- US0XX – Team-selected feature (`group_projects_choice.md`)  

Sprint 1 establishes:

- The **hybrid pytest strategy**
- The **Robot Framework acceptance strategy**
- The **TimeService testing strategy**
- The **CI/CD testing structure**
- The **regression testing approach**

No full feature automation is required in Sprint 1 — this sprint defines the **testing foundation**.

---

## 📅 Sprint Information  

* **Sprint:** 1 – Agile Documentation & Testing Strategy Setup  
* **Iteration Dates:** YYYY-MM-DD → YYYY-MM-DD  
* **Version Under Test:** Group `main` branch (migrated baseline)  
* **Prepared by:** [Your Name]  
* **Last Updated:** YYYY-MM-DD  

---

## 🎯 Test Objectives  

| ID | Objective | Success Metric |
|----|------------|----------------|
| OBJ-1 | Define and document hybrid pytest organization | Testing folders and markers documented |
| OBJ-2 | Define centralized Task validation strategy | Validation rules documented |
| OBJ-3 | Define TimeService automated testing approach | UI and API test plan documented |
| OBJ-4 | Define Robot Framework acceptance strategy | Robot test scope and lab outline documented |
| OBJ-5 | Define CI testing execution plan | All testing workflows planned |

---

## 📎 In-Scope Testing Strategy by User Story  

### US001 – Hybrid pytest Organization  
- Plan concern-based folder structure  
- Plan marker usage (`unit`, `integration`, `e2e`)  

### US002 – Centralize Task Validation  
- Define validation rules  
- Define shared schema strategy  

### US003 – Automated TimeService Testing  
- Define `/api/time` test coverage  
- Define UI browser test scope  

### US004 – Robot Framework Acceptance Suite  
- Define core user journeys  
- Define expected Robot artifacts  

### US005 – Team Choice Feature  
- Define test expectations and coverage  

---

## 🧩 Test Types  

| Type | Description |
|------|--------------|
| Unit Tests | Function and service-level tests |
| Integration Tests | API and service-to-storage tests |
| UI/E2E Tests | Browser verification |
| Acceptance Tests | Robot Framework user journeys |
| Edge Tests | Boundary and negative input tests |
| CI Tests | Workflow enforcement |
| Manual Tests | Visual and lab verification |

---

## 🛠️ Testing Tools  

| Tool | Purpose |
|------|-----------|
| `pytest` | Core testing framework |
| `pytest-cov` | Coverage tracking |
| `Flask Test Client` | API testing |
| `Playwright` / `Selenium` | UI automation |
| `Robot Framework` | Acceptance testing |
| `GitHub Actions` | CI/CD |
| `Postman` | Manual API testing |

---

## ⚙️ Test Environment Setup  

* **OS:** Ubuntu CI runner + local dev machines  
* **Python:** 3.11 (course requirement)  
* **Dependencies:** `requirements.txt`  
* **Virtual Environment:** `.venv`  
* **Local App Start:**  
  ```bash
  flask --app app run

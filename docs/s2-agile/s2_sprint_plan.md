# Sprint 2 Planning

Sprint 2 focuses on test structure refactoring, Time Service testing, and validation standardization.

---

## 1. Sprint Goals

* Implement hybrid pytest marker structure (PR3)
* Add Time Service endpoint testing (PR4)
* Centralize Task validation rules (PR5)
* Expand automated test coverage
* Update documentation to reflect changes

---

## 2. In Scope

* Hybrid pytest markers and folders
* `/api/time` endpoint
* Centralized validation logic
* Validation test cases
* CI test execution with markers

---

## 3. Out of Scope

* PUT/DELETE task endpoints
* JSON persistence
* Global error handling
* Robot Framework
* Additional user stories

---

## 4. Tools & Technologies

* Flask
* pytest + pytest-cov
* GitHub Actions
* Postman for manual API testing

---

## 5. Acceptance Criteria

* Time Service returns valid time and timezone
* Validation rejects invalid task input
* Tests properly grouped by pytest markers
* CI runs all marker groups successfully

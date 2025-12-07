# 🔮 Sprint 2 Test Plan

## 🌟 Test Objectives

| ID | Objective | Success Metric |
|----|-----------|----------------|
| OBJ-1 | Validate Time Service endpoint | `/api/time` returns datetime + timezone |
| OBJ-2 | Validate centralized task validation | Invalid titles rejected |
| OBJ-3 | Confirm pytest markers work | Marker execution filters tests |
| OBJ-4 | Ensure CI stability | All tests pass in GitHub Actions |

---

## Test Strategy

* TDD methodology
* Automated testing using pytest
* Manual validation using Postman
* CI execution using GitHub Actions

---

## Tools

* pytest
* pytest-cov
* Postman
* GitHub Actions

---

## Test Coverage Goal

* ≥ 90% coverage on validation and time features

---

## 📌 Test Scope by Feature

### PR4 – Time Service
- `/api/time` must return valid JSON time

### PR5 – Validation
- Empty title rejected
- Whitespace title rejected

### PR3 – Hybrid pytest
- Markers correctly group tests

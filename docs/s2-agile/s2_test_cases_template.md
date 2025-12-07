# 🍪 Sprint 2 Test Cases

These test cases validate Time Service, validation rules, and hybrid pytest structure.

---

## PR4 – Time Service

### TC-TIME-001: Get Current Time
- **Steps:** GET `/api/time`
- **Expected:** 200 OK with datetime and timezone
- **Test Type:** Automated

---

## PR5 – Centralized Validation

### TC-VAL-001: Reject Empty Title
- **Steps:** POST `/api/tasks` with empty title
- **Expected:** 400 Bad Request
- **Test Type:** Automated

### TC-VAL-002: Reject Whitespace Title
- **Steps:** POST `/api/tasks` with `"   "`
- **Expected:** 400 Bad Request
- **Test Type:** Automated

---

## PR3 – Hybrid pytest Structure

### TC-PYTEST-001: Marker Execution
- **Steps:** Run tests with `-m unit`
- **Expected:** Only unit tests execute

---

## Manual Tests

### TC-MANUAL-001: Time Endpoint via Postman
- **Steps:** GET `/api/time`
- **Expected:** Valid JSON time response

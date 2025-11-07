# Sprint 1 – Test Report

This document summarizes the results of the executed test cases for Lab s0-0. Each test case includes its outcome, tester comments, and any associated issues or observations.

---

## Test Coverage

Include `pytest-cov` summary/screenshot of the coverage report in your Sprint 1 Test Report. Ensure all US004, US005, US009, and US014 logic paths are covered. CI should block merges with insufficient coverage.

## 🧪 TC_US000-001: Run Sanity Check with Pytest

**Test Case ID:** TC-US000-001  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar  
**Test Date:** 2025-09-08 
**Comments:**  
Sanity check passed with no issues
**Screenshot:** ...\images\s1\sanity_test.PNG

## 🧪 TC-US000-002: Verify that `create_app()` returns a Flask instance

**Test Case ID:** TC-US000-002  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar
**Test Date:** 2025-09-08
**Comments:**  
App failed but fixed
**Screenshot:** ...\images\s1\failed_app_flask_tests.PNG ,  ...\images\s1\pass_app_flask_tests.PNG


## 🧪 TC-US000-003: Flask app returns 404 on root when no routes are defined

**Test Case ID:** TC-US000-003  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar 
**Test Date:**  2025-09-08 
**Comments:**  
Flask app returns 404 as expected.
**Screenshot:** ...\images\s1\flask_run.PNG

---

## 🧪 TC-US000-004 Verify Flask Application Runs

**Test Case ID:** TC-US000-003  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar
**Test Date:** 2025-09-08
**Comments:**  
Application has success 
**Screenshot:** ...\images\s1\application_success.PNG

---

## 🧪 TC-US001-001: Health Check API

**Test Case ID:** TC-US001-001  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar  
**Test Date:** 2025-09-08
**Comments:**  
API failed because of AssertionError, fixed and functions well
**Screenshot:** ...\images\s1\health_test_fail.PNG , ...\images\s1\health_test_pass.PNG

## 🧪 TC-US002-001: Add Valid Task

**Test Case ID:** TC-US002-001  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar
**Test Date:** 2025-09-16  
**Comments:**  
Error found no collectors, fixed and functions properly  
**Screenshot:** ...\images\s1\tc_us002_001_failure2.PNG , ...\images\s1\tc_us002_001_pass.PNG

## 🧪 TC-US002-002: Add Task with Empty Title

**Test Case ID:** TC-US002-002  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar 
**Test Date:** 2025-09-16
**Comments:**  
Failed because of AssertionError but fixed and functions properly
**Screenshot:** ...\images\s1\tc_us002_002_failure.PNG , ...\images\s1\tc_us002_002_pass.PNG

## 🧪 TC-US002-003: Add Task with Missing Title

**Test Case ID:** TC-US002-003  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar 
**Test Date:** 2025-09-16  
**Comments:**  
Failed due to KeyError, fixed later
**Screenshot:** ...\images\s1\tc_us002_003_failure.PNG , ...\images\s1\tc_us002_003_pass.PNG

## 🧪 TC-US003-001: View Tasks When None Exist

**Test Case ID:** TC-US003-001  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar  
**Test Date:** 2025-09-16  
**Comments:**  
Failed due to AssertionError, fixed and working properly
**Screenshot:** ...\images\s1\tc_us003_001_failure1.PNG , ...\images\s1\tc_us003_001_pass.PNG

## 🧪 TC-US003-002: View Tasks When Tasks Exist

**Test Case ID:** TC-US003-002  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar
**Test Date:** 2025-09-16
**Comments:**  
Passed the first time


## 🧪 TC-US003-003: Invalid Method on Tasks Endpoint

**Test Case ID:** TC-US003-003  
**Result:** X Pass ☐ Fail  
**Tester:** Nathaniel Edgar  
**Test Date:** 2025-09-16  
**Comments:**  
Passed the first time
**Screenshot:** ...\images\s1\tc_us003_003_pass




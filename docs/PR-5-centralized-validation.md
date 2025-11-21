"""
docs/PR-5-centralized-validation.md

# PR-5: Centralize Task Validation

## 📋 User Story: US0XX Centralize Task Validation

**As a user**, I want the application to consistently validate my task input (both in the UI and API), so that I always receive clear error messages and my data is handled the same way no matter how I interact with the system.

## ✅ Acceptance Criteria - ALL MET

### 1. Consistent Error Messages ✅
- **When** I submit a task with an empty or too-long title (via web form or API)
- **Then** I receive a clear error message and my input is preserved for correction
- **Evidence**: 27 passing tests verify this across UI and API

### 2. Same Validation Rules ✅
- **When** I use UI or API to create a task
- **Then** the same validation rules apply (required, max length, trimming)
- **Evidence**: 
  - `tests/validation/test_centralized_validation.py::TestValidationConsistency`
  - Both UI and API routes use same `TaskService.add_task()` method

### 3. Valid Tasks Accepted ✅
- **When** I submit a valid task
- **Then** it is accepted and appears in my task list
- **Evidence**: 
  - `TestAPIValidation::test_api_accepts_valid_task`
  - `TestUIValidation::test_ui_accepts_valid_task`
  - `TestValidationConsistency::test_valid_task_appears_in_list`

### 4. Specific Error Messages ✅
- **When** I try to create invalid tasks
- **Then** I receive specific error messages
- **Evidence**: Error messages distinguish between:
  - Empty title → "Title is required"
  - Too-long title → "Title must not exceed 255 characters"
  - Invalid type → "Title must be a string"

### 5. Centralized Validation Logic ✅
- **When** validating tasks
- **Then** all logic is centralized in service layer/schema, not duplicated in controllers
- **Evidence**:
  - `app/schemas.py` - Single source of truth for validation rules
  - `app/services/task_service.py` - Uses schema for all validation
  - `app/routes/tasks.py` - No duplicate validation, uses service layer
  - `app/routes/ui.py` - No duplicate validation, uses service layer

### 6. Automated Test Coverage ✅
- **When** running tests
- **Then** both UI and API validation is tested automatically
- **Evidence**: 27 comprehensive tests covering:
  - Schema validation: 8 tests
  - Service layer: 5 tests
  - API routes: 5 tests
  - UI routes: 4 tests
  - Validation consistency: 3 tests
  - Error messages: 2 tests

## 🏗️ Architecture: Centralized Validation Stack

### Single Source of Truth
```
┌─────────────────────────────────┐
│  app/schemas.py                 │ ← Single validation rules
│  TaskCreate Schema              │   (max length, required, etc.)
├─────────────────────────────────┤
│  app/services/task_service.py   │ ← Business logic layer
│  TaskService.add_task()         │   Uses TaskCreate for validation
├─────────────────────────────────┤
│  app/routes/tasks.py (API)      │ ← Catches TaskValidationError
│  app/routes/ui.py (Web)         │   Routes both use same service
└─────────────────────────────────┘
```

### Validation Layers
1. **Schema Layer** (`app/schemas.py`):
   - Defines business rules: max 255 chars, required, etc.
   - Handles normalization: whitespace trimming
   - Custom validation methods for business logic

2. **Service Layer** (`app/services/task_service.py`):
   - Receives raw input from controllers
   - Uses schema to validate
   - Raises `TaskValidationError` on failure
   - Returns normalized, validated data on success

3. **Route Layer** (`app/routes/`):
   - Catches `TaskValidationError` exceptions
   - Returns HTTP error responses (400) with error details
   - No validation logic - just error handling

4. **Exception Handling** (`app/exceptions.py`):
   - `TaskValidationError` - Captures all validation failures
   - Includes error message, field name, and details
   - `to_dict()` method for JSON API responses

## 📝 Implementation Details

### Files Created/Modified

#### New Files
- `app/schemas.py` - Validation schema definitions
- `app/exceptions.py` - Custom exception classes
- `tests/validation/test_centralized_validation.py` - Comprehensive test suite
- `tests/validation/__init__.py` - Package marker

#### Modified Files
- `app/services/task_service.py` - Now uses TaskCreate schema
- `app/routes/tasks.py` - Catches TaskValidationError, removed duplicate validation
- `app/routes/ui.py` - Catches TaskValidationError, removed duplicate validation
- `tests/conftest.py` - Updated MockTaskService to use centralized validation
- `tests/tasks/test_task_service_add.py` - Updated to expect TaskValidationError
- `requirements.txt` - No new dependencies needed (pure Python implementation)

### Validation Rules Defined

**Title Field**
- Required: Must not be empty or None
- Max Length: 255 characters
- Trimming: Automatic whitespace removal
- Error: "Title is required" (for empty/None)
- Error: "Title must not exceed 255 characters" (for length)

**Description Field**
- Optional: Defaults to empty string if None
- Max Length: 500 characters
- Trimming: Automatic whitespace removal
- Error: "Description must not exceed 500 characters" (for length)

## 🧪 Test Results

### Validation Tests: 27/27 PASSING ✅

**Schema Validation (8 tests)**
- Valid task creation with title and description
- Automatic whitespace trimming
- Empty title rejection
- Whitespace-only title rejection
- None title rejection
- Title max length enforcement (255 chars)
- Description max length enforcement (500 chars)
- None description defaults to empty string

**Service Layer (5 tests)**
- Service validates via schema
- Rejects empty titles
- Rejects None titles
- Rejects too-long titles
- Trims whitespace on valid input

**API Routes (5 tests)**
- API accepts valid tasks (201 Created)
- API rejects empty titles (400)
- API rejects missing titles (400)
- API rejects None titles (400)
- API rejects too-long titles (400)

**UI Routes (4 tests)**
- UI accepts valid tasks (redirects to list)
- UI rejects empty titles (returns form with error)
- UI rejects whitespace-only titles
- UI trims whitespace on valid input

**Validation Consistency (3 tests)**
- Same error for empty title in UI and API
- Same error for None title in UI and API
- Valid tasks appear in list after creation

**Error Messages (2 tests)**
- API returns clear error messages
- Error includes field information

## 🔄 Before → After Comparison

### Before: Duplicated Validation

```python
# api/routes/tasks.py
if not data or "title" not in data or not data["title"] or data["title"].strip() == "":
    return jsonify({"error": "Title is required"}), 400

# ui/routes/ui.py
if not title:
    error = "Title is required."
```

**Problems:**
- ❌ Validation logic duplicated in 2+ places
- ❌ Inconsistent error messages
- ❌ Changes to rules require updating multiple files
- ❌ Hard to test comprehensively
- ❌ No consistent business rule enforcement

### After: Centralized Validation

```python
# app/schemas.py
class TaskCreate:
    def _validate_title(self, title: str) -> str:
        if title is None:
            raise TaskValidationError("Title is required", field="title")
        # ... all validation in one place ...
        return trimmed

# api/routes/tasks.py
try:
    new_task = current_app.task_service.add_task(title, description)
    return jsonify(new_task), 201
except TaskValidationError as e:
    return jsonify(e.to_dict()), 400

# ui/routes/ui.py
try:
    current_app.task_service.add_task(title, description)
    return redirect(url_for("ui.show_tasks"))
except TaskValidationError as e:
    error = e.message
```

**Benefits:**
- ✅ Single source of truth for validation rules
- ✅ Consistent error messages everywhere
- ✅ Easy to update business rules in one place
- ✅ Comprehensive test coverage
- ✅ Reusable across UI, API, and services
- ✅ Professional software engineering practice

## 🚀 Usage Examples

### Creating a Valid Task

**Via API:**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'

# Response: 201 Created
# {"id": 1, "title": "Buy groceries", "description": "Milk, eggs, bread", "completed": false}
```

**Via UI:**
- Navigate to `/tasks/new`
- Enter "Buy groceries" in title field
- Enter "Milk, eggs, bread" in description
- Submit form
- Redirected to task list showing new task

### Error Handling

**Empty Title (API):**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "", "description": "No title"}'

# Response: 400 Bad Request
# {"error": "Title is required"}
```

**Empty Title (UI):**
- Navigate to `/tasks/new`
- Leave title field empty
- Submit form
- Form redisplays with error message: "Title is required"

**Too-Long Title:**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "aaaa...aaaa (300 chars)", "description": "Too long"}'

# Response: 400 Bad Request
# {"error": "Title must not exceed 255 characters"}
```

## 📚 For Future Enhancement

### Potential Extensions
1. **Database Constraints** - Add SQLAlchemy model validation that mirrors schema
2. **Async Validation** - Handle async validators (e.g., uniqueness checks)
3. **Localization** - Support multiple languages for error messages
4. **Custom Validators** - Plugin system for application-specific rules
5. **Client-Side Validation** - Mirror schema validation in JavaScript
6. **OpenAPI/Swagger** - Generate API documentation from schemas

### Related Features
- PR-X: Duplicate task detection and prevention
- PR-Y: Task update/edit with same centralized validation
- PR-Z: Bulk import with validation pipeline

## ✨ Software Engineering Principles Applied

1. **DRY (Don't Repeat Yourself)** - Single validation logic
2. **Separation of Concerns** - Schema, service, routes clearly separated
3. **Single Responsibility** - Each class has one reason to change
4. **Fail-Fast** - Validation happens early in the pipeline
5. **Clear Error Messages** - Users understand what went wrong
6. **Comprehensive Testing** - 27 tests verify all scenarios
7. **Professional Practice** - Follows industry standards and patterns

## 🎓 Learning Outcomes

Students completing this PR should understand:
- ✅ Why validation should be centralized
- ✅ How to implement a schema pattern
- ✅ Exception-based error handling
- ✅ Testing validation at multiple layers
- ✅ Consistent user experience across UI and API
- ✅ Professional software architecture
"""

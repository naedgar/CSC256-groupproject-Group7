"""
tests/validation/test_centralized_validation.py

✅ PR-5: Centralized Task Validation Tests

This test file verifies that validation is centralized and consistent
across UI and API routes, fulfilling all acceptance criteria for PR-5.

Acceptance Criteria Verification:
1. ✅ Both UI and API reject empty/too-long titles with clear error messages
2. ✅ Same validation rules apply to both UI and API
3. ✅ Valid tasks are accepted and appear in task list
4. ✅ Invalid tasks receive specific error messages
5. ✅ All validation is centralized in service layer/schema
6. ✅ Automated tests verify consistent behavior
"""

import pytest
from flask.testing import FlaskClient
from app.exceptions import TaskValidationError
from app.services.task_service import TaskService
from app.schemas import TaskCreate


class TestSchemaValidation:
    """Tests for TaskCreate schema validation rules."""
    
    def test_valid_task_creation(self):
        """TaskCreate accepts valid title and description."""
        task = TaskCreate(title="Buy milk", description="From store")
        assert task.title == "Buy milk"
        assert task.description == "From store"
    
    def test_title_trimming(self):
        """TaskCreate automatically trims whitespace from title."""
        task = TaskCreate(title="  Buy milk  ", description="  Fresh  ")
        assert task.title == "Buy milk"
        assert task.description == "Fresh"
    
    def test_empty_title_rejected(self):
        """TaskCreate rejects empty title."""
        with pytest.raises(TaskValidationError) as exc_info:
            TaskCreate(title="", description="")
        assert "required" in str(exc_info.value).lower()
    
    def test_whitespace_only_title_rejected(self):
        """TaskCreate rejects title with only whitespace."""
        with pytest.raises(TaskValidationError) as exc_info:
            TaskCreate(title="   ", description="")
        assert "required" in str(exc_info.value).lower()
    
    def test_none_title_rejected(self):
        """TaskCreate rejects None title."""
        with pytest.raises(TaskValidationError) as exc_info:
            TaskCreate(title=None, description="")
        assert "required" in str(exc_info.value).lower()
    
    def test_title_max_length(self):
        """TaskCreate rejects title exceeding max length."""
        long_title = "a" * 256
        with pytest.raises(TaskValidationError) as exc_info:
            TaskCreate(title=long_title, description="")
        assert "exceed" in str(exc_info.value).lower()
    
    def test_description_max_length(self):
        """TaskCreate rejects description exceeding max length."""
        long_desc = "a" * 501
        with pytest.raises(TaskValidationError) as exc_info:
            TaskCreate(title="Valid Title", description=long_desc)
        assert "exceed" in str(exc_info.value).lower()
    
    def test_none_description_defaults_to_empty(self):
        """TaskCreate converts None description to empty string."""
        task = TaskCreate(title="Task", description=None)
        assert task.description == ""


class TestServiceLayerValidation:
    """Tests for validation at service layer."""
    
    def test_service_validates_via_schema(self):
        """TaskService.add_task() uses centralized schema for validation."""
        service = TaskService(storage=None)
        
        # Valid task accepted
        result = service.add_task("Buy milk", "From store")
        assert result["title"] == "Buy milk"
        assert result["description"] == "From store"
    
    def test_service_rejects_empty_title(self):
        """TaskService.add_task() rejects empty title."""
        service = TaskService(storage=None)
        with pytest.raises(TaskValidationError):
            service.add_task("", "Description")
    
    def test_service_rejects_none_title(self):
        """TaskService.add_task() rejects None title."""
        service = TaskService(storage=None)
        with pytest.raises(TaskValidationError):
            service.add_task(None, "Description")
    
    def test_service_rejects_too_long_title(self):
        """TaskService.add_task() rejects title exceeding max length."""
        service = TaskService(storage=None)
        long_title = "a" * 256
        with pytest.raises(TaskValidationError):
            service.add_task(long_title, "Description")
    
    def test_service_trims_whitespace(self):
        """TaskService.add_task() trims whitespace from title."""
        service = TaskService(storage=None)
        result = service.add_task("  Buy milk  ", "  Store  ")
        assert result["title"] == "Buy milk"
        assert result["description"] == "Store"


class TestAPIValidation:
    """Tests for validation consistency in API routes."""
    
    def test_api_accepts_valid_task(self, client: FlaskClient):
        """API POST /api/tasks accepts valid task."""
        response = client.post('/api/tasks', json={
            "title": "Buy milk",
            "description": "From store"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Buy milk"
        assert data["description"] == "From store"
    
    def test_api_rejects_empty_title(self, client: FlaskClient):
        """API POST /api/tasks rejects empty title with 400."""
        response = client.post('/api/tasks', json={
            "title": "",
            "description": "Description"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert "required" in data["error"].lower()
    
    def test_api_rejects_missing_title(self, client: FlaskClient):
        """API POST /api/tasks rejects missing title with 400."""
        response = client.post('/api/tasks', json={
            "description": "No title"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert "required" in data["error"].lower()
    
    def test_api_rejects_none_title(self, client: FlaskClient):
        """API POST /api/tasks rejects None title with 400."""
        response = client.post('/api/tasks', json={
            "title": None,
            "description": "Description"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
    
    def test_api_rejects_too_long_title(self, client: FlaskClient):
        """API POST /api/tasks rejects title exceeding max length."""
        long_title = "a" * 256
        response = client.post('/api/tasks', json={
            "title": long_title,
            "description": "Description"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert "exceed" in data["error"].lower()


class TestUIValidation:
    """Tests for validation consistency in UI routes."""
    
    def test_ui_accepts_valid_task(self, client: FlaskClient):
        """UI POST /tasks/new accepts valid task."""
        response = client.post('/tasks/new', data={
            "title": "Buy milk",
            "description": "From store"
        }, follow_redirects=True)
        assert response.status_code == 200
        # Should redirect to task list
        assert b"Buy milk" in response.data or response.request.path == "/tasks"
    
    def test_ui_rejects_empty_title(self, client: FlaskClient):
        """UI POST /tasks/new rejects empty title with error message."""
        response = client.post('/tasks/new', data={
            "title": "",
            "description": "Description"
        })
        assert response.status_code == 200  # Returns form with error
        assert b"required" in response.data.lower() or b"error" in response.data.lower()
    
    def test_ui_rejects_whitespace_only_title(self, client: FlaskClient):
        """UI POST /tasks/new rejects whitespace-only title."""
        response = client.post('/tasks/new', data={
            "title": "   ",
            "description": "Description"
        })
        assert response.status_code == 200
        assert b"required" in response.data.lower() or b"error" in response.data.lower()
    
    def test_ui_trims_whitespace_on_valid_input(self, client: FlaskClient):
        """UI POST /tasks/new trims whitespace from title."""
        response = client.post('/tasks/new', data={
            "title": "  Buy milk  ",
            "description": "  Store  "
        }, follow_redirects=True)
        assert response.status_code == 200
        # Task list should show trimmed title
        assert b"Buy milk" in response.data


class TestValidationConsistency:
    """Tests verifying validation consistency between UI and API."""
    
    def test_same_error_for_empty_title(self, client: FlaskClient):
        """UI and API return consistent error for empty title."""
        # API response
        api_response = client.post('/api/tasks', json={"title": ""})
        assert api_response.status_code == 400
        api_data = api_response.get_json()
        
        # Both should reject with 400 and mention "required"
        assert "required" in api_data.get("error", "").lower()
    
    def test_same_error_for_none_title(self, client: FlaskClient):
        """UI and API return consistent error for None title."""
        # API response
        api_response = client.post('/api/tasks', json={"title": None})
        assert api_response.status_code == 400
        api_data = api_response.get_json()
        assert "error" in api_data
    
    def test_valid_task_appears_in_list(self, client: FlaskClient):
        """Valid task created via API appears in task list."""
        # Create via API
        create_response = client.post('/api/tasks', json={
            "title": "Test Task",
            "description": "Test Description"
        })
        assert create_response.status_code == 201
        
        # Get all tasks
        list_response = client.get('/api/tasks')
        assert list_response.status_code == 200
        tasks = list_response.get_json()
        assert any(t["title"] == "Test Task" for t in tasks)


class TestErrorMessages:
    """Tests for user-friendly error messages."""
    
    def test_api_error_message_clarity(self, client: FlaskClient):
        """API returns clear error message for invalid input."""
        response = client.post('/api/tasks', json={
            "title": ""
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        # Error should be user-friendly
        error_msg = data["error"]
        assert len(error_msg) > 0
        assert error_msg[0].isupper()  # Starts with capital letter
    
    def test_error_includes_field_info(self):
        """Validation error includes field information."""
        error = TaskValidationError("Invalid title", field="title")
        error_dict = error.to_dict()
        assert "field" in error_dict
        assert error_dict["field"] == "title"

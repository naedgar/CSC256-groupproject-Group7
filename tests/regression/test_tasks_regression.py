"""
tests/regression/test_tasks_regression.py

PR-7: Regression Test Suite for Tasks (TaskService / /api/tasks)

This comprehensive test suite covers all task operations to ensure:
- POST Add Task (valid + invalid/edge cases)
- GET List Tasks (empty → non-empty)
- PUT Mark Complete (valid ID, already complete, invalid ID)
- DELETE Remove Task (valid ID, invalid ID)
- Error handling (400/404 as applicable)
"""

import pytest
from flask.testing import FlaskClient


class TestTasksRegressionPostAddTask:
    """Regression tests for POST /api/tasks - Add Task operation"""
    
    def test_add_valid_task_with_description(self, client: FlaskClient):
        """TC-REG-TASKS-001: Add valid task with title and description"""
        response = client.post('/api/tasks', json={
            "title": "Buy groceries",
            "description": "Milk, eggs, bread"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Buy groceries"
        assert data["description"] == "Milk, eggs, bread"
        assert data["completed"] is False
        assert "id" in data
    
    def test_add_valid_task_without_description(self, client: FlaskClient):
        """TC-REG-TASKS-002: Add valid task without description"""
        response = client.post('/api/tasks', json={
            "title": "Buy groceries"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Buy groceries"
        assert data["description"] == ""
        assert data["completed"] is False
    
    def test_add_task_with_empty_description(self, client: FlaskClient):
        """TC-REG-TASKS-003: Add task with empty description"""
        response = client.post('/api/tasks', json={
            "title": "Task Title",
            "description": ""
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["description"] == ""
    
    def test_add_task_with_whitespace_trimming(self, client: FlaskClient):
        """TC-REG-TASKS-004: Title and description whitespace is trimmed"""
        response = client.post('/api/tasks', json={
            "title": "  Task Title  ",
            "description": "  Description  "
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Task Title"
        assert data["description"] == "Description"
    
    def test_add_task_missing_title_field(self, client: FlaskClient):
        """TC-REG-TASKS-005: POST without title field returns 400"""
        response = client.post('/api/tasks', json={
            "description": "No title field"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
    
    def test_add_task_empty_title(self, client: FlaskClient):
        """TC-REG-TASKS-006: POST with empty title returns 400"""
        response = client.post('/api/tasks', json={
            "title": "",
            "description": "Empty title"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert "required" in data["error"].lower()
    
    def test_add_task_null_title(self, client: FlaskClient):
        """TC-REG-TASKS-007: POST with null title returns 400"""
        response = client.post('/api/tasks', json={
            "title": None,
            "description": "Null title"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
    
    def test_add_task_whitespace_only_title(self, client: FlaskClient):
        """TC-REG-TASKS-008: POST with whitespace-only title returns 400"""
        response = client.post('/api/tasks', json={
            "title": "   ",
            "description": "Whitespace only"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
    
    def test_add_task_title_too_long(self, client: FlaskClient):
        """TC-REG-TASKS-009: POST with title exceeding max length returns 400"""
        long_title = "a" * 256
        response = client.post('/api/tasks', json={
            "title": long_title,
            "description": "Too long"
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
    
    def test_add_task_description_too_long(self, client: FlaskClient):
        """TC-REG-TASKS-010: POST with description exceeding max length returns 400"""
        long_desc = "a" * 501
        response = client.post('/api/tasks', json={
            "title": "Valid Title",
            "description": long_desc
        })
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
    
    def test_add_task_invalid_json(self, client: FlaskClient):
        """TC-REG-TASKS-011: POST with invalid JSON returns error"""
        response = client.post('/api/tasks',
            data="invalid json",
            content_type='application/json'
        )
        assert response.status_code in [400, 415]
    
    def test_add_task_max_length_title_accepted(self, client: FlaskClient):
        """TC-REG-TASKS-012: POST with title at max length (255) is accepted"""
        max_title = "a" * 255
        response = client.post('/api/tasks', json={
            "title": max_title,
            "description": "At max length"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert len(data["title"]) == 255
    
    def test_add_task_incremental_ids(self, client: FlaskClient):
        """TC-REG-TASKS-013: Multiple tasks get incremental IDs"""
        response1 = client.post('/api/tasks', json={"title": "Task 1"})
        id1 = response1.get_json()["id"]
        
        response2 = client.post('/api/tasks', json={"title": "Task 2"})
        id2 = response2.get_json()["id"]
        
        assert id2 == id1 + 1


class TestTasksRegressionGetListTasks:
    """Regression tests for GET /api/tasks - List Tasks operation"""
    
    def test_get_tasks_empty_list(self, client: FlaskClient):
        """TC-REG-TASKS-101: GET /api/tasks returns empty array when no tasks"""
        response = client.get('/api/tasks')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) == 0
    
    def test_get_tasks_single_task(self, client: FlaskClient):
        """TC-REG-TASKS-102: GET /api/tasks returns single task"""
        # Create task
        client.post('/api/tasks', json={"title": "Task 1"})
        
        # Get tasks
        response = client.get('/api/tasks')
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 1
        assert data[0]["title"] == "Task 1"
    
    def test_get_tasks_multiple_tasks(self, client: FlaskClient):
        """TC-REG-TASKS-103: GET /api/tasks returns multiple tasks"""
        # Create multiple tasks
        for i in range(5):
            client.post('/api/tasks', json={"title": f"Task {i+1}"})
        
        # Get tasks
        response = client.get('/api/tasks')
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 5
    
    def test_get_tasks_includes_all_fields(self, client: FlaskClient):
        """TC-REG-TASKS-104: GET /api/tasks returns all required fields"""
        # Create task
        client.post('/api/tasks', json={
            "title": "Test Task",
            "description": "Test Description"
        })
        
        # Get tasks
        response = client.get('/api/tasks')
        data = response.get_json()
        task = data[0]
        
        assert "id" in task
        assert "title" in task
        assert "description" in task
        assert "completed" in task
    
    def test_get_tasks_preserves_order(self, client: FlaskClient):
        """TC-REG-TASKS-105: GET /api/tasks maintains insertion order"""
        titles = ["Alpha", "Beta", "Gamma", "Delta"]
        for title in titles:
            client.post('/api/tasks', json={"title": title})
        
        response = client.get('/api/tasks')
        data = response.get_json()
        returned_titles = [t["title"] for t in data]
        assert returned_titles == titles


class TestTasksRegressionPutCompleteTask:
    """Regression tests for PUT /api/tasks/<id> - Mark Task Complete"""
    
    def test_complete_valid_task(self, client: FlaskClient):
        """TC-REG-TASKS-201: PUT marks valid task as completed"""
        # Create task
        create_response = client.post('/api/tasks', json={"title": "Task"})
        task_id = create_response.get_json()["id"]
        
        # Complete task
        response = client.put(f'/api/tasks/{task_id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["completed"] is True
    
    def test_complete_task_returns_updated_task(self, client: FlaskClient):
        """TC-REG-TASKS-202: PUT returns complete task object"""
        create_response = client.post('/api/tasks', json={
            "title": "Task Title",
            "description": "Task Description"
        })
        task_id = create_response.get_json()["id"]
        
        response = client.put(f'/api/tasks/{task_id}')
        data = response.get_json()
        
        assert data["id"] == task_id
        assert data["title"] == "Task Title"
        assert data["description"] == "Task Description"
        assert data["completed"] is True
    
    def test_complete_task_not_found(self, client: FlaskClient):
        """TC-REG-TASKS-203: PUT with invalid ID returns 404"""
        response = client.put('/api/tasks/9999')
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
    
    def test_complete_already_completed_task(self, client: FlaskClient):
        """TC-REG-TASKS-204: PUT on already completed task works"""
        # Create and complete task
        create_response = client.post('/api/tasks', json={"title": "Task"})
        task_id = create_response.get_json()["id"]
        client.put(f'/api/tasks/{task_id}')
        
        # Complete again
        response = client.put(f'/api/tasks/{task_id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["completed"] is True
    
    def test_complete_task_with_zero_id(self, client: FlaskClient):
        """TC-REG-TASKS-205: PUT with ID 0 returns 404"""
        response = client.put('/api/tasks/0')
        assert response.status_code == 404
    
    def test_complete_task_with_negative_id(self, client: FlaskClient):
        """TC-REG-TASKS-206: PUT with negative ID returns 404"""
        response = client.put('/api/tasks/-1')
        assert response.status_code == 404
    
    def test_complete_persists_across_requests(self, client: FlaskClient):
        """TC-REG-TASKS-207: Completed status persists across GET requests"""
        # Create and complete
        create_response = client.post('/api/tasks', json={"title": "Task"})
        task_id = create_response.get_json()["id"]
        client.put(f'/api/tasks/{task_id}')
        
        # Verify via GET
        list_response = client.get('/api/tasks')
        tasks = list_response.get_json()
        task = next(t for t in tasks if t["id"] == task_id)
        assert task["completed"] is True


class TestTasksRegressionDeleteTask:
    """Regression tests for DELETE /api/tasks/<id> - Remove Task"""
    
    def test_delete_valid_task(self, client: FlaskClient):
        """TC-REG-TASKS-301: DELETE removes valid task"""
        # Create task
        create_response = client.post('/api/tasks', json={"title": "Task"})
        task_id = create_response.get_json()["id"]
        
        # Delete task
        response = client.delete(f'/api/tasks/{task_id}')
        assert response.status_code == 200
    
    def test_delete_task_removes_from_list(self, client: FlaskClient):
        """TC-REG-TASKS-302: DELETE removes task from list"""
        # Create two tasks
        client.post('/api/tasks', json={"title": "Task 1"})
        create_response = client.post('/api/tasks', json={"title": "Task 2"})
        task_id = create_response.get_json()["id"]
        
        # Delete second task
        client.delete(f'/api/tasks/{task_id}')
        
        # Verify it's gone
        list_response = client.get('/api/tasks')
        tasks = list_response.get_json()
        assert not any(t["id"] == task_id for t in tasks)
        assert len(tasks) == 1
    
    def test_delete_task_not_found(self, client: FlaskClient):
        """TC-REG-TASKS-303: DELETE with invalid ID returns 404"""
        response = client.delete('/api/tasks/9999')
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data
    
    def test_delete_task_twice(self, client: FlaskClient):
        """TC-REG-TASKS-304: DELETE same task twice returns 404 second time"""
        # Create and delete
        create_response = client.post('/api/tasks', json={"title": "Task"})
        task_id = create_response.get_json()["id"]
        client.delete(f'/api/tasks/{task_id}')
        
        # Delete again
        response = client.delete(f'/api/tasks/{task_id}')
        assert response.status_code == 404
    
    def test_delete_task_with_zero_id(self, client: FlaskClient):
        """TC-REG-TASKS-305: DELETE with ID 0 returns 404"""
        response = client.delete('/api/tasks/0')
        assert response.status_code == 404
    
    def test_delete_task_with_negative_id(self, client: FlaskClient):
        """TC-REG-TASKS-306: DELETE with negative ID returns 404"""
        response = client.delete('/api/tasks/-1')
        assert response.status_code == 404


class TestTasksErrorHandling:
    """Regression tests for error handling across all task operations"""
    
    def test_all_operations_return_json(self, client: FlaskClient):
        """TC-REG-TASKS-401: All operations return JSON responses"""
        # POST
        post_response = client.post('/api/tasks', json={"title": "Task"})
        assert post_response.content_type.startswith('application/json')
        
        # GET
        get_response = client.get('/api/tasks')
        assert get_response.content_type.startswith('application/json')
    
    def test_error_responses_have_error_field(self, client: FlaskClient):
        """TC-REG-TASKS-402: Error responses include 'error' field"""
        response = client.post('/api/tasks', json={"title": ""})
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert isinstance(data["error"], str)
    
    def test_404_for_nonexistent_task(self, client: FlaskClient):
        """TC-REG-TASKS-403: Operations on nonexistent tasks return 404"""
        assert client.put('/api/tasks/9999').status_code == 404
        assert client.delete('/api/tasks/9999').status_code == 404
    
    def test_400_for_validation_errors(self, client: FlaskClient):
        """TC-REG-TASKS-404: Validation errors return 400"""
        invalid_requests = [
            {"title": ""},
            {"title": None},
            {"title": "   "},
            {"title": "a" * 256},
        ]
        
        for invalid_data in invalid_requests:
            response = client.post('/api/tasks', json=invalid_data)
            assert response.status_code == 400

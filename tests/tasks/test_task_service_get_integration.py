import pytest
from app.services.task_service import TaskService
from app.models.task import Task


@pytest.fixture(autouse=True)
def clean_task_service():
    # If _tasks is a list, clear it before each test
    TaskService()._tasks.clear()
    # If using a singleton, re-instantiate or reset its state here
    TaskService._instance = None

import pytest

pytestmark = pytest.mark.integration


def test_get_tasks_when_none_exist_integration():
    """
    TC-RF004-002 (integration)
    Integration test for TaskService.get_tasks() when no tasks exist (Task object refactor)
    """
    service = TaskService(storage=None)
    tasks = service.get_tasks()
    assert isinstance(tasks, list)
    assert tasks == []
    # Internal: _tasks should also be empty
    assert hasattr(service, "_tasks")
    assert service._tasks == []

def test_get_tasks_returns_added_tasks_integration():
    """
    TC-RF004-002 (integration)
    Integration test for TaskService.get_tasks() after adding tasks (Task object refactor)
    """
    service = TaskService(storage=None)
    task1 = service.add_task("Task1", "Grocery")
    task2 = service.add_task("Task2", "Study")
    all_tasks = service.get_tasks()

    # Should return list of dicts (backward compatibility)
    assert isinstance(all_tasks, list)
    assert len(all_tasks) >= 2

    # Check dict structure (created_at may be None when no time_service is injected)
    for task in all_tasks:
        assert set(task.keys()) == {"id", "title", "description", "completed", "created_at"}

    # Check values
    titles = [task["title"] for task in all_tasks]
    assert "Task1" in titles
    assert "Task2" in titles

    # Internal: _tasks should contain Task objects
    assert hasattr(service, "_tasks")
    assert all(isinstance(t, Task) for t in service._tasks)
    assert any(t.title == "Task1" for t in service._tasks)
    assert any(t.title == "Task2" for t in service._tasks)
# app/routes/tasks.py
from flask import Blueprint, request, jsonify, current_app
from app.exceptions import TaskValidationError
# ✅ Phase 2: Remove direct storage imports - we'll use injected service instead
# from app.services.task_storage import load_tasks, save_tasks
# 
# 🔄 DEPENDENCY INJECTION TRANSFORMATION COMPLETE:
# All routes now use current_app.task_service instead of direct storage function calls.
# This enables better testing, mock storage, and cleaner architecture.
# 
# ✅ VALIDATION CENTRALIZATION (PR-5):
# Validation is now centralized in TaskService using Pydantic schemas.
# Routes catch TaskValidationError and return consistent error responses.

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

def get_next_id():
    """Get the next available task ID based on existing tasks.
    
    TEMPORARY: This helper function will be replaced when refactoring to use a database.
    In a database, we'll use auto-incrementing primary keys or UUIDs.
    """
    tasks = current_app.task_service.get_all_tasks()
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

@tasks_bp.route('/reset', methods=['POST'])
def reset_tasks():
    """
    Development endpoint to reset tasks data.
    WARNING: Only use for testing/development!
    """
    # Clear all tasks using injected service
    current_app.task_service.clear_tasks()
    return jsonify({"message": "Tasks reset successfully"}), 200

@tasks_bp.route('', methods=['POST'])
def add_task():
    """ Create a task or return a validation error.

    ✅ PR-5: Centralized validation via TaskService using Pydantic schemas.
    
    Valid Request:
        {"title": "Buy milk", "description": "..."}
    
    Invalid:
        - Missing title
        - Empty title      
        - Title too long (>255 chars)
        - Non-string title
    """
    data = request.get_json() or {}
    
    try:
        # Extract from JSON - TaskService.add_task will validate
        title = data.get("title")
        description = data.get("description", "")
        
        # Service layer now does ALL validation via Pydantic schema
        new_task = current_app.task_service.add_task(title, description)
        return jsonify(new_task), 201
        
    except TaskValidationError as e:
        # Consistent error response for validation failures
        return jsonify(e.to_dict()), 400
    except Exception as e:
        # Unexpected errors
        return jsonify({"error": f"Internal error: {str(e)}"}), 500

@tasks_bp.route('', methods=['GET'])
def list_tasks():
    """Return the list of all tasks. GET /api/tasks"""
    tasks = current_app.task_service.get_all_tasks()
    return jsonify(tasks), 200

@tasks_bp.route("/<int:task_id>", methods=["PUT"])
def complete_task(task_id):
    """
    US005 - tests/tasks/test_complete_task.py`
    """
    updated_task = current_app.task_service.complete_task(task_id)
    if updated_task:
        return jsonify(updated_task), 200
    return jsonify({"error": "Task not found"}), 404

@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted_task = current_app.task_service.delete_task(task_id)
    if deleted_task:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404